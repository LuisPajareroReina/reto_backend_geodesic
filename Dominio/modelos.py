"""
Clase dedicada a definir las clases y sus atributos
"""
from datetime import datetime

class Usuario:
    def __init__(self, id_usuario, id_perfil_acceso, nombre, apellido, empresa, password):
        self.id_usuario = id_usuario
        self.id_perfil_acceso = id_perfil_acceso
        self.nombre = nombre
        self.apellido = apellido
        self.empresa = empresa
        self.password = password
        # Lista con
        self.lista_puntos_acceso = []

    def check_login(self, input_password):
        return self.password == input_password

    def asignar_puntos_acceso(self, lista_puntos_acceso):
        """
        Rellenar la lista de accesos con objetos de la clase Punto
        """
        for punto in lista_puntos_acceso:
            self.lista_puntos_acceso.append(Punto(*punto))

    def check_acceso(self, id_punto):
        for punto in self.lista_puntos_acceso:
            if punto.id_punto == id_punto:
                return True

        return False

    def get_punto(self, id_punto):
        for punto in self.lista_puntos_acceso:
            if punto.id_punto == id_punto:
                return punto

        return None


class Punto:
    def __init__(self, id_punto, nombre_instalacion, descripcion):
        self.id_punto = id_punto
        self.nombre_instalacion = nombre_instalacion
        self.descripcion = descripcion

class RegistroAcceso:
    def __init__(self, id_registro, id_usuario, id_punto, fecha_hora_acceso=None):
        self.id_registro = id_registro
        self.id_usuario = id_usuario
        self.id_punto = id_punto
        self.fecha_hora_acceso = fecha_hora_acceso or datetime.now()


