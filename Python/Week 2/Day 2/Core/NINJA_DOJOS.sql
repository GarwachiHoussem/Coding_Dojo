SELECT * FROM dojos_and_ninjas.ninjas;

INSERT INTO Ninjas (Dojo_id,first_name,last_name,age)
VALUES (1,"KACEM","gomri",55),(2,"YASSIN","tborski",24),(3,"BELHSAN","3amri",29);

INSERT INTO Ninjas (Dojo_id,first_name,last_name,age)
VALUES (1,"KACEM","gomri",55),(1,"YASSIN","tborski",24),(1,"BELHSAN","3amri",29);

INSERT INTO Ninjas (Dojo_id,first_name,last_name,age)
VALUES (2,"RAMI","gomri",55),(2,"RANIM","tborski",24),(2,"RANIA","3amri",29);


INSERT INTO Ninjas (Dojo_id,first_name,last_name,age)
VALUES (3,"RAbia","gomri",55),(3,"Rihab","tborski",24),(3,"Rihab","atari",29);

SELECT * FROM Ninjas WHERE Dojo_id =3;

SELECT * FROM ninjas Order By Dojo_id DESC LIMIT 1;

Select * FROM ninjas 
left join dojos on Dojo_id = Dojo_id where ninjas.id=12;

Select * FROM ninjas 
left join dojos on Dojo_id = Dojo_id;

