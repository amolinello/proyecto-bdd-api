El programa en main.py es una api creada por fastapi para consultar en formato JSON la información de un cliente según su ID,
trae información como Id, user, passw, email, state y last_log consultado desde la base de datos.

El archivo db_conexion.py se encarga de la conexión y las consultas en la base de datos, creando una clase, usando metodos
de clase y POO, sin usar pool de conexiónes para la bd.