#!/usr/bin/env python3

from pxi16parser import nsclpxi16evread as nscl
from parsegen import matwrite
import numpy as np

if __name__ == "__main__":
	
	import sys
	filename=sys.argv[1]
	matfilename1=sys.argv[2]
	matfilename2=sys.argv[3]
	overwrite=int(sys.argv[4])
	PID=np.ndarray(shape=(8192,4096),dtype=np.int32)
	ScintEnLeft=np.ndarray(shape=(1,8192),dtype=np.int32)
	
	with open(filename, mode='rb') as f:
		while(1):
			temp=nscl(f)
			if temp == -1:
				break
			elif temp == 0:
				continue
			else:
				sevtmult=len(temp)
				t1=0
				t2=0
				dE=0
				t3=0
				
				for i in range(0,sevtmult,1):
					if temp[i].iddet == 353: #MSX 100
						dE = dE+1
						Energy=temp[i].energy
					if temp[i].iddet == 245: #Image Scintillator Left
						t1 = t1+1
						temptime=temp[i].ctimef
						t1time = temp[i].time + (temp[i].ctime/16384)
						if temptime == 1:
							t1time = t1time*4
						else:
							t1time = t1time*8
							
						Eleft=temp[i].energy
					if temp[i].iddet == 232: #Cross Scintillaotr B2
						t2 = t2+1
						temptime = temp[i].ctimef
						t2time = temp[i].time + (temp[i].ctime/16384)
						if temptime == 1:
							t1time = t1time*4
						else:
							t1time = t1time*8

				if (t1 >= 1) and t2 >= 1 and dE >= 1:
					deltatime=(t1time-t2time)
					#if t1time > t2time:
					#	deltatime=((t1time-t2time)*4)
					#else:
					#	deltatime=((t2time-t1time)*4)
					
					deltatime=(deltatime)*10-2000
					print("sevtmult:",sevtmult,"iddet:",temp[i].iddet,"t1time:",t1time,"t2time:",t2time,"tdiff:",deltatime,"energy:",Energy,"Eleft:",Eleft)
					if (Energy >=0 and Energy < 8192) and (deltatime >=0 and deltatime < 4096):
						PID[Energy][int(deltatime)]=PID[Energy][int(deltatime)]+1
					if (Eleft >= 0 and Eleft < 8192):
						ScintEnLeft[0][Eleft]=ScintEnLeft[0][Eleft]+1				
				
	matwrite(matfilename1,dimy=8192,dimx=4096,arr=PID,overwrite=overwrite)
	matwrite(matfilename2,dimy=1,dimx=8192,arr=ScintEnLeft,overwrite=overwrite)
