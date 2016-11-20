package models;

public class Author {
	private String id;
	private String name;
	private Double rank;
	
	public Author(Author a, Double rank) {
		this.id = a.id;
		this.name = a.name;
		this.rank = rank;
	}
	
	public Author(String id, String name) {
		this.id = id;
		this.name = name;
		this.rank = 0.0;
	}
	
	public Author(String id, String name, Double rank) {
		this.id = id;
		this.name = name;
		this.rank = rank;
	}
	
	public String get_id() {
		return id;
	}
	
	public void set_id(String id) {
		this.id = id;
	}
	
	public String get_name() {
		return name;
	}
	
	public void set_name(String name) {
		this.name = name;
	}
	
	public Double get_rank() {
		return rank;
	}
	
	public void set_rank(Double rank) {
		this.rank = rank;
	}
	
	public String toString() {
		return this.name + " " + this.rank;
	}
}
