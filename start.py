import fibonacci
print "\n"
print "Student Name: Lam Hon Sum"
print "Student ID: 1155058981"
print fibonacci.init()
y = int(raw_input("Please input an integer to show the value of Fibonacci Sequence: "))

if y < 0:
    print 'Input cannot less than 0.'
else:
    for n in range(0,y):
     result = fibonacci.fib(n)
     print result,
