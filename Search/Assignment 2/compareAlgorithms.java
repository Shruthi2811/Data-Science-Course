/**
 * Created by Vipul Munot on 10/9/2016.
 */
import java.io.*;
import java.nio.file.Paths;
import org.apache.lucene.search.*;
import org.apache.lucene.index.*;
import org.apache.lucene.analysis.Analyzer;
import org.apache.lucene.store.FSDirectory;
import org.apache.lucene.document.Document;
import org.apache.lucene.queryparser.classic.*;
import org.apache.lucene.search.similarities.*;
import org.apache.lucene.analysis.standard.StandardAnalyzer;

public class compareAlgorithms {

    final String OpenTag = "<top>";
    final String closeTag = "</top>";
    FileWriter shortDesc;
    FileWriter longDesc;
    IndexReader reader;
    IndexSearcher indexSearch;
    Analyzer analyzer;
    QueryParser parser;

    private BufferedReader textReader;

    String file_path;

    compareAlgorithms(String file_path, String similarity){

        this.file_path = file_path;

        try {
            reader = DirectoryReader.open(FSDirectory.open(Paths.get("E:\\IUB\\Search\\Assignment 2\\index\\")));	} catch (IOException e) {
            e.printStackTrace();
        }

        indexSearch = new IndexSearcher(reader);
        setSimilarity(similarity);

        analyzer =	new	StandardAnalyzer();
        parser = new QueryParser("TEXT", analyzer);

        try {
            shortDesc = new FileWriter(similarity + "shortQueryResults.txt");
            longDesc = new FileWriter(similarity + "longQueryResults.txt");
        } catch (IOException e) {
            e.printStackTrace();
        }

        try
        {
            textReader = new BufferedReader(new FileReader(file_path));
        }
        catch (IOException ioexception)
        {
            System.out.println("File Not Found");
        }
    }

    void setSimilarity(String similarity)
    {
        switch(similarity)
        {
            case "BM25":
                indexSearch.setSimilarity(new BM25Similarity());
                break;
            case "LMDirichlet":
                indexSearch.setSimilarity(new LMDirichletSimilarity());
                break;
            case "LMJelinekMercer":
                indexSearch.setSimilarity(new LMJelinekMercerSimilarity((float) 0.7));
                break;
            case "Classic":
                indexSearch.setSimilarity(new ClassicSimilarity());
                break;
        }
    }

    public void inputRead()
    {
        try
        {
            String line = textReader.readLine();
            boolean start = false;
            String num = "";
            String title = "";
            String desc = "";

            while (line != null)
            {
                if(line.contains(OpenTag))
                {
                    start = true;
                    num = "";
                    title = "";
                    desc = "";
                }
                while(!line.contains(closeTag) && start)
                {
                    if(line.contains("<num>"))
                    {
                        while(!(line.contains("<dom>")))
                        {
                            num+= line + " ";
                            line = textReader.readLine();
                        }
                    }
                    if(line.contains("<title>"))
                    {
                        while(!(line.contains("<desc>")))
                        {
                            title+= line + " ";
                            line = textReader.readLine();
                        }
                    }
                    if(line.contains("<desc>"))
                    {
                        while(!(line.contains("<smry>")))
                        {
                            desc+= line + " ";
                            line = textReader.readLine();
                        }
                    }
                    line = textReader.readLine();
                }
                if(line.contains(closeTag))
                {
                    start = false;
                    desc = desc.substring(20).trim();
                    num = num.substring(14).trim();
                    title = title.substring(15).trim();
                    comparison(title,num,"run-short");
                    comparison(desc,num,"run-long");
                }
                line = textReader.readLine();
            }
            textReader.close();

        } catch (IOException e)
        {
            e.printStackTrace();
        }
    }

    public void comparison(String queryString, String num, String lengthType)

    {

        Query query;

        try {

            TopScoreDocCollector ranker = TopScoreDocCollector.create(1000);

            query = parser.parse(queryString);

            indexSearch.search(query, ranker);


            ScoreDoc[] docs = ranker.topDocs().scoreDocs;


            for(int i = 0; i < docs.length; i++) {

                Document doc = indexSearch.doc(docs[i].doc);
                String outputline = num +" " + 0 + " "+ doc.get("DOCNO") + " "+ (i+1) + " " +docs[i].score + " " + lengthType + "\n";
                System.out.println(outputline);
                write_file(outputline,lengthType);

            }



        } catch (ParseException | IOException e) {

            e.printStackTrace();

        }


    }


    private void write_file(String outputline, String lengthType) {
        try {
            if(lengthType.equals("run-short"))
            {
                shortDesc.append(outputline);
            }
            else
            {
                longDesc.append(outputline);
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }




    public static void main(String[] args) throws IOException {
        BufferedReader indexed = new BufferedReader(new InputStreamReader(System.in));
        String query_path;
        final String classic = "Classic";
        final String lmdir = "LMDirichlet";
        final String lmje = "LMJelinekMercer";
        final String bm25 = "BM25";
        String simAlgo = classic;
        int Userchoice =1;
        query_path = "E:\\IUB\\Search\\Assignment 2\\topics.51-100";
        System.out.println("Enter algorithm choice" +
                "1: BM25\n" +
                "2: LMDirichlet\n" +
                "3: LMJelinekMercer\n" +
                "4: Classic\n");

        Userchoice = Integer.parseInt(indexed.readLine());
        switch(Userchoice){
            case 1: simAlgo = bm25; break;
            case 2: simAlgo = lmdir; break;
            case 3: simAlgo = lmje; break;
            case 4: simAlgo = classic;
            default: break;
        }
        compareAlgorithms comparison = new compareAlgorithms(query_path,simAlgo);
        comparison.inputRead();
        comparison.longDesc.close();
        comparison.shortDesc.close();
        comparison.reader.close();
        System.out.println("files created");

    }
}