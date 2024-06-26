package com.houssem.Books_API.services;

import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.houssem.Books_API.models.Book;
import com.houssem.Books_API.repositories.BookRepository;

@Service
public class BookService {

	//BUSINESS LOGIC
	// CRUD
	
	//DEPENDENCY INJECTION
	// adding the book repository as a dependency(bookRepo)
	@Autowired
	private BookRepository bookRepo;
	
	// READ ALL
	public List<Book> allBooks(){
		return bookRepo.findAll();
	}
	
	// CREATE
	public Book createBook(Book b) {
		return bookRepo.save(b);
	}
	
	
	// READ ONE
	public Book findBookById(Long id) {
		Optional<Book> maybeBook = bookRepo.findById(id);
		if(maybeBook.isPresent()) {
			return maybeBook.get();
		}else {
			return null;
		}
	}
	
	// UPDATE
	public Book updateBook(Book b) {
		return bookRepo.save(b);
	}
	
	// DELETE
	public void deleteBook(Long id) {
		bookRepo.deleteById(id);
	}

	public Book updateBook(Long id, String title, String desc, String lang, Integer numOfPages) {
		// TODO Auto-generated method stub
		return null;
	}
	
	
	
	

}
