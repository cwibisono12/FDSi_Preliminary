#!/usr/bin/env python3

###Class for Projection and Histogram Reader
##2nd Version-- 06/11/2023
###Usage: Only for Clarion2-Trinity
#C. Wibisono 10/19/2022

import numpy as np
import matplotlib.pyplot as plt

class trpmat:
	
	def __init__(self,infile,ydim,xdim,xlow,xup,ylow,yup):
		self.infile=infile
		self.ydim=ydim
		self.xdim=xdim
		self.xlow=xlow
		self.xup=xup
		self.ylow=ylow
		self.yup=yup
	
	def readparse(self):
		y=np.fromfile(self.infile,dtype=np.int32,sep="",count=-1)
		ytrp=np.reshape(y,(int(self.ydim),int(self.xdim)))
		return ytrp

class projmodgui(trpmat):

	def __init__(self,line,infile,ydim,xdim,xlow,xup,ylow,yup):
		self.index=0
		self.line=line
		self.x=line.get_xdata()
		self.y=line.get_ydata()
		self.xlow=0
		self.ylow=0
		self.bkgleft=0
		self.bkgright=0
		self.vertical=[]
		trpmat.__init__(self,infile,ydim,xdim,xlow,xup,ylow,yup)

	def connect(self):
                self.line.figure.canvas.mpl_connect('button_press_event',self.onclick)
                self.line.figure.canvas.mpl_connect('key_press_event',self.project)

	def onclick(self,event):
                if event.inaxes != self.line.axes:
                        return

                vline = self.line.axes.axvline(x=event.xdata)
                self.vertical.append(vline)

                if len(self.vertical) > 4:
                        for i in range(0,4,1):
                                #self.vertical[i].remove()
                                #del self.vertical[i]
                                abc=self.vertical.pop(0)
                                abc.remove()
                        #for i in range(0,4,1):
                        #       del self.vertical[i]
                        self.index=0

                self.line.figure.canvas.draw()
                self.index=self.index+1
                print('index:',self.index,'xdata:',event.xdata,'ydata:',event.ydata,'x:',self.x[int(event.xdata)],'y(x):',self.y[int(event.xdata)-min(self.x)])
                #print(len(self.vertical))              
                if self.index == 1:
                        self.bkgleft = self.x[int(event.xdata)-min(self.x)]
                if self.index == 2:
                        self.bkgright = self.x[int(event.xdata)-min(self.x)]
                if self.index == 3:
                        self.xlow = self.x[int(event.xdata)-min(self.x)]
                if self.index == 4:
                        self.xup = self.x[int(event.xdata)-min(self.x)]
                        self.index = 0

	def project(self,event):
		xproj=np.zeros(int(self.xdim),dtype=np.int32)
		yproj=np.zeros(int(self.ydim),dtype=np.int32)
		xprojb=np.zeros(int(self.xdim),dtype=np.int32)
		yprojb=np.zeros(int(self.ydim),dtype=np.int32)
		xprojbs=np.zeros(int(self.xdim),dtype=np.int32)
		yprojbs=np.zeros(int(self.ydim),dtype=np.int32)
		widthgate=int(xup)-int(xlow)
		widthbackg=int(bkgright)-int(bkgleft)	
		if event.key == 'x':
			for i in range(0,int(self.xdim),1):
				for j in range(int(xlow),int(xup)+1,1):
					xproj[i]=xproj[i]+ytrp[j,i]
			
			for i in range(0,int(self.xdim),1):
				for j in range(int(bkgleft),int(bkgright)+1,1):
					xprojb[i]=xprojb[i]+ytrp[j,i]
				xprojbs[i]=(widthgate/(widthgate+widthbackg))*xproj[i]-(widthbackg/(widthgate+widthbackg))*xprojb[i]
			return xprojbs
		
	
		if event.key == 'y':
			for j in range(0,int(self.ydim),1):
				for i in range(int(xlow),int(xup)+1,1):
					yproj[j]=yproj[j]+ytrp[j,i]
				
			for j in range(0,int(self.ydim),1):
				for i in range(int(bkgleft),int(bkgright)+1,1):
					yprojb[j]=yprojb[j]+ytrp[j,i]
		
				yprojbs[j]=(widthgate/(widthgate+widthbackg))*yproj[j]-(widthbackg/(widthgate+widthbackg))*yprojb[j]
			return yprojbs
	

	
