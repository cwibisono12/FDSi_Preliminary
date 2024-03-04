#!/usr/bin/env python3

	
def PID(pxi16obj):
	'''
	Function to Generate dE and TOF
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

	if (t1 >= 1) and t2 >= 1 and dE >= 1:
		deltatime=(t1time-t2time)
				
		deltatime=(deltatime)*10 - 2000
		print("sevtmult:",sevtmult,"iddet:",pxi16obj[i].iddet,"t1time:",t1time,"t2time:",t2time,"tdiff:",deltatime,"energy:",Energy,"Eleft:",Eleft)
			
		return Energy, deltatime

	else:
		return "Not Found"
