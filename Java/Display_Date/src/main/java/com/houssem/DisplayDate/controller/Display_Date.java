package com.houssem.DisplayDate.controller;

import java.text.SimpleDateFormat;
import java.util.Date;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller

@RequestMapping("/")

public class Display_Date {
	@GetMapping("/")
	public String Home() {

		return "Display_Date.jsp";
	}

	@GetMapping("/date")
	public String Date(Model model) {

		SimpleDateFormat dddd = new SimpleDateFormat("EEE, d MMM yyyy");

		Date date = new Date();
		model.addAttribute("date", dddd.format(date));

		return "Date.jsp";
	}

	@GetMapping("/time")
	public String Time(Model model) {
		
		SimpleDateFormat tttt = new SimpleDateFormat ("hh 'o''clock' a");
		
		
		Date time = new Date();
		model.addAttribute("time", tttt.format(time));
		
		
		
		return "Time.jsp";
	}

}
