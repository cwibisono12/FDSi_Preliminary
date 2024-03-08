#!/usr/bin/env python3
from struct import *


def imwrite(fpr, implant):
	'''
	Function to write implant event into a file
	C. Wibisono
	03/07 '24 
	'''
	p=Struct("@i")
	q=Struct("@Q")
	imflag=Struct("@h")
	fpr.write(imflag.pack(1)) #identifier for implant
	fpr.write(p.pack(int(implant[0]))) #delta E
	fpr.write(p.pack(int(implant[1]))) #TOF
	fpr.write(p.pack(int(implant[2][0]*1000))) #x position
	fpr.write(p.pack(int(implant[2][1]*1000))) #y position
	fpr.write(q.pack(int(implant[3]))) #time



def imread(fpr):
	'''
	Function to write implant event into a file
	C. Wibisono
	03/07 '24 
	'''
	p=Struct("@i")
	q=Struct("@Q")
	imflag=Struct("@h")
	flagim,=imflag.unpack(fpr.read(2))
	dE,=p.unpack(fpr.read(4))
	TOF,=p.unpack(fpr.read(4))
	xpos,=p.unpack(fpr.read(4))
	ypos,=p.unpack(fpr.read(4))
	imtime,=q.unpack(fpr.read(8))	
	print("implant---","energy:",dE,"TOF:",TOF,"( x, y):",xpos,ypos,"imtime",imtime)

def betaread(fpr):
	'''
	Function to read beta event into a file
	C. Wibisono
	03/07 '24
	'''
	p=Struct("@i")
	q=Struct("@Q")
	r=Struct("@h")
	betaflag=Struct("@h")
	flagbeta,=betaflag.unpack(fpr.read(2))
	xpos,=p.unpack(fpr.read(4))
	ypos,=p.unpack(fpr.read(4))
	betatime,=q.unpack(fpr.read(8))
	gmult,=r.unpack(fpr.read(2))
	
	
	for i in range(gmult):
		fpr.read(2)
		fpr.read(4)

	print("decay---","(x,y):",xpos,ypos,"betatime:",betatime,"gmult:",gmult)

def betawrite(fpr, beta, Clover):
	'''
	Function to write beta event into a file
	C. Wibisono
	03/07 '24
	'''
	p=Struct("@i")
	q=Struct("@Q")
	r=Struct("@h")
	betaflag=Struct("@h")
	fpr.write(betaflag.pack(2)) #identifier for beta
	fpr.write(p.pack(int(beta[0][0]*1000))) #x position
	fpr.write(p.pack(int(beta[0][1]*1000))) #y position
	fpr.write(q.pack(int(beta[1]))) #betatime
	idClover = []
	energy = []
	for i, j in Clover.items():
		idClover.append(i)
		energy.append(j)
	gmult=len(energy)
	fpr.write(r.pack(gmult)) #germanium multiplicity
	for i in range(gmult):
		fpr.write(r.pack(int(idClover[i]))) #Clover ID
		fpr.write(p.pack(int(energy[i]))) #Energy

