-- Archivo para crear una base de datos de prueba
-- NOTA: SI LA BASE DE DATOS TE DICE QUE NO TIENES PERMISOS REVISAR EL OWNER DE LAS TABLAS PSQL

-- Eliminar el contenido de las tablas o las tablas mismas si no existen previamente
--DROP TABLE IF EXISTS Registro_acceso;
DROP TABLE IF EXISTS Usuarios;
DROP TABLE IF EXISTS Acceso_perfil_punto;
DROP TABLE IF EXISTS Puntos;
DROP TABLE IF EXISTS perfil_acceso;

CREATE TABLE Puntos (
    ID_punto SERIAL PRIMARY KEY,
    nombre_instalacion VARCHAR(100),
    descripcion VARCHAR(100)
);

CREATE TABLE Perfil_acceso (
    ID_perfil_acceso SERIAL PRIMARY KEY,
    descripcion VARCHAR(100)
);


CREATE TABLE Usuarios (
    ID_usuario SERIAL PRIMARY KEY,
    ID_perfil_acceso INT,
    Nombre VARCHAR(50),
    Apellido VARCHAR(50),
    Empresa VARCHAR(50),
    password VARCHAR(50),
    FOREIGN KEY (ID_perfil_acceso) REFERENCES Perfil_acceso(ID_perfil_acceso)
);

CREATE TABLE Acceso_perfil_punto (
    ID_perfil_acceso INT,
    ID_punto INT,
	FOREIGN KEY (ID_perfil_acceso) REFERENCES Perfil_acceso(ID_perfil_acceso),
	FOREIGN KEY (ID_punto) REFERENCES Puntos(ID_punto)
);

CREATE TABLE Registro_acceso (
    ID_registro SERIAL PRIMARY KEY,
    ID_usuario INT,
    ID_punto INT,
    fecha_hora_acceso TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (ID_usuario) REFERENCES Usuarios(ID_usuario),
    FOREIGN KEY (ID_punto) REFERENCES Puntos(ID_punto)
);



INSERT INTO puntos (nombre_instalacion, descripcion) VALUES
--1
('Gimnasio GoFit Talavera', 'Monitoreo de PH agua'),
('Gimnasio GoFit Talavera', 'Monitoreo de tensión eléctrica punto 1'),
('Gimnasio GoFit Talavera', 'Actuador Naranja'),
('Gimnasio GoFit Talavera', 'Actuador Verde'),
--5
('Gimnasio GoFit Valladolid', 'Monitoreo de PH agua'),
('Gimnasio GoFit Valladolid', 'Actuador Azul'),
('Gimnasio GoFit Valladolid', 'Contador de litros de agua'),
--8
('Nestle', 'Monitoreo de PH agua'),
('Nestle', 'Monitoreo nivel de agua'),
('Nestle', 'Válvula de vaciado'),
('Nestle', 'Actuador Naranja'),
('Nestle', 'Actuador Morado');



INSERT INTO perfil_acceso (descripcion) VALUES
('Monitoreo GoFit Talavera'), --1
('Actuador Naranja GoFit Talavera'), --2
('Actuadores GoFit Talavera'), --3
('Admin GoFit Talavera y Valladolid'), --4

('Monitoreo GoFit Talavera y Valladolid'), --5
('Mantenimiento GoFit Valladolid'), --6
('Admin GoFit Valladolid'), --7

('Monitoreo del tanque agua Nestle'), --8
('Trabajadores de la planta Nestle'), --9
('Mantenimiento del tanque de agua Nestle'), --10
('Admin Nestle'), --11
('Monitoreo GoFit Talavera y Valladolid'); --12



INSERT INTO acceso_perfil_punto (ID_perfil_acceso, id_punto) VALUES
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

