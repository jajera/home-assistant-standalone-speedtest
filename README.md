# home-assistant-standalone-speedtest

## Running the test
python3 -m unittest discover -s tests -p 'test_*.py'

## Generate requirements
pip install pipreqs
pipreqs . --force

## Prerequisites
pip install -r requirements.txt

## Script
Copy this script to your local directory

## Configuration
The top const.py contains the required global configurations
├── const.py

example

```ini
MAX_RUNTIME = 60
RUN_INTERVAL = 60
HA_BASE_URL = "http://192.168.5.5:8123"
HA_ACCESS_TOKEN = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx.xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

The const.py under speedtest_runner contains the sensor name that would reflect in homeassistant
├── speedtest_runner
│   ├── const.py

example

```ini
UPLOAD_SENSOR_NAME = "sensor.speedtest_upload2"
DOWNLOAD_SENSOR_NAME = "sensor.speedtest_download2"
PING_SENSOR_NAME = "sensor.speedtest_ping2"
```

## Running SpeedTest
python3 main.py