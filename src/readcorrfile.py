#!/usr/bin/env python3

from struct import *
from correvent import imread as r1
from correvent import betaread as r2


if __name__ == "__main__":
	import sys
	filecorr = sys.argv[1]
	q=Struct("@h")
	with open(filecorr, mode ='rb') as f:
		while(1):
			buff=f.read(2)
			if buff == b'':
				break
			flag, = q.unpack(buff)
			f.seek(-2,1)
			if flag == 1:
				r1(f)
			else:
				r2(f)
