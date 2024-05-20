package com.houssem.Project.repositories;

import java.util.List;

import org.springframework.data.repository.CrudRepository;

import com.houssem.Project.models.Musicien;

public interface MusicienRepository extends CrudRepository<Musicien, Long> {
	List<Musicien> findAll();

}
