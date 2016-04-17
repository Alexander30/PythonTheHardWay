name='Zed A. Shaw'
age=35
height=182
weight=76
eyes='Blue'
teeth='yellow'
hair='Brown'
heightInches=height/2.54
weightPounds=weight/0.45
print "Person has %i cm, it is %d inches(decimal),\
 %.3f inch(float)" %(height, heightInches, heightInches)
print "Person has %i kg, it is %.3f pounds" %(weight, weightPounds)

print "If I add %d, %d, and %d I get %d." %(
age, height, weight, age + height + weight)

print "toto je testovanie string formating s r flagom: %r" % {"key":'value'}