# speedtest_runner/speedtest_runner.py
import speedtest
from collections import namedtuple
import asyncio
import async_timeout
from const import MAX_RUNTIME
from .const import (
    ATTRIBUTION,
    DOWNLOAD_DEVICE_CLASS,
    DOWNLOAD_FRIENDLY_NAME,
    DOWNLOAD_SENSOR_NAME,
    DOWNLOAD_UNIT_OF_MEASUREMENT,
    ICON,
    PING_DEVICE_CLASS,
    PING_FRIENDLY_NAME,
    PING_SENSOR_NAME,
    PING_UNIT_OF_MEASUREMENT,
    STATE_CLASS,
    UPLOAD_DEVICE_CLASS,
    UPLOAD_FRIENDLY_NAME,
    UPLOAD_SENSOR_NAME,
    UPLOAD_UNIT_OF_MEASUREMENT,
)

DownloadAttributes = namedtuple(
    "DownloadAttributes",
    [
        "attribution",
        "bytes_received",
        "device_class",
        "friendly_name",
        "icon",
        "server_country",
        "server_id",
        "server_name",
        "state_class",
        "unit_of_measurement",
    ],
)

UploadAttributes = namedtuple(
    "UploadAttributes",
    [
        "attribution",
        "bytes_sent",
        "device_class",
        "friendly_name",
        "icon",
        "server_country",
        "server_id",
        "server_name",
        "state_class",
        "unit_of_measurement",
    ],
)

PingAttributes = namedtuple(
    "PingAttributes",
    [
        "attribution",
        "device_class",
        "friendly_name",
        "icon",
        "server_country",
        "server_id",
        "server_name",
        "state_class",
        "unit_of_measurement",
    ],
)

DownloadResult = namedtuple(
    "DownloadResult",
    [
        "speed",
        "sensor_name",
        "attributes",
    ],
)

UploadResult = namedtuple(
    "UploadResult",
    [
        "speed",
        "sensor_name",
        "attributes",
    ],
)

PingResult = namedtuple(
    "PingResult",
    [
        "response",
        "sensor_name",
        "attributes",
    ],
)

SpeedTestResult = namedtuple(
    "SpeedTestResult",
    [
        "download",
        "upload",
        "ping",
    ],
)


class SpeedTestRunner:
    def __init__(self, loop=None):
        self.st = speedtest.Speedtest()
        self.loop = loop or asyncio.get_event_loop()

    async def _get_server_info(self):
        download_speed = await self.loop.run_in_executor(None, self.st.download)
        upload_speed = await self.loop.run_in_executor(None, self.st.upload)
        ping_response = self.st.results.ping

        download_attributes = DownloadAttributes(
            attribution=ATTRIBUTION,
            bytes_received=self.st.results.bytes_received,
            device_class=DOWNLOAD_DEVICE_CLASS,
            friendly_name=DOWNLOAD_FRIENDLY_NAME,
            icon=ICON,
            server_country=self.st.results.server["country"],
            server_id=self.st.results.server["id"],
            server_name=self.st.results.server["name"],
            state_class=STATE_CLASS,
            unit_of_measurement=DOWNLOAD_UNIT_OF_MEASUREMENT,
        )

        upload_attributes = UploadAttributes(
            attribution=ATTRIBUTION,
            bytes_sent=self.st.results.bytes_sent,
            device_class=UPLOAD_DEVICE_CLASS,
            friendly_name=UPLOAD_FRIENDLY_NAME,
            icon=ICON,
            server_country=self.st.results.server["country"],
            server_id=self.st.results.server["id"],
            server_name=self.st.results.server["name"],
            state_class=STATE_CLASS,
            unit_of_measurement=UPLOAD_UNIT_OF_MEASUREMENT,
        )

        ping_attributes = PingAttributes(
            attribution=ATTRIBUTION,
            device_class=PING_DEVICE_CLASS,
            friendly_name=PING_FRIENDLY_NAME,
            icon=ICON,
            server_country=self.st.results.server["country"],
            server_id=self.st.results.server["id"],
            server_name=self.st.results.server["name"],
            state_class=STATE_CLASS,
            unit_of_measurement=PING_UNIT_OF_MEASUREMENT,
        )

        return SpeedTestResult(
            DownloadResult(
                speed=round(download_speed/1_000_000, 2),
                sensor_name=DOWNLOAD_SENSOR_NAME,
                attributes=download_attributes,
            ),
            UploadResult(
                speed=round(upload_speed/1_000_000, 2),
                sensor_name=UPLOAD_SENSOR_NAME,
                attributes=upload_attributes,
            ),
            PingResult(
                response=round(ping_response, 0),
                sensor_name=PING_SENSOR_NAME,
                attributes=ping_attributes,
            ),
        )

    async def _run_speedtest_async(self):
        async with async_timeout.timeout(MAX_RUNTIME):
            await self.loop.run_in_executor(None, self.st.get_best_server)
            server_info = await self._get_server_info()

            return SpeedTestResult(
                server_info.download,
                server_info.upload,
                server_info.ping,
            )

    async def run_speedtest(self):
        try:
            return await self._run_speedtest_async()
        except asyncio.TimeoutError:
            print(f"Speed test timed out after exceeding MAX_RUNTIME: {MAX_RUNTIME}.")
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None
