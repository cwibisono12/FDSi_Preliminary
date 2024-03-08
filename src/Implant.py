#!/usr/bin/env python3

	
def Implant(pxi16obj):
	'''
	Function to Deduce Implant
	Implant is defined as heavy ions which also appear in the low-gain
	C. Wibisono
	03/01 '24
	Function Argument(s):
	pxi16obj ---> see the pxi16parser module
	Return(s):
	Energy(int), TOF (float)
	'''
	sevtmult=len(pxi16obj)
	dE = 0
	t1 = 0
	t2 = 0	
	al1 = 0
	al2 = 0
	al3 = 0
	al4 = 0
	fdynode = 0
	enal1 = []
	enal2 = []
	enal3 = []
	enal4 = []
	tl1 = []
	tl2 = []
	tl3 = []
	tl4 = []
	for i in range(0,sevtmult,1):
		if pxi16obj[i].iddet == 353: #MSX 100
			dE = dE+1
			Energy=pxi16obj[i].energy
		if pxi16obj[i].iddet == 245: #DB3PPAC Anode Down
			t1 = t1+1
			pxi16objtime=pxi16obj[i].ctimef
			t1time = pxi16obj[i].time + (pxi16obj[i].ctime/16384)
			#t1time = pxi16obj[i].time
			if pxi16objtime == 1:
				t1time = t1time*8
			else:
				t1time = t1time*4			
				Eleft=pxi16obj[i].energy
					
		if pxi16obj[i].iddet == 232: #Cross Scint T2
			t2 = t2+1
			pxi16objtime = pxi16obj[i].ctimef
			t2time = pxi16obj[i].time + (pxi16obj[i].ctime/16384)
			#t2time = pxi16obj[i].time
			if pxi16objtime == 1:
				t2time = t2time*8
			else:
				t2time = t2time*4

		
		if pxi16obj[i].iddet >= 216 and pxi16obj[i].iddet <= 219:
			if pxi16obj[i].iddet == 216:
				al1 = al1 + 1
				tl1objtime = pxi16obj[i].ctimef
				tl1time = pxi16obj[i].time + (pxi16obj[i].ctime/16384)
				if tl1objtime == 1:
					tl1time = tl1time * 8
				else:
					tl1time = tl1time * 4
				enal1.append(pxi16obj[i].energy)
				tl1.append(tl1time)

			if pxi16obj[i].iddet == 217:
				al2 = al2 + 1
				tl2objtime = pxi16obj[i].ctimef
				tl2time = pxi16obj[i].time + (pxi16obj[i].ctime/16384)
				if tl2objtime == 1:
					tl2time = tl2time * 8
				else:
					tl2time = tl2time * 4
				enal2.append(pxi16obj[i].energy)
				tl2.append(tl2time)

			if pxi16obj[i].iddet == 218:
				al3 = al3 + 1
				tl3objtime = pxi16obj[i].ctimef
				tl3time = pxi16obj[i].time + (pxi16obj[i].ctime/16384)
				if tl3objtime == 1:
					tl3time = tl3time * 8
				else:
					tl3time = tl3time * 4
				enal3.append(pxi16obj[i].energy)
				tl3.append(tl3time)

			if pxi16obj[i].iddet == 219:
				al4 = al4 + 1
				tl4objtime = pxi16obj[i].ctimef
				tl4time = pxi16obj[i].time + (pxi16obj[i].ctime/16384)
				if tl4objtime == 1:
					tl4time = tl4time * 8
				else:
					tl4time = tl4time * 4
				enal4.append(pxi16obj[i].energy)
				tl4.append(tl4time)
		
		if pxi16obj[i].iddet == 209: #low gain dynode
			fdynode = 1		

	if (t1 >= 1) and t2 >= 1 and dE >= 1 and (al1 >= 1 and al2 >= 1 and al3 >= 1 and al4 >= 1) and fdynode == 1:
		deltatime=(t1time-t2time)
				
		deltatime=(deltatime)*10 - 2000
		#print("sevtmult:",sevtmult,"iddet:",pxi16obj[i].iddet,"t1time:",t1time,"t2time:",t2time,"tdiff:",deltatime,"energy:",Energy,"Eleft:",Eleft)
		
		maxenal1 = max(enal1)
		maxenal2 = max(enal2)
		maxenal3 = max(enal3)
		maxenal4 = max(enal4)
		

		maxtl1 = max(tl1)
		maxtl2 = max(tl2)
		maxtl3 = max(tl3)
		maxtl4 = max(tl4)

		sumenal = maxenal1 +  maxenal2 + maxenal3 + maxenal4
		timeimplant = (maxtl1 + maxtl2 + maxtl3 + maxtl4)/4.
		flaglgain = 0
		
		if sumenal > 0:
			xions = (maxenal4 + maxenal3)/sumenal
			yions = (maxenal2 + maxenal3)/sumenal
			
			if xions > 0 and xions < 1 and yions > 0 and yions < 1:
				flaglgain = flaglgain + 1 
				position = [xions, yions]
				
		if flaglgain == 1:
			implantcoords=[]
			implantcoords.append(Energy)
			implantcoords.append(deltatime)
			implantcoords.append(position)
			implantcoords.append(timeimplant)
			print("Implantevent","---","dE:",implantcoords[0],"TOF:",implantcoords[1],"(x,y):",implantcoords[2],"imtime:",implantcoords[3])
			return implantcoords
		else:
			return "Not Found"

	else:
		return "Not Found"
