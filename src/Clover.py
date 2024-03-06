#!/usr/bin/env python3

from pxi16parser import nsclpxi16evread as nscl
from parsegen import matwrite
import numpy as np
from readcalibclover import readcalibclover as r


def Clover(filecalib, pxi16obj):
	'''
	Clover Function Processor:
	C. Wibisono
	03/03 '24
	Function Argument(s):
	filecalib: file pointer for calibration
	pxi16obj: pixie16 object data class --->see pxi16parser module for details
	Return:
	Clover object (dict): key (Clover ID) value (Clover energy)
	'''
	Ge=r(filecalib)
	sevtmult=len(pxi16obj)
	Cl1=0
	Cl2=0
	Cl3=0
	Cl5=0
	Cl6=0
	Cl7=0
	Cl9=0
	Cl10=0
	Cl11=0
	Cl12=0
	Cl13=0
	Cl1en=[]
	Cl2en=[]
	Cl3en=[]
	Cl5en=[]
	Cl6en=[]
	Cl7en=[]
	Cl9en=[]
	Cl10en=[]
	Cl11en=[]
	Cl12en=[]
	Cl13en=[]
	Cl={}
				
	for i in range(0,sevtmult,1):
		if pxi16obj[i].iddet >= 256 and pxi16obj[i].iddet <=259: #Cl1
			Cl1=Cl1+1
			energy=2.*Ge[str(pxi16obj[i].iddet)][1]*pxi16obj[i].energy+Ge[str(pxi16obj[i].iddet)][0]
			Cl1en.append(energy)
					
		if pxi16obj[i].iddet >= 260 and pxi16obj[i].iddet <=263: #Cl2
			Cl2=Cl2+1
			energy=2.*Ge[str(pxi16obj[i].iddet)][1]*pxi16obj[i].energy+Ge[str(pxi16obj[i].iddet)][0]
			Cl2en.append(energy)
					
		if pxi16obj[i].iddet == 264 or pxi16obj[i].iddet == 267 or (pxi16obj[i].iddet >= 308 and pxi16obj[i].iddet <= 309): #Cl3
			Cl3=Cl3+1
			energy=2.*Ge[str(pxi16obj[i].iddet)][1]*pxi16obj[i].energy+Ge[str(pxi16obj[i].iddet)][0]
			Cl3en.append(energy)
					
		if pxi16obj[i].iddet >= 272 and pxi16obj[i].iddet <= 275: #Cl5
			Cl5=Cl5+1
			energy=2.*Ge[str(pxi16obj[i].iddet)][1]*pxi16obj[i].energy+Ge[str(pxi16obj[i].iddet)][0]
			Cl5en.append(energy)
	
		if pxi16obj[i].iddet >= 276 and pxi16obj[i].iddet <= 279: #Cl6
			Cl6=Cl6+1
			energy=2.*Ge[str(pxi16obj[i].iddet)][1]*pxi16obj[i].energy+Ge[str(pxi16obj[i].iddet)][0]
			Cl6en.append(energy)
	
		if (pxi16obj[i].iddet >= 310 and pxi16obj[i].iddet <= 312) or pxi16obj[i].iddet == 283: #Cl7
			Cl7=Cl7+1
			energy=2.*Ge[str(pxi16obj[i].iddet)][1]*pxi16obj[i].energy+Ge[str(pxi16obj[i].iddet)][0]
			Cl7en.append(energy)
	
						
		if pxi16obj[i].iddet >= 288 and pxi16obj[i].iddet <= 291: #Cl9
			Cl9=Cl9+1
			energy=2.*Ge[str(pxi16obj[i].iddet)][1]*pxi16obj[i].energy+Ge[str(pxi16obj[i].iddet)][0]
			Cl9en.append(energy)
			
		if pxi16obj[i].iddet >= 292 and pxi16obj[i].iddet <= 295: #Cl10
			Cl10=Cl10+1
			energy=2.*Ge[str(pxi16obj[i].iddet)][1]*pxi16obj[i].energy+Ge[str(pxi16obj[i].iddet)][0]
			Cl10en.append(energy)

		if pxi16obj[i].iddet >= 296 and pxi16obj[i].iddet <= 299: #Cl11
			Cl11=Cl11+1
			energy=2.*Ge[str(pxi16obj[i].iddet)][1]*pxi16obj[i].energy+Ge[str(pxi16obj[i].iddet)][0]
			Cl11en.append(energy)
	
		if (pxi16obj[i].iddet >= 340 and pxi16obj[i].iddet <= 341) or (pxi16obj[i].iddet >=302 and pxi16obj[i].iddet <= 303): #Cl12
			Cl12=Cl12+1
			energy=2.*Ge[str(pxi16obj[i].iddet)][1]*pxi16obj[i].energy+Ge[str(pxi16obj[i].iddet)][0]
			Cl12en.append(energy)

		if pxi16obj[i].iddet >= 304 and pxi16obj[i].iddet <= 307: #Cl13
			Cl13=Cl13+1
			energy=2.*Ge[str(pxi16obj[i].iddet)][1]*pxi16obj[i].energy+Ge[str(pxi16obj[i].iddet)][0]
			Cl13en.append(energy)
					
	if Cl1 >= 1:
		n=len(Cl1en)
		if n <= 4:
			realen=int(sum(Cl1en))
			if realen >= 0 and realen < 8192:
				Cl['1']=realen
				#print("Cl1:",realen)	
	
	if Cl2 >= 1:
		n=len(Cl2en)
		if n <= 4:
			realen=int(sum(Cl2en))
			if realen >= 0 and realen < 8192:
				Cl['2']=realen
				#print("Cl2:",realen)

	if Cl3 >= 1:
		n=len(Cl3en)
		if n <= 4:
			realen=int(sum(Cl3en))
			if realen >= 0 and realen < 8192:
				Cl['3']=realen
				#print("Cl3:",realen)	
	
	if Cl5 >= 1:
		n=len(Cl5en)
		if n <= 4:
			realen=int(sum(Cl5en))
			if realen >= 0 and realen < 8192:
				Cl['5']=realen
				#print("Cl5:",realen)	

	if Cl6 >= 1:
		n=len(Cl6en)
		if n <= 4:
			realen=int(sum(Cl6en))
			if realen >= 0 and realen < 8192:
				Cl['6']=realen
				#print("Cl6:",realen)	
	
	if Cl7 >= 1:
		n=len(Cl7en)
		if n <= 4:
			realen=int(sum(Cl7en))
			if realen >= 0 and realen < 8192:
				Cl['7']=realen
				#print("Cl6:",realen)	

	if Cl9 >= 1:
		n=len(Cl9en)
		if n <= 4:
			realen=int(sum(Cl9en))
			if realen >= 0 and realen < 8192:
				Cl['9']=realen
				#print("Cl9:",realen)	

				
	if Cl10 >= 1:
		n=len(Cl10en)
		if n <= 4:
			realen=int(sum(Cl10en))
			if realen >= 0 and realen < 8192:
				Cl['10']=realen
				#print("Cl10:",realen)	

	if Cl11 >= 1:
		n=len(Cl11en)
		if n <= 4:
			realen=int(sum(Cl11en))
			if realen >= 0 and realen < 8192:
				Cl['11']=realen
				#print("Cl11:",realen)

	if Cl12 >= 1:
		n=len(Cl12en)
		if n <= 4:
			realen=int(sum(Cl12en))
			if realen >= 0 and realen < 8192:
				Cl['12']=realen
				#print("Cl12:",realen)	
			
	if Cl13 >= 1:
		n=len(Cl13en)
		if n <= 4:
			realen=int(sum(Cl13en))
			if realen >= 0 and realen < 8192:
				Cl['13']=realen
				#print("Cl13:",realen)	

	return Cl	


