#!/usr/bin/env python3
from struct import *
from dataclasses import dataclass

'''
@dataclass
class imevent:
	imflag: int
	imID: int
	dE: int
	TOF: int
	x: int
	y: int
	imtime: int
	gmult: int	

@dataclass
class betaevent:
	betaflag: int
	x: int
	y: int
	betatime: int
	gmult: int

'''

def imwrite(fpr, implant, impID, Clover):
	'''
	Function to write implant event into a file
	C. Wibisono
	03/07 '24 
	'''
	p=Struct("@i")
	q=Struct("@Q")
	imflag=Struct("@B")
	imid=Struct("@H")
	fpr.write(imflag.pack(1)) #identifier for implant event
	fpr.write(imid.pack(impID))
	fpr.write(p.pack(int(implant[0]))) #delta E
	fpr.write(p.pack(int(implant[1]))) #TOF
	fpr.write(p.pack(int(implant[2][0]*1000))) #x position
	fpr.write(p.pack(int(implant[2][1]*1000))) #y position
	fpr.write(q.pack(int(implant[3]))) #time
	idClover = []
	energy = []
	for i, j in Clover.items():
		idClover.append(i)
		energy.append(j)
	gmult = len(energy)
	fpr.write(imflag.pack(gmult))
	for k in range(gmult):
		fpr.write(imflag.pack(int(idClover[k])))
		fpr.write(p.pack(energy[k]))

def imread(fpr):
	'''
	Function to read implant event into a file
	C. Wibisono
	03/07 '24 
	'''
	p=Struct("@i")
	q=Struct("@Q")
	r=Struct("@H")
	imflag=Struct("@B")
	flagim,=imflag.unpack(fpr.read(1))
	impid,=r.unpack(fpr.read(2))
	dE,=p.unpack(fpr.read(4))
	TOF,=p.unpack(fpr.read(4))
	xpos,=p.unpack(fpr.read(4))
	ypos,=p.unpack(fpr.read(4))
	imtime,=q.unpack(fpr.read(8))
	gmult,=imflag.unpack(fpr.read(1))
	gammas = {}
	for i in range(gmult):
		gamid, = imflag.unpack(fpr.read(1))
		gamen, = p.unpack(fpr.read(4))
		gammas[str(gamid)] = gamen	
	#print("implant---",impid,"energy:",dE,"TOF:",TOF,"( x, y):",xpos,ypos,"imtime",imtime)
	imarr = [flagim, impid, dE, TOF, xpos, ypos, imtime, gmult]
	#temp = imevent(flagim, impid, dE, TOF, xpos, ypos, imtime)
	return imarr, gammas
	
def betaread(fpr):
	'''
	Function to read beta event into a file
	C. Wibisono
	03/07 '24
	'''
	p=Struct("@i")
	q=Struct("@Q")
	r=Struct("@h")
	betaflag=Struct("@B")
	flagbeta,=betaflag.unpack(fpr.read(1))
	xpos,=p.unpack(fpr.read(4))
	ypos,=p.unpack(fpr.read(4))
	betatime,=q.unpack(fpr.read(8))
	gmult,=betaflag.unpack(fpr.read(1))
	
	gammas={}
	for i in range(gmult):
		gamid, =betaflag.unpack(fpr.read(1))
		gamenergy, =p.unpack(fpr.read(4))
		gammas[str(gamid)] = gamenergy

	#print("decay---","(x,y):",xpos,ypos,"betatime:",betatime,"gmult:",gmult)
	#temp = betaevent(flagbeta, xpos, ypos, betatime, gmult)
	betaarr=[flagbeta, xpos, ypos, betatime, gmult]
	
	#if gmult == 0:
	#	return temp
	#else:
	#	arr = [temp, gammas]
	#	return arr
	return betaarr, gammas	

def betawrite(fpr, beta, Clover):
	'''
	Function to write beta event into a file
	C. Wibisono
	03/07 '24
	'''
	p=Struct("@i")
	q=Struct("@Q")
	betaflag=Struct("@B")
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
	fpr.write(betaflag.pack(gmult)) #germanium multiplicity
	for i in range(gmult):
		fpr.write(betaflag.pack(int(idClover[i]))) #Clover ID
		fpr.write(p.pack(int(energy[i]))) #Energy

