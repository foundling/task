#!/usr/bin/python

open('filename.txt','w')

# didn't save it, lets call it something

f = open('filename.txt','w')
f.write('')
f.close()

f = open('filename.txt','r+') # open a file named efilename.txt for reading and writing
f.write('the hindenberg')
print "writing 'the hindenberg'"

f.write('the hindenberg')
print "writing 'the hindenberg'"
print f.read()  

f.write('')

print 'reading...'
if not f.read():
  print '< nothing >'

''' code snippet 

the hindenbergthe hindenberg

'''

