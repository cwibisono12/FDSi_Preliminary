#!/usr/bin/env python3

from pxi16parser import nsclpxi16evread as nscl
from parsegen import matwrite
import numpy as np

if __name__ == "__main__":
	
	import sys
	filename=sys.argv[1]
	matfilename1=sys.argv[2] #ImplantIons
	matfilename2=sys.argv[3] #ImplantBeta
	matfilename3=sys.argv[4] #ImplantX
	matfilename4=sys.argv[5] #ImplantY
	overwrite=int(sys.argv[6])
	ImplantIons=np.ndarray(shape=(1000,1000),dtype=np.int32)
	ImplantBeta=np.ndarray(shape=(1000,1000),dtype=np.int32)
	ImplantX=np.ndarray(shape=(1000,1000),dtype=np.int32)
	ImplantY=np.ndarray(shape=(1000,1000),dtype=np.int32)
	#PID=np.ndarray(shape=(8192,4096),dtype=np.int32)
	#ScintEnLeft=np.ndarray(shape=(1,8192),dtype=np.int32)
	
	with open(filename, mode='rb') as f:
		while(1):
			temp=nscl(f)
			if temp == -1:
				break
			elif temp == 0:
				continue
			else:
				sevtmult=len(temp)
				ah1=0
				ah2=0
				ah3=0
				ah4=0
				al1=0
				al2=0
				al3=0
				al4=0
				enah1=[]
				enah2=[]
				enah3=[]
				enah4=[]
				enal1=[]
				enal2=[]
				enal3=[]
				enal4=[]
				'''
				xions=0
				yions=0
				xbeta=0
				ybeta=0
				'''
				for i in range(0,sevtmult,1):
					if temp[i].iddet >=212 and temp[i].iddet <=219:
						if temp[i].iddet == 212:
							ah1=ah1+1
							enah1.append(temp[i].energy)
						if temp[i].iddet == 213:
							ah2=ah2+1
							enah2.append(temp[i].energy)
						if temp[i].iddet == 214:
							ah3=ah3+1
							enah3.append(temp[i].energy)
						if temp[i].iddet == 215:
							ah4=ah4+1
							enah4.append(temp[i].energy)

						if temp[i].iddet == 216:
							al1=al1+1
							enal1.append(temp[i].energy)
						if temp[i].iddet == 217:
							al2=al2+1
							enal2.append(temp[i].energy)
						if temp[i].iddet == 218:
							al3=al3+1
							enal3.append(temp[i].energy)
						if temp[i].iddet == 219:
							al4=al4+1
							enal4.append(temp[i].energy)
				flag=0
				if (al1 >= 1) and (al2 >= 1) and al3 >= 1 and al4 >=1 and ah1>=1 and ah2 >=1 and ah3>=1 and ah4>=1:
					maxenal1=max(enal1)
					maxenal2=max(enal2)
					maxenal3=max(enal3)
					maxenal4=max(enal4)
					maxenah1=max(enah1)
					maxenah2=max(enah2)
					maxenah3=max(enah3)
					maxenah4=max(enah4)
			
					sumal=maxenal1+maxenal2+maxenal3+maxenal4
					sumah=maxenah1+maxenah2+maxenah3+maxenah4
					
					if sumal > 0 and sumah > 0:
						xions=(maxenal4+maxenal3)/sumal
						yions=(maxenal2+maxenal3)/sumal
						xbeta=(maxenah4+maxenah3)/sumah
						ybeta=(maxenah2+maxenah3)/sumah

						if xions > 0 and xions <1 and yions>0 and yions <1:
							flag=flag+2
						if xbeta > 0 and xbeta <1 and ybeta >0 and ybeta <1:
							flag=flag+4

						if flag & 1 == 0:
							print("xions:",xions,"yions:",yions)
							print("xbeta:",xbeta,"ybeta:",ybeta)
					
							xions=int(xions*1000)
							yions=int(yions*1000)
							xbeta=int(xbeta*1000)
							ybeta=int(ybeta*1000)
							if xions >= 0 and xions <999 and yions >= 0 and yions <999:
								ImplantIons[yions][xions]=ImplantIons[yions][xions]+1
							if xbeta >= 0 and xbeta < 999 and ybeta >=0 and ybeta < 999:
								ImplantBeta[ybeta][xbeta]=ImplantBeta[ybeta][xbeta]+1
							if xions >=0 and xions < 999 and xbeta >=0 and xbeta < 999:
								ImplantX[xions][xbeta]=ImplantX[xions][xbeta]+1
							if yions >=0 and yions < 999 and ybeta >=0 and ybeta < 999:
								ImplantY[yions][ybeta]=ImplantY[yions][ybeta]+1

					
	matwrite(matfilename1,dimy=1000,dimx=1000,arr=ImplantIons,overwrite=overwrite)
	matwrite(matfilename2,dimy=1000,dimx=1000,arr=ImplantBeta,overwrite=overwrite)
	matwrite(matfilename3,dimy=1000,dimx=1000,arr=ImplantX,overwrite=overwrite)
	matwrite(matfilename4,dimy=1000,dimx=1000,arr=ImplantY,overwrite=overwrite)
