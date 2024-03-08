#!/usr/bin/env python3

from struct import *
from correvent import imread as r1
from correvent import betaread as r2


if __name__ == "__main__":
	import sys
	filecorr = sys.argv[1]
	q=Struct("@B")
	implants=0
	betas=0
	with open(filecorr, mode ='rb') as f:
		while(1):
			buff=f.read(1)
			if buff == b'':
				break
			flag, = q.unpack(buff)
			f.seek(-1,1)
			if flag == 1:
				r1(f)
				implants = implants + 1
			else:
				r2(f)
				betas = betas + 1

	print("implants#:", implants, "betas#:", betas, "total:", implants + betas)
