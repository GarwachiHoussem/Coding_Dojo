package com.houssem.Project.controllers;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;

import com.houssem.Project.models.Musicien;
import com.houssem.Project.models.User;
import com.houssem.Project.services.MusicienService;
import com.houssem.Project.services.UserService;

import jakarta.servlet.http.HttpSession;
import jakarta.validation.Valid;


@Controller 
public class MusicienController {
	@Autowired
	MusicienService musicienService;
	@Autowired
	UserService userServ;
	
	@GetMapping("/songs")
	public String homesong(Model model ,HttpSession s) {
		// Guard route
        Long userId = (Long) s.getAttribute("userId");
        if (userId == null) {
            return "redirect:/";
        }
        
       User loggedsUser = userServ.findById(userId);
        List<Musicien> songs = musicienService.allsongs();
		model.addAttribute("songs", songs);
		model.addAttribute("user", loggedsUser);
		
		return "dashboard.jsp";	
	}
	
	@GetMapping("/songs/new")
	public String song(@ModelAttribute("song") Musicien song, Model model) {
		
		return "song.jsp";
		}
	@PostMapping("/songs/new")
	public String song(@Valid @ModelAttribute("song") Musicien song, BindingResult result, Model model, HttpSession s) {
		if(result.hasErrors()) {
//			List<Song> songs = songService.allsongs();
//			model.addAttribute("songs", songs);
			
			return "song.jsp";
		}else {
			Long userId = (Long) s.getAttribute("userId");
	        User user=userServ.findById(userId);
	        song.setPerson(user);
	        musicienService.createSong(song);
			return "redirect:/songs";
		}
	}
	;
	@GetMapping("/songs/{id}/edit")
	public String edit(@PathVariable("id") Long id, Model model,HttpSession s ) {
		// Guard route
        Long userId = (Long) s.getAttribute("userId");
        if (userId == null) {
            return "redirect:/";
        }
		model.addAttribute("song", musicienService.findSong(id));
		return "edit.jsp";
	}
	
	@PutMapping("/songs/{id}/edit")
	public String update(
			@PathVariable("id") Long id, 
			Model model, 
			@Valid @ModelAttribute("song") Musicien song, 
			BindingResult result) {
		if(result.hasErrors()) {
			model.addAttribute("song", musicienService.findSong(id));
			return "redirect:/{id}/edit";
		}else {
	        Musicien existingSong = musicienService.findSong(id);
	        if (existingSong != null) {
	            int colabs = existingSong.getColabs();
	            song.setColabs(colabs + 1);

	          
	            musicienService.updateSong(song);
	        }
	        // Redirect to the songs page
	        return "redirect:/songs";
	    }
	}
	
	@GetMapping("/songs/{id}")
	public String showSong(@PathVariable("id") Long id, Model model) {
		model.addAttribute("song", musicienService.findSong(id));
		return "show.jsp";
	}
	@DeleteMapping("/songs/{id}/delete")
	public String deleteSong(@PathVariable("id") Long id) {
	Musicien song=  musicienService.findSong(id);
	musicienService.deleteSong(song);
	return "redirect:/songs";
	}
	
	
}

