# Mandala - DadoSoft 2021
# Windows10 - Python 3.8.5

# usa tkinter (interfaccia)
from tkinter import *
from tkinter import filedialog

from math import sin,cos,pi
import random as R

# usa PIL (gestione immagini)
from PIL import Image, ImageTk ,ImageGrab,ImageOps
from PIL import ImageDraw, ImageFont

# usa DadoMandalaLib1
from DadoMandalaLib1 import *
''' Contenuti in DadoMandalaLib1.py
      CreaCooPol(NVe,Rmin,Rmax,Amp,SA):
      Ruota(Lz,Az,anR):
      CartFromPolar(l,a,cx,cy):
      CreaCorona(NVe,Rmin,Rmax,Amp,SA,Specchia):
      DatiRett_Vertici(x,y,lx,ly,ang):
      Stampa(Lr,Ar):
'''

def ColorRand2():
  # colori random tra 0 e 0xFFFFFF
  colF="#"+"%06X" % R.randint(0, 0xFFFFFF)
  colO="#"+"%06X" % R.randint(0, 0xFFFFFF)
  return colF,colO

def Cancella():
  C.delete('all')

### COMANDI CREA

def CreaPoligoni():
  MsgFilOulDisabled(vFil.get(), vOuLi.get())

  iNP=vNP.get()
  Rmax=vRaMa.get()
  Rmin=vRaMi.get()
  Amp= pi/iNP*2
  SoAng = vSA.get()
  
  L,A = CreaCooPol(vNL.get(),Rmin,Rmax,Amp,SoAng)
  colF,colO =ColorRand2()

  DisegnaP(L,A,colF,colO)
  if vSp.get() :
    L2,A2 = Specchia(L,A,0)
    DisegnaP(L2,A2,colF,colO)
  for i in range (1,iNP):
    L1,A1 = Ruota(L,A,2*pi/iNP*i)
    DisegnaP(L1,A1,colF,colO)
    if vSp.get() :
      L2,A2 = Specchia(L1,A1,4*pi/iNP*i)
      DisegnaP(L2,A2,colF,colO)

def CreaFiore():
  MsgFilOulDisabled(vFil.get(), vOuLi.get())

  iNP=vNP.get()
  Rmin=vRaMi.get()
  Rmax=vRaMa.get()
  Amp= pi/iNP*2
  SA = vSA.get()
  iNL=vNL.get()
  Specchia=vSp.get()
  
  L0,A0= CreaCorona(iNL,Rmin,Rmax,Amp,SA,Specchia)
  Lg=L0
  Ag=A0
  for i in range (1,iNP):
    L1,A1 = Ruota(L0,A0,2*pi/iNP*i)
    Lg = Lg + L1
    Ag = Ag + A1

  colF,colO = ColorRand2()
  DisegnaP(Lg,Ag,colF,colO)

  #minimo di lista
  Lmin=min(Lg)
  NGra=vNGra.get()
  ASco=vASco.get() *Amp/ 100 
  for i in range(1,NGra):
    Lg= [l-(Lmin/NGra) for l in Lg]
    Ag= [a-ASco for a in Ag]
    colF="#"+"%06X" % R.randint(0, 0xFFFFFF)
    DisegnaP(Lg,Ag,colF,colO)

def CreaLinee():
  MsgFilOulDisabled(vFil.get(), vOuLi.get())
    
  iNP=vNP.get()
  Rmax=vRaMa.get()
  Rmin=vRaMi.get()
  Amp= pi/iNP*2
  SoAng = vSA.get()
  NumLinee=vNL.get()*2+1
  
  L,A = CreaCooPol(NumLinee,Rmin,Rmax,Amp,SoAng)
  colF,colO =ColorRand2()

  DisegnaL(L,A,colF,colO)
  if vSp.get() :
    L2,A2 = Specchia(L,A,0)
    DisegnaL(L2,A2,colF,colO)
  for i in range (1,iNP):
    L1,A1 = Ruota(L,A,2*pi/iNP*i)
    DisegnaL(L1,A1,colF,colO)
    if vSp.get() :
      L2,A2 = Specchia(L1,A1,4*pi/iNP*i)
      DisegnaL(L2,A2,colF,colO)

def CreaCerchi():
  MsgFilOulDisabled(vFil.get(), vOuLi.get())
    
  iNP=vNP.get()
  Rmax=vRaMa.get()
  Rmin=vRaMi.get()
  Amp= pi/iNP*2
  SoAng = vSA.get()
  NumLinee=vNL.get()*2
  
  L,A = CreaCooPol(NumLinee,Rmin,Rmax,Amp,SoAng)
  colF,colO =ColorRand2()

  DisegnaC(L,A,colF,colO)
  if vSp.get() :
    L2,A2 = Specchia(L,A,0)
    DisegnaC(L2,A2,colF,colO)
  for i in range (1,iNP):
    L1,A1 = Ruota(L,A,2*pi/iNP*i)
    DisegnaC(L1,A1,colF,colO)
    if vSp.get() :
      L2,A2 = Specchia(L1,A1,4*pi/iNP*i)
      DisegnaC(L2,A2,colF,colO)

def CreaRettangoli():
  CreaRettangoliOvali(0)

def CreaOvali():
  CreaRettangoliOvali(1)

def CreaRandom():
  ### MsgFilOulDisabled(vFil.get(), vOuLi.get())
  sNP.set(R.randint(3,24))
  sRaMi.set(R.randint(10,200))
  sRaMa.set(R.randint(100,315))
  vSmo.set(R.randint(0,1))
  vSp.set(R.randint(0,1))
  vFil.set(R.randint(0,1))
  vOuLi.set(R.randint(0,1))
  if vFil.get()==0:
    vOuLi.set(1)
  sLP.set(R.randint(1,6))
  sNL.set(R.randint(3,6))
  sSA.set(R.randint(0,100))
  sNGra.set(R.randint(1,30))
  sASco.set(R.randint(0,100))
  for v in range (5):
    CreaNumero(R.randint(0,6))
    
def CreaNumero(S):
  switcher = {
        0: CreaPoligoni,
        1: CreaFiore,
        2: CreaLinee,
        3: CreaCerchi,
        4: CreaRettangoli,
        5: CreaOvali
    }
    # Chiama una funzione a seconda del numero
  func=switcher.get(S, lambda: Niente)
  return func()

def Niente():
  pass
  
  
def CreaRettangoliOvali(smooth):
  MsgFilOulDisabled(vFil.get(), vOuLi.get())

  iNP=vNP.get()
  Rmax=vRaMa.get()
  Rmin=vRaMi.get()
  Amp= pi/iNP*2
  SoAng = vSA.get()
  latoX=R.randint(5,50)
  latoY=R.randint(5,50)

  colF,colO = ColorRand2()

  L,A = CreaCooPol(vNL.get(),Rmin,Rmax,Amp,SoAng)

  for i in range(len(L)): #prima punta
    y= L[i]*sin(A[i])
    x= L[i]*cos(A[i])
    DisegnaRetOval(x,y,latoX,latoY,A[i],colF,colO,smooth)

  if vSp.get() : #prima specchiatura
    L2,A2 = Specchia(L,A,0)
    for i in range(len(L)):
      y= L2[i]*sin(A2[i])
      x= L2[i]*cos(A2[i])                              
      DisegnaRetOval(x,y,latoX,latoY,A2[i],colF,colO,smooth)

  for a in range (1,iNP):
    L1,A1 = Ruota(L,A,2*pi/iNP*a)
    for i in range (len(L)):
      y= L1[i]*sin(A1[i])
      x= L1[i]*cos(A1[i])                              
      DisegnaRetOval(x,y,latoX,latoY,A1[i],colF,colO,smooth)

      if vSp.get() :
        L2,A2 = Specchia(L1,A1,4*pi/iNP*i)
        for i in range (len(L)):
          y= L2[i]*sin(A2[i])
          x= L2[i]*cos(A2[i])
          DisegnaRetOval(x,y,latoX,latoY,A2[i],colF,colO,smooth)

######################################


# DISEGNA

def DisegnaP(l,a,colF,colO):
  ''' Disegna poligono
      l    Lista lunghezze
      a    Lista angoli
      colF Colore interno
      colO Colore bordo
  '''
  bSmo= vSmo.get()
  fill = colF if vFil.get() else ''
  outl = colO if vOuLi.get() else ''
  wid=vLB.get()  
  co=CartFromPolar(l,a,cx,cy)
  C.create_polygon(co,fill=fill,outline=outl,smooth=bSmo,width=wid)

def DisegnaL(l,a,colF,colO):
  # converte coodinate polari in XY
  # e disegna il poligono
  fill = colF if vFil.get() else ''
  outl = colO if vOuLi.get() else ''
  wid=vLB.get()
  bSmo= vSmo.get()
  co=CartFromPolar(l,a,cx,cy)
  C.create_line(co,fill=fill,width=wid,smooth=bSmo,capstyle=ROUND)

def DisegnaC(l,a,colF,colO):
  # converte coodinate polari in XY
  # e disegna il poligono
  fill = colF if vFil.get() else ''
  outl = colO if vOuLi.get() else ''
  wid=vLB.get()  
  co=[]
  for i in range(0,len(l)):
    x1= cx+l[i]*sin(a[i])-10
    y1= cy+l[i]*cos(a[i])-10
    x2= cx+l[i]*sin(a[i])+10
    y2= cy+l[i]*cos(a[i])+10
    C.create_oval(x1,y1,x2,y2,fill=fill,outline=outl,width=wid)

  
def DisegnaRetOval(x,y,lx,ly,ang,colF,colO,Smooth):
  #    x,y Coordinate del centro del rettangolo
  #  lx,ly Lati del rettangolo
  #    ang Angolo di rotazione in radianti
  #   colF Colore Fill riempimento
  #   colO Colore Outline bordo
  # Smooth 1=Ovali 0=Rettangoli
  co = DatiRett_Vertici(cx+x,cy+y,lx,ly,ang)
  fill = colF if vFil.get() else ''
  outl = colO if vOuLi.get() else ''
  wid=vLB.get() 
  C.create_polygon(co,fill=fill,outline=outl,smooth=Smooth,width=wid)

######################################

### Function con PIL per gestione immagini

def BoxG(Widget):
    # Ritorna valori limiti del Widget rispetto allo schermo
    Parent=Widget.nametowidget(Widget.winfo_parent())
    x1 = Parent.winfo_rootx() + Widget.winfo_x()
    y1 = Parent.winfo_rooty() + Widget.winfo_y()
    x2 = x1 + Widget.winfo_width()
    y2 = y1 + Widget.winfo_height()
    return x1,y1,x2,y2

def Salva():
  filename = filedialog.asksaveasfilename(initialfile='Mandala.png',
                  defaultextension='.png',
                  filetypes = (('Image PNG', '.png'), ('Image JPG','.jpg')))
  if not filename:
    return
  else:
    Im2 = ImageGrab.grab(bbox=BoxG(C))
    Im2.save(filename)
######################################

### UNDO

def Undo():
  global Ph2
  C.create_image(cx*2,cy*2,image=Ph2, anchor='se')
  #lOu.configure(text="NON\nPRONTO")
    
def CopiaInMemoria():
    global Ph2
    Im1 = ImageGrab.grab(bbox=BoxG(C))
    Ph2 = ImageTk.PhotoImage(Im1)

def MsgFilOulDisabled(F,O):
  CopiaInMemoria()
  # se Fill e Outline sono disabilitati, non mostra niente
  if (F + O) > 0 :
    lOu.configure(text="OK ") 
  else:
    lOu.configure(text="ERRORE\nFill e Outline\n disabilitati") 

##################################################    

cx=320
cy=320

Win = Tk()
#Win.geometry('%sx%s' % (cx*2+2+200,cy*2+2)) calcolata
Win.title("DadoSoft - Mandala")
Win.resizable(False, False)

FCanvas = Frame(Win, bg='gray', width=cx*2, height=cy*2,bd=1, relief=FLAT,padx=1,pady=1)
FComand = Frame(Win, width=208, height=cy*2+10,bd=2, relief=GROOVE)

FCanvas.grid(row=0, column=0)
FComand.grid(row=0, column=1)

C = Canvas(FCanvas,width=cx*2,height=cy*2)
C.pack()

FCanvas.grid(column=1)
FComand.grid(column=2)

##################################################  
YP=22
YY=2

# Label OUT
lOu = Label(FComand,text="VAI",bd=0, relief=GROOVE)
lOu.pack()
lOu.place(x=100+2 ,y=YY , height=40, width=100) 

#   Button Cancella
bStop = Button(FComand, text="Cancella", command=Cancella)
bStop.pack()
bStop.place(x=2,y=YY,height=20, width=100) 

YY +=YP
#   Button Undo
bUndo = Button(FComand, text="UNDO", command=Undo)
bUndo.pack()
bUndo.place(x=2,y=YY,height=20, width=100) 

YY +=YP
   
##################################################################
### PARAMETRI

#   Numero punte
    # Label
lNP = Label(FComand,text="Numero punte")
lNP.pack()
lNP.place(x=2 ,y=YY , height=40, width=100)    
    #Scale
vNP = IntVar()
sNP = Scale(FComand, variable = vNP ,orient=HORIZONTAL, from_=3, to=32)
sNP.set(5)
sNP.place(x=100+2 ,y=YY , height=40, width=100)

YY +=YP
YY +=YP
#   Raggio minimo
    # Label
lRM = Label(FComand,text="Raggio Minimo")
lRM.place(x=2 ,y = 6+80 , height=40, width=100)    
    #Scale
vRaMi = IntVar()
sRaMi = Scale(FComand, variable = vRaMi ,orient=HORIZONTAL, from_=0, to=cx)
sRaMi.set(0)
sRaMi.place(x=100+2 ,y=YY , height=40, width=100)
YY +=YP
YY +=YP
#   Raggio massimo
    # Label
lRM = Label(FComand,text="Raggio Massimo")
lRM.place(x=2 ,y=YY , height=40, width=100)    
    #Scale
vRaMa = IntVar()
sRaMa = Scale(FComand, variable = vRaMa ,orient=HORIZONTAL, from_=0, to=cx)
sRaMa.set(320)
sRaMa.place(x=100+2 ,y=YY , height=40, width=100)

YY +=YP
YY +=YP
#   Smooth
vSmo = IntVar()
rbSmo = Checkbutton(FComand,anchor=W, text="Smooth", variable=vSmo)
vSmo.set(0)
rbSmo.place(x=2,y=YY,height=20,width=100)

#   Specchia
vSp = IntVar()
rSp = Checkbutton(FComand,anchor=W, text="Specchia", variable=vSp)
vSp.set(1)
rSp.place(x=100+2,y=YY,height=20,width=100)

YY +=YP
#   Fill
vFil = IntVar()
rbFil = Checkbutton(FComand,anchor=W, text="Fill", variable=vFil)
vFil.set(1)
rbFil.place(x=2,y=YY,height=20,width=100)

#   OutLine
vOuLi = IntVar()
rbOuLi = Checkbutton(FComand,anchor=W, text="OutLine", variable=vOuLi)
vOuLi.set(1)
rbOuLi.place(x=100+2,y=YY,height=20,width=100)

YY +=YP
#   Larghezza OutLine
    # Label
lLP = Label(FComand,text="Larghezza\n bordo")
lLP.place(x=2 ,y=YY , height=40, width=100)    
    #Scale
vLB = IntVar()
sLP = Scale(FComand, variable = vLB ,orient=HORIZONTAL, from_=1, to=10)
sLP.set(2)
sLP.place(x=100+2 ,y=YY , height=40, width=100)

YY +=YP
YY +=YP
#   Numero Lati
    # Label
lNL = Label(FComand,text="Numero Lati")
lNL.place(x=2 ,y=YY , height=40, width=100)    
    #Scale
vNL = IntVar()
sNL = Scale(FComand, variable = vNL ,orient=HORIZONTAL, from_=3, to=6)
sNL.set(3)
sNL.place(x=100+2 ,y=YY , height=40, width=100)

YY +=YP
YY +=YP
#   Sovvrapposizione angolo
    # Label
lSA = Label(FComand,text="Sovvrapposizione\n angolo in %")
lSA.place(x=2 ,y=YY , height=40, width=100)    
    #Scale
vSA = IntVar()
sSA = Scale(FComand, variable = vSA ,orient=HORIZONTAL, from_=0, to=100)
sSA.set(0)
sSA.place(x=100+2 ,y=YY , height=40, width=100)
YY +=YP
YY +=YP

#################################################################
### COMANDI CREAZIONE

#   Button Linee
bLi = Button(FComand, text="Linee", command=CreaLinee)
bLi.pack()
bLi.place(x=2,y=YY,height=20, width=100)
#   Button Cerchi
bCe = Button(FComand, text="Cerchi", command=CreaCerchi)
bCe.place(x=100+2,y=YY,height=20, width=100)
YY +=YP

#   Button Rettangoli
bRe = Button(FComand, text="Rettangoli", command=CreaRettangoli)
bRe.place(x=2,y=YY,height=20, width=100)
#   Button Ovali
bOv = Button(FComand, text="Ovali", command=CreaOvali)
bOv.place(x=100+2,y=YY,height=20, width=100)
YY +=YP

#   Button POLIGONI
bStart = Button(FComand, text="Poligoni", command=CreaPoligoni)
bStart.place(x=2,y=YY,height=20, width=100)   
#   Button Random
bRandom = Button(FComand, text="Random", command=CreaRandom)
bRandom.place(x=100+2,y=YY,height=20, width=100)
YY +=YP


### Comandi e parametri per fiore
YY +=YP/2

#   Button Fiore
bSm = Button(FComand, text="Fiore", command=CreaFiore)
bSm.place(x=2,y=YY,height=20, width=100)
YY +=YP

#   Numero Giri
    # Label
lNGra = Label(FComand,text="Numero\nGiri")
lNGra.place(x=2 ,y=YY, height=40, width=100)    
    #Scale
vNGra = IntVar()
sNGra = Scale(FComand, variable = vNGra ,orient=HORIZONTAL, from_=1, to=20)
sNGra.set(5)
sNGra.place(x=100+2 ,y=YY , height=40, width=100)
YY +=YP
YY +=YP

#   Angolo scorrimento
    # Label
lASco = Label(FComand,text="Angolo\nscorrimento %")
lASco.place(x=2 ,y=YY , height=40, width=100)    
    #Scale
vASco = IntVar()
sASco = Scale(FComand, variable = vASco ,orient=HORIZONTAL, from_=0, to=100)
sASco.set(10)
sASco.place(x=100+2 ,y=YY , height=40, width=100)
YY +=YP
YY +=YP

#   Button Fiore
bSalva = Button(FComand, text="Salva", command=Salva)
bSalva.place(x=2,y=YY,height=20, width=100)

### FINE interfaccia


if __name__ == "__main__":
  print('Mandala - DadoSoft')
  Win.mainloop()
