TRUNCATE TABLE public.acceso_perfil_punto;
--SELECT * FROM public.acceso_perfil_punto;

INSERT INTO acceso_perfil_punto (id_perfil, id_punto) VALUES
(1,1),
(1,2),

(2,3),

(3,3),
(3,4),
-- Carlos Rodriguez
(4,1),
(4,2),
(4,3),
(4,4),
(4,5),
(4,6),
(4,7),
-- Belen
(5,1),
(5,2),
(5,5),
(5,7),


(6,5),
(6,6),

(7,5),
(7,6),
(7,7),

(8,8),
(8,9),
(8,10),

(9,9),

(10,8),
(10,11),
(10,12),

(11,8),
(11,9),
(11,10),
(11,11),
(11,12);

SELECT * FROM public.acceso_perfil_punto;

TRUNCATE TABLE public.usuarios;

INSERT INTO Usuarios (ID_perfil_acceso, Nombre, Apellido, Empresa, password) VALUES
(1, 'Alberto', 'Villalba', 'GoFit Talavera', '123456789'), --1
(2, 'Juan', 'Aprendiz', 'GoFit Talavera', '123456789'), --2
(3, 'Lucas', 'Veterano', 'GoFit Talavera', '123456789'),--3
(4, 'Carlos', 'Rodriguez', 'GoFit Global', 'admin'),--4
(2, 'Lucia', 'Aprendiz', 'GoFit Talavera', '123456789'),--5
(5, 'Belen', 'Sainz', 'GoFit Global', '123456789'),--6
(6, 'Pedro', 'Gomez', 'GoFit Valladolid', '123456789'),--7
(6, 'Amancio', 'Sanchez', 'GoFit Valladolid', '123456789'),
(7, 'Maria', 'Martin', 'GoFit Valladolid', 'admin'),
(8, 'Javier', 'Morales', 'Nestle', '123456789'),
(9, 'Lucia', 'Lopez', 'Nestle', '123456789'),
(9, 'Mario', 'Sanz', 'Nestle', '123456789'),
(9, 'Juan', 'Rubio', 'Nestle', '123456789'),
(10, 'Paco', 'Jimenez', 'Nestle', '123456789'),
(11, 'Fernando', 'Alonso', 'Nestle', 'admin');