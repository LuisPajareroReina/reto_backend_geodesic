"""
Clase dedicada a interactuar con la BBDD postgreSQL
"""

import psycopg2

class UsuarioBBDD:
    def __init__(self, config_bbdd):
        self.config_bbdd = config_bbdd

    def conexion_bbdd(self):
        # con **self.config_bbdd desempaquetamos el dict y lo pasamos como parametros
        conn = psycopg2.connect(**self.config_bbdd)
        return conn

    def get_usuario_bbdd(self, id_usuario):
        conn = self.conexion_bbdd()
        cur = conn.cursor()
        cur.execute("""
                    SELECT * FROM Usuarios
                    WHERE id_usuario = %s
                """, (id_usuario,))
        result = cur.fetchone()
        cur.close()
        conn.close()
        return result

    def get_puntos_acceso_bbdd(self, id_usuario):
        conn = self.conexion_bbdd()
        cur = conn.cursor()
        cur.execute("""
                            SELECT 
                                P.ID_punto,
                                P.nombre_instalacion,
                                P.descripcion
                            FROM 
                                Usuarios U
                            JOIN 
                                Perfil_acceso A ON U.ID_perfil_acceso = A.ID_perfil
                            JOIN 
                                Acceso_perfil_punto APP ON A.ID_perfil = APP.ID_perfil
                            JOIN 
                                Puntos P ON APP.ID_punto = P.ID_punto
                            WHERE 
                                U.ID_usuario = %s;
                        """, (id_usuario,))
        result = cur.fetchall()
        cur.close()
        conn.close()
        return result
