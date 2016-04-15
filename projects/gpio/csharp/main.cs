using System;
using RaspberryPiDotNet;

namespace Gpio
{
    class Program
    {
        static void Main(string[] args)
        {
            var pinRed = new GPIOFile(GPIOPins.V2_GPIO_27);
            var pinYellow = new GPIOFile(GPIOPins.V2_GPIO_17);
            var pinGreen = new GPIOFile(GPIOPins.V2_GPIO_04);

            // Turn off everything
            pinRed.Write(false);
            pinYellow.Write(false);
            pinGreen.Write(false);
            Console.WriteLine("Everything initialized");

            System.Threading.Thread.Sleep(2000);

            pinGreen.Write(true);

            System.Threading.Thread.Sleep(2000);
        }
    }
}
