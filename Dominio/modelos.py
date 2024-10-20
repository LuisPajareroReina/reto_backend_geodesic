"""
Clase dedicada al core del backend y definir las clases
"""


class Usuario:
    def __init__(self, id_usuario, id_perfil_acceso, nombre, apellido, empresa, password):
        self.id_usuario = id_usuario
        self.id_perfil_acceso = id_perfil_acceso
        self.nombre = nombre
        self.apellido = apellido
        self.empresa = empresa
        self.password = password

    def printUsuario(self):
        return {
            'id_usuario': self.id_usuario,
            'id_perfil_acceso': self.id_perfil_acceso,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'empresa': self.empresa,
            'password': self.password
        }
