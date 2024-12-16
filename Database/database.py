import peewee
import datetime
db = peewee.MySQLDatabase('Banco_de_Dados',
                          user="root",
                          password='admin',
                          host='127.0.0.1',
                          port=3306)
db.connect()
class Usuarios(peewee.Model):
    nome = peewee.CharField(20)
    email = peewee.CharField(40)
    inserido_data = peewee.DateField(default=datetime.datetime.now)
    class Meta:
        database = db

db.create_tables([Usuarios])

db.close()