package main

import (
	"fmt"
	"github.com/stianeikeland/go-rpio"
	"time"
)

func main() {
	err := rpio.Open()
	if err != nil {
		panic("No access to the gpios")
	}

	pinRed := rpio.Pin(27)
	pinYellow := rpio.Pin(17)
	pinGreen := rpio.Pin(4)

	// Turn off everything
	pinRed.Low()
	pinYellow.Low()
	pinGreen.Low()

	fmt.Println("Everything initialized")

	time.Sleep(time.Second * 2)

	pinGreen.High()
}
