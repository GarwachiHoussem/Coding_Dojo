package com.houssem.Books_API.controllers;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;

import com.houssem.Books_API.services.BookService;

@Controller
public class BookController {
@Autowired
BookService bookservice;


@GetMapping("/")
public String index(){
return"redirect:books";	
}
@GetMapping("/books/{id}")
public String show(Model model, @PathVariable("id") Long id){
	model.addAttribute("Book", bookservice.findBookById(id));
return"show.jsp";	
}


}
