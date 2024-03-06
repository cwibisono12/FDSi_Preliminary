#!/usr/bin/env python3

from pxi16parser import nsclpxi16evread as nscl
from parsegen import matwrite
import numpy as np
from Implant import Implant
from Decay import Decay
from Clover import Clover

if __name__ == "__main__":
	import sys
	'''
	Below is an example of how to use several modules above to generate implants and decay events:
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
				flagImplant=0
				result = Implant(temp)
				
				if result != 'Not Found':
					flagImplant == 1
					energy = result[0]
					tof = result[1]
					if (energy >= 0 and energy < 8192) and tof > 0 and tof < 4096:
						PIDarr[int(energy)][int(tof)]=PIDarr[int(energy)][int(tof)] + 1
					xions=result[2][0]*1000
					yions=result[2][1]*1000
					if (xions >= 0 and xions <1000) and (yions >=0 and yions < 1000):
						ImplantIonsarr[int(yions)][int(xions)]=ImplantIonsarr[int(yions)][int(xions)] + 1							
				

				result2 = Decay(temp)
				flagDecay = 0			
				if result2 != 'Not Found':
					flagDecay = 1
					xbeta=result2[0][0]*1000
					ybeta=result2[0][1]*1000
					
					if (xbeta >= 0 and xbeta< 1000) and (ybeta>=0 and ybeta < 1000):				
						ImplantBetaarr[int(ybeta)][int(xbeta)]=ImplantBetaarr[int(ybeta)][int(xbeta)]+1

			
				if flagImplant == 0 and flagDecay == 1:
					Ge = Clover(filecalib,temp)
					for i, j in Ge.items():
						Cloverarr[int(i)][j]=Cloverarr[int(i)][j] + 1

	matwrite(matfilename1,dimy=8192,dimx=4096,arr=PIDarr,overwrite=overwrite)
	matwrite(matfilename2,dimy=16,dimx=8192,arr=Cloverarr,overwrite=overwrite)
	matwrite(matfilename3,dimy=1000,dimx=1000,arr=ImplantIonsarr,overwrite=overwrite)
	matwrite(matfilename4,dimy=1000,dimx=1000,arr=ImplantBetaarr,overwrite=overwrite)

