#!/usr/bin/env python3
from struct import *
from correvent import imread
from correvent import betaread


def buildcorr(fcorr, *, timecorr = 150000000):
	'''
	Function to build time correlation
	C. Wibisono
	03/08 '24
	Function Argument(s)
	fcorr: file correlator pointer objects --> see correvent module
	timecorr: (int) correlation timing window (default = 150 ms)
	Return:
	correlation objects 
	'''
	corrtime = -1
	tdiff = -1
	corrobj = []
	p = Struct("@B")
	q = Struct("@H")
	r = Struct("@i")
	s = Struct("@Q")
	n = 0 #flag to set whether there is still remnant hits that needs to be filled into a new time window.
	while(1):
		
		buff = fcorr.read(1)
		
		if buff == b'':
			if n == 0:
				return -1
			else:
				break
		
		flag, = p.unpack(buff)
		fcorr.seek(-1,1)
		timeref = 0
		flagbeta = 0
		gmult = 0
		
		if flag == 1: #implant event
			temp = imread(fcorr)
			timeref = temp.imtime
			
		else: #beta event
			temp, ge = betaread(fcorr)
			timeref = temp[3]
			gmult = temp[4]
			flagbeta = 1

		if corrtime == -1:
			corrtime = timeref
			tdiff = 0
			n = n + 1
		else:
			tdiff = timeref - corrtime
			n = n + 1
		if tdiff > timecorr:
			if flagbeta == 0:
				fcorr.seek(-27,1)
				break
			else:			
				if gmult == 0:
					fcorr.seek(-18,1)
				else:
					fcorr.seek(-18-(5*gmult),1)

				break
	
		if flag == 1:
			implantflag = temp.imflag
			imID = temp.imID
			dE = temp.dE
			TOF = temp.TOF
			xpos = temp.x
			ypos = temp.y
			timeimplant = temp.imtime
			arr = [implantflag, imID, dE, TOF, xpos, ypos, timeimplant]	
			corrobj.append(arr)
		else:
			flagbeta = temp[0]
			xpos = temp[1]
			ypos = temp[2]
			betatime = temp[3]
			gmult = temp[4]
			arr = [flagbeta, xpos, ypos, betatime, gmult, ge]
			corrobj.append(arr)
	
	
	return corrobj

if __name__ == "__main__":
	import sys
	filecorr = sys.argv[1]
	implants = 0
	betas = 0
	with open(filecorr, mode ='rb') as f:
		while(1):
			result = buildcorr(f, timecorr = 150000000)
			if result == -1:
				break
			else:
				mult=len(result)
				identifier = 0
				for i in range(mult):
					if result[i][0] == 1: #imevent
						implants = implants + 1
						print("mult:", mult, "implant:", result[i][1], "(x,y):", result[i][4], result[i][5], "imtime:", result[i][6])
					else:
						betas = betas + 1
						print("mult:" ,mult, "betastime:", result[i][3], "(x, y):", result[i][1],result[i][2],"gmult:", result[i][4])					
			
	print("implants#:",implants,"betas#:",betas,"total#:",implants + betas)
