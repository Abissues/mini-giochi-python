﻿import win32console, win32gui, win32con
import random
import os
import socket
import hashlib
import time
import datetime
import uuid
import platform
import subprocess
import tkinter as tk
from tkinter import messagebox


tempo = str(datetime.datetime.now().strftime("%H:%M:%S: %Y-%m-%d"))
hwnd = win32console.GetConsoleWindow()
if hwnd:
   hMenu = win32gui.GetSystemMenu(hwnd, 0)
   if hMenu:
       win32gui.DeleteMenu(hMenu, win32con.SC_CLOSE, win32con.MF_BYCOMMAND)


def menu(): #menu
    print("1-per chiudere")
    print("2-roulette")
    print("3-blackjack")
    print("4-indovina la carta")
    print("5-fondi")
    print("6-slot")
    print("7-dadi")
    print("8-informazioni-personali")
    print("9-riepilogo in html")
    print("10-cambio nome")
    print("11-sicurezza")

def html():
    f = open('giocate.txt','r')
    giocatori = f.readline()
    giocatori=int(giocatori)
    f.close()
    l=open('vincite.txt','r')
    vincite=l.readline()
    vincite=int(vincite)
    l.close()
    percentuale=vincite/giocatori
    percentuale1=percentuale*100
    f = open('stats.html','w+')
    message = """<html>
    <head></head>
    <body><p>Hai vinto """ + str(vincite) + """ partite hai giocato """ + str(giocatori) + """ partite la  percentuale è   """ + str(percentuale1) +  """% </p></body>
    </html>"""
    f.write(message)
    f.close()
    os.startfile('stats.html')

def scegli(): #scelta menu
    try:
        modalita = int(input("scegli la modalità di gioco "))
        while modalita not in [1,2,3,4,5,6,7,8,9,10,11]:
            print("modalità di gioco non disponibile ")
            modalita = int(input("scegli la modalità di gioco "))
        if modalita == 1:
            chiudere()
        if modalita == 2:
            roulette()
        if modalita == 3:
            blackjack()
        if modalita == 4:
            indovinalacarta()
        if modalita == 5:
            ricarica()
        if modalita == 6:
            slot()
        if modalita == 7:
            dadi()
        if modalita == 8:
            informazioni()
        if modalita == 9:
            html()
        if modalita == 10:
            cambianome()
        if modalita == 11:
            SICUREZZA()
    except ValueError:
        print("errore inserire solo numeri")
   
def SICUREZZA():
    if os.path.exists("sicurezza.txt") is False:
        x=input("vuoi mettere una password di sicurezza ")
        if x == "si":
            s=input("inserisci ")
            passW=open("sicurezza.txt","w+")
            f=passW.write(s)
            passW.close()
    else:
        d=input("vuoi eliminare ")
        if d=="si":
            os.remove("sicurezza.txt")
            
def password():
    if os.path.exists("sicurezza.txt") is False:
        pass
    else:
        x=input("inserisci password ")
        l=open("sicurezza.txt","r")
        f=l.readline()
        if f==x:
            pass
        else:
            exit()


hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
F = socket.gethostname()


def cambianome():
    x=random.randint(1000,9999)
    print(x)
    f=int(input("per piacere inserisci il codice di sicurezza "))
    vincita = open('fondi-giocatore.txt','r')
    soldi = vincita.readline()
    soldi = int(soldi)
    vincita.close()
    try:
       molti=open("molti.txt","r")
       fa=molti.readline()
       molti.close()
    except:
       molti=open("molti.txt","w+")
       molti.write(str(1))
       molti.close()
       molti=open("molti.txt","r")
       fa=molti.readline()
       molti.close()
    soldif=500*int(fa)
    if f==x:
        print("sono,sicuro di voler cambiare nome costo $ " + str(soldif) + ",premere si ")
        x=input()
        if x== "si":
            print("pagamento in corso")
            vincita=open("fondi-giocatore.txt","w")
            soldi=soldi-(500*int(fa))
            vincita.write(str(soldi))
            vincita.close()
            molti=open("molti.txt","w")
            fa=int(fa)+1
            molti.write(str(fa))
            print("pagamento riuscito")
            nuovo_nome=input("inserire nuovo nome ")
            cambio_nome=open("giocatore.txt",'w')
            cambio_nome.write(nuovo_nome)
            cambio_nome.close()
            os.execl("main.py")
    else:
        print("errore")

def ban(): #ban
    F = socket.gethostname()
    with open('ban.txt','r')  as f:
        for line in f:
            if line == F:
                print("sei stato bannato")
                print("mi spiace caro " + str(F) + " ergo il tuo saldo sarà azzerato + :)")
                pin=open("fondi-giocatore.txt",'w')
                pin.write("0")
                pin.close()
                time.sleep(9)
                exit()
                banned = open('ban.txt', 'r')
                banned.close()
                break


def lista(): #comandi extra
    print("soldi")


def giocatore():
    with open('giocatore.txt') as file:
        f = open('giocatore.txt','r')
        giocatori = f.readline()
        f.close()
    print("benvenuto")
    print(giocatori)
    

def comandi():
    comando = input("inserire comando")
    if comando == "soldi":
        soldi = open('fondi-giocatore.txt','r')
        soldi = soldi.readlines()
        print(soldi)





def bancav():
    patrimonioo = open('banca.txt','r')
    patrimonio = patrimonioo.readline()
    patrimonio = int(patrimonio)
    if patrimonio == 0:
        print("banca vuota riavvio necessario")
        patrimonio = int(patrimonio + 300000)
        soldi = open('banca.txt','w')
        soldi.write(str(patrimonio))
        soldi.close()
    else:
        pass


def newusers(): #nuovo utente
    f = open("newusers.txt","w+")
    subprocess.check_call(["attrib","+H","newusers.txt"])
    login = input("inserire il nome utente")
    log = open("giocatore.txt", 'w')
    log.write(login)
    log.close()

def GetUUID():
   cmd = 'wmic csproduct get uuid'
   uuid = str(subprocess.check_output(cmd))
   pos1 = uuid.find("\\n")+2
   uuid = uuid[pos1:-15]
   return uuid
def autoban(): #ban automatico
    z = os.stat("giocatore.txt").st_size
    if z == 0 and os.path.isfile('newusers.txt') is True:
        f = open('ban.txt','a')
        f.write(hostname)
        f.close()
        exit()


def ricarica(): #aggiungi soldi al conto utente
    sa = open('fondi-giocatore.txt','r')
    soldi = sa.readline()
    print(soldi)
    ricarica=int(input("ti quanto vuoi ricaricare "))
    soldi = int(soldi)
    totale = soldi + ricarica
    ricarico = open('fondi-giocatore.txt','w')
    ricarico.write(str(totale))
    sa.close()

def giocata():
    try:
        sa = open('fondi-giocatore.txt','r')
        soldi = sa.readline()
        print(soldi)
        giocata = int(input("quanto vuoi giocare "))
        soldi = int(soldi)
        if giocata > soldi:
            print("stai giocando troppo ")
            root = tk.Tk()
            root.withdraw()
            MsgBox = tk.messagebox.askquestion ('elevato','hai giocato un numero troppo elevato',icon = 'error')
            root.destroy()
            exit()
        if giocata == 0:
            root = tk.Tk()
            root.withdraw()
            MsgBox = tk.messagebox.askquestion ('NULL','hai giocato 0',icon = 'error')
            root.destroy()
            exit()
        else:
            rimanenti = soldi - giocata
            ric = open('fondi-giocatore.txt','w')
            ric.write(str(rimanenti))
            sa.close()
            memoria = open("memoria.txt",'w')
            memoria.write(str(giocata))
            memoria.close()
            gio=open("giocate.txt","r")
            gioc=gio.readline()
            gioc=int(gioc)
            gio.close()
            gioca=open("giocate.txt","w")
            totale=gioc+1
            gioca.write(str(totale))
            gioca.close()
    except ValueError:
        root = tk.Tk()
        root.withdraw()
        MsgBox = tk.messagebox.askquestion ('NULL','non hai scritto correttamente un numero',icon = 'error')
        root.destroy()

def ammonizioni():
    f = open('ammonizioni.txt','r')
    giocatori = f.readline()
    f.close()
    if giocatori == "3":
        f = open('ban.txt','w')
        f.write(hostname)
        f.close()
        exit()
        ban()

def informazioni():
    sa = open('fondi-giocatore.txt','r')
    soldi = sa.readline()
    sa.close()
    print("credito attuale " + soldi)
    f = open('giocatore.txt','r')
    giocatori = f.readline()
    f.close()
    print("nome =  ",giocatori)
    print("nome del tuo computer = ",hostname)
    print("ip = ",IPAddr)
    x=os.getlogin()
    print("nome utente pc = " + str(x))
    f = open('giocate.txt','r')
    giocatori = f.readline()
    f.close()
    print("hai giocato " + giocatori + " partite")
    f = open('ammonizioni.txt','r')
    giocatori = f.readline()
    f.close()
    print("identificatore " + str(GetUUID()))
    print("advice " + giocatori)
    os.system("PAUSE")

def vincita():
    root = tk.Tk()
    root.withdraw()
    MsgBoxa = messagebox.showinfo("Title", "Hai vinto")
    root.destroy()
    vincita = open('fondi-giocatore.txt','r')
    soldi = vincita.readline()
    soldi = int(soldi)
    bancav()
    pino = open("memoria.txt.",'r')
    giocata = pino.readline()
    giocata = int(giocata)
    banca=open("banca.txt","r")
    asso=banca.readline()
    asso= int(asso)
    banca.close()
    assow=giocata*2
    banca=open("banca.txt","w")
    rimanente=asso-assow
    banca.write(str(rimanente))
    banca.close()
    vincitaa = soldi + giocata + assow
    of = open('fondi-giocatore.txt','w')
    of.write(str(vincitaa))
    vincita.close()
    log = open("transizioni.txt",'a')
    log.write(str('\n' + tempo + "si è verificata una perdita della banca di " + str(assow) ))
    log.close()
    l=open('vincite.txt','r')
    vincite=l.readline()
    vincite=int(vincite)
    l.close()
    vincitep=vincite+1
    l=open('vincite.txt','w')
    l.write(str(vincitep))
    l.close()


def perdita():
    root = tk.Tk()
    root.withdraw()
    MsgBoxaa = messagebox.showinfo("Title", "Hai perso")
    root.destroy()
    pino = open("memoria.txt.",'r')
    giocata = pino.readline()
    giocata = int(giocata)
    pino.close()
    banca = open("banca.txt","r")
    sano = banca.readline()
    sano=int(sano)
    banca.close()
    bancone=open("banca.txt","w")
    totale = sano+giocata
    bancone.write(str(totale))
    bancone.close()
    log = open("transizioni.txt",'a')
    log.write(str('\n' + tempo + "si è verificata una vincita della banca di " + str(giocata)))
    log.close()
    
    

def indovinalacarta():#indovina la carta
    giocata()
    print("scegli una carta da 1-13")
    vincente = random.randint(1,13)
    scelta = int(input())
    if scelta == vincente:
        #print("hai vinto")
        vincita()
    else:
        perdita()
        #print("hai perso")

def slot():
    giocata()
    print("generando")
    time.sleep(5)
    x=random.randint(0,9)
    y=random.randint(0,9)
    z=random.randint(0,9)
    a=random.randint(0,9)
    b=random.randint(0,9)
    c=random.randint(0,9)
    d=random.randint(0,9)
    e=random.randint(0,9)
    f=random.randint(0,9)

    print("-----------------")
    print("|",x,"|",y,"|",z,"|")
    print("|",a,"|",b,"|",c,"|")
    print("|",d,"|",e,"|",f,"|")
    print("-----------------")
    
    if x==y and y==z and z==a and a==b and b==c and c==d and d==e and e==f:
        print("hai fatto jackpot")
        vincita()
    elif x==y and y==z:
        vincita()
    elif a==b and b==c:
        vincita()
    elif d==e and e==f:
        vincita()
    elif x==b and b==f:
        vincita()
    elif z==b and b==d:
        vincita()
    elif x==a and x==d:
        vincita()
    elif y==b and b==e:
        vincita()
    elif z==c and c==f:
        vincita()
    else:
        perdita()

def blackjack():
    giocata()
    print("benvenuto nel blackjack")
    x=int(input("premi 1 per giocare a modalita facile, 2 per modalita difficile "))
    if x == 1:
        banco = random.randint(10,21)
        if banco != 21:
            banco = banco + 1
            print("il banco ha " + str(banco))
            print("mescolando")
            time.sleep(2)
            giocatore =  random.randint(0,13)
            print(giocatore)
            continuare = str(input("continuare "))
            while continuare == "si":
                if giocatore > 21:
                    print("hai superato 21 ")
                    break
                giocatore = giocatore +  random.randint(1,13)
                print(giocatore)
                continuare = str(input("continuare "))
            if continuare != "si":
                if banco > giocatore or giocatore > 21:
                    perdita()
                else:
                    vincita()

    else:
        print("modalita difficile attivata ")
        banco = random.randint(10,21)
        if banco != 21:
            banco = banco + 1
            print("mescolando")
            time.sleep(2)
            giocatore =  random.randint(1,13)
            print(giocatore)
            continuare = str(input("continuare "))
            while continuare == "si":
                giocatore = giocatore +  random.randint(1,13)
                if giocatore > 21:
                    print("hai superato 21 ")
                    break
                continuare = str(input("continuare "))
            if continuare != "si":
                continuare = False
                if banco > giocatore or giocatore > 21:
                    perdita()
                else:
                    vincita()

def roulette():
    giocata()
    giocare = input("vuoi giocare solo con i colori = 1 o anche con i numeri = 2")
    if giocare == "1":
       colore = str(input("scelga un colore (Rosso o nero) "))
       if colore == "rosso":
           colore = 1
       else:
         colore = 2
         coloreWin =   random.randint(1,2)
       if coloreWin == colore:
          vincita()
       else:
          perdita()
    else:
        colore = str(input("scelga un colore (Rosso o nero) "))
        numero = int(input("scelga un numero "))
        if colore == "rosso":
            colore = 1
        else:
            colore = 2
        coloreWin =   random.randint(1,2)
        numeroWin =  random.randint(1,90)
        if colore == coloreWin and numero == numeroWin:
            vincita()
        else:
            perdita()
        if coloreWin == 1:
            coloreWin="rosso"
        else:
            coloreWin="nero"
        print(coloreWin,numeroWin)
    os.system("PAUSE")

def dadi():
    giocata()
    print("benvenuto nel gioco dei dadi")
    x=int(input("premi 1 per giocare a modalita facile, 2 per modalita difficile "))
    if x == 1:
        print("benvenuto nel gioco dei dadi")
        x=random.randint(1,10)
        vita=3
        print("il tuo compito è cercare di indovinare qunato uscira nel lancio di " + str(x) + " lanci")
        dado = 0
        while x>0:
            dadop=random.randint(1,6)
            dado = dado + dadop
            x=x-1
        print("-----------------")
        while vita>0:
            giocatore=int(input("scegli il tuo numero "))
            if giocatore == dado:
                vincita()
                break
            else:
                if giocatore>dado:
                    print("troppo alto")
                else:
                    print("troppo basso")
            vita=vita-1
            if vita == 0:
                perdita()
    else:
        print("benvenuto nel gioco dei dadi")
        x=random.randint(1,10)
        vita=3
        print("il tuo compito è cercare di indovinare qunato uscira nel lancio di " + str(x) + " lanci")
        facce=random.randint(3,12)
        print("il dado ha " + str(facce) + " facce")
        dado = 0
        while x>0:
            dadop=random.randint(1,facce)
            dado = dado + dadop
            x=x-1
        print("-----------------")
        while vita>0:
            giocatore=int(input("scegli il tuo numero "))
            if giocatore == dado:
                print("hai vinto")
                vincita()
                break
            else:
                if giocatore>dado:
                    print("troppo alto")
                else:
                    print("troppo basso")
            vita=vita-1
            if vita == 0:
                perdita()

def chiudere():
    exit()         


    
def main():
    while True:
        os.system("CLS")
        try:
            if os.path.isfile("newusers.txt") is False:
                newusers()
            else:
                pass
            print("sono le " + tempo)
            password()
            bancav()
            giocatore()
            ban()
            autoban()
            ammonizioni()
            menu()
            scegli()
        except UnboundLocalError:
            MsgBox = tk.messagebox.askquestion ('Exit Application','è stato rilevato un errore vuoi loggarlo',icon = 'error')
            root = tk.Tk()
            root.withdraw()
            MsgBox = messagebox.showerror("Error", "Errore rilevato")
            tk.messagebox.showinfo('Exit','puoi trovare il log a nel file errore.txt' )
            root.destroy()
            log = open("errore.txt",'a')
            log.write('\n' + tempo + "si è verificato un errore ")
            log.close()
   
main()

    
