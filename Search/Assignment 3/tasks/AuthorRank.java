package tasks;

import java.util.HashMap;

import models.Author;

import edu.uci.ics.jung.algorithms.scoring.PageRank;
import edu.uci.ics.jung.graph.DirectedSparseGraph;

public class AuthorRank {

	public static void main(String[] args) {
		
		DirectedSparseGraph<Integer, Integer> graph = new DirectedSparseGraph<Integer, Integer>();
		HashMap<Integer, Author> names = new HashMap<Integer, Author>();
		
		compute.parseFile(graph, names);
		
		PageRank<Integer, Integer> ranker = new PageRank<Integer, Integer>(graph, 0.1);

		ranker.evaluate();
		
		compute.getTopAuthors(graph, names, ranker);

	}

}
