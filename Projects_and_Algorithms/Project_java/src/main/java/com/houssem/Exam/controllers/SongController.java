package com.houssem.Exam.controllers;

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

import com.houssem.Exam.models.Song;
import com.houssem.Exam.models.User;
import com.houssem.Exam.services.SongService;
import com.houssem.Exam.services.UserService;

import jakarta.servlet.http.HttpSession;
import jakarta.validation.Valid;


@Controller 
public class SongController {
	@Autowired
	SongService songService;
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
        List<Song> songs = songService.allsongs();
		model.addAttribute("songs", songs);
		model.addAttribute("user", loggedsUser);
		
		return "dashboard.jsp";	
	}
	
	@GetMapping("/songs/new")
	public String song(@ModelAttribute("song") Song song, Model model) {
		
		return "song.jsp";
		}
	@PostMapping("/songs/new")
	public String song(@Valid @ModelAttribute("song") Song song, BindingResult result, Model model, HttpSession s) {
		if(result.hasErrors()) {
//			List<Song> songs = songService.allsongs();
//			model.addAttribute("songs", songs);
			
			return "song.jsp";
		}else {
			Long userId = (Long) s.getAttribute("userId");
	        User user=userServ.findById(userId);
	        song.setPerson(user);
			songService.createSong(song);
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
		model.addAttribute("song", songService.findSong(id));
		return "edit.jsp";
	}
	
	@PutMapping("/songs/{id}/edit")
	public String update(
			@PathVariable("id") Long id, 
			Model model, 
			@Valid @ModelAttribute("song") Song song, 
			BindingResult result) {
		if(result.hasErrors()) {
			model.addAttribute("song", songService.findSong(id));
			return "redirect:/{id}/edit";
		}else {
	        Song existingSong = songService.findSong(id);
	        if (existingSong != null) {
	            int colabs = existingSong.getColabs();
	            song.setColabs(colabs + 1);

	          
	            songService.updateSong(song);
	        }
	        // Redirect to the songs page
	        return "redirect:/songs";
	    }
	}
	
	@GetMapping("/songs/{id}")
	public String showSong(@PathVariable("id") Long id, Model model) {
		model.addAttribute("song", songService.findSong(id));
		return "show.jsp";
	}
	@DeleteMapping("/songs/{id}/delete")
	public String deleteSong(@PathVariable("id") Long id) {
	Song song=  songService.findSong(id);
	songService.deleteSong(song);
	return "redirect:/songs";
	}
	
	
}

