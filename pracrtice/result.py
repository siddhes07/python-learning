marks = int (input ( " enter your marks : " ) )

if ( marks >= 90):
    print ( "grade = 'a'" )

elif ( marks >= 80 and marks < 90 ):
    print ( "grade = 'b'" )

elif (marks>=70 and marks<80 ):
    print ( "grade = 'c'" )

elif (marks>=60 and marks<70 ):
    print ( "grade = 'd'" )
else:
    print ( " fail" )