package com.houssem.Daikichi_Path_Variables.controllers;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/daikichi")
public class Daikichi_Path_Variables {
	
	@GetMapping("/")
	public String Home () {
		return "Welcome!";
	}
	
	@GetMapping("/today")
	public String Today() {
		return "Today you will find luck in all your endeavors!";
	}
	@GetMapping("/tomorrow")
	public String Tomorrow() {
		return "Tomorrow, an opportunity will arise, so be sure to be open to new ideas";
	}
	@RequestMapping("/travel/{location}")
	public String travel (@PathVariable("location") String gps) {
		return "Congratulation! you will soon travel to "+ gps +"!";
	}
	
	@GetMapping("/lotto/{number}")
	public String lotto(@PathVariable("number") Integer number) {
		if(number%2==0) {
			return "You will take a grand journey in the near future, but be weary of tempting offers";
		}
		return "You have enjoyed the fruits of your labor but now is a great time to spend time with family and friends.";
	}


}
