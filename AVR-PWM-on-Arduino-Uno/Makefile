dir:
	mkdir -p build

build: dir
	avr-gcc -c -std=gnu99 -Os -Wall -ffunction-sections -fdata-sections -mmcu=atmega328p -DF_CPU=16000000 -o build/pulse.o pulse.c
	avr-gcc -Os -mmcu=atmega328p -ffunction-sections -fdata-sections -Wl,--gc-sections -o build/pulse.elf build/pulse.o
	avr-objcopy -O ihex -R .eeprom build/pulse.elf build/pulse.hex

flash: build
	sudo avrdude -V -c arduino -p atmega328p -P /dev/ttyACM0 -b 115200 -U flash:w:build/pulse.hex:i

clean:
	rm build/*.o build/*.bin build/*.hex