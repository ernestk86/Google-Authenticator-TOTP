CS370 Ernest Kim Spring 2020

Programming Assignment 2

PREPARATIONS/ASSUMPTIONS:
- This program assumes that version 3.7 of Python is installed
- This program uses these libraries that may need to be installed
  - pyqrcode
  - pypng
    - To install pyqrcode type "pip install pyqrcode"
    - To install pypng type "pip install pypng"

TO RUN:
- Open a command terminal
- Navigate to folder with program file

TO PRINT QR CODE:
- Type "python kim_ernest_prog_2.py --generate-qr"
- File name "kim_ernest_GA_QR_code.png" should appear
in same folder as program file
- Scan QR code into Google Authenticator app on an Android Phone
- Watch TOTP generate in Google Authenticator app

TO GENERATE TOTP:
- Type "python kim_ernest_prog_2.py --get-otp"
- New 6 digit otp will print on screen every 30 seconds
- Otp should match code on Google Authenticator app
if QR Code from above was scanned

BRIEF IMPLEMENTATION EXPLANATION:
The code for this program is split into 2 halves. The first half
is for the QR code. The information in the QR code is a URI that
the Google Authenticator app expects. QR code is printed on a
png file. The second half is for the OTP that is generated
every 30 seconds. The key is hard coded in and there is a 
helper function to convert an integer to a bytestring. Then in a 
while loop, the counter for the HMAC is calculated and converted to 
a bytestring. The bytestring is for the HMAC generator. The resulting 
hashed value is converted into a hex byte string. The offset is 
calculated, then a check is done to make sure the MSB is 0. The 
resulting string from the offset is converted to a decimal value which 
is then modulated by 10^6. The resulting OTP is printed on the screen
with instructions for how to stop. Then the program sleeps for 30
seconds and reiterates in the while loop. 










