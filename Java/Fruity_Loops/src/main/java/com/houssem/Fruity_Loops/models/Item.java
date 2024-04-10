package com.houssem.Fruity_Loops.models;

public class Item {
	public String name;
	public Double price;
	
	
//CONSTRUCTOR
	public Item (String name, Double price) {
		this.name= name;
		this.price = price;
	}
	
	
	// Getter & Setters
	public String getName() {
		return name;
	}


	public void setName(String name) {
		this.name = name;
	}


	public Double getPrice() {
		return price;
	}


	public void setPrice(Double price) {
		this.price = price;
	}
	

}
