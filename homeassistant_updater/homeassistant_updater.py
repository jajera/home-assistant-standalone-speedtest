# homeassistant_updater/homeassistant_updater.py
import aiohttp
import async_timeout
import json
import asyncio
from const import MAX_RUNTIME


class HomeAssistantUpdater:
    def __init__(self, ha_base_url, access_token, loop=None):
        self.ha_base_url = ha_base_url
        self.access_token = access_token
        self.loop = loop or asyncio.get_event_loop()
        self.headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
        }

    async def update_sensor(self, sensor_entity_id, new_value, **attributes):
        url = f"{self.ha_base_url}/api/states/{sensor_entity_id}"
        data = {"state": str(new_value)}

        if attributes:
            data["attributes"] = attributes

        async with aiohttp.ClientSession() as session:
            async with async_timeout.timeout(MAX_RUNTIME):
                async with session.post(
                    url, data=json.dumps(data), headers=self.headers
                ) as response:
                    if response.status == 200:
                        print(f"Sensor {sensor_entity_id} created successfully.")
                    elif response.status == 201:
                        print(f"Sensor {sensor_entity_id} updated successfully.")
                    else:
                        print(
                            f"Failed to update sensor {sensor_entity_id}. Status code: {response.status}"
                        )
