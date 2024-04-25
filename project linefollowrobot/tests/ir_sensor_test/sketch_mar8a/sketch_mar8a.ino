const int NUM_IR_SENSORS = 5;

struct IR_sensor{
  int pin;
  int val;
};

IR_sensor ir_sensors[NUM_IR_SENSORS] = {
  {34, 0},
  {35, 0},
  {32, 0},
  {33, 0},
  {25, 0}
};

bool send_values = false;

void setup() {
  for (int i = 0; i<NUM_IR_SENSORS;i++){
    pinMode(ir_sensors[i].pin, INPUT);
  }

  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read(); // Read the incoming command
    // You can perform actions based on the received command
    if (command == 'S') {
      send_values = true;
    } else if (command == 'T') {
      send_values = false;
    }
  }

  if (send_values){
    read_ir_sensors();

    print_ir_values();
  }

  delay(20);
}

void read_ir_sensors(){
  for (int i = 0; i<NUM_IR_SENSORS;i++){
    ir_sensors[i].val = analogRead(ir_sensors[i].pin);
  }

  int test = 0;
}

void print_ir_values(){
  char buffer[50];

  sprintf(buffer, "");
  for (int i = 0; i < NUM_IR_SENSORS-1; i++) {
    sprintf(buffer + strlen(buffer), "%u,", ir_sensors[i].val);
  }
  sprintf(buffer + strlen(buffer), "%u\n", ir_sensors[NUM_IR_SENSORS - 1].val);
  Serial.print(buffer);
}
