package com.houssem.Omikuji_Form.controllers;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

import jakarta.servlet.http.HttpSession;

@Controller


public class MainController {
	@GetMapping("/omikuji")
	public String index() {

		return "index.jsp";
	}
	
	@PostMapping("/processForm")
	public String show(@RequestParam("number") Integer number,
						@RequestParam("city") String city,
						@RequestParam("person") String person,
						@RequestParam("hobby") String hobby,
						@RequestParam("living") String living,
						@RequestParam("say") String say,
						HttpSession session) {
		System.out.println(number +city+ person+ hobby+ living+
				say+"dsfdsfsdsd");
		session.setAttribute("number", number);
		session.setAttribute("city", city);
		session.setAttribute("person", person);
		session.setAttribute("hobby", hobby);
		session.setAttribute("living", living);
		session.setAttribute("say", say);

		return "redirect:/omikuji/show";
	}
	@GetMapping("/omikuji/show")
	public String show() {

		return "show.jsp";
	}
	
	
	
	
	
	
}


