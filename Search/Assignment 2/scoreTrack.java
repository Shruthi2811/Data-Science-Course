package Assignment2;


import java.io.*;
import java.util.*;
import java.util.function.Consumer;


public class scoreTrack {

	public List<termScores> termScoresList;
	public Set<String> relevantDocumentIDs;
	private String queryID;
	
	public scoreTrack(String queryID)
	{
		this.queryID = queryID;
		termScoresList = new ArrayList<termScores>();
		relevantDocumentIDs = new HashSet<String>();
	}



	public void agg_query_tem_scores(termScores termScores)
	{
		termScoresList.add(termScores);
	}
	

	public double getDocumentScore(String docNo)
	{
		double documentScoreForQuery = 0;
		
		for(termScores termScores : termScoresList)
		{
			documentScoreForQuery += termScores.pull_DocScore(docNo);
		}
		
		return documentScoreForQuery;
	}

	public void agg_relevant_documents(String docNO)
	{
		relevantDocumentIDs.add(docNO);
	}

	public Map<String, Double> getDocumentIdToScoreMap()
	{
		Map<String, Double> documentScoreMap = new HashMap<String, Double>();
		
		for(String docNo : relevantDocumentIDs)
		{
			double score = this.getDocumentScore(docNo);
			documentScoreMap.put(docNo, score);
		}
		
		return documentScoreMap;
	}
	
	public void write_top_results(String outputFilePath) throws IOException {

		Map<String, Double> documentIdToScoreMap = this.getDocumentIdToScoreMap();
		
		File outputFile = new File(outputFilePath);
		outputFile.getParentFile().mkdirs();
		if(outputFile.exists() == false)
		{
			outputFile.createNewFile();
		}
		FileWriter fileWriter = new FileWriter(outputFile, true);
		
		print_score printscore = new print_score(fileWriter, this.queryID);

		documentIdToScoreMap.entrySet().stream()
		.sorted(Collections.reverseOrder(Map.Entry.comparingByValue()))
		.limit(1000).forEachOrdered(printscore);
		
		fileWriter.flush();
		fileWriter.close();
	}

	
}
class termScores {

    public Map<String, Double> documentIdToScoreMap;
    private String queryTermString;


    public termScores(String queryTerm) {
        this.queryTermString = queryTerm;
        documentIdToScoreMap = new HashMap<String, Double>();
    }


    public void agg_documentScore(String docNO, double score) {
        documentIdToScoreMap.put(docNO, score);
    }

    public double pull_DocScore(String docNo) {
        double documentScore = 0;
        if (documentIdToScoreMap.containsKey(docNo)) {
            documentScore = documentIdToScoreMap.get(docNo);
        }
        return documentScore;
    }
}

class print_score implements Consumer<Map.Entry<String, Double>> {


    private FileWriter fileWriter;
    private String queryID;
    private int documentRank;

    public print_score(FileWriter fileWriter, String queryID) {
        // TODO Auto-generated constructor stub
        this.fileWriter = fileWriter;
        this.queryID = queryID;
        this.documentRank = 1;
    }

    public void accept(Map.Entry<String, Double> entry) {
        // TODO Auto-generated method stub
        try
        {
            String line = this.queryID + " "+ "Q0"+ " "+ entry.getKey()+ " "+ documentRank+ " "+ entry.getValue() + " "+ "run-1 \n";
            fileWriter.append(line);
            documentRank++;
        }
        catch(IOException e)
        {
            System.out.println("Unable to write- " + entry.getKey());
            e.printStackTrace();
        }
    }

}