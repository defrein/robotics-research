//Simulasi Trafic Light

int ledMerah = 6;
int ledKuning = 5;
int ledHijau = 4;

void setup()
{
  pinMode(ledMerah, OUTPUT);
  pinMode(ledKuning, OUTPUT);
  pinMode(ledHijau, OUTPUT);
}

void loop()
{
  digitalWrite(ledMerah, HIGH);
  digitalWrite(ledKuning, LOW);
  digitalWrite(ledHijau, LOW);
  delay(3000);
  digitalWrite(ledMerah, LOW);
  digitalWrite(ledKuning, HIGH);
  digitalWrite(ledHijau, LOW);
  delay(3000);
  digitalWrite(ledMerah, LOW);
  digitalWrite(ledKuning, LOW);
  digitalWrite(ledHijau, HIGH);
  delay(3000);
}
