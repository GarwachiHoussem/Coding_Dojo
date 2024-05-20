package com.houssem.Project.services;

import java.util.List;
import java.util.Optional;

import org.springframework.stereotype.Service;

import com.houssem.Project.models.Musicien;
import com.houssem.Project.repositories.MusicienRepository;

@Service
public class MusicienService {
	private final MusicienRepository songRepository;
	
	
	public MusicienService(MusicienRepository songRepository) {
		this.songRepository= songRepository;
	}
	public List<Musicien> allsongs() {
		return songRepository.findAll();
	}

	public Musicien createSong(Musicien song) {
		return songRepository.save(song);
	}
	
	public Musicien findSong(Long id) {
		Optional<Musicien> optionalSong = songRepository.findById(id);
		if (optionalSong.isPresent()) {
			return optionalSong.get();
		} else {
			return null;
		}
	}

	public Musicien updateSong(Musicien song) {
		return songRepository.save(song);
	}

	
	public void deleteSong(Musicien song) {
		songRepository.delete(song);
	}
	
	
	
	
	
}
