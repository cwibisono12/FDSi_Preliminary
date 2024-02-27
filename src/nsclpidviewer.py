#!/usr/bin/env python3
import projmod as p
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import rebin2d as r
import numpy as np

def openpidfile(filename,xlow,xup,ylow,yup,binfactor,x1,x2):
	PID=p.clarion(filename,8192,4096,0,4095,0,8191)
	PIDobj=PID.readparse()
	PIDobjrebin=r.rebin2d(PIDobj,8192,4096,binfactor,binfactor).rebin()
	Energy=PID.project(2,0,0,4095,0,0,PIDobj)
	x=np.arange(0,8192,1)

	fig,ax=plt.subplots()
	ax.imshow(PIDobjrebin,cmap='gist_ncar',origin='lower',extent=[0,4095,0,8191],aspect='auto',norm=LogNorm())
	ax.set_xlim(xlow,xup)
	ax.set_ylim(ylow,yup)
	#ax[1].plot(x[x1:x2],Energy[x1:x2],linewidth=0.85,ls='steps-mid')
	plt.show()


if __name__ == "__main__":
	import sys
	filename=sys.argv[1]
	xlow=int(sys.argv[2])
	xup=int(sys.argv[3])
	ylow=int(sys.argv[4])
	yup=int(sys.argv[5])
	binfactor=int(sys.argv[6])
	openpidfile(filename,xlow,xup,ylow,yup,binfactor,100,4000)
