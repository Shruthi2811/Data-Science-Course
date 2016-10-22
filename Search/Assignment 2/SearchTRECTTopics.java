package Assignment2;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.lang.reflect.InvocationTargetException;

import org.apache.lucene.benchmark.quality.QualityQuery;
import org.apache.lucene.benchmark.quality.trec.TrecTopicsReader;
import org.apache.lucene.queryparser.classic.ParseException;
import org.apache.lucene.search.similarities.ClassicSimilarity;
import org.apache.lucene.search.similarities.Similarity;


public class SearchTRECTTopics {

	public static void out_top_results(Similarity similarity, String algorithmName) throws IOException, ParseException, IllegalAccessException, IllegalArgumentException, InvocationTargetException, NoSuchMethodException, SecurityException
	{
		// 1. Read the queries from trec topics
		TrecTopicsReader trecTopicReader = new TrecTopicsReader();
		BufferedReader bufferedReader = new BufferedReader(new FileReader(Intialize.topicPath));
		QualityQuery[] qualityQueries = trecTopicReader.readQueries(bufferedReader);

		// 2. Get calculate query score each document 
		for(int queryIndex=0; queryIndex < qualityQueries.length; queryIndex++)
		{
			QualityQuery qualityQuery = qualityQueries[queryIndex];
			String queryID = qualityQuery.getQueryID();

			{
				String titleQuery = qualityQuery.getValue(Intialize.queryTitle);
				String cleanedTitleQuery = title_cleaning(titleQuery);
				scoreTrack titleQueryScore = EasySearch.query_scores(cleanedTitleQuery, queryID, similarity);
				String OutputFilePath = Intialize.outputDir + "/" + algorithmName + "ShortQuery" + ".txt";
				titleQueryScore.write_top_results(OutputFilePath);

			}

			{
				String descQuery = qualityQuery.getValue(Intialize.queryDesc);
				String cleanedDescQuery = desc_cleaning(descQuery);
				scoreTrack descQueryScore = EasySearch.query_scores(cleanedDescQuery, queryID, similarity);
				String OutputFilePath = Intialize.outputDir + "/" + algorithmName + "LongQuery" + ".txt";
				descQueryScore.write_top_results(OutputFilePath);

			}


		}
		System.out.println("All the queries have executed successfully.");
	}

	public static String title_cleaning(String queryString)
	{
		String cleanedQuery = null;

		int colonIndex = queryString.indexOf(":");
		cleanedQuery = queryString.substring(colonIndex+1, queryString.length());

		return cleanedQuery;
	}

	public static String desc_cleaning(String queryString)
	{
		String cleanedQuery = null;

		int smryIndex = queryString.indexOf("<smry>");
		if(smryIndex != -1 )
		{
			cleanedQuery = queryString.substring(0, smryIndex);
		}

		return cleanedQuery;
	}

	public static void main(String[] args) {

		try {

			Similarity ClassicSimilarity = new ClassicSimilarity();
			out_top_results(ClassicSimilarity, "vipmunot_");
		} 
		catch (IOException e) {
			// TODO Auto-generated catch block
			System.out.println("Error While Reading topics");
			e.printStackTrace();
		} 
		catch (ParseException e) {
			// TODO Auto-generated catch block
			System.out.println("Error While processing queries");
			e.printStackTrace();
		}
		catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}


	}

}
