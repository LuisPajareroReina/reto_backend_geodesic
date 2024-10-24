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
                                Perfil_acceso A ON U.ID_perfil_acceso = A.ID_perfil_acceso
                            JOIN 
                                Acceso_perfil_punto APP ON A.ID_perfil_acceso = APP.ID_perfil_acceso
                            JOIN 
                                Puntos P ON APP.ID_punto = P.ID_punto
                            WHERE 
                                U.ID_usuario = %s;
                        """, (id_usuario,))
        result = cur.fetchall()
        cur.close()
        conn.close()
        return result

    def get_instalaciones_acceso_bbdd(self, id_usuario):
        conn = self.conexion_bbdd()
        cur = conn.cursor()
        cur.execute("""
                            SELECT DISTINCT
                                P.nombre_instalacion
                            FROM 
                                Usuarios U
                            JOIN 
                                Perfil_acceso A ON U.ID_perfil_acceso = A.ID_perfil_acceso
                            JOIN 
                                Acceso_perfil_punto APP ON A.ID_perfil_acceso = APP.ID_perfil_acceso
                            JOIN 
                                Puntos P ON APP.ID_punto = P.ID_punto
                            WHERE 
                                U.ID_usuario = %s;
                        """, (id_usuario,))
        result = cur.fetchall()
        cur.close()
        conn.close()
        return result

    def get_perfil_acceso_bbdd(self, id_usuario):
        conn = self.conexion_bbdd()
        cur = conn.cursor()
        cur.execute("""
                            SELECT DISTINCT
                                A.descripcion
                            FROM 
                                Usuarios U
                            JOIN 
                                Perfil_acceso A ON U.ID_perfil_acceso = A.ID_perfil_acceso
                            WHERE 
                                U.ID_usuario = %s;
                        """, (id_usuario,))
        result = cur.fetchall()
        cur.close()
        conn.close()
        return result

    def delete_usuario_bbdd(self, id_usuario):
        conn = self.conexion_bbdd()
        cur = conn.cursor()

        # doble check
        cur.execute("""
                                SELECT id_usuario FROM Usuarios
                                WHERE id_usuario = %s;
                            """, (id_usuario,))

        check = cur.fetchone()

        if check:
            cur.execute("""
                                DELETE FROM Usuarios
                                WHERE id_usuario = %s;
                            """, (id_usuario,))
            conn.commit()
            result = f"Usuario [ID: {id_usuario}] ha sido eliminado."
            cur.close()
            conn.close()

            return result

        else:

            return f"El usuario [ID: {id_usuario}] no existe en la base de datos"




    def detele_acceso_punto_bbdd(self, usuario, id_punto):
        # Eliminar del perfil_acceso el punto asociado
        # pasos:
        #   1. identificar el ID_perfil_acceso --> usuario.id_perfil_acceso
        #   2. eliminar acceso_perfil_punto donde esté el id_punto

        id_perfil_acceso = usuario.id_perfil_acceso

        conn = self.conexion_bbdd()
        cur = conn.cursor()

        # doble check
        cur.execute("""
                   SELECT * FROM acceso_perfil_punto 
                   WHERE id_perfil_acceso = %s AND id_punto = %s
               """, (id_perfil_acceso, id_punto))

        check = cur.fetchone()

        if check:

            cur.execute("""
                                DELETE FROM acceso_perfil_punto
                                    WHERE id_perfil_acceso = %s AND id_punto = %s;      
                            """, (id_perfil_acceso, id_punto))
            conn.commit()
            result = f"El acceso al punto [ID: {id_punto}] ha sido eliminado para el usuario [ID: {usuario.id_usuario} | {usuario.nombre}]."
            cur.close()
            conn.close()
            return result

        else:
            return f"El usuario [ID: {usuario.id_usuario} | {usuario.nombre}] no tiene acceso al punto [ID: {id_punto}]"

    def add_acceso_punto_bbdd(self, usuario, id_punto):
        # Añadir al perfil_acceso el punto asociado
        # pasos:
        #   1. identificar el ID_perfil_acceso --> usuario.id_perfil_acceso
        #   2. añadir acceso_perfil_punto donde esté el id_punto

        id_perfil_acceso = usuario.id_perfil_acceso

        conn = self.conexion_bbdd()
        cur = conn.cursor()

        # doble check
        cur.execute("""
                   SELECT * FROM acceso_perfil_punto 
                   WHERE id_perfil_acceso = %s AND id_punto = %s
               """, (id_perfil_acceso, id_punto))

        check = cur.fetchone()

        if check:
            return f"El usuario [ID: {usuario.id_usuario} | {usuario.nombre}] ya tiene acceso al punto [ID: {id_punto}]"

        else:
            cur.execute("""
                            INSERT INTO acceso_perfil_punto VALUES
                                (%s,%s);      
                        """, (id_perfil_acceso, id_punto))
            conn.commit()
            result = f"Se ha concedido el acceso al punto [ID: {id_punto}] para el usuario [ID: {usuario.id_usuario} | {usuario.nombre}]."
            cur.close()
            conn.close()
            return result


class PuntoBBDD:
    def __init__(self, config_bbdd):
        self.config_bbdd = config_bbdd

    def conexion_bbdd(self):
        # con **self.config_bbdd desempaquetamos el dict y lo pasamos como parametros
        conn = psycopg2.connect(**self.config_bbdd)
        return conn

    def get_instalacion(self, id_punto):
        conn = self.conexion_bbdd()
        cur = conn.cursor()

        cur.execute("SELECT nombre_instalacion FROM Puntos WHERE id_punto = %s", id_punto)

        nombre_instalacion = cur.fetchall()

        cur.close()
        conn.close()

        if nombre_instalacion:
            return nombre_instalacion
        return None


class RegistroAccesoBBDD:
    def __init__(self, config_bbdd):
        self.config_bbdd = config_bbdd

    def conexion_bbdd(self):
        # con **self.config_bbdd desempaquetamos el dict y lo pasamos como parametros
        conn = psycopg2.connect(**self.config_bbdd)
        return conn

    def set_registro_acceso_bbdd(self, registro_acceso):
        """
        Crea un nuevo registro de acceso en la base de datos.
        """
        conn = self.conexion_bbdd()

        with conn.cursor() as cursor:
            query = """
                INSERT INTO Registro_acceso (id_usuario, id_punto, fecha_hora_acceso)
                VALUES (%s, %s, %s)
            """
            cursor.execute(query, (registro_acceso.id_usuario,
                                   registro_acceso.id_punto,
                                   registro_acceso.fecha_hora_acceso))
            conn.commit()

    def get_todos_registros_acceso_bbdd(self):
        conn = self.conexion_bbdd()
        cur = conn.cursor()

        cur.execute("SELECT * FROM Registro_acceso")
        registros = cur.fetchall()

        cur.close()
        conn.close()

        return registros if registros else []
