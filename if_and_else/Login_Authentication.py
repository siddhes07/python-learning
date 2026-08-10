username = input("Enter username: ")
password = input("Enter password: ")
otp = input("Enter OTP: ")

correct_username = "admin"
correct_password = "python123"
correct_otp = "4567"

if username != correct_username:
    print("Invalid Username")

elif password != correct_password:
    print("Invalid Password")

elif otp != correct_otp:
    print("Invalid OTP")

else:
    print("Login Successful")