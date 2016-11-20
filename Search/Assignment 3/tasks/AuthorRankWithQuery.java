package tasks;

import java.io.*;
import java.util.HashMap;
import models.Author;
import org.apache.commons.collections15.Transformer;
import org.apache.lucene.analysis.Analyzer;
import org.apache.lucene.analysis.standard.StandardAnalyzer;
import org.apache.lucene.index.*;
import org.apache.lucene.queryparser.classic.*;
import org.apache.lucene.search.*;

import org.apache.lucene.search.similarities.BM25Similarity;
import org.apache.lucene.store.FSDirectory;


import edu.uci.ics.jung.algorithms.scoring.PageRankWithPriors;
import edu.uci.ics.jung.graph.DirectedSparseGraph;

public class AuthorRankWithQuery {

	static HashMap<Integer, Author> names;
	static double sumup = 0;

	public static void main(String[] args) throws  IOException,
			ParseException {
		// TODO Auto-generated method stub

		DirectedSparseGraph<Integer, Integer> graph = new DirectedSparseGraph<Integer, Integer>();
		names = new HashMap<Integer, Author>();

		HashMap<Integer, Integer> reverseMapping = compute.parseFile(
				graph, names);

		String query_lst[] = { "data mining" , "information retrieval", "machine learning" };
		for (String str : query_lst) {

			sumup = 0;
			for (Integer id : names.keySet())
				names.replace(id, new Author(names.get(id), 0.0));


			IndexReader reader = DirectoryReader.open(FSDirectory
					.open(new File("E:/IUB/Search/assignment 3/assignment3/author_index")));
			IndexSearcher searcher = new IndexSearcher(reader);
			Analyzer analyzer = new StandardAnalyzer();
			searcher.setSimilarity(new BM25Similarity());

			QueryParser parser = new QueryParser("content", analyzer);
			Query query = parser.parse(str);
			System.out.println("Searching for: " + query.toString("content"));

			TopDocs results = searcher.search(query, 300);
			ScoreDoc[] hits = results.scoreDocs;

			for (int i = 0; i < hits.length; i++) {

				org.apache.lucene.document.Document doc = searcher
						.doc(hits[i].doc);
				

				Author a = names.get(reverseMapping.get(Integer.parseInt(doc.get("authorid").toString())));
				names.replace(reverseMapping.get(Integer.parseInt(doc.get("authorid").toString())),
						new Author(a, a.get_rank() + hits[i].score));
				sumup += hits[i].score;

			}

			Transformer<Integer, Double> vertex_prior = new Transformer<Integer, Double>() {

				@Override
				public Double transform(Integer v) {
					return (double) names.get(v).get_rank() / sumup;
				}
			};

			PageRankWithPriors<Integer, Integer> ranker = new PageRankWithPriors<Integer, Integer>(
					graph, vertex_prior, 0.1);


			ranker.evaluate();

			compute.getTopAuthors(graph, names, ranker);

		}
	}

}
