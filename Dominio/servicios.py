"""
En esta clase se definen los casos de uso del problema
"""
from Dominio.modelos import Usuario, Punto, RegistroAcceso


class ServicioUsuario:
    def __init__(self, usuario_modelo):
        self.usuario_modelo = usuario_modelo

    def get_usuario(self, id_usuario):
        datos_usuario = self.usuario_modelo.get_usuario_bbdd(id_usuario)
        if datos_usuario:
            return Usuario(*datos_usuario)
        return None

    def get_puntos_acceso(self, id_usuario):
        puntos_acceso = self.usuario_modelo.get_puntos_acceso_bbdd(id_usuario)
        if puntos_acceso:
            return puntos_acceso
        return None

    def get_instalaciones_acceso(self, id_usuario):
        instalaciones_acceso = self.usuario_modelo.get_instalaciones_acceso_bbdd(id_usuario)
        if instalaciones_acceso:
            return instalaciones_acceso
        return None

    def get_perfil_acceso(self, id_usuario):
        perfil_acceso = self.usuario_modelo.get_perfil_acceso_bbdd(id_usuario)
        if perfil_acceso:
            return perfil_acceso
        return None

    def detele_usuario(self, id_usuario):
        response = self.usuario_modelo.delete_usuario_bbdd(id_usuario)
        return response

    def detele_acceso_punto(self, usuario, id_punto):
        response = self.usuario_modelo.detele_acceso_punto_bbdd(usuario,id_punto)
        return response
    def add_acceso_punto(self, usuario, id_punto):
        response = self.usuario_modelo.add_acceso_punto_bbdd(usuario,id_punto)
        return response

class ServicioPunto:
    def __init__(self, punto_modelo):
        self.punto_modelo = punto_modelo

    def get_punto(self, id_punto):
        datos_punto = self.punto_modelo.get_punto_bbdd(id_punto)
        if datos_punto:
            return Punto(*datos_punto)
        return None

class ServicioRegistroAcceso:
    def __init__(self, registro_modelo):
        self.registro_modelo = registro_modelo

    def set_registro(self, id_usuario, id_punto, datetime):
        registro_acceso = RegistroAcceso(id_usuario, id_punto, datetime)
        registro_acceso.set_registro(self.registro_modelo)



