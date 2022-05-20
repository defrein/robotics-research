//Menyalakan LED dengan Push Button

int pinLed =3;
int pinPushButton = 4;

void setup()
{
  pinMode(pinLed, OUTPUT);
  pinMode(pinPushButton, INPUT_PULLUP);
  Serial.begin(9600);
}

void loop()
{
  int statusPushButton = digitalRead(pinPushButton);
  
  if (statusPushButton == HIGH){
    digitalWrite(pinLed, LOW);
  } else {
    digitalWrite(pinLed, HIGH);
    Serial.println("Led sedang menyala");
  }
}
