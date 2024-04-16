package com.houssem.Books_API.controllers;

import java.util.List;

import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.houssem.Books_API.models.Book;
import com.houssem.Books_API.services.BookService;

@RestController
public class BooksApi {
	private final BookService bookService;

	public BooksApi(BookService bookService) {
		this.bookService = bookService;
	}

	// other methods removed for brevity
	@GetMapping("/api/books")
	public List<Book> getAllBook() {
		List<Book> bookList = bookService.allBooks();
		return bookList;
	}

	@RequestMapping(value="/api/books" , method= RequestMethod.POST)
	 public Book create(@RequestParam(value="title") String title, 
		 		@RequestParam(value="description") String desc, 
		 		@RequestParam(value="language") String lang,
		 		@RequestParam(value="pages") Integer numOfPages) {
		 			
		 			Book newBook= new Book(title,desc,lang,numOfPages );
		 					return bookService.createBook(newBook);
		 
	 }

	@RequestMapping(value="/api/books/{id}", method= RequestMethod.PUT)
	public Book update(@PathVariable("id") Long id,
			@RequestParam(value = "title") String title,
			@RequestParam(value = "description") String desc, 
			@RequestParam(value = "language") String lang,
			@RequestParam(value = "pages") Integer numOfPages) {
		Book book = new Book( title, desc, lang, numOfPages);
		book.setId(id);
		return bookService.createBook(book);
	}

	@DeleteMapping("/api/books/{id}")
	public void destroy(@PathVariable("id") Long id) {
		bookService.deleteBook(id);
	}

}
