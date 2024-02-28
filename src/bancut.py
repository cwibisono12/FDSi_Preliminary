#!/usr/bin/env python3


def bancut(x,y,X,Y,n):
	'''
	Function to check whether a particular point is located inside the cuts defined by the array X,Y:
	C. Wibisono
	02/27 '24
	Function Arguments:
	x: (float) xtest coordinate
	y: (float) ytest coordinate
	X: (float) array 
	Y: (float) array
	n: number of points for the closed drawed cuts		
	'''
	j=n-1
	result=0
	for i in range(n):
		if( ((Y[i] < y and Y[j] >= y) or (Y[j] < y and Y[i] >= y)) and (X[i] <=x or X[j] <=x)):
			temp = (X[i] + (y-Y[i])/(Y[j]-Y[i])*(X[j]-X[i])<x)
			result=result ^ temp
		j=i

	return result


if __name__ == "__main__":
	import sys
	X=[1.0,4.0,4.0,1.0,1.0]
	Y=[1.0,1.0,4.0,4.0,1.0]
	x=float(sys.argv[1])
	y=float(sys.argv[2])
	print("result:",bancut(x,y,X,Y,5))	
