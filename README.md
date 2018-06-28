# IoT Friends

esp32 code for interacting with friends over MQTT through AWS IoT

## Board set up
 * Run on boards with the esp wroom32 chip, eg the Adafruit Huzzah
 * Very similar steps to setting up a esp8266:
  https://learn.adafruit.com/micropython-basics-how-to-load-micropython-on-a-board/esp8266
 * You'll need to download the latest ESP32 bin to flash the board:
  sudo esptool.py --chip esp32 --port /dev/ttyUSB0 write_flash -z 0x1000 ../esp32-20180524-v1.9.4-85-gdf9b7e8f.bin
 * Install ampy for interacting with the obard:
  https://learn.adafruit.com/micropython-basics-load-files-and-run-code/install-ampy

## Assuming ampy is installed upload code:
export AMPY_PORT=/dev/ttyUSB0
 * Try it:
   ampy run main.py
 * Upload it:
   ampy put main.py
The environment variable doesn't always seem to work, and you may need sudo, if so, try:
  sudo ampy -p /dev/ttyUSB0 put main.py

### To get on:
screen $AMPY_PORT 115200
