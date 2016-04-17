#decimal string formatiing
x="There are \t\t %d types of people." % 10
binary="binary\t"
do_not="don't"
#string formating
y="Those who know %s and those who %s." %(binary, do_not)

print x
print y
#string formating via python object reaosn of added ''
print "I said: %r."%x
#another string formatting
print "I also said: '%s'." %y

hillarious=False
joke_evaluation="Isn't that joke so funny?! %r"

#printing string var with added var as python object
print joke_evaluation % hillarious

w="This is the left side of..."
e="a string with a right side."

#printing the concatenation of two string vars
print w+e 