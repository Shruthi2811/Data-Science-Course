package Assignment2;

import java.io.*;
import java.nio.file.Paths;
import org.apache.lucene.analysis.standard.StandardAnalyzer;
import org.apache.lucene.benchmark.quality.*;
import org.apache.lucene.benchmark.quality.trec.TrecTopicsReader;
import org.apache.lucene.index.*;
import org.apache.lucene.queryparser.classic.*;
import org.apache.lucene.queryparser.flexible.standard.QueryParserUtil;
import org.apache.lucene.search.*;
import org.apache.lucene.search.similarities.*;
import org.apache.lucene.store.FSDirectory;


public class CompareAlgorithms {

	public static void write_files(TopDocs topDocs, IndexSearcher indexSearcher, String queryID, String outputFilePath) throws IOException
	{
		File outputFile = new File(outputFilePath);
		outputFile.getParentFile().mkdirs();
		if(outputFile.exists() == false)
		{
			outputFile.createNewFile();
		}
		FileWriter fileWriter = new FileWriter(outputFile, true);
		
		ScoreDoc[] scoreDocs = topDocs.scoreDocs;
		
		for(int docIndex = 0; docIndex < scoreDocs.length; docIndex++)
		{
			ScoreDoc scoreDoc = scoreDocs[docIndex];
			String docNo = indexSearcher.doc(scoreDoc.doc).get("DOCNO");
			String line = queryID + " "+ "Q0"+ " "+ docNo+ " "+ (docIndex+1)+ " "+ scoreDoc.score+ " "+ "run-1 \n";
			fileWriter.append(line);

		}
		
		fileWriter.flush();
		fileWriter.close();
	}

	public static void top_results(Similarity similarity, String algoName) throws IOException, ParseException
	{
		// 1. Read the queries from trec topics
		TrecTopicsReader trec_reader = new TrecTopicsReader();
		BufferedReader bufferedReader = new BufferedReader(new FileReader(Intialize.topicPath));
		QualityQuery[] qualityQueries = trec_reader.readQueries(bufferedReader);

		
		//2.Create searcher
		IndexReader indexReader = DirectoryReader.open(FSDirectory.open(Paths.get(Intialize.indexPath)));
		IndexSearcher indexSearcher = new IndexSearcher(indexReader);
		StandardAnalyzer analyzer = new StandardAnalyzer();
		indexSearcher.setSimilarity(similarity);
		
		/* Task-1 : [1] Parsing query using analyzer */
		QueryParser queryParser = new QueryParser("TEXT", analyzer); 
		
		
		for(int queryIndex=0; queryIndex < qualityQueries.length; queryIndex++)
		{
			QualityQuery qual_query = qualityQueries[queryIndex];
			String queryID = qual_query.getQueryID();


			{
				String titleStringQuery = qual_query.getValue(Intialize.queryTitle);
				String cleanedTitleQuery = SearchTRECTTopics.title_cleaning(titleStringQuery);
				Query titleQuery = queryParser.parse(QueryParserUtil.escape(cleanedTitleQuery));
				TopDocs topDocs = indexSearcher.search(titleQuery, 1000);
				String outputFilePath = Intialize.outputDir + "/" + algoName + "ShortQuery" + ".txt";
				write_files(topDocs, indexSearcher, queryID, outputFilePath);

			}



			{
				String descStringQuery = qual_query.getValue(Intialize.queryDesc);
				String cleanedDescQuery = SearchTRECTTopics.desc_cleaning(descStringQuery);
				Query descQuery = queryParser.parse(QueryParserUtil.escape(cleanedDescQuery));
				TopDocs topDocs = indexSearcher.search(descQuery, 1000);
				String outputFilePath = Intialize.outputDir + "/" + algoName + "LongQuery" + ".txt";
				write_files(topDocs, indexSearcher, queryID, outputFilePath);

			}


		}
		System.out.println("All the queries for " + algoName + "executed successfully");
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub

		try 
		{
            BufferedReader indexed = new BufferedReader(new InputStreamReader(System.in));
            final String classic = "Classic";
            final String lmdir = "LMDirichlet";
            final String lmje = "LMJelinek";
            final String bm25 = "BM25";
            int Userchoice =1;
            System.out.println("Enter algorithm choice\n" +
                    "1: BM25\n" +
                    "2: LMDirichlet\n" +
                    "3: LMJelinekMercer\n" +
                    "4: Classic\n");

            Userchoice = Integer.parseInt(indexed.readLine());
            switch(Userchoice){
                case 1: top_results(new BM25Similarity(), bm25); break;
                case 2: top_results(new LMDirichletSimilarity(), lmdir); break;
                case 3: top_results(new LMJelinekMercerSimilarity((float) 0.7), lmje); break;
                case 4: top_results(new ClassicSimilarity(), classic); break;
                default: break;
            }
		} 
		catch (IOException e) {

			e.printStackTrace();
		} 
		catch (ParseException e) {

			e.printStackTrace();
		}
	}

}
