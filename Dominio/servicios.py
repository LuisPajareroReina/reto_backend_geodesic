"""
En esta clase se definen los casos de uso del problema
"""
from Dominio.modelos import Usuario


class UsuarioServicio:
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

