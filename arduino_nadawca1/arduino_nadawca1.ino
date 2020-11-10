void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println("200\n"); // prędkosc = 0km/h
  delay(500);
  Serial.println("390\n"); // procent naladowania baterii 90%
  delay(1000);
  Serial.println("401\n"); // zmiana trybu jazdy na D
  delay(1000);
  Serial.println("201\n"); // prędkosc
  delay(400);
    Serial.println("203\n"); // prędkosc
  delay(400);
    Serial.println("205\n"); // prędkosc
  delay(400);
    Serial.println("207\n"); // prędkosc
  delay(200);
    Serial.println("210\n"); // prędkosc
  delay(200);
    Serial.println("212\n"); // prędkosc
  delay(2000);
    Serial.println("209\n"); // prędkosc
  delay(200);
    Serial.println("206\n"); // prędkosc
  delay(200);
      Serial.println("202\n"); // prędkosc
  delay(200);
      Serial.println("200\n"); // prędkosc
  delay(200);
  Serial.println("411\n"); // zmiana trybu jazdy na P
  delay(5000);
  
  
  

}
