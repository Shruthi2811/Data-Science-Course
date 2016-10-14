/**
 * Created by Vipul
 * Lucene version - 6.2.1
 */

import java.io.IOException;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.logging.*;
import org.apache.lucene.analysis.Analyzer;
import org.apache.lucene.analysis.core.*;
import org.apache.lucene.analysis.standard.StandardAnalyzer;
import org.apache.lucene.index.*;
import org.apache.lucene.queryparser.classic.ParseException;
import org.apache.lucene.queryparser.classic.QueryParser;
import org.apache.lucene.search.IndexSearcher;
import org.apache.lucene.search.Query;
import org.apache.lucene.search.TopDocs;
import org.apache.lucene.store.FSDirectory;
import org.apache.lucene.util.BytesRef;

public class indexComparison {

    public static final String index_dir = "E:\\IUB\\Search\\Assignment 1\\index_folder_";

    private static void SearchQuery(String input,String path) throws IOException, ParseException{
        IndexReader reader = DirectoryReader.open(FSDirectory.open(Paths.get(path)));
        IndexSearcher searcher = new IndexSearcher(reader);
        Analyzer analyzer = new StandardAnalyzer();
        QueryParser parser = new QueryParser("TEXT", analyzer);
        Query query = parser.parse(input);
        TopDocs results = searcher.search(query, 10);
        System.out.println("Hits: "+results.totalHits);

        reader.close();
    }
    private static void printing_stats(String path) throws IOException{

        IndexReader indexReader = DirectoryReader.open(FSDirectory.open(Paths.get(path)));
        Terms vocabulary = MultiFields.getTerms(indexReader,"TEXT");

        System.out.println("Total Number of documents in Corpus is = " +indexReader.maxDoc());

        System.out.println("Number of documents containing the term\"new\" for field\"TEXT\": "+indexReader.docFreq(new Term("TEXT","new")));

        System.out.println("Number of occurences of\"new\" in the field\"TEXT\": "+indexReader.totalTermFreq(new Term("TEXT","new")));

        System.out.println("Size of the vocabulary for TEXT field:"+vocabulary.size());

        System.out.println("Number of documents that have at least one term for TEXT field: " +vocabulary.getDocCount());

        System.out.println("Number of tokens for TEXT field:"+vocabulary.getSumTotalTermFreq());

        System.out.println("Number of postings for TEXT field:"+vocabulary.getSumDocFreq());
       /* TermsEnum iterator = vocabulary.iterator();
        BytesRef byteRef;
        System.out.println("\n*******Vocabulary-Start**********");

        while((byteRef = iterator.next()) !=null)
        {
            String term = byteRef.utf8ToString();
            System.out.print(term+"\t");
        }
        System.out.println("\n*******Vocabulary-End**********");*/
        indexReader.close();
    }

    public static void main(String[] args) throws IOException {
        generateIndex index = new generateIndex();
        List<Analyzer> analyzer_list = new ArrayList<>();
        String path="";
        analyzer_list.add(new StandardAnalyzer());
        analyzer_list.add(new SimpleAnalyzer());
        analyzer_list.add(new StopAnalyzer());
        analyzer_list.add(new KeywordAnalyzer());
        Scanner scn = new Scanner(System.in);
        System.out.println("Enter a query string");
        String input = scn.nextLine();

        for (Analyzer analyzerType : analyzer_list) {
            try {
                System.out.println("\n");
                System.out.println("Analyzing stats for analyzer: "+analyzerType);
                index.createIndex(analyzerType, Boolean.FALSE,analyzer_list.indexOf(analyzerType));
                path= index_dir+Boolean.FALSE.toString()+"_"+analyzer_list.indexOf(analyzerType);
                SearchQuery(input, path);
                printing_stats(path);
            } catch (ParseException ex) {
                Logger.getLogger(indexComparison.class.getName()).log(Level.SEVERE, null, ex);
            }
        }
    }
}