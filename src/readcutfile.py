#!/usr/bin/env python3


def readcutfile(cutfile):
	'''
	Function to read the cutfile
	C. Wibisono
	03/06 '24
	Usage:
	Read the cutfile and return the X, Y coordinates for each Implant
	Function Argument(s):
	cutfile: filecut
	Return:
	Implants (dict): key: implant identifier, values: x, y coordinates (list)
	'''
	Implants = {}
	with open(cutfile, mode='r') as f:
		lines = f.readlines()
		for line in lines:
			if line.find('#') == -1:
				row = line.split()
				ImplantID = row[0]
				n = int(row[1])
				x = float(row[2])
				y = float(row[3])
				if ImplantID in Implants.keys():
					Implants[ImplantID][0].append(x)
					Implants[ImplantID][1].append(y)
				else:
					X=[]
					Y=[]
					X.append(x)
					Y.append(y)
					Implants[ImplantID]=[X,Y]

	return Implants



if __name__ == "__main__":
	import sys
	filecut=sys.argv[1]
	result = readcutfile(filecut)
	for i, j in result.items():
		print(i, result[i])
