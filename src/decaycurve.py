#!/usr/bin/env python3

from buildcorr import buildcorr as corr
from parsegen import matwrite
import matplotlib.pyplot as plt
import numpy as np

def decaycurve(filecorr, *, timebuild = 150000000, radius = 500):

	'''
	Function to generate decay curve, gamma spectrum associated with beta events,
	and gamma spectum asscociated with implant events.
	C. Wibisono
	03/10 '24
	Function Argument(s):
	filecorr: correlation file object
	timebuild: correlation timing window
	radius: radius between implant and beta
	Return(s):
	decayhist: int[4][300] decay matrix
	decayen: int[4][8192] gamma energy matrix associated with betas
	isomeren: int[4][8192] gamma energy matrix associated with implants			
	'''

	decayhist = np.ndarray(shape=(4,300),dtype=np.int32)
	decayen = np.ndarray(shape=(4,8192),dtype=np.int32)
	isomeren = np.ndarray(shape=(4,8192),dtype=np.int32)

	for i in range(0,4,1):
		for j in range(0,300,1):
			decayhist[i][j] = 0

	for i in range(0,4,1):
		for j in range(0,8192,1):
			decayen[i][j] = 0
			isomeren[i][j] = 0

	'''
	x=np.arange(0,300,1)
	y41P=np.zeros(300)
	y42P=np.zeros(300)
	y43P=np.zeros(300)
	y44P=np.zeros(300)
	'''
	with open(filecorr, mode='rb') as f:
		while(1):
			result = corr(f, timecorr = timebuild)
			if result == -1:
				break
			else:
				mult = len(result)
				flag41P = 0
				flag42P = 0
				flag43P = 0
				flag44P = 0
				P41 = []
				P42 = []
				P43 = []
				P44 = []
				betas = []
				#ebetas = []
				betaflag = 0

				for i in range(mult):
					
					if result[i][0] == 1: #implant event:
						if result[i][1] == 4115:
							flag41P = flag41P + 1
							P41.append([result[i][4],result[i][5],result[i][6]]) #[x,y,t]
							for p, q in result[i][8].items():
								isomeren[0][q] = isomeren[0][q] + 1	
						if result[i][1] == 4215:
							flag42P = flag42P + 1
							P42.append([result[i][4],result[i][5],result[i][6]])
							for p, q in result[i][8].items():
								isomeren[1][q] = isomeren[1][q] + 1	
						if result[i][1] == 4315:
							flag43P = flag43P + 1
							P43.append([result[i][4],result[i][5],result[i][6]])
							for p, q in result[i][8].items():
								isomeren[2][q] = isomeren[2][q] + 1	
						if result[i][1] == 4415:
							flag44P = flag44P + 1
							P44.append([result[i][4],result[i][5],result[i][6]])
							for p, q in result[i][8].items():
								isomeren[3][q] = isomeren[3][q] + 1	
						

					else: #betaevents
						betaflag = betaflag + 1
						betas.append([result[i][1],result[i][2],result[i][3],result[i][5]]) #[x,y,t,e]
						#ebetas.append(result[i][5])


				nbetas = len(betas)
				if flag41P >= 1 and betaflag >= 1:
					n41P = len(P41)
					
					for i in range(n41P):
						temp41P = []
						k = []
						for j in range(nbetas):
							r = ((P41[i][0] - betas[j][0])**2. + (P41[i][1] - betas[j][1])**2.) ** 0.5
							timediff = (-P41[i][2] + betas[j][2])/1000000.
							if r <= radius and (timediff >= 0. and timediff < 300.) :
								temp41P.append(int(timediff))
								k.append(j)
						if len(temp41P) > 0:
							time41P = min(temp41P)
							indexgamma =k[temp41P.index(time41P)] #beta event that is associated with gammas
							#print("41P:",time41P)
							#y41P[time41P]=y41P[time41P]+1
							decayhist[0][time41P] = decayhist[0][time41P] + 1
							for i, j in betas[indexgamma][3].items():
								decayen[0][j]=decayen[0][j]+1
								print("41P:",time41P,"Eg:",j)
								
					del P41
			
				if flag42P >= 1 and betaflag >= 1:
					n42P = len(P42)
					for i in range(n42P):
						temp42P = []
						k = []
						for j in range(nbetas):
							r = ((P42[i][0] - betas[j][0])**2. + (P42[i][1] - betas[j][1])**2.) ** 0.5
							timediff = (-P42[i][2] + betas[j][2])/1000000.
							if r <= radius and (timediff >= 0. and timediff < 300.) :
								temp42P.append(int(timediff))
								k.append(j)
						if len(temp42P) > 0:
							time42P = min(temp42P)
							indexgamma =k[temp42P.index(time42P)] #beta event that is associated with gammas
							#print("42P:",time42P)
							#y42P[time42P]=y42P[time42P]+1
							decayhist[1][time42P] = decayhist[1][time42P] + 1
							for i, j in betas[indexgamma][3].items():
								decayen[1][j]=decayen[1][j]+1
								print("42P:",time42P,"Eg:",j)
					
					del P42

				if flag43P >= 1 and betaflag >= 1:
					n43P = len(P43)
					for i in range(n43P):
						temp43P = []
						k = []
						for j in range(nbetas):
							r = ((P43[i][0] - betas[j][0])**2. + (P43[i][1] - betas[j][1])**2.) ** 0.5
							timediff = (-P43[i][2] + betas[j][2])/1000000.
							if r <= radius and (timediff >= 0. and timediff < 300.) :
								temp43P.append(int(timediff))
								k.append(j)
						if len(temp43P) > 0:
							time43P = min(temp43P)
							indexgamma =k[temp43P.index(time43P)] #beta event that is associated with gammas
							#print("43P:",time43P)
							#y43P[time43P]=y43P[time43P]+1
							decayhist[2][time43P] = decayhist[2][time43P] + 1
							for i, j in betas[indexgamma][3].items():
								decayen[2][j]=decayen[2][j]+1
								print("43P:",time43P,"Eg:",j)
					del P43
				
				
				if flag44P >= 1 and betaflag >= 1:
					n44P = len(P44)
					for i in range(n44P):
						temp44P = []
						k = []
						for j in range(nbetas):
							r = ((P44[i][0] - betas[j][0])**2. + (P44[i][1] - betas[j][1])**2.) ** 0.5
							timediff = (-P44[i][2] + betas[j][2])/1000000.
							if r <= radius and (timediff >= 0. and timediff < 300.) :
								temp44P.append(int(timediff))
								k.append(j)
						if len(temp44P) > 0:
							time44P = min(temp44P)
							indexgamma =k[temp44P.index(time44P)] #beta event that is associated with gammas
							print("44P:",time44P)
							#y44P[time44P]=y44P[time44P]+1	
							decayhist[3][time44P] = decayhist[3][time44P] + 1
							for i, j in betas[indexgamma][3].items():
								decayen[3][j]=decayen[3][j]+1
								print("44P:",time44P,"Eg:",j)
					del P44

				'''
				if flag42P >= 1 and betaflag >= 1:
					n42P = len(P42)
					nbetas = len(betas)
					dt = []
					xim = []
					xbeta = []
					yim = []
					ybeta = []
					for i in range(n42P):
						for j in range(nbetas):
							r = ((P42[i][0] - betas[j][0])**2. + (P42[i][1] - betas[j][1])**2.) ** 0.5
							timediff = (P42[i][2] - betas[j][2])/1000000.
							print("xim:",P42[i][0],"xb:",betas[j][0],"yim:",P42[i][1],"yb:",betas[j][1],"r",r,"time:",timediff)
							if r <= radius and timediff > 0.0005:
								#dt.append(timediff)
								xim.append(P42[i][0])
								xbeta.append(betas[j][0])
								yim.append(P42[i][1])
								ybeta.append(betas[i][1])		
	
				'''

	return decayhist, decayen, isomeren
	'''
	#matwrite(filemat, dimy = 5, dimx = 300, arr=decayhist, overwrite = 1)
	fig,ax=plt.subplots(2,2)
	ax[0,0].plot(x,y41P,label='41P')
	ax[0,1].plot(x,y42P,label='42P')
	ax[1,0].plot(x,y43P,label='43P')
	ax[1,1].plot(x,y44P,label='44P')
	ax[0,0].legend()
	ax[0,1].legend()
	ax[1,0].legend()
	ax[1,1].legend()
	plt.show()
	'''
	'''
	fig, ax =plt.subplots(2,2)
	let = str(implant)
	fig.suptitle(let[0:2]+"P"+"\n"+"Implants and Betas"+"\n"+"Pixel Coordinates")
	#num = int(len(dt)/2)
	numim = int(len(xim)/2)
	numbeta = int(len(xbeta)/2)
	#for i in range(num):
	#	print(dt[i])
	#ax[0].hist(dt, bins=num)
	ax[0,0].hist(xim,bins=numim)
	ax[0,0].set_xlabel("x_implant")
	ax[1,0].hist(xbeta,bins=numbeta)
	ax[1,0].set_xlabel("x_beta")
	ax[0,1].hist(yim,bins=numim)
	ax[0,1].set_xlabel("y_implant")
	ax[1,1].hist(ybeta,bins=numbeta)
	ax[1,1].set_xlabel("y_beta")
	plt.show()
	'''

if __name__ == "__main__":
	import sys
	from parsegen import matwrite
	filecorrelation = sys.argv[1]
	decaymat = sys.argv[2]
	decayen = sys.argv[3]
	isomeren = sys.argv[4]
	timewindow = int(sys.argv[5])
	radiusbetaim = int(sys.argv[6])
	overwrite = int(sys.argv[7])

	hist_t, hist_e, hist_isomer = decaycurve(filecorrelation, timebuild = timewindow, radius = radiusbetaim)
	matwrite(decaymat, dimy = 4, dimx = 300, arr=hist_t, overwrite = overwrite)												
	matwrite(decayen, dimy = 4, dimx = 8192, arr=hist_e, overwrite = overwrite)												
	matwrite(isomeren, dimy = 4, dimx = 8192, arr=hist_isomer, overwrite = overwrite)												
