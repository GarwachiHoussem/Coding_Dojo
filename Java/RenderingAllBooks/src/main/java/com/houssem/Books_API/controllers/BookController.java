package com.houssem.Books_API.controllers;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

import com.houssem.Books_API.models.Book;
import com.houssem.Books_API.services.BookService;

@Controller
public class BookController {
@Autowired
BookService bookservice;


@GetMapping("/")
public String index(){
return"redirect:books";	
}
@GetMapping("/books")
public String show(Model model){
	List<Book> books = bookservice.allBooks();
	model.addAttribute("Book", books);
	
return"index.jsp";	
}


}
