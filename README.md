# home-assistant-standalone-speedtest

## Running the test

```bash
python3 -m unittest discover -s tests -p 'test_*.py'
```

## Generate requirements

```bash
pip install pipreqs
pipreqs . --force
```

## Prerequisites

```bash
pip install -r requirements.txt
```

## Script
Copy this script to your local directory

## Configuration

```
├── const.py
├── speedtest_runner
│   ├── const.py
```

The top const.py contains the required global configurations

example

```ini
MAX_RUNTIME = 60
RUN_INTERVAL = 60
HA_BASE_URL = "http://192.168.5.5:8123"
HA_ACCESS_TOKEN = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx.xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

The const.py under speedtest_runner contains the sensor name that would reflect in homeassistant

example

```ini
UPLOAD_SENSOR_NAME = "sensor.speedtest_upload2"
DOWNLOAD_SENSOR_NAME = "sensor.speedtest_download2"
PING_SENSOR_NAME = "sensor.speedtest_ping2"
```

## Running SpeedTest
python3 main.py