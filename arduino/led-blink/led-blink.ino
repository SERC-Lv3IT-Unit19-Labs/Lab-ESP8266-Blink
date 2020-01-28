/*
ESP8266 LED Blink
*/

#define LED 5 // define the pin the LED is attached to

/*
 * The setup function. We only start the sensors here
 */
void setup(void)
{
  pinMode(LED, OUTPUT); // Initialise the LED pin as an OUTPUT
}

/*
 * Main function, get and show the temperature
 */
void loop(void)
{
  digitalWrite(LED, HIGH);  // Turn the LED on
  delay(1000);              // Wait for 1 second
  digitalWrite(LED, LOW);   // Turn the LED off
  delay(1000);              // Wait for 1 second
}
