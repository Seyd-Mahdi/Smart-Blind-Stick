const int trigPin = 9;
const int echoPin = 10;
const int buzzer = 11;
const int ledPin = 13;

long duration;
int distance;
int safetyDistance;

unsigned long previousMillis = 0;
unsigned long buzzerOnMillis = 0;
bool isBuzzerActive = false;

void setup() {
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(buzzer, OUTPUT);
  pinMode(ledPin, OUTPUT);

  digitalWrite(ledPin, HIGH);
}

void loop() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  duration = pulseIn(echoPin, HIGH, 12000);

  if (duration == 0) {
    distance = 100;
  } else {
    distance = (duration / 2) / 29.1;
  }
  
  safetyDistance = distance;
  unsigned long currentMillis = millis();

  if (safetyDistance > 15 && safetyDistance <= 50) {
    int delayTime = map(safetyDistance, 15, 50, 15, 350);

    if (!isBuzzerActive && (currentMillis - previousMillis >= delayTime)) {
      tone(buzzer, 1500);
      isBuzzerActive = true;
      buzzerOnMillis = currentMillis;
    }

    if (isBuzzerActive && (currentMillis - buzzerOnMillis >= 50)) { 
      noTone(buzzer);
      isBuzzerActive = false;
      previousMillis = currentMillis;
    }
  } 
  else if (safetyDistance > 0 && safetyDistance <= 15) {
    tone(buzzer, 2200);
    isBuzzerActive = true;
  } 
  else {
    noTone(buzzer);
    isBuzzerActive = false;
  }
}
