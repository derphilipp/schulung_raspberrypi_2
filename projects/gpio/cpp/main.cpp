#include <iostream>
#include <wiringPi.h>

const int PIN_RED = 2;
const int PIN_YELLOW = 0;
const int PIN_GREEN = 7;

int main() {

    if (wiringPiSetup() ==-1){
        return 1;
    }

    pinMode(PIN_RED, OUTPUT);
    pinMode(PIN_YELLOW, OUTPUT);
    pinMode(PIN_GREEN, OUTPUT);

    // Turn off everything
    digitalWrite(PIN_RED, 0);
    digitalWrite(PIN_YELLOW, 0);
    digitalWrite(PIN_GREEN, 0);

    std::cout << "Everything initialized" << std::endl;

    delay(2000);

    digitalWrite(PIN_GREEN, 1);
}
