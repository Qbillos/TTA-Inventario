import mysql.connector

# Establece la conexión con la base de datos
class DataBase:
    def __init__(self):
        self.connection=mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="tta" 
        )
        self.cursor = self.connection.cursor()
        



# sqlinsertar = "INSERT INTO `productos` (`id`, `nombre`, `precio`, `categoria`) VALUES (NULL, 'pinky', '782192', 'comida');"


# i= 0
# while i <= 10 :
#     db.cursor.execute(sqlinsertar)
#     db.connection.commit()
#     i = i + 1
    

