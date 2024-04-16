package com.houssem.Books_API.repositories;

import java.util.List;

import org.springframework.data.repository.CrudRepository;

import com.houssem.Books_API.models.Book;

public interface BookRepository extends CrudRepository<Book, Long> {
	
	// Find All books 
	List<Book> findAll();

}
