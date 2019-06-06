#include <IRremote.h>
IRsend irsend;
bool sent;
void whatdoyoumean(){
  sent = true;
  switch(Serial.parseInt()){
    case 1: irsend.sendSAMSUNG(0xE0E040BF,32);
    case 2: irsend.sendSAMSUNG(0xE0E0F00F,32);
    case 3: irsend.sendSAMSUNG(0xE0E0E01F,32);
    case 4: irsend.sendSAMSUNG(0xE0E0D02F,32);
    case 5: irsend.sendSAMSUNG(0xE0E0807F,32);
    case 6: irsend.sendSAMSUNG(0xE0E006F9,32);
    case 7: irsend.sendSAMSUNG(0xE0E08679,32);
    case 8: irsend.sendSAMSUNG(0xE0E0A659,32);
    case 9: irsend.sendSAMSUNG(0xE0E046B9,32);
    case 10: irsend.sendSAMSUNG(0xE0E016E9,32);
    default: sent = false;
  }
  if (sent){
    Serial.println("sent");
  }
}

void setup(){
  Serial.begin(9600);
  Serial.print("power = 1, mute = 2, volup = 3, voldn = 4, input = 5, up = 6, down = 7, left = 8, right = 9, centre = 10");

}

void loop() {
  while(Serial.available() == 0){}
  whatdoyoumean();
}

