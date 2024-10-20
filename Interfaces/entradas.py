import psycopg2
from flask import Blueprint
from Infraestructura.postgresql import UsuarioBBDD
from Dominio.servicios import UsuarioServicio


# Configuración de la conexión a la base de datos
config_bbdd = {
    'database': "reto_backend_geodesic",
    'user': "admin_geodesic",
    'host': 'localhost',
    'password': "admin",
    'port': "5433"
}



usuario_bbdd = UsuarioBBDD(config_bbdd)

usuario_servicio = UsuarioServicio(usuario_bbdd)


# FLASK
main = Blueprint('main', __name__)
@main.route('/<id_usuario>', methods=['GET'])
def get_usuario_flask(id_usuario):
    usuario = usuario_servicio.get_usuario(id_usuario)

    if usuario:
        info_usuario = {
            'id_usuario': usuario.id_usuario,
            'Nombre' : usuario.nombre,
            'Apellido': usuario.apellido,
            'Empresa': usuario.empresa
        }

        lista_puntos_acceso = usuario_servicio.get_puntos_acceso(id_usuario)
        info_usuario['Puntos con acceso'] = lista_puntos_acceso
        return info_usuario

    return "Error obteninedo Usuario"

