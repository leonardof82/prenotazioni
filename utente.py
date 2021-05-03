class Utente():
    
    def __init__(self,nome,cognome,indirizzo,cf,email,numero,pw):
        self.Nome = nome
        self.Cognome = cognome
        self.indirizzo=indirizzo
        self.cf=cf
        self.Email = email
        self.numero = numero
        self.pw = pw

    def password (self,nuova_pw, vecchia_pw):
        if(self.pw==vecchia_pw):
            self.pw=nuova_pw
        else:
            print("la pass non concide")


    def stamp (self):
        print(" \nNome: %s  \nCognome: %s \nIndirizzo: %s \nCf: %s \nEmail: %s\nNumero: %s"%(self.Nome,self.Cognome,self.indirizzo,self.cf,self.Email,self.numero))
class Messaggio():

    def __init__(self,contenuto,utente):
        self.contenuto = contenuto
        self.utente = utente
    
class Sms(Messaggio):

    def __init__(self,contenuto,utente):
        super().__init__(contenuto,utente)
        self.numero = self.utente.numero

    def invia(self):
        print("Messaggio: %s\nNumero: %s" % (self.contenuto,self.numero))


class Email(Messaggio):

    def __init__(self,contenuto,utente):
        super().__init__(contenuto,utente)
        self.email = self.utente.email   

'''class tavolo():
    def __init__(self,id_tavolo,n_max):
        self.id_tavolo=id_tavolo
        self.n_max=4
        self.calendario={}

    def prenota(self,n_utente,n_persone,data_ora):
        self.n_persone=n_persone'''


class Tavolo():

    def __init__(self,id_tavolo):
        self.id_tavolo = id_tavolo
        self.n_max = 4
        self.prenotazioni = []

    def prenota(self,utente,npersone,data,ora):
        if (0 < npersone <= self.n_max):
            if(not(self.prenotato(data,ora))):
                self.prenotazioni.append(Prenotazione(utente,data,ora,npersone))          
                print("\nPrenotazione effettuata a nome di %s , per %d persone.\nData e ora: %s\n" %(utente.nome.title()+" "+utente.cognome.title(),npersone,data+" "+ora))

            else:
                print("Il tavolo è già prenotato per questa data e ora!")
        else:
            print("Il numero di persone è superiore a 4!")
              
    
    def prenotato(self,data,ora):
        for pr in self.prenotazioni:
            if(pr.data == data and pr.ora == ora):
                return True
            else:
                return False

    def stampacal(self):
        for pr in self.prenotazioni:
           print("Data: "+pr.data+" Ora: " +pr.ora)



class Prenotazione():

    def __init__(self,utente,data,ora,npersone):
        self.utente = utente
        self.data = data
        self.ora = ora
        self.npersone = npersone
        



myUtente = Utente("leonardo","fiorini","via leoncavallo","frnlrd582jstrneh","pagani21@virgilio.it","328517485")
mess_num = Sms("Contenuto",myUtente)
mess_num.invia() 
myUtente.stamp()    











'''def password (self):
        vecchia_pw=input("inserisci vecchia pass")
        if(self.pw==vecchia_pw):
            nuova_pw=input("inserisci nuova pass")
            self.pw=nuova_pw
            print(self.pw) '''