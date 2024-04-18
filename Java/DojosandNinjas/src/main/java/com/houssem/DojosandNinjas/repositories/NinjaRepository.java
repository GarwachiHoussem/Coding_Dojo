package com.houssem.DojosandNinjas.repositories;

import java.util.List;


import org.springframework.data.repository.CrudRepository;

import com.houssem.DojosandNinjas.models.Dojo;
import com.houssem.DojosandNinjas.models.Ninja;

public interface NinjaRepository extends CrudRepository<Ninja, Long> {
	
	List<Ninja> findAll();
	List<Ninja> findAllByDojo(Dojo dojo);
}