#!/usr/bin/env python3

from pxi16parser import nsclpxi16evread as nscl
from parsegen import matwrite
import numpy as np
from Implant import Implant
from Decay import Decay
from Clover import Clover
from bancut import bancut 
from readcutfile import readcutfile as read
from correvent import imwrite as im
from correvent import betawrite as beta


if __name__ == "__main__":
	import sys
	'''
	Below is an example of how to use several modules above to generate implants and decay events:
	C. Wibisono
	03/03 '24
	'''
	filename = sys.argv[1] #rawdata 
	filecalib = sys.argv[2] #Clover Calibration file
	cutfile = sys.argv[3]
	filecorr = open(sys.argv[4], mode = 'wb')
	
	ImplantIDdict = read(cutfile) #Open the Cut File
	n41Pcut = len(ImplantIDdict['41P'][0])
	n42Pcut = len(ImplantIDdict['42P'][0])
	n43Pcut = len(ImplantIDdict['43P'][0])
	n44Pcut = len(ImplantIDdict['44P'][0])
	
	

	with open(filename, mode='rb') as f:
		while(1):
			temp=nscl(f)
			if temp == -1:
				break
			elif temp == 0:
				continue
			else:
				flagImplant=0
				flag41P = 0
				flag42P = 0
				flag43P = 0
				flag44P = 0
				result = Implant(temp)
				
				if result != 'Not Found':
					flagImplant == 1
					energy = result[0]
					tof = result[1]
					#if (energy >= 0 and energy < 8192) and tof > 0 and tof < 4096:
					#	PIDarr[int(energy)][int(tof)]=PIDarr[int(energy)][int(tof)] + 1
					xions=result[2][0]*1000
					yions=result[2][1]*1000
					
					
					flag41P = bancut(tof, float(energy), ImplantIDdict['41P'][0], ImplantIDdict['41P'][1], n41Pcut)
					flag42P = bancut(tof, float(energy),ImplantIDdict['42P'][0], ImplantIDdict['42P'][1], n42Pcut)
					flag43P = bancut(tof, float(energy),ImplantIDdict['43P'][0], ImplantIDdict['43P'][1], n43Pcut)
					flag44P = bancut(tof, float(energy), ImplantIDdict['44P'][0], ImplantIDdict['44P'][1], n44Pcut)
 			
					
					#Ge = Clover(filecalib, temp)
					
					#if (xions >= 0 and xions <1000) and (yions >=0 and yions < 1000):
					#	ImplantIonsarr[int(yions)][int(xions)]=ImplantIonsarr[int(yions)][int(xions)] + 1							
				
					if flag41P == 1:
						print("41P")
						im(filecorr,result)	
						#Ge1 = Clover(filecalib, temp)					
						#for i, j in Ge1.items():
						#	Clover41P[int(i)][j] = Clover41P[int(i)][j] + 1

					
					if flag42P == 1:
						print("42P")
						im(filecorr,result)
						#Ge2 = Clover(filecalib, temp)					
						#for i, j in Ge2.items():
						#	Clover42P[int(i)][j] = Clover42P[int(i)][j] + 1
				

					if flag43P == 1:
						print("43P")
						im(filecorr,result)
						#Ge3 = Clover(filecalib, temp)					
						#for i, j in Ge3.items():
						#	Clover43P[int(i)][j] = Clover43P[int(i)][j] + 1

					if flag44P == 1:
						print("44P")
						im(filecorr,result)
						
						#Ge4 = Clover(filecalib, temp)					
						#for i, j in Ge4.items():
						#	Clover44P[int(i)][j] = Clover44P[int(i)][j] + 1
	

				
				result2 = Decay(temp)
				flagDecay = 0			
				if result2 != 'Not Found':
					Ge = Clover(filecalib, temp)
					beta(filecorr, result2, Ge)


	filecorr.close()
