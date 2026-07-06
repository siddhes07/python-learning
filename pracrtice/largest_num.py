a = int(input ("enter first number : "))
b = int(input ("enter second number : "))
c = int(input ("enter third number : "))

if ( a > b and a> c ):
    print ( " a is the largest number " )
elif ( b > a and b> c ):
    print ( " b is the largest number " )
elif ( c > a and c> b ):
    print ( " c is the largest number " )
else:
    print ( " all numbers are equal " )