/**
 * Created by Vipul
 * Lucene version - 6.2.1
*/
import java.io.*;
import org.apache.lucene.analysis.Analyzer;
import org.apache.lucene.analysis.standard.StandardAnalyzer;
import org.apache.lucene.document.*;
import org.apache.lucene.util.*;
import org.apache.lucene.index.*;
import org.apache.lucene.index.IndexWriterConfig.OpenMode;

import org.apache.lucene.store.*;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.*;
import java.util.regex.*;


public class generateIndex {
    String files_dir = "E:\\IUB\\Search\\Assignment 1\\corpus";
    String index_dir = "E:\\IUB\\Search\\Assignment 1\\index_folder_";
    String INDEX_READER_DIRECTORY = "E:\\IUB\\Search\\Assignment 1\\index_folder_true_0";

    Pattern tags  = Pattern.compile("<DOC>(.+?)</DOC>", Pattern.DOTALL |Pattern.MULTILINE);
    List<String> headings= Collections.unmodifiableList(Arrays.asList("DOCNO", "HEAD","BYLINE","DATELINE","TEXT"));
    ArrayList<HashMap<String, String>> documents = new ArrayList();

    public void createIndex(Analyzer analyzer,Boolean FieldsCondition, Integer index) throws IOException {
        Directory directory = FSDirectory.open(Paths.get(index_dir+FieldsCondition.toString()+"_"+index));

        System.out.println(" Indexing to directory '" + index_dir+FieldsCondition.toString()+"_"+index);

        IndexWriterConfig iwc = new IndexWriterConfig(analyzer);
        iwc.setOpenMode(OpenMode.CREATE);
        IndexWriter indexWriter = new IndexWriter(directory, iwc);
        File dir = new File(files_dir);
        File[] files = dir.listFiles();
        for (File file : files) {
            String path = file.getCanonicalPath();
            String text = new String(Files.readAllBytes(Paths.get(path)), StandardCharsets.UTF_8);

            final List<String> tagValues = new ArrayList<>();
            final Matcher matcher = tags.matcher(text);
            while (matcher.find()) {
                tagValues.add(matcher.group(1));
            }

            for (String arg : tagValues) {
                HashMap<String, String> tempDoc = new HashMap<String, String>();
                String tagData = "";
                for (String indexValue : headings) {
                    String temp = "<"+indexValue+">(.+?)</"+indexValue+">";
                    tagData = getTagValuesInDoc(arg,Pattern.compile(temp, Pattern.DOTALL |Pattern.MULTILINE));
                    tempDoc.put(indexValue,tagData.replaceAll("[\\t\\n\\r]"," "));
                }
                documents.add(tempDoc);
            }
        }


        for (HashMap<String, String> document : documents) {
            indexDoc(indexWriter, document, FieldsCondition);
        }
        indexWriter.forceMerge(1);
        indexWriter.commit();
        indexWriter.close();
    }
    void printing_stats() throws IOException{

        IndexReader indexReader = DirectoryReader.open(FSDirectory.open(Paths.get(INDEX_READER_DIRECTORY)));

        System.out.println("Total Number of documents in Corpus is = " +indexReader.maxDoc());

        System.out.println("Number of documents containing the term\"new\" for field\"TEXT\": "+indexReader.docFreq(new Term("TEXT","new")));

        System.out.println("Number of occurences of\"new\" in the field\"TEXT\": "+indexReader.totalTermFreq(new Term("TEXT","new")));

        Terms vocabulary = MultiFields.getTerms(indexReader,"TEXT");

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

    private List<String> getTagValues(final String strToParse, final Pattern tagName) {
        final List<String> tagValues = new ArrayList<>();
        final Matcher matcher = tagName.matcher(strToParse);
        while (matcher.find()) {
            tagValues.add(matcher.group(1));
        }
        return tagValues;
    }

    private String getTagValuesInDoc(final String strToParse, final Pattern tagName) {
        String tagValues ="";
        final Matcher matcher = tagName.matcher(strToParse);
        while (matcher.find()) {
            if(!tagValues.isEmpty())
                tagValues=tagValues+" "+matcher.group(1);
            else
                tagValues=matcher.group(1);
        }
        return tagValues;
    }
    /** Indexes a single document
     * @throws IOException */
    static void indexDoc(IndexWriter writer, HashMap<String, String> document, Boolean FieldsCondition) throws IOException {
        // make a new, empty document
        Document lDoc = new Document();
        if (FieldsCondition){
            lDoc.add(new StringField("DOCNO", document.get("DOCNO"),Field.Store.YES));
            lDoc.add(new TextField("HEAD", document.get("HEAD"),Field.Store.YES));
            lDoc.add(new TextField("BYLINE", document.get("BYLINE"),Field.Store.YES));
            lDoc.add(new TextField("DATELINE", document.get("DATELINE"),Field.Store.YES));
            lDoc.add(new TextField("TEXT", document.get("TEXT"),Field.Store.YES));
        }else{
            lDoc.add(new TextField("TEXT", document.get("TEXT"),Field.Store.YES));
        }
        writer.addDocument(lDoc);
    }
    public static void main(String[] args) throws IOException {
        generateIndex index = new generateIndex();
        index.createIndex(new StandardAnalyzer(),Boolean.TRUE,0);
        index.printing_stats();
    }
}


/*
Output:
 Indexing to directory 'C:\Users\Ganesh\Desktop\Vipul\index_folder_true_0
Total Number of documents in Corpus is = 84474
Number of documents containing the term"new" for field"TEXT": 38604
Number of occurences of"new" in the field"TEXT": 83642
Size of the vocabulary for TEXT field:233384
Number of documents that have at least one term for TEXT field: 84456
Number of tokens for TEXT field:26649680
Number of postings for TEXT field:18049815
 */