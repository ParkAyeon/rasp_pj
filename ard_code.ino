#include <Servo.h>

#define SWITCH_PIN 5
#define SERVO_PIN 7
#define LED_PIN 8
#define BUZZER_PIN 10

Servo servo;

bool led_state = false;
bool motor_state = false;

void setup() {
    pinMode(BUZZER_PIN, OUTPUT);
    pinMode(LED_PIN, OUTPUT);
    pinMode(SWITCH_PIN, INPUT);
    servo.attach(7);
    Serial.begin(9600);
}

void loop() {
    if(digitalRead(SWITCH_PIN) == HIGH){
      noTone(BUZZER_PIN);
    }

    if (Serial.available() > 0) {
        char command = Serial.read();

        if (command == '1') {
          if(led_state == false){
            digitalWrite(LED_PIN, HIGH);
            Serial.println("LED ON");
            led_state = true;
          }
          else{
            digitalWrite(LED_PIN, LOW);
            led_state = false;
          }
        }

        else if (command == '2') {
            tone(BUZZER_PIN, 1000);
            Serial.println("Buzzer ON");
        }


        else if (command == '3') {
          if(motor_state == false){
            servo.write(180);
            Serial.println("Servo Moter Moved");
            motor_state = true;
          }
          else{
            servo.write(90);
            motor_state = false;
          }

        }

        else if (command == '0') {
            noTone(BUZZER_PIN);
            digitalWrite(LED_PIN, LOW);
            servo.write(90);
        }
    }
}

