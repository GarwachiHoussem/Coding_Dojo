package com.houssem.Exam.models;

import java.util.Date;

import jakarta.persistence.Entity;
import jakarta.persistence.FetchType;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.Table;
import jakarta.validation.constraints.NotNull;
import jakarta.validation.constraints.Size;

@Entity
@Table(name="songs")
public class Song {
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private Long id;
	
	
	@NotNull
	@Size(min= 5, message="Title must be at least 5 characters")
	private String title;

	@NotNull
	@Size(min =5 , message="Genre must be at least 5 characters")
	private String genre;
	
	private int colabs=1;
	
	
	public int getColabs() {
		return colabs;
	}


	public void setColabs(int colabs) {
		this.colabs = colabs;
	}


	@NotNull
	@Size(min= 5, message="Lyrics must be at least 5 characters")
	private String lyrics;
	private Date updatedAt;
    
	// many to one
	@ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name="user_id")
    private User person;


	
	
	public Date getUpdatedAt() {
		return updatedAt;
	}


	public void setUpdatedAt(Date updatedAt) {
		this.updatedAt = updatedAt;
	}


	public User getPerson() {
		return person;
	}


	public void setPerson(User person) {
		this.person = person;
	}


	// Constructor
	public Song() {
		
	}


	// Getters&Setters
	public Long getId() {
		return id;
	}


	public void setId(Long id) {
		this.id = id;
	}


	public String getTitle() {
		return title;
	}


	public void setTitle(String title) {
		this.title = title;
	}





	public String getGenre() {
		return genre;
	}


	public void setGenre(String genre) {
		this.genre = genre;
	}


	public String getLyrics() {
		return lyrics;
	}


	public void setLyrics(String lyrics) {
		this.lyrics = lyrics;
	}


	
	
	
	
}
