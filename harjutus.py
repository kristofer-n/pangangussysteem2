# Kristofer Nagaicevs IS24 11.02.25

# Parent Class
class User(): # loob klassi User 
    def __init__(self,name,age,gender): # initialiseerija, nime, vanuse ja soo atribuutidega
        self.name = name # määrab atribuudi
        self.age = age # määrab atribuudi
        self.gender = gender # määrab atribuudi

    def show_details(self): # meetod, sellel on ligipääs kõikidele atribuutidele ja meetodile, mis on selles klassis, näitab kasutajale oma andmeid
        print("Personal Details") # väljastab sõne
        print("") # väljastab sõne
        print("Name ", self.name) # väljastab sõne ja atribuudi väärtuse
        print("Age ", self.age) # väljastab sõne ja atribuudi väärtuse
        print("Gender ", self.gender) # väljastab sõne ja atribuudi väärtuse

#Child Class
class Bank(User): # loob klassi Bank, mis on User alamklass ja seega pärandab User klassi atribuudid ja meetodid
    def __init__(self,name,age,gender):  # initialiseerija samade atribuutidega, mis ülemklassil
        super().__init__(name,age,gender) # superfunktsioon praktiliselt kopeerib meetodi ülemklassist ja teeb uuesti
        self.balance = 0 # määrab arve peal oleva raha arvu

    def deposit(self,amount): # meetod deposiidi tegemiseks, sellel on klassi self atribuut kui ka amount atribuut
        self.amount = amount # määrab atribuudi
        self.balance = self.balance + amount # arvutab arve peal oleva raha arvu peale deposiiti
        print("Account balance has been updated : £", self.balance) # väljastab kasutajale info, et kui palju on arve peal raha

    def withdraw(self,amount): # meetod raha välja võtmiseks, sarnane deposiidi meetodiga
        self.amount = amount # määrab atribuudi
        if(self.amount > self.balance): # kui rohkem raha tahetakse välja võtta, kui kontos on:
            print("Insufficient Funds │ Balance Available : £", self.balance) # väljastab sõnumi, et pole piisavalt raha ja ütleb konto peal oleva raha summa
        else: # aga kui on piisavalt raha, et välja vätta tahetud summa
            self.balance = self.balance - self.amount # siis lahutatakse väljavõtva summa olevast rahast
            print("Account balance has been updated : £", self.balance) # väljastab kasutajale info, et kui palju on arve peal raha

    def view_balance(self): # meetod, mis näitab kasutajale, kui palju raha on kontol ja kasutaja andmeid.
        self.show_details() # kasutab meetodit, mis näitab kasutajale oma andmeid
        print("Account balance has been updated : £", self.balance) # väljastab kasutajale info, et kui palju on arve peal raha

# teine versioon