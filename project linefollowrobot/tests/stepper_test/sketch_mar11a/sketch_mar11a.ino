#include <AccelStepper.h>
const int read_pin = 32;

// Define the stepper motor and the pins that is connected to
AccelStepper stepper1(1,12,13);

uint32_t trigger = 0;
int current_position = 0;

bool running = false;

void setup() {
  pinMode(read_pin, INPUT);
  
  stepper1.setMaxSpeed(1000);
  stepper1.setSpeed(200);

  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();
    
    if (command == 'S') {
      running = !running;

    }
  }

  if (running){
    //Serial.println(stepper1.currentPosition());
    
    stepper1.runSpeed();
  }
}