import psycopg2

class base_de_datos():
    # Conexión a db
    @classmethod
    def conexion_db(cls):
        cls.conn = psycopg2.connect(
            host= "localhost",
            port= "5433",
            user= "postgres",
            password= "admin",
            database= "proyecto_one",
        )
        return cls.conn
    # Cursor de db
    def cursor_api(self,):
        self.cursor_comandos = self.conexion_db().cursor()
        return self.cursor_comandos

    # SELECT en db según ID
    def seleccionar_id(self, id: int):
        self.comandos = self.cursor_api()
        self.comandos.execute(f'SELECT * FROM login_users_db WHERE id={id}')
        self.respuesta_valores = self.comandos.fetchall()
        if self.respuesta_valores == []:
            print(f'El "id={id}" no tiene información en la base de datos / No existente')
            return {}
        else:
            # Ejercicio: Seleccionar titulo columnas de la base de datos
            self.comandos.execute(f"SELECT column_name FROM information_schema.columns WHERE table_schema = 'public' and table_name ='login_users_db'")
            self.respuesta_titulos = self.comandos.fetchall()
            self.lista_titulos = [i[0] for i in self.respuesta_titulos ]
        # Devuelve un diccionario con Nombre de la columna y valor encontrado por id
        self.respuesta_consulta = dict(zip(self.lista_titulos, *self.respuesta_valores))
        self.comandos.close()
        self.cursor_comandos.close()
        self.conn.close()
        # Retorna un diccionario con {nombre columna: valor de la columna}
        return self.respuesta_consulta

if __name__ == '__main__':
    conexion = base_de_datos()
    print(conexion.seleccionar_id(1))
    