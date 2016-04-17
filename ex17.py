from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

open_file = open(from_file)
indata = open_file.read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
#print "Ready, hit RETURN to continue, CTRL-C to abort."
#raw_input()

in_file = open(to_file, "w")
in_file.write(indata)

open_file.close()
in_file.close()
print "Alright, all done."

