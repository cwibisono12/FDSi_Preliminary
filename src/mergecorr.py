#!/usr/bin/env python3
from struct import *
from correvent import imread as im

def mergecorr(fin, fout):
	'''
	Function to merge .corr files into a single file
	C. Wibisono
	Function Argument(s):
	fin: fileinput *.corr file
	fout: fileout *.corr file
	'''
	imflag=Struct("@B")
	p=Struct("@i")
	q=Struct("@Q")
	imid=Struct("@H")
	betaflag=Struct("@B")
	with open(fout, mode='ab') as fw:
		with open(fin, mode='rb') as fr:
			while(1):
				buff = fr.read(1)
				if buff == b'':
					break
				
				fr.seek(-1,1)
				flag, = imflag.unpack(buff)
				if flag == 1:
					temp = im(fr)
					fw.write(imflag.pack(1))
					fw.write(imid.pack(temp.imID))
					fw.write(p.pack(temp.dE))
					fw.write(p.pack(temp.TOF))
					fw.write(p.pack(temp.x))
					fw.write(p.pack(temp.y))
					fw.write(q.pack(temp.imtime))
				else:
					flagbetaevent, = betaflag.unpack(fr.read(1))
					fw.write(betaflag.pack(flagbetaevent))
					x, =p.unpack(fr.read(4))
					y, =p.unpack(fr.read(4))
					betatime, = q.unpack(fr.read(8))
					#g,= betaflag.unpack(fr.read(1))	
					fw.write(p.pack(x))
					fw.write(p.pack(y))
					fw.write(q.pack(betatime))
					gmult, = betaflag.unpack(fr.read(1))
					fw.write(betaflag.pack(gmult))
					for i in range(gmult):
						clid, = betaflag.unpack(fr.read(1))
						clen, = p.unpack(fr.read(4))
						fw.write(betaflag.pack(clid))
						fw.write(p.pack(clen))
					


if __name__ == "__main__":
	import sys
	filecorrin = sys.argv[1]
	filecorrout = sys.argv[2]
	mergecorr(filecorrin, filecorrout)	
