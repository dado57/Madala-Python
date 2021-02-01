# Mandala - DadoSoft 2021
# Windows10 - Python 3.8.5

from math import sin,cos,pi
import random as R

def CreaCooPol(NVe,Rmin,Rmax,Amp,SA):
  ''' Crea vertici random in coordinate polari
    Ritorna lista di Lunghezze e lista di Angoli
    NVe  Numero Vertici
    Rmin Raggio Minimo
    Rmax Raggio Massimo
    Amp  Ampiezza range angolo in radianti
    Sa   Sovvrapposizione Angolo
  '''
  Lr=[]
  Ar=[]
  for i in range(0,NVe):
    Lr.append(R.random() * (Rmax-Rmin) + Rmin)
    Ar.append((R.random() * (Amp+(Amp*SA/10)))-(Amp*SA/20))
    # print(i)
  return Lr,Ar

def Ruota(Lz,Az,anR):
  ''' Ruota Vertici di anR
    Ritorna Lista di Lunghezze e Lista di Angoli
    Lz  Lista lunghezze in pixel
    Az  Lista angoli in radianti
    anR Angolo in radianti della rotazione
  '''
  L1=Lz.copy()
  A1=[]
  for i in Az:
    A1.append(i+anR)
  return L1,A1

def Specchia(Lz,Az,anR):
  ''' Specchia Vertici rispetto a un angolo
      Ritorna Lista di Lunghezze e Lista di Angoli
       Lz Lista lunghezze
       Az Lista angoli in radianti
      anR Angolo in radianti su cui specchiare
  '''
  L1=Lz.copy()
  A1=[]
  for i in Az:
    A1.append(anR-i)
  return L1,A1


def CartFromPolar(l,a,cx,cy):
  ''' Da coordinate Cartesiane a Polari'''
  co=[]
  for i in range(0,len(l)):
    x= cx+l[i]*sin(a[i])
    y= cy+l[i]*cos(a[i])
    co.append(x)
    co.append(y)
  return co
      
def CreaCorona(NVe,Rmin,Rmax,Amp,SA,Specchia):
  ''' Crea ruota e specchia 
      Ritorna lista di Lunghezze e lista di Angoli
      NVe  Numero Vertici
      Rmin Raggio Minimo
      Rmax Raggio Massimo
      Amp  Ampiezza range angolo in radianti
  '''
  Lr=[]
  Ar=[]
  if Specchia: 
    Ang=Amp/2
  else:
    Ang=Amp
    
  for i in range(0,NVe):
    Lr.append(R.random() * (Rmax-Rmin) + Rmin)
    Ar.append(((R.random() * (Ang+(Ang*SA/50)))-(Ang/100*SA))/NVe*i)

  if Specchia: 
    Ls=Lr.copy()
    Ls.reverse()
    As=Ar.copy()
    As.reverse()
    # aggiunge Ang ad ogni elemento della lista As
    As = list(map(lambda e:e+Ang, As))
    Lr.extend(Ls)
    Ar.extend(As)

  return Lr,Ar
   

##################################################

def DatiRett_Vertici(x,y,lx,ly,ang):
  # converte da:
  #   x,y Centro rettangolo
  # lx,ly Lati rettangolo
  #   ang Angolo rotazione
  # a coordinate 4 vertici del rettangolo
  ax=lx/2*cos(ang)-ly/2*sin(ang)  
  ay=lx/2*sin(ang)+ly/2*cos(ang)
  bx=ly/2*sin(ang)+lx/2*cos(ang)
  by=ly/2*cos(ang)-lx/2*sin(ang)
  x1=x+ax
  y1=y+ay
  x2=x+bx
  y2=y-by
  x3=x-ax
  y3=y-ay
  x4=x-bx
  y4=y+by
  return [x1,y1,x2,y2,x3,y3,x4,y4]



def Stampa(Lr,Ar):
  # Stampa lista di Lunghezze e Angoli
  fmtL = "L=" + ''.join(["{:>7.2f}"]*len(Lr))
  fmtA = "A=" + ''.join(["{:>7.2f}"]*len(Ar))
  print ('')
  print ('--',Ar)
  print(fmtL.format(*Lr))
  print(fmtA.format(*Ar))




