#!/usr/bin/env python3

from pxi16parser import nsclpxi16evread as nscl
from parsegen import matwrite
import numpy as np

if __name__ == "__main__":
	
	import sys
	filename=sys.argv[1]
	filecalib=sys.argv[2]
	matfilename1=sys.argv[3]
	overwrite=int(sys.argv[4])
	Clover=np.ndarray(shape=(16,8192),dtype=np.int32)

	Ge={}
	with open(filecalib,mode='r') as fcal:
		lines = fcal.readlines()
		for line in lines:
			if line.find('#') == -1:
				row=line.split()
				Cloverid=row[0]
				intercept=float(row[1])
				slope=float(row[2])	
				Ge[Cloverid]=[intercept,slope]

	
	with open(filename, mode='rb') as f:
		while(1):
			temp=nscl(f)
			if temp == -1:
				break
			elif temp == 0:
				continue
			else:
				sevtmult=len(temp)
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

				
				for i in range(0,sevtmult,1):
					if temp[i].iddet >= 256 and temp[i].iddet <=259: #Cl1
						Cl1=Cl1+1
						energy=2.*Ge[str(temp[i].iddet)][1]*temp[i].energy+Ge[str(temp[i].iddet)][0]
						Cl1en.append(energy)
					
					if temp[i].iddet >= 260 and temp[i].iddet <=263: #Cl2
						Cl2=Cl2+1
						energy=2.*Ge[str(temp[i].iddet)][1]*temp[i].energy+Ge[str(temp[i].iddet)][0]
						Cl2en.append(energy)
					
					if temp[i].iddet == 264 or temp[i].iddet == 267 or (temp[i].iddet >= 308 and temp[i].iddet <= 309): #Cl3
						Cl3=Cl3+1
						energy=2.*Ge[str(temp[i].iddet)][1]*temp[i].energy+Ge[str(temp[i].iddet)][0]
						Cl3en.append(energy)
					
					if temp[i].iddet >= 272 and temp[i].iddet <= 275: #Cl5
						Cl5=Cl5+1
						energy=2.*Ge[str(temp[i].iddet)][1]*temp[i].energy+Ge[str(temp[i].iddet)][0]
						Cl5en.append(energy)
	
					if temp[i].iddet >= 276 and temp[i].iddet <= 279: #Cl6
						Cl6=Cl6+1
						energy=2.*Ge[str(temp[i].iddet)][1]*temp[i].energy+Ge[str(temp[i].iddet)][0]
						Cl6en.append(energy)
	
					if (temp[i].iddet >= 310 and temp[i].iddet <= 312) or temp[i].iddet == 283: #Cl7
						Cl7=Cl7+1
						energy=2.*Ge[str(temp[i].iddet)][1]*temp[i].energy+Ge[str(temp[i].iddet)][0]
						Cl7en.append(energy)
	
						
					if temp[i].iddet >= 288 and temp[i].iddet <= 291: #Cl9
						Cl9=Cl9+1
						energy=2.*Ge[str(temp[i].iddet)][1]*temp[i].energy+Ge[str(temp[i].iddet)][0]
						Cl9en.append(energy)
			
					if temp[i].iddet >= 292 and temp[i].iddet <= 295: #Cl10
						Cl10=Cl10+1
						energy=2.*Ge[str(temp[i].iddet)][1]*temp[i].energy+Ge[str(temp[i].iddet)][0]
						Cl10en.append(energy)

					if temp[i].iddet >= 296 and temp[i].iddet <= 299: #Cl11
						Cl11=Cl11+1
						energy=2.*Ge[str(temp[i].iddet)][1]*temp[i].energy+Ge[str(temp[i].iddet)][0]
						Cl11en.append(energy)
	
					if (temp[i].iddet >= 340 and temp[i].iddet <= 341) or (temp[i].iddet >=302 and temp[i].iddet <= 303): #Cl12
						Cl12=Cl12+1
						energy=2.*Ge[str(temp[i].iddet)][1]*temp[i].energy+Ge[str(temp[i].iddet)][0]
						Cl12en.append(energy)

					if temp[i].iddet >= 304 and temp[i].iddet <= 307: #Cl13
						Cl13=Cl13+1
						energy=2.*Ge[str(temp[i].iddet)][1]*temp[i].energy+Ge[str(temp[i].iddet)][0]
						Cl13en.append(energy)
					
				if Cl1 >= 1:
					n=len(Cl1en)
					if n <= 4:
						realen=int(sum(Cl1en))
						if realen >= 0 and realen < 8192:
							Clover[1][realen]=Clover[1][realen]+1			
							print("Cl1:",realen)	
	
				if Cl2 >= 1:
					n=len(Cl2en)
					if n <= 4:
						realen=int(sum(Cl2en))
						if realen >= 0 and realen < 8192:
							Clover[2][realen]=Clover[2][realen]+1			
							print("Cl2:",realen)

				if Cl3 >= 1:
					n=len(Cl3en)
					if n <= 4:
						realen=int(sum(Cl3en))
						if realen >= 0 and realen < 8192:
							Clover[3][realen]=Clover[3][realen]+1			
							print("Cl3:",realen)	
	
				if Cl5 >= 1:
					n=len(Cl5en)
					if n <= 4:
						realen=int(sum(Cl5en))
						if realen >= 0 and realen < 8192:
							Clover[5][realen]=Clover[5][realen]+1			
							print("Cl5:",realen)	

				if Cl6 >= 1:
					n=len(Cl6en)
					if n <= 4:
						realen=int(sum(Cl6en))
						if realen >= 0 and realen < 8192:
							Clover[6][realen]=Clover[6][realen]+1			
							print("Cl6:",realen)	
	
				if Cl7 >= 1:
					n=len(Cl7en)
					if n <= 4:
						realen=int(sum(Cl7en))
						if realen >= 0 and realen < 8192:
							Clover[7][realen]=Clover[7][realen]+1			
							print("Cl6:",realen)	

				if Cl9 >= 1:
					n=len(Cl9en)
					if n <= 4:
						realen=int(sum(Cl9en))
						if realen >= 0 and realen < 8192:
							Clover[9][realen]=Clover[9][realen]+1			
							print("Cl9:",realen)	

				
				if Cl10 >= 1:
					n=len(Cl10en)
					if n <= 4:
						realen=int(sum(Cl10en))
						if realen >= 0 and realen < 8192:
							Clover[10][realen]=Clover[10][realen]+1			
							print("Cl10:",realen)	

				if Cl11 >= 1:
					n=len(Cl11en)
					if n <= 4:
						realen=int(sum(Cl11en))
						if realen >= 0 and realen < 8192:
							Clover[11][realen]=Clover[11][realen]+1			
							print("Cl11:",realen)

				if Cl12 >= 1:
					n=len(Cl12en)
					if n <= 4:
						realen=int(sum(Cl12en))
						if realen >= 0 and realen < 8192:
							Clover[12][realen]=Clover[12][realen]+1			
							print("Cl12:",realen)	
			
				if Cl13 >= 1:
					n=len(Cl13en)
					if n <= 4:
						realen=int(sum(Cl13en))
						if realen >= 0 and realen < 8192:
							Clover[13][realen]=Clover[13][realen]+1			
							print("Cl13:",realen)	
	

	matwrite(matfilename1,dimy=16,dimx=8192,arr=Clover,overwrite=overwrite)
