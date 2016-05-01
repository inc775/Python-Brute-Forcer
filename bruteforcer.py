import hashlib
import itertools
import string
import time
import md5
import sys

file = raw_input("Enter filename: ")
with open(file) as f:
    hashes = f.read().splitlines()
stime = time.time()
a_z = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789~!@#$%^&*()_"
m = hashlib.md5()
numhash = len(hashes)
found = 0
for i in range(16):
	for c in itertools.permutations(a_z,i):
		for num in hashes:
			mdhash = hashlib.md5(''.join(c)).hexdigest()
			if(mdhash == num):
				print "Password found for hash: %s" %(hashlib.md5(''.join(c)).hexdigest())
				print "The password is %s"%(''.join(c))
				print "It took %s seconds"%(time.time() - stime)
				found += 1
			if(found == numhash):
				sys.exit(0)