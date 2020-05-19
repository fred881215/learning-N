unsigned long previousMillis = 0;
const long interval = 1000;    // 設定間隔時間，1000ms
char chr;
 
void setup() {
  Serial.begin(9600);
}
 
void loop() {
  unsigned long currentMillis = millis();
 
  if (currentMillis - previousMillis >= interval) {
    previousMillis = currentMillis;
    Serial.println("hello!");
  }

  CREATE TABLE EMPLOYEE (
  id INT NOT NULL AUTO_INCREMENT,
  name varchar(50) NOT NULL,
  descr varchar(200),
  price INT NOT NULL,
  PRIMARY KEY(id)
);