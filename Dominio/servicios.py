"""
En esta clase se definen los casos de uso del problema
"""
from Dominio.modelos import Usuario, Punto


class ServicioUsuario:
    def __init__(self, usuario_bbdd):
        self.usuario_bbdd = usuario_bbdd

    def get_usuario(self, id_usuario):
        datos_usuario = self.usuario_bbdd.get_usuario_bbdd(id_usuario)
        if datos_usuario:
            return Usuario(*datos_usuario)
        return None

    def get_puntos_acceso(self, id_usuario):
        puntos_acceso = self.usuario_bbdd.get_puntos_acceso_bbdd(id_usuario)
        if puntos_acceso:
            return puntos_acceso
        return None

    def get_instalaciones_acceso(self, id_usuario):
        instalaciones_acceso = self.usuario_bbdd.get_instalaciones_acceso_bbdd(id_usuario)
        if instalaciones_acceso:
            return instalaciones_acceso
        return None

    def get_perfil_acceso(self, id_usuario):
        perfil_acceso = self.usuario_bbdd.get_perfil_acceso_bbdd(id_usuario)
        if perfil_acceso:
            return perfil_acceso
        return None

    def detele_usuario(self, id_usuario):
        response = self.usuario_bbdd.delete_usuario_bbdd(id_usuario)
        return response

    def detele_acceso_punto(self, usuario, id_punto):
        response = self.usuario_bbdd.detele_acceso_punto_bbdd(usuario, id_punto)
        return response
    def add_acceso_punto(self, usuario, id_punto):
        response = self.usuario_bbdd.add_acceso_punto_bbdd(usuario, id_punto)
        return response


class ServicioRegistroAcceso:
    def __init__(self, registro_acceso_bbdd):
        self.registro_acceso_bbdd = registro_acceso_bbdd

    def set_registro(self, registro):
        self.registro_acceso_bbdd.set_registro_acceso_bbdd(registro)

    def get_todos_registros_acceso(self):
        response = self.registro_acceso_bbdd.get_todos_registros_acceso_bbdd()
        if response:
            return response
        return None


