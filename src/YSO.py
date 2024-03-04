#!/usr/bin/env python3

def YSO(pxi16obj):	
	'''
	Function to Process YSO:
	C. Wibisono
	03/01/2024
	Function Argument(s):
	pxi16obj: object from pxi16data class
	Return:
	postion[[xions,yions],[xbeta,ybeta]]
	'''
	sevtmult=len(pxi16obj)
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
				

	for i in range(0,sevtmult,1):
		if pxi16obj[i].iddet >=212 and temp[i].iddet <=219:
			
			if pxi16obj[i].iddet == 212:
				ah1=ah1+1
				enah1.append(pxi16obj[i].energy)

			if pxi16obj[i].iddet == 213:
				ah2=ah2+1
				enah2.append(pxi16obj[i].energy)

			if pxi16obj[i].iddet == 214:
				ah3=ah3+1
				enah3.append(pxi16obj[i].energy)

			if pxi16obj[i].iddet == 215:
				ah4=ah4+1
				enah4.append(pxi16obj[i].energy)

			if pxi16obj[i].iddet == 216:
				al1=al1+1
				enal1.append(pxi16obj[i].energy)
						
			if pxi16obj[i].iddet == 217:
				al2=al2+1
				enal2.append(pxi16obj[i].energy)
						
			if pxi16obj[i].iddet == 218:
				al3=al3+1
				enal3.append(pxi16obj[i].energy)
						
			if pxi16obj[i].iddet == 219:
				al4=al4+1
				enal4.append(pxi16obj[i].energy)
				

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

			if xions> 0 and xions <1 and yions> 0 and yions <1:
				flag=flag+2
				
			if xbeta> 0 and xbeta <1 and ybeta> 0 and ybeta <1:
				flag=flag+4

			if flag & 1 == 0:
				print("xions:",xions,"yions:",yions)
				print("xbeta:",xbeta,"ybeta:",ybeta)
					
				xions=int(xions*1000)
				yions=int(yions*1000)
				xbeta=int(xbeta*1000)
				ybeta=int(ybeta*1000)
							
				position=[[xions,yions],[xbeta,ybeta]]
	
	return position					
