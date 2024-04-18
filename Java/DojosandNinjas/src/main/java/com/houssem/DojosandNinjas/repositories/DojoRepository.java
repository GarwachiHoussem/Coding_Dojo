package com.houssem.DojosandNinjas.repositories;

import java.util.List;

import org.springframework.data.repository.CrudRepository;

import com.houssem.DojosandNinjas.models.Dojo;


public interface DojoRepository extends CrudRepository<Dojo, Long> {

	List<Dojo> findAll();
}