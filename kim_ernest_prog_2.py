# Author:       Ernest Kim
# Date:         6/5/20
# Description:  This program will generate a QR code on a png file that can be scanned by the
#               Google Authenticator App on Android. This program will also print out a 6 digit OTP
#               every 30 seconds that should match the one on the GA App once you scan the generated
#               QR code.

import pyqrcode
from hashlib import sha1
import hmac
import base64
import math
import time
import sys

# Generate QR command
if sys.argv[1] == "--generate-qr":
    # String which represents the QR code
    qr_string = "otpauth://totp/Ernest_Kim_CS370?secret=JBSWY3DPEHPK3PXP"

    # Generate QR code
    new_QR = pyqrcode.create(qr_string)

    # Create and save the png file naming "myqr.png"
    new_QR.png('kim_ernest_GA_QR_code.png', scale=6)


# Helper function to convert an integer into a byte string
def int_to_bytestring(i: int, padding: int = 8) -> bytes:
    b_string = bytearray()

    while i != 0:
        b_string.append(i & 0xFF)
        i >>= 8

    return bytes(bytearray(reversed(b_string)).rjust(padding, b'\0'))

# Get One Time Password command
if sys.argv[1] == "--get-otp":
    # Secret Key
    key = base64.b32decode(b"JBSWY3DPEHPK3PXP")

    while True:
        # Counter for HMAC-SHA1 based on time at 30 second intervals
        time_counter = math.floor(time.time() / 30)
        counter = int_to_bytestring(time_counter)

        # Generate HMAC-SHA1 value
        hashed_value = hmac.new(key, counter, sha1)

        # Convert hashed value into hex byte string
        hex_byte_string = hashed_value.hexdigest()

        # Calculate offset
        offset = int(hex_byte_string[39], 16) * 2

        # Generate dynamic binary code
        DBC = list(hex_byte_string[offset] + hex_byte_string[offset + 1] + hex_byte_string[offset + 2] + \
            hex_byte_string[offset + 3] + hex_byte_string[offset + 4] + hex_byte_string[offset + 5] + \
            hex_byte_string[offset + 6] + hex_byte_string[offset + 7])

        # Make sure MSB is 0
        if ord(DBC[0]) >= 97:
            DBC[0] = chr(ord(DBC[0]) - 47)
        elif ord(DBC[0]) >= 48 and ord(DBC[0]) <= 57:
            DBC[0] = chr(ord(DBC[0]) - 8)

        # Convert list to a string
        DBC_string = str(DBC[0] + DBC[1] + DBC[2] + DBC[3] + DBC[4] + DBC[5] + DBC[6] + DBC[7])

        # Convert string into a base 10 decimal with 6 digits
        OTP = int(DBC_string, 16)
        OTP = OTP % 1000000

        # Print results and exit method
        print(OTP)
        print("Press CTRL + C to exit")

        # Wait 30 seconds before printing out next value of TOTP
        time.sleep(30)
