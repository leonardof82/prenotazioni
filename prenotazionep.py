class Utente():
    
    def __init__(self,nome,cognome,indirizzo,cf,password,privacy,email,numero):
        self.nome = nome
        self.cognome = cognome
        self.indirizzo = indirizzo
        self.cf = cf
        self.password = password
        self.privacy = privacy
        self.email = email
        self.numero = numero

    def stampa(self):
        print("Nome: \t%s \nCognome: %s \nIndirizzo: %s \nCodice Fiscale: %s \nEmail: %s \nNumero: %s \nPassword: ******" % (self.nome,self.cognome,self.indirizzo,self.cf,self.email,self.numero))

    def modificaPw(self,oldPassword, newPassword):
        if(self.password == oldPassword):
            self.password = newPassword
            print("Password modificata con successo! password: %s"% self.password)
        else:
            print("Passowrd Errata!")
            
    def registrazione(self,lista):
        lista.append(self)
        print("Registrazione Effettuata!")


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


class Tavolo():

    def __init__(self,id_tavolo):
        self.id_tavolo = id_tavolo
        self.n_max = 4
        self.prenotazioni = []

    def prenota(self,utente,npersone,data,orai,n_ore=2):
 
        if (0 < npersone <= self.n_max): #controllo  che le persone sono giuste
            if(not(self.prenotato(data,orai,n_ore))): #controllo che il tavolo non sia prenotato
                self.prenotazioni.append(Prenotazione(utente,npersone,data,orai,n_ore))          
                print("\nPrenotazione effettuata a nome di %s , per %d persone.\nData  %s e ora: %d.00\n" %(utente.nome.title()+" "+utente.cognome.title(),npersone,data+" ",orai))

            else:
                print("Il tavolo è già prenotato per questa data e ora!")
        else:
            print("Il numero di persone è superiore a 4!")
              
    
    def prenotato(self,data,orai,n_ore):
        oraf = orai+n_ore
        for pr in self.prenotazioni:
            if(pr.data == data and (pr.orai <= orai < pr.oraf or pr.orai < oraf <= pr.oraf)):
                return True
        return False

    def stampacal(self):
        for pr in self.prenotazioni:
           print("Data: %s Ora: %d.00 - %d.00"% (pr.data,pr.orai,pr.oraf))


class Prenotazione():

    def __init__(self,utente,npersone,data,ora,n_ore=2):
        self.utente = utente
        self.data = data
        self.orai = ora
        self.n_ore = n_ore
        self.oraf = self.orai+n_ore
        self.npersone = npersone





ListaUtenti = []
myUtente = Utente("Pietro","Ferrulli","Via Roma 123","frrptr123123123123","pippo123",True,"pppp@outlook.it","346123456")

myTavolo = Tavolo(1)


myTavolo.prenota(myUtente,2,"27/04/2021",13)
myTavolo.prenota(myUtente,2,"28/04/2021",12)
myTavolo.prenota(myUtente,4,"27/04/2021",15)
myTavolo.prenota(myUtente,3,"27/04/2021",12)

print("-----Calendario Tavolo-----")
myTavolo.stampacal()