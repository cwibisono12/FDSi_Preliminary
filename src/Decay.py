#!/usr/bin/env python3

	
def Decay(pxi16obj):
	'''
	Function to Deduce Decay event
	Decay is defined as event where there is no hit in any of the upstream PIN Detectors
	and there is a hit on the high-gain:
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
	ah1 = 0
	ah2 = 0
	ah3 = 0
	ah4 = 0
	enah1 = []
	enah2 = []
	enah3 = []
	enah4 = []
	timeah1 = []
	timeah2 = []
	timeah3 = []
	timeah4 = []
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

		
		if pxi16obj[i].iddet >= 212 and pxi16obj[i].iddet <= 215:
			if pxi16obj[i].iddet == 212:
				ah1 = ah1 + 1
				th1 = pxi16obj[i].ctimef
				th1time = pxi16obj[i].time + (pxi16obj[i].ctime/16384)
				if th1 == 1:
					th1time = th1time * 8
				else:
					th1time = th1time * 4
				enah1.append(pxi16obj[i].energy)
				timeah1.append(th1time)

			if pxi16obj[i].iddet == 213:
				ah2 = ah2 + 1
				th2 = pxi16obj[i].ctimef
				th2time = pxi16obj[i].time + (pxi16obj[i].ctime/16384)
				if th2 == 1:
					th2time = th2time * 8
				else:
					th2time = th2time * 4
				enah2.append(pxi16obj[i].energy)
				timeah2.append(th2time)

			if pxi16obj[i].iddet == 214:
				ah3 = ah3 + 1
				th3 = pxi16obj[i].ctimef
				th3time = pxi16obj[i].time + (pxi16obj[i].ctime/16384)
				if th3 == 1:
					th3time = th3time * 8
				else:
					th3time = th3time * 4
				enah3.append(pxi16obj[i].energy)
				timeah3.append(th3time)

			if pxi16obj[i].iddet == 215:
				ah4 = ah4 + 1
				th4 = pxi16obj[i].ctimef
				th4time = pxi16obj[i].time + (pxi16obj[i].ctime/16384)
				if th4 == 1:
					th4time = th4time * 8
				else:
					th4time = th4time * 4
				enah4.append(pxi16obj[i].energy)
				timeah4.append(th4time)
			

	if (t1 == 0) and t2 == 0 and dE == 0 and (ah1 >= 1 and ah2 >= 1 and ah3 >= 1 and ah4 >= 1):
		#deltatime=(t1time-t2time)
				
		#deltatime=(deltatime)*10 - 2000
		#print("sevtmult:",sevtmult,"iddet:",pxi16obj[i].iddet,"t1time:",t1time,"t2time:",t2time,"tdiff:",deltatime,"energy:",Energy,"Eleft:",Eleft)
		
		maxenah1 = max(enah1)
		maxenah2 = max(enah2)
		maxenah3 = max(enah3)
		maxenah4 = max(enah4)

		maxth1 = max(timeah1)
		maxth2 = max(timeah2)
		maxth3 = max(timeah3)
		maxth4 = max(timeah4)
		
		sumenah = maxenah1 +  maxenah2 + maxenah3 + maxenah4
		timedecay = (maxth1 + maxth2 + maxth3 + maxth4)/4.
		flaghgain = 0
		
		if sumenah > 0:
			xbeta = (maxenah4 + maxenah3)/sumenah
			ybeta = (maxenah2 + maxenah3)/sumenah
			
			if xbeta > 0 and xbeta < 1 and ybeta > 0 and ybeta < 1:
				flaghgain = flaghgain + 1 
				position = [xbeta, ybeta]
		
		if flaghgain == 1:
			betacoords=[]
			betacoords.append(position)
			betacoords.append(timedecay)
			print("Decayevent","---","(x,y):",betacoords[0],"betatime:",betacoords[1])
			return betacoords
		else:
			return "Not Found"

	else:
		return "Not Found"
