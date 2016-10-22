package Assignment2;

import java.io.*;
import java.nio.file.Paths;
import org.apache.lucene.search.*;
import org.apache.lucene.index.*;
import org.apache.lucene.store.FSDirectory;

import org.apache.lucene.search.similarities.*;
import org.apache.lucene.analysis.standard.StandardAnalyzer;
import java.io.IOException;
import java.lang.reflect.InvocationTargetException;
import java.util.*;

import org.apache.lucene.queryparser.classic.*;
import org.apache.lucene.queryparser.flexible.standard.QueryParserUtil;
import org.apache.lucene.util.BytesRef;


public class EasySearch {

	public static scoreTrack query_scores(String queryString, String queryID, Similarity similarity) throws IOException, ParseException, IllegalAccessException, IllegalArgumentException, InvocationTargetException, NoSuchMethodException, SecurityException
	{

			IndexReader indexReader = DirectoryReader.open(FSDirectory.open(Paths.get(Intialize.indexPath)));
			IndexSearcher indexSearcher = new IndexSearcher(indexReader);
			StandardAnalyzer analyzer = new StandardAnalyzer();
			indexSearcher.setSimilarity(similarity);
			
			/* Task-1 : [1] Parsing query using analyzer */
			QueryParser queryParser = new QueryParser("TEXT", analyzer); 
			Query query = queryParser.parse(QueryParserUtil.escape(queryString));
			Set<Term> queryTerms = new HashSet<Term>();
			query.createWeight(indexSearcher,false).extractTerms(queryTerms);

			int corpusDocumentCount = indexReader.maxDoc();
			scoreTrack queryScore = new scoreTrack(queryID);


			List<LeafReaderContext> leafReaderContexts = indexReader.getContext().reader().leaves();
			
			/* Task-1: [2] Calculating relevance score each term in query */
			for(Term queryTerm: queryTerms)
			{
				int documentFrequencyForTerm = indexReader.docFreq(queryTerm);
				
				termScores queryTermScore = new termScores(queryTerm.text());
				
				for(LeafReaderContext leafReaderContext : leafReaderContexts)
				{
					PostingsEnum posting = MultiFields.getTermDocsEnum(leafReaderContext.reader(),"TEXT", new BytesRef(queryTerm.text()));
					if(posting != null)
					{
						while(posting.nextDoc() != PostingsEnum.NO_MORE_DOCS)
						{
							int TFinDoc = posting.freq();
							String docNO = indexSearcher.doc(posting.docID() + leafReaderContext.docBase).get("DOCNO");
							long nonDocLen = leafReaderContext.reader().getNormValues("TEXT").get(posting.docID());
							
							double normDocLen = (float) similarity.getClass().getMethod("decodeNormValue", long.class).invoke(similarity, nonDocLen);
							
							double DocLen = 1 / (normDocLen * normDocLen);
                            double tFScore = (TFinDoc/DocLen);

                            double iDFScore = Math.log(1+(corpusDocumentCount/documentFrequencyForTerm));

                            double relevance_score_term =  tFScore * iDFScore;

							queryTermScore.agg_documentScore(docNO, relevance_score_term);
							queryScore.agg_relevant_documents(docNO);

						}
					}

				}
				queryScore.agg_query_tem_scores(queryTermScore);
			}
			indexReader.close();
			return queryScore;
	}

	public static void main(String[] args) {
		try
		{
			BufferedReader getinput = new BufferedReader(new InputStreamReader(System.in));
            System.out.println("Enter Search Query");
            String queryString = getinput.readLine();
            FileWriter fileWriter = new FileWriter(Intialize.outputDir + "easySearch.txt",true);

			String queryID = "1";
			Similarity ClassicSimilarity = new ClassicSimilarity();

			scoreTrack queryScore = query_scores(queryString, queryID, ClassicSimilarity);

			/* Task-1 [3]: Calculating relevance score for query w.r.t. to documents */
			for(String docNo : queryScore.relevantDocumentIDs)
			{
                System.out.println("DocumentID: " + docNo + "     Score:" + queryScore.getDocumentScore(docNo));
                fileWriter.append("DocumentID: " + docNo + "     Score:" + queryScore.getDocumentScore(docNo)+"\n");
			}
			fileWriter.flush();
            fileWriter.close();
		} 
		catch (IOException e) {
			System.out.println("Error while reading index directory.");
			e.printStackTrace();
		} 
        catch (Exception e) {
			e.printStackTrace();
		}
	}

}
