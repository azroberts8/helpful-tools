# Programming an Arduino Uno with AVR
Arduinos are great for small projects and Arduino IDE is good when you're first getting started with your Arduino. However, I got tired of Arduino IDE pretty quickly. This is probably an unpopular opinion but I would prefer to use traditional C or C++, compile with GCC, and flash the binary to the chip manually.

By ditching Arduino IDE we have the freedom to use whatever IDE and programming language that we prefer for our projects. This can include C, C++, Rust, or even assembly if you want to take it that far. Using this method we have control over how our program is compiled which can reduce the size it takes on the Arduino device compared to using the Arduino IDE.

For this guide I will be converting a simple Arduino project that slowly pulses an LED connected to pin 11 using PWM and timer interrupts into traditional C code and flashing it to the chip without the use of Arduino IDE.

*Note:* [Low Level Learning](https://www.youtube.com/@LowLevelLearning) has a [good video](https://youtu.be/j4xw8QomkXs) that I referenced during this project however I had issues with the binaries generated from his compile commands where the Arduino would sit idle and not do anything. *(I'm presuming it couldn't execute the binary for some reason)* I found [this post on Stack Overflow](https://stackoverflow.com/questions/32413959/avr-gcc-with-arduino) to be helpful in resolving my issues.

## Prerequisites
I am running the latest version of Ubuntu Desktop natively for my setup. We'll need the following packages to get started.
- `avr-libc`: The appropriate C libraries for AVR chips to link with our programs
- `gcc-avr`: Our compiler for compiling and linking our C code to AVR binaries
- `binutils-avr`: Used for changing the format of our binary for a format avrdude can work with
- `avrdude`: Flashes our binary to the Arduino

```bash
sudo apt update
sudo apt install avr-libc gcc-avr binutils-avr avrdude
```

## Migratiging Our Project To C
The default boilerplate code presented in Arduino IDe when you create a project is the following:
```C
void setup() {
    // put your setup code here, to run once:
}

void loop() {
    // put your main code here, to run repeatedly:
}
```

Given this structure and assuing you have not used any functions or macros specific to the Arduino IDE, the absolute simplest way to migrate our code would be to create a `.c` file with whose contents look like this:
```C
#include <avr/io.h>

// paste entire Arduino IDE project here

int main(void) {
    setup();

    while(1) {
    	loop();
    }
}
```

If we were not migrating this project we do not necessarily *need* our `setup()` and `loop()` functions. Instead we can think more like we would when writing a normal C program. Additionally, if we use any interrupts or other special features we will need to include them at the top of our program. See [pulse.c](pulse.c) for how I implemented ISRs.

## Identifying Arduino Location
Make sure your Arduino is connected to your system and run the following command:
```bash
ls /dev | grep ACM
```
This should have an output like `ttyACM0`. Note this location for later when we are flashing the chip with avrdude.

## Compiling And Flashing
### Compiling & Linking
Compile:
```bash
avr-gcc -c -std=gnu99 -Os -Wall -ffunction-sections -fdata-sections -mmcu=atmega328p -DF_CPU=16000000 -o pulse.o pulse.c
```

Link:
```bash
avr-gcc -Os -mmcu=atmega328p -ffunction-sections -fdata-sections -Wl,--gc-sections -o pulse.elf pulse.o
```
Explanation:
- `-c` means "compile to object file only, do not link"
- `-std=gnu99` means "My code conforms to C99 and I use GNU extensions"
- `-Os` means "optimize for executable size rather than code speed"
- `-Wall` means "turn on (almost) all warnings"
- `-ffunction-sections -fdata-sections` is necessary for the `-Wl,--gc-sections` optimization
- `-mmcu=atmega328p` means "the MCU part number is ATmega 328P"
- `-DF_CPU=16000000` means "the clock frequency is 16 MHz" (adjust for your actual clock frequency)
- `-Wl,--gc-sections` means "tell the linker to drop unused function and data sections" (this helps reduce code size)
*Borrowed from [the Stack Overflow post](https://stackoverflow.com/questions/32413959/avr-gcc-with-arduino)with minor tweak*

### Copying To Intel Hex
```bash
avr-objcopy -O ihex -R .eeprom pulse.elf pulse.hex
```
We convert the program binary to an Intel hex file since this is supported by avrdude

### Flashing to Arduino
```bash
sudo avrdude -V -c arduino -p atmega328p -P /dev/ttyACM0 -b 115200 -U flash:w:pulse.hex:i
```
Change the `/dev/ttyACM0` to the location of your Arduino determined in the previous section

## Conclusion
After executing the avrdude command to flash our program to the Arduino, the arduino should start running it the same way that it would after flashing from the Arduino IDE. If you encounter compiler errors, make sure that you have included all the necessary libraries (Arduino IDE automatically includes the libraries when using it) and check that you are not using functions or macros specific to Arduino IDE such as `digitalWrite()`. If you expereince issues flashing the Arduino or your program is not executing the same as it was from the Arduino IDE, check [the Low Level Learning video](https://youtu.be/j4xw8QomkXs) and [Stack Overflow post](https://stackoverflow.com/questions/32413959/avr-gcc-with-arduino) for alternative compiler and writer flags. The flags I included in this guide are the ones that worked for me with my Arduino Uno that I purchased over 10 years ago.