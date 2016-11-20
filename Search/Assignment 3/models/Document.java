package models;

public class Document {
	
	private Integer authorID;
	private Double rank;
	private String content;
	
	public Document(String authorID, String content) {
		this.authorID = Integer.parseInt(authorID);		
		this.content = content;
	}
	
	public Document(String authorID, Double rank, String content) {
		this.authorID = Integer.parseInt(authorID);
		this.rank = rank;
		this.content = content;
	}

	public Integer getAuthorID() {
		return authorID;
	}

	public void setAuthorID(String authorID) {
		this.authorID = Integer.parseInt(authorID);
	}

	public Double getRank() {
		return rank;
	}

	public void setRank(Double rank) {
		this.rank = rank;
	}

	public String getContent() {
		return content;
	}

	public void setContent(String content) {
		this.content = content;
	}

}
