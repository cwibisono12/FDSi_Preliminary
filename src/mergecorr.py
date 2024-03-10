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
					temp, Ge = im(fr)
					#flagimevent, =imflag.unpack(fr.read(1))
					fw.write(imflag.pack(temp[0]))
					fw.write(imid.pack(temp[1]))
					fw.write(p.pack(temp[2]))
					fw.write(p.pack(temp[3]))
					fw.write(p.pack(temp[4]))
					fw.write(p.pack(temp[5]))
					fw.write(q.pack(temp[6]))
					fw.write(imflag.pack(temp[7]))
					gmult = temp[7]
					if gmult > 0:
						for i,j in Ge.items():
							fw.write(imflag.pack(int(i)))
							fw.write(p.pack(j))
			
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
