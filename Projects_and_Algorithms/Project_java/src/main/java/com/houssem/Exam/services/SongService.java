package com.houssem.Exam.services;

import java.util.List;
import java.util.Optional;

import org.springframework.stereotype.Service;

import com.houssem.Exam.models.Song;
import com.houssem.Exam.repositories.SongRepository;

@Service
public class SongService {
	private final SongRepository songRepository;
	
	
	public SongService(SongRepository songRepository) {
		this.songRepository= songRepository;
	}
	public List<Song> allsongs() {
		return songRepository.findAll();
	}

	public Song createSong(Song song) {
		return songRepository.save(song);
	}
	
	public Song findSong(Long id) {
		Optional<Song> optionalSong = songRepository.findById(id);
		if (optionalSong.isPresent()) {
			return optionalSong.get();
		} else {
			return null;
		}
	}

	public Song updateSong(Song song) {
		return songRepository.save(song);
	}

	
	public void deleteSong(Song song) {
		songRepository.delete(song);
	}
	
	
	
	
	
}
