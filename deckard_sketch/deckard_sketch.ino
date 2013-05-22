// Sweep
// by BARRAGAN <http://barraganstudio.com> 
// This example code is in the public domain.


#include <Servo.h> 
//#include <Math.h>

 
Servo xServo;  // create servo object to control a servo 
Servo yServo;  // a maximum of eight servo objects can be created 

int SERVO_MIN_POS = 0;
int SERVO_MAX_POS = 180;

 
int xPos = SERVO_MAX_POS/2;    // variable to store the servo position 
int yPos = SERVO_MAX_POS/2;

int increment =10;
 
void setup() 
{ 
  xServo.attach(8);
  yServo.attach(9);  // attaches the servo on pin 9 to the servo object 
  
 Serial.begin(9600);
 
 
 
} 
 
 
void loop() 
{ 
  // send data only when you receive data:
  if (Serial.available() > 0) {
    // read the incoming byte:
    int keyPressed = Serial.read();
  
    // say what you got:
    Serial.print("I received: ");
    Serial.println(keyPressed, DEC);
    
    switch(keyPressed)
    {
      case 119:  //w
        yPos -= increment;
        break; 
      case 115:  //s
        yPos += increment;
        break;
      case 100: //d
        xPos -= increment;
        break;
      case 97:  //a
        xPos += increment;
        break;
      default:
        Serial.println(keyPressed, DEC);
        Serial.print(" not recognized.");
    }
    
    xPos = constrain(xPos, SERVO_MIN_POS, SERVO_MAX_POS);
    yPos = constrain(yPos, SERVO_MIN_POS, SERVO_MAX_POS);
  }
  
    xServo.write(xPos);
    yServo.write(yPos);
} 
