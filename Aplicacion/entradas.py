from flask import Blueprint, request
from datetime import datetime

from Dominio.modelos import RegistroAcceso
from Infraestructura.postgresql import UsuarioBBDD, RegistroAccesoBBDD
from Dominio.servicios import ServicioUsuario, ServicioPunto

# Configuración de la conexión a la base de datos
config_bbdd = {
    'database': "reto_backend_geodesic",
    'user': "admin_geodesic",
    'host': 'localhost',
    'password': "admin",
    'port': "5433"
}

# FLASK
main = Blueprint('main', __name__)


@main.route('/<int:id_usuario>', methods=['GET'])
def login(id_usuario):
    # Obtener la contraseña desde el header
    password = request.headers.get('Authorization')

    usuario_bbdd = UsuarioBBDD(config_bbdd)
    servicio_usuario = ServicioUsuario(usuario_bbdd)
    usuario = servicio_usuario.get_usuario(id_usuario)

    if usuario:
        if usuario.check_login(password):
        # Login OK

            info_usuario = {
                'id_usuario': usuario.id_usuario,
                'Nombre': usuario.nombre,
                'Apellido': usuario.apellido,
                'Empresa': usuario.empresa
            }

            perfil_acceso = servicio_usuario.get_perfil_acceso(id_usuario)
            info_usuario['Perfil acceso'] = perfil_acceso
            lista_puntos_acceso = servicio_usuario.get_puntos_acceso(id_usuario)

            info_usuario['Puntos con acceso'] = lista_puntos_acceso
            lista_instalaciones_acceso = servicio_usuario.get_instalaciones_acceso(id_usuario)
            info_usuario['Instalaciones con acceso'] = lista_instalaciones_acceso

            return info_usuario

        else:
            return "Contraseña incorrecta"

    return "Usuario no existe/no se encuentra"


@main.route('/<int:id_usuario>/<int:id_punto>', methods=['GET'])
def acceder_punto(id_usuario, id_punto):
    #obtener la contraseña del header
    password = request.headers.get('Authorization')

    usuario_bbdd = UsuarioBBDD(config_bbdd)
    servicio_usuario = ServicioUsuario(usuario_bbdd)
    usuario = servicio_usuario.get_usuario(id_usuario)

    if usuario:
        if usuario.check_login(password):
            # Login OK
            lista_puntos_acceso = servicio_usuario.get_puntos_acceso(id_usuario)
            usuario.asignar_puntos_acceso(lista_puntos_acceso)
            if usuario.check_acceso(id_punto):
                # Acceso OK

                # Obtener información del punto
                punto = usuario.get_punto(id_punto)

                # Crear log
                registro_acceso = RegistroAcceso(None, id_usuario, id_punto, datetime.now())
                registro_acceso_bbdd = RegistroAccesoBBDD(config_bbdd)
                registro_acceso.set_registro(registro_acceso_bbdd)

                return (
                    f"Acceso al punto {id_punto} : {punto.descripcion}\n"
                    f"Usuario ID {id_usuario} : {usuario.nombre} {usuario.apellido}\n"
                    f"Fecha: {registro_acceso.fecha_hora_acceso}")

            else:

                return f"Acceso denegado al punto {id_punto}"

        else:
            return "Contraseña incorrecta"
    else:
        return "Usuario no se encuentra"


@main.route('/delete/<int:id_usuario>', methods=['DELETE'])
def delete_usuario(id_usuario):
    try:
        usuario_bbdd = UsuarioBBDD(config_bbdd)
        servicio_usuario = ServicioUsuario(usuario_bbdd)

        response = servicio_usuario.detele_usuario(id_usuario)
        return response
    except Exception as e:
        return {'error': str(e)}, 500

@main.route('/delete/<int:id_usuario>/<int:id_punto>', methods=['DELETE'])
def delete_acceso_punto(id_usuario, id_punto):
    try:
        usuario_bbdd = UsuarioBBDD(config_bbdd)
        servicio_usuario = ServicioUsuario(usuario_bbdd)
        usuario = servicio_usuario.get_usuario(id_usuario)

        response = servicio_usuario.detele_acceso_punto(usuario, id_punto)
        return response

    except Exception as e:
        return {'error': str(e)}, 500

@main.route('/add/<int:id_usuario>/<int:id_punto>', methods=['POST'])
def add_acceso_punto(id_usuario, id_punto):
    try:
        usuario_bbdd = UsuarioBBDD(config_bbdd)
        servicio_usuario = ServicioUsuario(usuario_bbdd)
        usuario = servicio_usuario.get_usuario(id_usuario)

        response = servicio_usuario.add_acceso_punto(usuario, id_punto)
        return response

    except Exception as e:
        return {'error': str(e)}, 500
