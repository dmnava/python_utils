#!/usr/bin/env python3

import sys
import argparse

parser = argparse.ArgumentParser(description='Splits a binary file on the supplied delimiter.')
group = parser.add_mutually_exclusive_group(required = True)
group.add_argument('-t', '--text', help = 'The delimiter in string form')
group.add_argument('-b', '--binary', help = 'The delimiter in hexadecimal form')
parser.add_argument('file', help='The file to be splitted')

args = parser.parse_args()
inputFile = sys.argv[1]
pattern = bytes(args.text, 'utf-8') if args.binary == None else bytes.fromhex(args.binary)

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


with open(args.file, 'rb') as f_in :
  fileIdx = 0
  while True:
    with open(args.file + '.part' + str(fileIdx), 'wb') as f_out:
      bytes = getNextBytes(f_in)
      while (bytes != b'' and bytes != None):
        f_out.write(bytes)
        bytes = getNextBytes(f_in)
      f_out.flush()
      if bytes == None:
        break
      fileIdx += 1
