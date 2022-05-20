/*Program arduino dengan ultrasonic distance sensor */


//inisialisasi
int trigPin = 10;
int echoPin = 11;
int ledGreen = 3;
int ledYellow = 4;
int ledRed = 5;

long duration;
int jarakCm;

void setup(){
pinMode(trigPin, OUTPUT);     //trigPin sebagai output
pinMode(echoPin, INPUT);    //echoPin sebagai input
pinMode (ledGreen, OUTPUT);   //lampu hijau sebagai output
pinMode (ledYellow, OUTPUT);  //lampu kuning sebagai output
pinMode (ledRed, OUTPUT);   //lampu merah sebagai output
}

void loop() {
  digitalWrite(trigPin, LOW);     //trigPin diberi sinyal LOW (di-OFF kan)
  delayMicroseconds(2);       //selama 2 microseconds
  digitalWrite(trigPin, HIGH);    //trigPin diberi sinyal HIGH
  delayMicroseconds(10);      //selama 10 microseconds
  digitalWrite(trigPin, LOW);     //trigPin diberi sinyal LOW (di-OFF kan)
  duration = pulseIn(echoPin, HIGH); //variable echoPin menunggu sinyal pantul HIGH
  jarakCm = (duration/2) * 0.034;   //rumus jarak dalam cm
  
  if (jarakCm >= 150) {       //jika jarak lebih atau sama dengan 150 cm  
    digitalWrite(ledGreen, HIGH); //lampu hijau menyala
    digitalWrite(ledYellow, LOW);
    digitalWrite(ledRed, LOW);
  }
  else if (jarakCm >= 50){      //selainnya, jika jarak lebih atau sama dengan 50 cm
    digitalWrite(ledGreen, LOW);
    digitalWrite(ledYellow, HIGH);  //lampu kuning menyala
    digitalWrite(ledRed, LOW);
  }
  else {              //selain itu,
    digitalWrite(ledGreen, LOW);
    digitalWrite(ledYellow, LOW);
    digitalWrite(ledRed, HIGH);   //lampu merah menyala
  } 
}
