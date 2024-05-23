#!/usr/bin/env python3

from pxi16parser import nsclpxi16evread as nscl
from parsegen import matwrite
import numpy as np
from Implant import Implant
from Decay import Decay
from Clover import Clover
from bancut import bancut 
from readcutfile import readcutfile as read

if __name__ == "__main__":
	import sys
	'''
	Below is an example of how to use several modules above to generate gamma spectrum that are in coincidence with implants:
	C. Wibisono
	03/03 '24
	'''
	filename = sys.argv[1] #rawdata 
	filecalib = sys.argv[2] #Clover Calibration file
	cutfile = sys.argv[3]
	Clover41P=np.ndarray(shape=(16,8192),dtype = np.int32)
	Clover42P=np.ndarray(shape=(16,8192),dtype = np.int32)
	Clover43P=np.ndarray(shape=(16,8192),dtype = np.int32)
	Clover44P=np.ndarray(shape=(16,8192),dtype = np.int32)
	matfilename1=sys.argv[4] #41P
	matfilename2=sys.argv[5] #42P
	matfilename3=sys.argv[6] #43P
	matfilename4=sys.argv[7] #44P
	overwrite=int(sys.argv[8])
	#PIDarr=np.ndarray(shape=(8192,4096),dtype=np.int32)
	#Cloverarr=np.ndarray(shape=(16,8192),dtype=np.int32)
	#ImplantIonsarr=np.ndarray(shape=(1000,1000),dtype=np.int32)
	#ImplantBetaarr=np.ndarray(shape=(1000,1000),dtype=np.int32)
	
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
					xions=result[2][0]*1000
					yions=result[2][1]*1000
					
					
					flag41P = bancut(tof, float(energy), ImplantIDdict['41P'][0], ImplantIDdict['41P'][1], n41Pcut)
					flag42P = bancut(tof, float(energy),ImplantIDdict['42P'][0], ImplantIDdict['42P'][1], n42Pcut)
					flag43P = bancut(tof, float(energy),ImplantIDdict['43P'][0], ImplantIDdict['43P'][1], n43Pcut)
					flag44P = bancut(tof, float(energy), ImplantIDdict['44P'][0], ImplantIDdict['44P'][1], n44Pcut)
 			
					
					
				
					if flag41P == 1:
						print("41P")
						Ge1 = Clover(filecalib, temp)					
						for i, j in Ge1.items():
							Clover41P[int(i)][j] = Clover41P[int(i)][j] + 1

					
					if flag42P == 1:
						print("42P")
						Ge2 = Clover(filecalib, temp)					
						for i, j in Ge2.items():
							Clover42P[int(i)][j] = Clover42P[int(i)][j] + 1
				

					if flag43P == 1:
						print("43P")
						Ge3 = Clover(filecalib, temp)					
						for i, j in Ge3.items():
							Clover43P[int(i)][j] = Clover43P[int(i)][j] + 1

					if flag44P == 1:
						print("44P")
						Ge4 = Clover(filecalib, temp)					
						for i, j in Ge4.items():
							Clover44P[int(i)][j] = Clover44P[int(i)][j] + 1
	


	matwrite(matfilename1,dimy=16,dimx=8192,arr=Clover41P,overwrite=overwrite)
	matwrite(matfilename2,dimy=16,dimx=8192,arr=Clover42P,overwrite=overwrite)
	matwrite(matfilename3,dimy=16,dimx=8192,arr=Clover43P,overwrite=overwrite)
	matwrite(matfilename4,dimy=16,dimx=8192,arr=Clover44P,overwrite=overwrite)

