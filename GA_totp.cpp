/*******************************************************************************************************
**  Author:         Ernest Kim
**  Description:    This program will generate a QR code on a png file that can be scanned by the
**                  Google Authenticator App on Android. This program will also print out a 6 digit OTP
**                  every 30 seconds that should match the one on the GA App once you scan the generated
**                  QR code.
********************************************************************************************************/
#include "HMAC_SHA1.h"
 
BYTE Key[20] ;
BYTE digest[20] ; 

unsigned char *test = "Hi There" ; 
memset(Key, 0x0b, 20) ;
CHMAC_SHA1 HMAC_SHA1 ;
HMAC_SHA1.HMAC_SHA1(test, strlen(test), Key, sizeof(Key), digest) ;
 


int main(){

    return 0;
}