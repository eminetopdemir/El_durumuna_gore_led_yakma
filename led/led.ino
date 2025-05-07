
int ledPin = 13; 

void setup() {
  pinMode(ledPin, OUTPUT);     
  Serial.begin(9600);         
}

void loop() {
  if (Serial.available() > 0) { 
    char okuma = Serial.read(); 

    if (okuma == '1') {
      digitalWrite(ledPin, HIGH); 
    } 
    else if (okuma == '0') {
      digitalWrite(ledPin, LOW);  
    }
  }
}
