# -*- coding: utf-8 -*-
import os
import sys
import json
import fileinput
import copy


if len(sys.argv) != 2:
    print("usage: BSX_Patcher.py filein.bs")
    sys.exit(1)
    
out1 = open(sys.argv[1],"rb+")   
out2 = open("BSX_Patcher.py","rb")

#    00 !! 11 33 ÿÿ €0 ð0
  
out1.seek(0, os.SEEK_END)
filesize = out1.tell()

out1.seek(0x7FD0)
bitFD0 = out1.read(1).hex()

out1.seek(0x7FD1)
bitFD1 = out1.read(1).hex()

out1.seek(0x7FD2)
bitFD2 = out1.read(1).hex()

out1.seek(0x7FD3)
bitFD3 = out1.read(1).hex()

out1.seek(0x7FD4)
bitFD4 = out1.read(1).hex()

out1.seek(0x7FD5)
bitFD5 = out1.read(1).hex()

out1.seek(0x7FDA)
bitFDA = out1.read(1).hex()

out1.seek(0x7FD8)
bit1 = out1.read(1).hex()

out1.seek(0xFFD0)
bitFFD0 = out1.read(1).hex()

out1.seek(0xFFD1)
bitFFD1 = out1.read(1).hex()

out1.seek(0xFFD2)
bitFFD2 = out1.read(1).hex()

out1.seek(0xFFD3)
bitFFD3 = out1.read(1).hex()

out1.seek(0xFFD4)
bitFFD4 = out1.read(1).hex()

out1.seek(0xFFD5)
bitFFD5 = out1.read(1).hex()

out1.seek(0xFFDA)
bitFFDA = out1.read(1).hex()

out1.seek(0xFFD8)
bit2 = out1.read(1).hex()

out2.seek(0x109)  #bsx
bit20 = out2.read(1).hex()

out2.seek(0x10B)  #bsx
bit30 = out2.read(1).hex()

out2.seek(0x10E)  #bsx
bit21 = out2.read(1).hex()

out2.seek(0x111)  #bsx
bit31 = out2.read(1).hex()

out2.seek(0x114)  #bsx
bit32 = out2.read(1).hex()

out2.seek(0x117)  #bsx
bit33 = out2.read(1).hex()

out2.seek(0x11A)  #bsx
bit34 = out2.read(1).hex()

out2.seek(0x11D)  #bsx
bit35 = out2.read(1).hex()

if  (bit1) == (bit20) or (bit1) == (bit30):
    if (bitFD0) == (bit35):
        if (filesize) == (256 * 1024):
            out1.seek(0x7FD0)
            out1.write(bytes([0x03]))
        elif (filesize) == (512 * 1024):
              out1.seek(0x7FD0)
              out1.write(bytes([0x0F]))
        elif (filesize) >= (512 * 1024):
              out1.seek(0x7FD0)
              out1.write(bytes([0xFF]))
    elif (bitFD1) == (bit33):
          if (bitFD2) == (bit33):
              if (bitFD3) == (bit33):
                  out1.seek(0x7FD1)
                  out1.write(bytes([0x00]))
                  out1.seek(0x7FD2)
                  out1.write(bytes([0x00]))
                  out1.seek(0x7FD3)
                  out1.write(bytes([0x00]))
elif  (bit2) == (bit21) or (bit2) == (bit31):
      if (bitFFD0) == (bit35):
            if (filesize) == (256 * 1024):
                out1.seek(0xFFD0)
                out1.write(bytes([0x03]))
            elif (filesize) == (512 * 1024):
                  out1.seek(0xFFD0)
                  out1.write(bytes([0x0F]))
            elif (filesize) >= (512 * 1024):
                  out1.seek(0xFFD0)
                  out1.write(bytes([0xFF]))
      elif (bitFFD1) == (bit33):
              if (bitFFD2) == (bit33):
                  if (bitFFD3) == (bit33):
                      out1.seek(0xFFD1)
                      out1.write(bytes([0x00]))
                      out1.seek(0xFFD2)
                      out1.write(bytes([0x00]))
                      out1.seek(0xFFD3)
                      out1.write(bytes([0x00]))
                            
if  (bit1) == (bit20) or (bit1) == (bit30):
     if (bitFD5) >= (bit34):  
         out1.seek(0x7FD4)
         out1.write(bytes([0x00]))
         out1.seek(0x7FD5)
         out1.write(bytes([0x00]))
elif  (bit2) == (bit21) or (bit2) == (bit31):
       if (bitFFD5) >= (bit34):    
           out1.seek(0xFFD4)
           out1.write(bytes([0x00]))
           out1.seek(0xFFD5)
           out1.write(bytes([0x00]))
    
if  (bit1) == (bit20) or (bit1) == (bit30):
     if (bitFDA) != (bit32):    
         out1.seek(0x7FDA)
         out1.write(bytes([0x33]))
elif  (bit2) == (bit21) or (bit2) == (bit31):
       if (bitFFDA) != (bit32): 
           out1.seek(0xFFDA)
           out1.write(bytes([0x33]))