#python trials script
print('basic loop example...')
a=0
for i in xrange(10):
    a=a+i
print('a='+str(a))

#redundant parenthesis code smell
if ((a>10)):
    print('a>10')
elif a>20:
    print('a>20... never displayed...')
#FIXME test if fixme is found

#collapsing if statements mistake
if a>10:
    if a>20:
        print('a est high')

#code duplicates
a=0
for i in xrange(11):
    a=a+i
print('a='+str(a))

a=0
for i in xrange(11):
    a=a+i
print('a='+str(a))
a=0
for i in xrange(11):
    a=a+i
print('a='+str(a))

def test_above10():
   assert a>10

