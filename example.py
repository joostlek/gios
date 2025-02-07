"""Example for GIOS."""
import asyncio
import logging

from aiohttp import ClientError, ClientSession

from gios import ApiError, Gios, InvalidSensorsData, NoStationError

GIOS_STATION_ID = 568

logging.basicConfig(level=logging.DEBUG)


async def main() -> None:
    """Run main function."""
    async with ClientSession() as websession:
        gios = Gios(GIOS_STATION_ID, websession)
        try:
            data = await gios.async_update()
        except (ApiError, NoStationError, InvalidSensorsData, ClientError) as error:
            print(error)
            return

    latitude = gios.latitude
    longitude = gios.longitude
    station_name = gios.station_name
    print(f"Longitude: {longitude}")
    print(f"Latitude: {latitude}")
    print(f"Station name: {station_name}")
    print(data)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
