#!/usr/bin/env python3


def readcalibclover(filecalib):
	'''
	Function to generate Ge calibration coefficients:
	C. Wibisono
	03/03 '24
	Function Argument:
	filecalib: filepointer for Ge calibration
	Return:
	Ge (dict): Clover detector calibration parameter. Key: (Clover ID) Values: Intercept and Slope
	'''
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

	return Ge
