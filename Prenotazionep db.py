import peewee

db = peewee.SqliteDatabase('prenotazioni.db')

class Utente(peewee.Model):
    
    nome = peewee.CharField()
    cognome = peewee.CharField()
    indirizzo = peewee.CharField()
    cf = peewee.CharField()
    password = peewee.CharField()
    privacy = peewee.BooleanField()
    email = peewee.CharField()
    numero = peewee.CharField()


    class Meta:

        database = db
        db_table = 'utenti' 




class Tavolo(peewee.Model):

    ntavolo = peewee.IntegerField()
    nmax = peewee.IntegerField()


    class Meta:
        database = db
        db_table = 'tavoli'


class Prenotazione(peewee.Model):

    id_utente = peewee.IntegerField()
    id_tavolo = peewee.IntegerField()
    data = peewee.DateTimeField()
    ora = peewee.DateTimeField()

    class Meta:
        database = db
        db_table = 'prenotazioni'


Utente.create_table()
Tavolo.create_table()
Prenotazione.create_table()



