package tasks;

import java.io.*;
import java.util.*;
import models.Author;
import edu.uci.ics.jung.algorithms.scoring.PageRankWithPriors;
import edu.uci.ics.jung.graph.DirectedSparseGraph;



public class compute {
	public static HashMap<Integer, Integer> parseFile(
			DirectedSparseGraph<Integer, Integer> graph,
			HashMap<Integer, Author> names) {
		HashMap<Integer, Integer> reverseMapping = new HashMap<Integer, Integer>();
		try {
			BufferedReader in = new BufferedReader(new InputStreamReader(
					new FileInputStream("E:/IUB/Search/assignment 3/assignment3/author.net")));
			String line;
			int section = 0;
			int vertex_cnt = 0, edge_cnt = 0;
			while ((line = in.readLine()) != null) {
				if (line.contains("*")) {
					section++;
					continue;
				}

				StringTokenizer tokenizer = new StringTokenizer(line);
				if(section == 1) {
					Integer vertex = new Integer(tokenizer.nextToken());
					String name = tokenizer.nextToken().trim();
					names.put(vertex, new Author(vertex.toString(), name));
					reverseMapping.put(Integer.parseInt(name.substring(1,
							name.length() - 1)), vertex);
					graph.addVertex(vertex);
					vertex_cnt++;
				}

				else if (section == 2){
					Integer source = new Integer(tokenizer.nextToken());
					graph.addEdge(new Integer(edge_cnt), source, new Integer(
							tokenizer.nextToken()));
					edge_cnt++;

				}
			}
			in.close();
		} catch (Exception exp) {
			System.out.println("Exception while parsing " + exp.toString());
		}
		return reverseMapping;
	}

	public static void getTopAuthors(
			DirectedSparseGraph<Integer, Integer> graph,
			HashMap<Integer, Author> names,
			PageRankWithPriors<Integer, Integer> ranker) {
		ArrayList<Author> authorRanks = new ArrayList<Author>(names.size());
		for (Integer v : graph.getVertices()) {
			authorRanks.add(new Author(names.get(v), ranker.getVertexScore(v)));

		}

		Collections.sort(authorRanks, new Comparator<Author>() {

			public int compare(Author a1, Author a2) {
				return a2.get_rank().compareTo(a1.get_rank());
			}
		});

		System.out.println("Top 10 ranked authors are as following:");
		for (int i = 0; i < 10; i++) {
			System.out.println(authorRanks.get(i));
		}
	}
}
