# main.py
import asyncio
import datetime
from speedtest_runner.speedtest_runner import SpeedTestRunner
from homeassistant_updater.homeassistant_updater import HomeAssistantUpdater
from const import HA_BASE_URL, HA_ACCESS_TOKEN, RUN_INTERVAL, DEFAULT_NAME


async def main():
    speed_tester = SpeedTestRunner()

    ha_updater = HomeAssistantUpdater(HA_BASE_URL, HA_ACCESS_TOKEN)

    while True:
        result = await speed_tester.run_speedtest()

        if result is not None and result.download is not None:
            download_attributes = {
                "attribution": result.download.attributes.attribution,
                "bytes_received": result.download.attributes.bytes_received,
                "device_class": result.download.attributes.device_class,
                "friendly_name": result.download.attributes.friendly_name,
                "icon": result.download.attributes.icon,
                "server_country": result.download.attributes.server_country,
                "server_id": result.download.attributes.server_id,
                "server_name": result.download.attributes.server_name,
                "state_class": result.download.attributes.state_class,
                "unit_of_measurement": result.download.attributes.unit_of_measurement,
            }

            await ha_updater.update_sensor(
                result.download.sensor_name, result.download.speed, **download_attributes
            )

        if result is not None and result.upload is not None:
            upload_attributes = {
                "attribution": result.upload.attributes.attribution,
                "bytes_sent": result.upload.attributes.bytes_sent,
                "device_class": result.upload.attributes.device_class,
                "friendly_name": result.upload.attributes.friendly_name,
                "icon": result.upload.attributes.icon,
                "server_country": result.upload.attributes.server_country,
                "server_id": result.upload.attributes.server_id,
                "server_name": result.upload.attributes.server_name,
                "state_class": result.upload.attributes.state_class,
                "unit_of_measurement": result.upload.attributes.unit_of_measurement,
            }

            await ha_updater.update_sensor(
                result.upload.sensor_name, result.upload.speed, **upload_attributes
            )

        if result is not None and result.ping is not None:
            ping_attributes = {
                "attribution": result.ping.attributes.attribution,
                "device_class": result.ping.attributes.device_class,
                "friendly_name": result.ping.attributes.friendly_name,
                "icon": result.ping.attributes.icon,
                "server_country": result.ping.attributes.server_country,
                "server_id": result.ping.attributes.server_id,
                "server_name": result.ping.attributes.server_name,
                "state_class": result.ping.attributes.state_class,
                "unit_of_measurement": result.ping.attributes.unit_of_measurement,
            }

            await ha_updater.update_sensor(
                result.ping.sensor_name, result.ping.response, **ping_attributes
            )

        next_run_time = datetime.datetime.now() + datetime.timedelta(seconds=RUN_INTERVAL)
        print(f"{DEFAULT_NAME} next runtime: {next_run_time.strftime('%Y-%m-%d %H:%M:%S')}")

        await asyncio.sleep(RUN_INTERVAL)


if __name__ == "__main__":
    asyncio.run(main())
