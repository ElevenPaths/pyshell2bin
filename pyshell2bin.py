import binascii
import fileinput
import os
import re
import sys

def shell2bin(args):
 if len(args) < 2:
  print "Usage: %s shellcodefile binfile" % args[0]
  return
 else:
  try:
   with open(sys.argv[1], "r") as fileshell:
    flux = fileshell.read()
    flux = re.sub("[^0-9,^a-f,^A-F]", "",flux)
   with open(sys.argv[2], "wb") as filebin:
    filebin.write(binascii.unhexlify(flux))
    print "Done!"
  except IOError as e:
   print "I/O error({0}): {1}".format(e.errno, e.strerror)
  except:
   print "Unexpected error:", sys.exc_info()[0] 
if __name__=='__main__':
 shell2bin(sys.argv)
