package com.houssem.Hopper.s_Receipt.controllers;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

@Controller

public class MainController {
	// class definition and imports here...
    @GetMapping("/")
    public String index(Model model) {
        
        String name = "Band Music";
        String itemName = "David Garett";
        double price = 100.25;
        String description = "Violin Solo Rock music";
        String vendor = "Germany Concerto";
    
    	// Your code here! Add values to the view model to be rendered
        model.addAttribute("name", name);
        model.addAttribute("itemName", itemName);
        model.addAttribute("price", price);
        model.addAttribute("description", description);
        model.addAttribute("vendor", vendor);
    
        return "index.jsp";
    }
    //...
    

}
