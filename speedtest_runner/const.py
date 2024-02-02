# speedtest_runner/const.py
from __future__ import annotations
from typing import Final

ATTRIBUTION: Final = "Data retrieved from Speedtest.net by Ookla"
ICON: Final = "mdi:speedometer"
STATE_CLASS: Final = "measurement"
UPLOAD_SENSOR_NAME = "sensor.speedtest_upload2"
UPLOAD_DEVICE_CLASS: Final = "data_rate"
UPLOAD_FRIENDLY_NAME: Final = "SpeedTest Upload"
UPLOAD_UNIT_OF_MEASUREMENT: Final = "Mbit/s"
DOWNLOAD_SENSOR_NAME = "sensor.speedtest_download2"
DOWNLOAD_DEVICE_CLASS: Final = "data_rate"
DOWNLOAD_FRIENDLY_NAME: Final = "SpeedTest Download"
DOWNLOAD_UNIT_OF_MEASUREMENT: Final = "Mbit/s"
PING_SENSOR_NAME = "sensor.speedtest_ping2"
PING_DEVICE_CLASS: Final = "duration"
PING_FRIENDLY_NAME: Final = "SpeedTest Ping"
PING_UNIT_OF_MEASUREMENT: Final = "ms"
