import asyncio
from aiohttp import ClientSession
from aiohttp.web_exceptions import HTTPError
from api_keys import API_KEY

API_WEATHER = ("https://api.oceandrivers.com/v1.0/getAemetStation/Kiev/lastdata/",
               'https://www.metaweather.com/api/location/44418/',
               f'http://api.weatherstack.com/current?access_key={API_KEY}&query=Kharkiv')


async def get_weather_details_async(api_link, session):
    try:
        response = await session.request(method='GET', url=api_link)
        response.raise_for_status()
        print(f"Response status ({api_link}): {response.status}")
    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    response_json = await response.json()
    return response_json


async def oceandrivers(api_link, session):
    response = await get_weather_details_async(api_link, session)
    temperature = response.get('TEMPERATURE', None)
    print(f"Temperature on OCEANDRIVERS_API: {temperature}")
    return temperature


async def metaweather(api_link, session):
    response = await get_weather_details_async(api_link, session)
    current_info = response.get("consolidated_weather", [{}])[0]
    temperature = current_info.get('the_temp', None)
    print(f"Temperature on METAWEATHER_API: {temperature}")
    return temperature


async def weatherstack(api_link, session):
    response = await get_weather_details_async(api_link, session)
    current_info = response.get('current')
    temperature = current_info.get('temperature', None)
    print(f"Temperature on WEATHERSTACK_API: {temperature}")
    return temperature


async def run_program():
    async with ClientSession() as session:
        results = await asyncio.gather(oceandrivers(API_WEATHER[0], session), metaweather(API_WEATHER[1], session), weatherstack(API_WEATHER[2], session))
        a = sum(results) / len(results)
        print(f"Average of temperature is {a}")


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run_program())
    loop.close()


if __name__ == '__main__':
    main()
