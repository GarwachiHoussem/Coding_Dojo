package com.houssem.Exam.repositories;

import java.util.List;

import org.springframework.data.repository.CrudRepository;

import com.houssem.Exam.models.Song;

public interface SongRepository extends CrudRepository<Song, Long> {
	List<Song> findAll();

}
