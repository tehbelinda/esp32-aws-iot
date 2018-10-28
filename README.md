# ESP32 and AWS IoT

ESP32 MicroPython code for interacting with AWS IoT via MQTT

## Setup
 * Run on boards like the Adafruit HUZZAH32
 * Follow the very similar steps to [setting up ESP8266](https://learn.adafruit.com/micropython-basics-how-to-load-micropython-on-a-board/esp8266):
 * You'll need to [download the latest ESP32 bin](http://micropython.org/download/#esp32)
  to flash the board:
  
  `sudo esptool.py --chip esp32 --port /dev/ttyUSB0 write_flash -z 0x1000 esp32-20180524-v1.9.4-85-gdf9b7e8f.bin`
 * [Install ampy](https://learn.adafruit.com/micropython-basics-load-files-and-run-code/install-ampy) for interacting with the ESP32
  

## Deploy
 * Set the env var `export AMPY_PORT=/dev/ttyUSB0`
 * Run the code: `ampy run main.py`
 * Upload the code: `ampy put main.py`
 * Note: Exporting the environment variable doesn't always seem to work automatically, and you may need sudo, if so, try:
  `sudo ampy -p $AMPY_PORT put main.py`
 * To view: `sudo screen $AMPY_PORT 115200`

