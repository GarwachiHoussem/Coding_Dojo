package com.houssem.Counter.controllers;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;

import jakarta.servlet.http.HttpSession;

@Controller

public class CounterController {

	@GetMapping("/")
	public String index (HttpSession session) {
		
	Integer count = 0;
	if 
		(session.getAttribute("count") == null) {
		 session.setAttribute("count",0);}
	else 
	{
		count = (Integer) session.getAttribute("count");
		count++ ;
		session.setAttribute("count", count);
	}
		
			return "index.jsp";
	}

	@GetMapping("/counter")
	public String counter() {

		return "counter.jsp";
	}
	
	@GetMapping("/counterby2")
	public String counterbytwo(HttpSession session1) {
		Integer counttwo = 0;
		if 
			(session1.getAttribute("counttwo") == null) {
			 session1.setAttribute("counttwo",0);}
		else 
		{
			counttwo = (Integer) session1.getAttribute("counttwo");
			counttwo= counttwo+2 ;
			session1.setAttribute("counttwo", counttwo);
		}
		
		return "counterby2.jsp";
	}
	   @PostMapping("/reset")
	    public String reset(HttpSession session) {
	        session.setAttribute("count", 0);
	        session.setAttribute("counttwo", 0);
	        return "redirect:/";
	    }

}
