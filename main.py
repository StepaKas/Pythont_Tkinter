

from tkinter import *

from tkinter import  ttk

from tkinter import messagebox 

import MultiListbox as table

data = [

       ["Petr", "Bílý","045214/1512", "17. Listopadu", 15, "Ostrava", 70800,"poznamka" ,0, "Petros" ,"Jahoda123"],

       ["Jana", "Zelená","901121/7238", "Vozovna", 54, "Poruba", 78511,"" ,1,"Janos" , "banana69"],

       ["Karel", "Nový","800524/5417", "Porubská", 7, "Ostrava", 11150,"",  0,"Karlos", "123"],

      

       ["Martin", "Stříbrný","790407/3652", "Sokolovská", 247, "Brno", 54788,"nic" ,0, "Martinez" , "Alííík"],

        ["Jan", "Modrý","800524/5417", "K Mýtu", 7, "Praha", 11150,"",  0,"Janoska", "123"],

       ["Ondrej", "Červený","800524/5417", "OKD", 7, "Ostrava", 11150,"",  0,"Ondros", "123"],
       ["Tereza", "Veliká","800524/5417", "Porubská", 7, "Darkovice", 11150,"",  0,"Terezos", "123"],
       
       ["Kristina", "Malá","800524/5417", "Nová", 7, "Ostrava", 11150,"",  0,"Tinos", "321"],
       ["Adela", "Nízká","800524/5417", "Porubská", 7, "Hlučín", 11150,"",  0,"Karlosos", "21"],
       ["Natalie", "Malinová","800524/5417", "Stará", 7, "Ostrava", 11150,"",  0,"Natos", "321"],
       ["Sasa", "Modrý","800524/5417", "Porubská", 7, "Praha", 11150,"",  0,"Sasos", "321"]]

       

smeny = [

       ["17/6/2021" , "10:00" , "22:00" ,3, "Večer budem v restauraci párty, buďte připraveni, obsluhovat lidi, čepovat pivo a uklízet stoly"],

       ["20/6/2021" , "11:00" , "20:00" , 3 , "Bude vedro vemte si hodně pití a nějakou svačinku"],

       ["22/6/2021" , "09:00" , "18:00" , 4 , "Ráno budem uklízet, očekávejte že budem pracovat ne tak dlouho, jak jsem zvyklý"],

       ["25/6/2021" , "08:00" , "18:00" ,1 , "Očekáváme slabší přísun lidí proto se v bufetu bude vyskytovat jen jeden člověk." ]]

prihlaseni = [

       ["Petros" ,"20/6/2021"  ],
       ["Janos" ,"20/6/2021"  ],
       ["Petros" ,"17/6/2021"  ],
       ["Janos" ,"17/6/2021"  ],
       ["Karlos" ,"17/6/2021"  ],
       ["Petros" ,"22/6/2021"  ],
       ["Janos" ,"22/6/2021"  ],
       ["Karlos" ,"22/6/2021"  ],
       ["Martinez" ,"22/6/2021"  ],
       ["Petros" ,"25/6/2021"  ]


       ]
loginNick = ["Martinez"]

class App:


    def myhelp (self):

        print("Zadej své informace do formuláře, v druhém tabu je poznámka. Informace uložíš pomocí tlačítka \"Ulož\", \npo vybrání řádku v tabulce může záznam vymazat pomocít tlačítka \"Smaž\" a vyčisti všechny chlívečky pomocí tlačítka \"Vyčisti\"")

        return  

    def info (self):

        messagebox.showinfo("Nastavení", "Zatím nic") 

        return

        
    def LogOut (self):
        self.root.destroy() 
        login = Login()


      
        
    def MultBoxAdd(self):
        if self.enLName.get() == "" or self.enName.get() == "" or self.enRName.get() =="":
            messagebox.showerror("Chyba", "Jméno, příjmení a rodné číslo musí být vyplněno!")
            return False        
        else:
            return True

    def __init__(self, root):
        self.root =  root
        self.root.resizable(False, False)
        self.menubar = Menu(self.root)
        self.root.config(menu=self.menubar)      
        #Záložky

        self.filemenu = Menu(self.menubar, tearoff=0)

        self.filemenu2 = Menu(self.menubar, tearoff=0)

        self.filemenu3 = Menu(self.menubar, tearoff=0)

        self.filemenu.add_command(label="Konec", command=self.root.quit)

        self.filemenu2.add_command(label="Nastavení", command=self.info)

        self.filemenu3.add_command(label="Nápověda", command=self.myhelp)

        self.menubar.add_cascade(label="Soubor", menu=self.filemenu)

        self.menubar.add_cascade(label="Nastavení", menu=self.filemenu2)

        self.menubar.add_cascade(label="Nápověda", menu=self.filemenu3)

        # Hlavni taby
        self.Tacon = ttk.Notebook(self.root)
        self.Tacon.pack(pady = 5)
        self.Zamestnanci= Frame(self.Tacon, width=400, height=200 , bd = 2, relief=GROOVE)        
        self.Zamestnanci.pack(fill="both" , expand = True)
        self.Smeny= Frame(self.Tacon, width=400, height=200 , bd = 2, relief=GROOVE)        
        self.Smeny.pack(fill="both" , expand = True)
        self.Tacon.add(self.Zamestnanci, text='Zaměstnanci: ')
        self.Tacon.add(self.Smeny, text='Směny: ')

        self.row = IntVar()

        self.jmeno = StringVar()

        self.prijmeni = StringVar()

        self.rc = StringVar()

        self.ulice = StringVar()

        self.cp = StringVar()

        self.mesto = StringVar()

        self.psc = StringVar()

        self.mlb = table.MultiListbox(self.Zamestnanci, (('Jméno', 12), ('Příjmení',12), ('Rodné číslo', 12), ("Nick" , 12) ))

        for i in range(len(data)):

            self.mlb.insert(END, (data[i][0], data[i][1],data[i][2] , data[i][-2] ))

        self.mlb.pack(expand=YES,fill=BOTH, padx=10, pady=10)

        

        self.mlb.subscribe( lambda row: self.edit( row ) )

        

        self.nb = ttk.Notebook(self.Zamestnanci)






        

        self.nb.pack(fill=BOTH, padx=5, pady=5)




        

        

           

        self.fr = Frame(self.Zamestnanci, width=300, height=120)

        self.fr.pack(fill="both" , expand = True)

        PositionX = 70

        #Jmeno

        self.enName = Entry(self.fr)        

        self.laName = Label(self.fr , text = "Jméno: " )   

        self.laName.place(relx =0.1,rely = 0.0)

        self.enName.place(relx =0.4,rely = 0.0, width =150)

        #Příjmení

        self.enLName = Entry(self.fr)        

        self.laLName = Label(self.fr , text = "Příjmení: ")   

        self.laLName.place(relx =0.1,rely = 0.3)

        self.enLName.place(relx =0.4,rely = 0.3, width =150)

        #Rodné číslo

        self.enRName = Entry(self.fr)        

        self.laRName = Label(self.fr , text = "Rodné číslo: ")   

        self.laRName.place(relx =0.1,rely = 0.6)

        self.enRName.place(relx =0.4,rely = 0.6, width =150)

        

        

        #Taby

        self.TAB_CONTROL = ttk.Notebook(self.Zamestnanci)

        self.TAB_CONTROL.pack(pady = 5)

        self.frAdress = Frame(self.TAB_CONTROL, width=400, height=200 , bd = 2, relief=GROOVE)

        self.frPozn = Frame(self.TAB_CONTROL, width=300, height=200 , bd = 2, relief=GROOVE)

        self.frAdress.pack(fill="both" , expand = True)

        self.frPozn.pack(fill="both" , expand = True)

        

        self.TAB_CONTROL.add(self.frAdress, text='Adresa: ')

        self.TAB_CONTROL.add(self.frPozn, text='Poznámka: ')

        

        #Čudlíky

        self.butAdd = Button(self.Zamestnanci, text="Ulož", command = self.add )

        self.butAdd.pack(side="left" ,pady=5 , padx = 15)

        self.butNew = Button(self.Zamestnanci, text="Vyčisti", command = self.clear)

        self.butNew.pack(side="left" ,pady=5)

        self.butCancel = Button(self.Zamestnanci, text="Smaž", command = lambda: self.delete(self.row))

        self.butCancel.pack(side="left" ,pady=5, padx=20)

        self.butLogOut = Button(self.Zamestnanci, text="Logout" , command = self.LogOut)

        self.butLogOut.pack(side="right" ,pady=5 , padx = 15)


        #Poznamka

        self.poznText= Text(self.frPozn, width=50, height=5)

        self.scrol = Scrollbar(self.poznText)

        self.scrol.pack(side=RIGHT)

        self.poznText.pack(expand=1, fill=BOTH)

        self.poznText.focus_set()

        self.scrol.config(command=self.poznText.yview)

        self.poznText.config(yscrollcommand=self.scrol.set)

        

      

        #Ulice

        self.enUName = Entry(self.frAdress)        

        self.laUName = Label(self.frAdress , text = "Ulice:")   

        self.laUName.place(relx =0.1,rely = 0.1 )

        self.enUName.place(relx =0.4,rely = 0.1, width =70)

        #Číslo popisné

        self.enCPName = Entry(self.frAdress)        

        self.laCPName = Label(self.frAdress , text = "Číslo popisné:")   

        self.laCPName.place(relx =0.1,rely = 0.3)

        self.enCPName.place(relx =0.4,rely = 0.3, width =30)

        #Město

        self.enMName = Entry(self.frAdress)        

        self.laMName = Label(self.frAdress , text = "Město:")   

        self.laMName.place(relx =0.1,rely = 0.5)

        self.enMName.place(relx =0.4,rely = 0.5, width =100)

        #PSČ

        self.enPSCName = Entry(self.frAdress)        

        self.laPSCName = Label(self.frAdress , text = "PSČ:")   

        self.laPSCName.place(relx =0.1,rely = 0.70)

        self.enPSCName.place(relx =0.4,rely = 0.70, width =60)
        self.admin = IntVar()
        self.enAdminName = Checkbutton(self.frAdress ,variable=self.admin, onvalue=1, offvalue=0,)        
              
        self.laAdminName = Label(self.frAdress , text = "Admin:")   
               
        self.laAdminName.place(relx =0.1,rely = 0.85)
               
        self.enAdminName.place(relx =0.4,rely = 0.85, width =20)




        #### Edit smen
        self.root.title("Administrátorské okno")

    
        self.mlbSmeny = table.MultiListbox(self.Smeny, (('Datum', 6), ('Od',2), ('Do',2), ("Kapacita" ,2) ))

        for i in range(len(smeny)):

            self.mlbSmeny.insert(END, (smeny[i][0], smeny[i][1],smeny[i][2] , smeny[i][3] ))

        self.mlbSmeny.pack(expand=YES,fill=BOTH, padx=10, pady=10)

        

        self.mlbSmeny.subscribe( lambda row: self.editSmeny( row ) )

        

        self.nbSmeny = ttk.Notebook(self.Smeny)




        self.nbSmeny.pack(fill=BOTH, padx=5, pady=5)





        self.frSmeny = Frame(self.Smeny, width=300, height=120)
        self.frSmeny.pack(fill="both" , expand = True)
                

        #Inputy od směn

        self.Datum = Entry(self.frSmeny)        
        self.laDatum = Label(self.frSmeny , text = "Datum: " )  
        self.laDatum.place(relx =0.1,rely = 0.1)
        self.Datum.place(relx =0.4,rely = 0.1, width =90)

        self.Od = Entry(self.frSmeny)        
        self.laOd = Label(self.frSmeny , text = "Od: " )   
        self.laOd.place(relx =0.1,rely = 0.3)
        self.Od.place(relx =0.4,rely = 0.3, width =50)

        self.Do = Entry(self.frSmeny)        
        self.laDo = Label(self.frSmeny , text = "Do: " )   
        self.laDo.place(relx =0.1,rely = 0.5)
        self.Do.place(relx =0.4,rely = 0.5, width =50)        
        
        self.Kapacita = Entry(self.frSmeny)        
        self.laKapacita = Label(self.frSmeny , text = "Kapacita: " )   
        self.laKapacita.place(relx =0.1,rely = 0.7)
        self.Kapacita.place(relx =0.4,rely = 0.7, width =50)
           
        # Čudlíky od směn

        self.butAddSme = Button(self.Smeny, text="Ulož", command = self.addSmeny )

        self.butAddSme.pack(side="left" ,pady=5 , padx = 15)

        self.butNewSme = Button(self.Smeny, text="Vyčisti", command = self.clearSmeny)

        self.butNewSme.pack(side="left" ,pady=5)

        self.butCancelSme = Button(self.Smeny, text="Smaž", command = lambda: self.deleteSmena(self.row))

        self.butCancelSme.pack(side="left" ,pady=5, padx=20)

        self.butLogOutSme = Button(self.Smeny, text="Logout" , command = self.LogOut)

        self.butLogOutSme.pack(side="right" ,pady=5 , padx = 15)

        #["Petr", "Bílý","045214/1512", "17. Listopadu", 15, "Ostrava", 70800,"poznamka",1,"Pet0452" , "045214/1512" ],

    def add(self):
        nick = self.enName.get()[0 : 3] + self.enRName.get()[0:4]
        heslo = self.enRName.get()
        #print (self.admin , nick ,passs)
        if(self.MultBoxAdd()):
                    
            data.append([self.enName.get(),self.enLName.get(),self.enRName.get(), self.enUName.get(), self.enCPName.get(), self.enMName.get(),self.enPSCName.get(), self.poznText.get(1.0,END), self.admin.get(), nick ,heslo ])

            self.mlb.insert(END, (self.enName.get(),self.enLName.get(),self.enRName.get(), nick ))
        messagebox.showinfo("Uživatel", " Uživatel "+self.enName.get() + " " +self.enLName.get()+" přidán. Přihlašovací Nick je " + nick + " a prvotní heslo je " + heslo )

    def addSmeny(self):
               
                    
            smeny.append([self.Datum.get() , self.Od.get(),self.Do.get(),self.Kapacita.get() ])

            self.mlbSmeny.insert(END, (self.Datum.get() , self.Od.get(),self.Do.get(),self.Kapacita.get()) )
        
            messagebox.showinfo("Směna", " Směna přidána")

    

    def edit(self, row):

        self.row=row

        print (data[row])

        self.jmeno.set(data[row][0])
    def editSmeny(self, row):

        self.row=row

        print (smeny[row])


    def deleteSmena(self , row):
        self.row=row

        if self.row >= len(smeny) or len(smeny) <=0:

            return

        print("Smazáno ")

        print ( smeny[row])

        datum = smeny[row][0]
        od = smeny[row][1]
        do = smeny[row][2] 

        del smeny[row]

        self.mlbSmeny.delete(0, END)

        for i in range(len(smeny)):

            self.mlbSmeny.insert(END, (smeny[i][0], smeny[i][1],smeny[i][2], smeny[i][3]))

        messagebox.showinfo(title="Delete", message="Směna " + datum + " od " + od + " do  "+ do+ " smazán")

    def delete(self , row):

        self.row=row

        if self.row >= len(data) or len(data) <=0:

            return

        print("Smazáno ")

        print ( data[row])

        tempName = data[row][0]

        tempLName = data[row][1]

        del data[row]

        self.mlb.delete(0, END)

        for i in range(len(data)):

            self.mlb.insert(END, (data[i][0], data[i][1],data[i][2], data[i][-2]))

        messagebox.showinfo(title="Delete", message="Uživatel " + tempName + " " + tempLName + " smazán")

    def clear(self):

        self.enName.delete(0, END)

        self.enLName.delete(0, END)

        self.enRName.delete(0, END)



        self.enUName.delete(0, END)

        self.enMName.delete(0, END)

        self.enCPName.delete(0, END)

        self.enPSCName.delete(0, END)

        self.poznText.delete('1.0', END)

        messagebox.showinfo(title="Empty boxes", message="Vše smazáno")
    def clearSmeny(self):

        self.Datum.delete(0, END)
        self.Od.delete(0, END)
        self.Do.delete(0, END)
        self.Kapacita.delete(0, END)
        messagebox.showinfo(title="Empty boxes", message="Vše smazáno")
class PrihlasPracovnik:
    def editPrihlas(self, row):

        self.row=row

        print (smeny[row])
        


    def showInfo(self):
        messagebox.showinfo("Popis směny", smeny[self.row][4] )
    def prihlas(self):
        if (smeny[self.row][-2] == "Volno" and smeny[self.row][-1] == "❌"):
            print ("Prihlášen " + loginNick[0] +" na " + smeny[self.row][0])
            prihlaseni.append([loginNick[0] , smeny[self.row][0]])

            kapaci = 0
            volno = "Volno"
            for j in range (len(prihlaseni)):
                if smeny[self.row][0] == prihlaseni[j][1]:
                    kapaci +=1
            if kapaci >= int(smeny[self.row][3]):
                    volno = "Plno"    
            smeny[self.row][-2] = volno
            smeny[self.row][-1] = "✓"    
            self.mlbSmeny.delete(0,len(smeny))
            for i in range(len(smeny)):
                self.mlbSmeny.insert(END, (smeny[i][0], smeny[i][1],smeny[i][2] , smeny[i][3], smeny[i][-2], smeny[i][-1] ))
            messagebox.showinfo("Přihlášení", loginNick[0]  +" přihlášen úspěšně")
        else:
            print("Nepodarilo se prihlasit")

    def odhlas(self):
         if (smeny[self.row][-1] == "✓"):

             for j in range (len(prihlaseni) -1):
                
                if prihlaseni[j][0] == loginNick[0] and smeny[self.row][0] == prihlaseni[j][1]:
                    print("Ano")
                    prihlaseni.pop(j)
                    
                
             smeny[self.row][-1] = "❌"
             
             smeny[self.row][-2] = "Volno"
             
             self.mlbSmeny.delete(0,len(smeny))             
             for i in range(len(smeny)):
                        self.mlbSmeny.insert(END, (smeny[i][0], smeny[i][1],smeny[i][2] , smeny[i][3], smeny[i][-2], smeny[i][-1] ))
             messagebox.showinfo("Odhlášení", loginNick[0]  +" odhlášen úspěšně")
         else:
              print("Nepodarilo se odhlasit")

    def __init__(self , root):
        self.root = root
        self.root.geometry("500x300")
        self.root.title("Přihlášení na směnu")

    
        self.mlbSmeny = table.MultiListbox(self.root, (('Datum', 16), ('Od',8), ('Do', 8), ("Kapacita" , 12) ,("Volno" , 6) , ("Přihlášen", 10)))

        for i in range(len(smeny)):
            kapaci = 0
            prihlasen = "❌"
            volno = "Volno"
            for j in range (len(prihlaseni)):
                if smeny[i][0] == prihlaseni[j][1]:
                    kapaci +=1
                if prihlaseni[j][0] == loginNick[0] and smeny[i][0] == prihlaseni[j][1]:
                    prihlasen = "✓"
            if kapaci >= int(smeny[i][3]):
                    volno = "Plno"   
            
            if (len(smeny[i]) <=6):
                smeny[i].append(volno)
                smeny[i].append(prihlasen)
            else: 
                 smeny[i][-2] = volno
                 smeny[i][-1] = prihlasen
            self.mlbSmeny.insert(END, (smeny[i][0], smeny[i][1],smeny[i][2] , smeny[i][3], smeny[i][-2], smeny[i][-1]  ))

        self.mlbSmeny.pack(expand=YES,fill=BOTH, padx=10, pady=10)

        

        self.mlbSmeny.subscribe( lambda row: self.editPrihlas( row ) )

        

        self.nbSmeny = ttk.Notebook(self.root)




        self.nbSmeny.pack(fill=BOTH, padx=5, pady=5)





        self.frSmeny = Frame(self.root, width=300, height=10)
        self.frSmeny.pack(fill="both" , expand = True)
          #čudlíky     
        self.butPrihlas = Button(self.root, text="Přihlaš" ,command =self.prihlas )
        self.butPrihlas.pack(side="left" ,pady=5 , padx = 15)

        self.butOdhlas = Button(self.root, text="Odhlaš", command = self.odhlas)
        self.butOdhlas.pack(side="left" ,pady=5)

        self.butInfo = Button(self.root, text="Popisek", command = self.showInfo)
        self.butInfo.pack(side="left" ,pady=5 , padx=15)

        self.butLogOut = Button(self.root, text="Logout" , command = self.LogOut)
        self.butLogOut.pack(side="right" ,pady=5 , padx = 15)
    def LogOut (self):
        self.root.destroy() 
        login = Login()
class Login :
    def __init__(self):
        self.root = Tk()
        self.root.geometry("200x150")
        self.root.title("Login")
        self.root.config()
        self.fr = Frame(self.root, width=200, height=150, bg = "blue")

        self.fr.pack(fill="both" , expand = True)
        self.enName = Entry(self.fr)    
        self.laName = Label(self.fr , text = "Login: ",bg = "yellow" )   
        self.laName.place(relx =0.1,rely = 0.3)
        self.enName.place(relx =0.4,rely = 0.3, width =80)      


        self.passwordEntry = Entry(self.fr, show='*')    
        self.passwordLabel = Label(self.fr , text = "Heslo: ",bg = "yellow" )   
        self.passwordLabel.place(relx =0.1,rely = 0.5)
        self.passwordEntry.place(relx =0.4,rely = 0.5, width =80)  
    
        self.butAdd = Button(self.fr, text="Login", command = self.logged, bg = "grey")
        self.butAdd.pack(  side="bottom" , pady= 5)
        self.root.mainloop()
    def quit(self):
       self.root.destroy 
    def ValidLoginAdmin(self):
        for info in data:
            #print (self.enName.get() + " " +  info[-2] + " " + self.passwordEntry.get() + " " +info[-1]  )
            if self.enName.get() == info[-2] and self.passwordEntry.get() == info[-1]  and  info[-3] == 1:
                
                return True
        else:
            return False
    def ValidLoginWorker(self):
        for info in data:
            #print (self.enName.get() + " " +  info[-2] + " " + self.passwordEntry.get() + " " +info[-1]  )
            print (info[-2], info[-1])
            if self.enName.get() == info[-2] and self.passwordEntry.get() == info[-1]  :
                return True
        else:
            return False
    def logged(self):
        print ("Clicked")
        if self.ValidLoginAdmin()  or False :

            loginNick[0] = self.enName.get()
            if not self.NewBie():
                
                self.root.destroy()
                root = Tk()
                root.wm_title("Formulář")
                app = App(root)
                root.mainloop()
            else:
                
                self.root.destroy()
                passW = PassWordChange(True)
            
        elif self.ValidLoginWorker() or False:
            print (loginNick[0])
            loginNick[0] = self.enName.get()
            print (loginNick[0])
            if not self.NewBie():
                
                self.root.destroy()
                root = Tk()
                prac = PrihlasPracovnik(root)
            else:
                
                self.root.destroy()
                passW = PassWordChange(False)
    
        else:
            messagebox.showerror("Chyba", "Špatné přihlašovací údaje")
    def NewBie(self): 
        for info in data:
            if self.enName.get() == info[-2] and info[-1] == info[2]:
                return True
        return False
class PassWordChange:
    def __init__(self , is_admin):
        self.is_admin = is_admin
        self.root = Tk()
        self.fr = Frame(self.root, width=400, height=90)

        load = Image.open("Pivo.jpeg")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render

        self.fr.pack(fill="both" , expand = True)
        self.passEn = Entry(self.fr, show='*')    
        self.laPass = Label(self.fr , text = "Zadej nové heslo: " )   
        self.laPass.place(relx =0.1,rely = 0.3)
        self.passEn.place(relx =0.4,rely = 0.3, width =80)      


        self.passwordEntry = Entry(self.fr, show='*')    
        self.passwordLabel = Label(self.fr , text = "Potvď heslo: " )   
        self.passwordLabel.place(relx =0.1,rely = 0.7)
        self.passwordEntry.place(relx =0.4,rely = 0.7, width =80)  

        self.butContinue = Button(self.root, text="Potvrď", command = self.go)
        self.butContinue.pack( expand=True , pady= 20)
    def go(self):
        

        if self.passwordEntry.get() == self.passEn.get() and (self.passwordEntry.get()) != "" :
            for info in data:
                if loginNick[0] == info[-2]:
                    info[-1] = self.passwordEntry.get()
            if not self.is_admin:
                
                self.root.destroy()
                root = Tk()
                prac = PrihlasPracovnik(root)
            else:

                self.root.destroy()
                root = Tk()
                root.wm_title("Formulář")
                app = App(root)
                root.mainloop()
        else:
            messagebox.showerror("Chyba", "Zkus znova")
login = Login()







