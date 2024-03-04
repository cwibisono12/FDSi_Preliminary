#!/usr/bin/env python3

from pxi16parser import nsclpxi16evread as nscl
from parsegen import matwrite
import numpy as np
from PID import PID
from YSO import YSO
from Clover import Clover

if __name__ == "__main__":
	import sys
	'''
	Below is an example of how to use several modules above to generate multiple uncorrelated plots:
	C. Wibisono
	03/03 '24
	'''
	filename=sys.argv[1] #rawdata 
	filecalib=sys.argv[2] #Clover Calibration file
	matfilename1=sys.argv[3] #PID
	matfilename2=sys.argv[4] #Clover
	matfilename3=sys.argv[5] #Implant Ions
	matfilename4=sys.argv[6] #Implant Beta
	overwrite=int(sys.argv[7])
	PIDarr=np.ndarray(shape=(8192,4096),dtype=np.int32)
	Cloverarr=np.ndarray(shape=(16,8192),dtype=np.int32)
	ImplantIonsarr=np.ndarray(shape=(1000,1000),dtype=np.int32)
	ImplantBetaarr=np.ndarray(shape=(1000,1000),dtype=np.int32)
	
	with open(filename, mode='rb') as f:
		while(1):
			temp=nscl(f)
			if temp == -1:
				break
			elif temp == 0:
				continue
			else:
				Energy = 0
				TOF = 0
				flagPID=0
				flagYSO=0
				result=PID(temp)
				if result != 'Not Found':
					Energy, TOF = result
					flagPID=1
				Ge = Clover(filecalib,temp)
				result2 = YSO(temp)				
				if result2 != 'Not Found':
					YSOposition=result2
					flagYSO=1				

				#Fill the PID:
				if flagPID == 1:
					if (Energy >= 0 and Energy < 8192) and (TOF >= 0 and TOF < 4096):
						PIDarr[Energy][int(TOF)]=PIDarr[Energy][int(TOF)]+1						
	
				#Fill the Clover:
				for i,j in Ge.items():
					Cloverarr[int(i)][j]=Cloverarr[int(i)][j]+1
				
				#Fill the Implants: -Ions
				if flagYSO == 1:
					if (YSOposition[0][0] >= 0 and YSOposition[0][0] < 999) and (YSOposition[0][1] >= 0 and YSOposition[0][1] < 999):
						ImplantIonsarr[YSOposition[0][1]][YSOposition[0][0]]=ImplantIonsarr[YSOposition[0][1]][YSOposition[0][0]]+1
				
				#Fill the Implants: -Beta
					if (YSOposition[1][0] >= 0 and YSOposition[1][0] < 999) and (YSOposition[1][1] >= 0 and YSOposition[1][1] < 999):
						ImplantBetaarr[YSOposition[1][1]][YSOposition[1][0]]=ImplantBetaarr[YSOposition[1][1]][YSOposition[1][0]]+1
								

	matwrite(matfilename1,dimy=8192,dimx=4096,arr=PIDarr,overwrite=overwrite)
	matwrite(matfilename2,dimy=16,dimx=8192,arr=Cloverarr,overwrite=overwrite)
	matwrite(matfilename3,dimy=1000,dimx=1000,arr=ImplantIonsarr,overwrite=overwrite)
	matwrite(matfilename4,dimy=1000,dimx=1000,arr=ImplantBetaarr,overwrite=overwrite)
