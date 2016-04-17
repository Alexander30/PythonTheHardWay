import sys

script, first, second, third = sys.argv

print "This script is called:", sys.argv[0]
print "Your first variable is:", sys.argv[1]
print "Your second variable is:", second
print "Your third variable is:", int(third)

print raw_input("Daj dalsi input")