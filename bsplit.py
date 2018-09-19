#!/usr/bin/env python3

import sys

inputFile = sys.argv[1]
pattern = bytes(sys.argv[2], 'utf-8')

def getNextBytes(f):
  """ Returns a bytes object, which may be of zero length in case the pattern has been found. In case the file reaches EOF, None is returned """
  next = f.read(1)
  if next == b'':
    return None
  matchBuffer = bytearray(next)
  while (matchBuffer[-1] == pattern[len(matchBuffer) - 1]) :
    if (len(matchBuffer) == len(pattern)):
      return b''
    next = f.read(1)
    if next == b'':
      return matchBuffer
    matchBuffer.append(next[0])
  return matchBuffer


with open(inputFile, 'rb') as f_in :

  fileIdx = 0
  while True:
    with open(inputFile + '.part' + str(fileIdx), 'wb') as f_out:
      bytes = getNextBytes(f_in)
      while (bytes != b'' and bytes != None):
        f_out.write(bytes)
        bytes = getNextBytes(f_in)
      f_out.flush()
      if bytes == b'':
        fileIdx += 1
        continue
      elif bytes == None:
        break
