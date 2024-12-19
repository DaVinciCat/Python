from abc import ABC, abstractmethod
from typing import Any
from urllib.request import urlopen
from urllib.parse import urlencode
import json
from dataclasses import dataclass

@dataclass
class WeatherInfo:
    temperature: float
    feels_like: float | None = None
    description: str = ''
    wind: float = -1
    wind_deg: float = -1
    pressure: float = -1
    humidity: int = -1
    
    def __post_init__(self):
        if self.feels_like is None:
            self.feels_like = self.temperature
            
    def get_wind_direction(self) -> str:
        directions = (
            'С', 'ССВ', 'СВ', 'ВСВ', 'В', 'ВЮВ', 'ЮВ', 'ЮЮВ',
            'Ю', 'ЮЮЗ', 'ЮЗ', 'ЗЮЗ', 'З', 'ЗСЗ', 'СЗ', 'ССЗ',
            )
	    
        index = round(self.wind_deg / 22.5) % 16
        return directions[index]

class WeatherError(Exception):
    pass

class WeatherProvider(ABC):
    @abstractmethod
    def get_weather(self, city: str) -> WeatherInfo:
        pass

    def _call_api(self, url: str, **parameters: Any) -> Any:
        sq = urlencode(parameters)
        
        with urlopen(f'{url}?{sq}') as resp:
            if 'application/json' in resp.headers['Content-Type']:
                return json.load(resp)
            return resp.read().decode()
            
class OpenWeatherMap(WeatherProvider):
    API_BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'
    
    def __init__(self, api_key: str) -> None:
        super().__init__() # ???
        self.api_key = api_key
        
    def get_weather(self, city: str) -> WeatherInfo:
        #requests.get(self.API_BASE_URL) - лучше было бы так
        data = self._call_api(
            self.API_BASE_URL,
            appid=self.api_key,
            q=city,
            lang='ru',
            units='metric',
            )
        description = [i['description'] for i in data['weather']]
        #print(data)
        return WeatherInfo(
            temperature=data['main']['temp'],
            feels_like=data['main']['feels_like'],
            description=', '.join(description),
            wind=data['wind']['speed'],
            wind_deg=data['wind']['deg'],
            pressure=round(data['main']['pressure'] * 0.75),
            humidity=data['main']['humidity'],
        )
        
class WeatherAPI(WeatherProvider):
    API_BASE_URL = 'http://api.weatherapi.com/v1/current.json'
    
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key
        
    def get_weather(self, city: str) -> None:
        data = self._call_api(
            self.API_BASE_URL,
            key=self.api_key,
            q=city,
            lang = 'ru'
        )
        
        current = data['current']
        #print(current)
        return WeatherInfo(
            temperature=current['temp_c'],
            feels_like=current['feelslike_c'],
            description=current['condition']['text'],
            wind=round(current['wind_kph'] / 3.6, 1),
            wind_deg=current['wind_degree'],
            pressure=round(current['pressure_mb'] * 0.75),
            humidity=current['humidity']
        )
        
class WeatherProviderFactory:
    types: dict[str, type[WeatherProvider]] = {
        'OpenWeatherMap' : OpenWeatherMap,
        'WeatherApi' : WeatherAPI,
    }
    
    @classmethod
    def add_type(cls, name:str, weather_class: type[WeatherProvider]) -> None:
        if not name:
            raise WeatherError('Type must have a name.')
            
        if not issubclass(weather_class, WeatherProvider):
            raise WeatherError(f'Class {weather_class} is not WeatherProvider')
            
        cls.types[name] = weather_class
        
    @classmethod
    def create(cls, name: str, *args, **kwargs) -> WeatherProvider:
        weather_class = cls.types.get(name)
        
        if weather_class is None:
            raise WeatherError(f'Weather provider with name {name} not found.')
        
        return weather_class(*args, **kwargs)
        
    
 service = WeatherProviderFactory.create('WeatherAPI', 'fc824a2d3d444f26be7112344240412')
 print(service.get_weather('Санкт-Петербург'))
 
#service = OpenWeatherMap('c381c9ac149f656d61112fd06e182741')
#print(service.get_weather('Санкт-Петербург'))

#service = WeatherAPI('fc824a2d3d444f26be7112344240412')
#print(service.get_weather('Санкт-Петербург'))

#class Point2D
#    def __init__(self, x: int, y: int) -> None:
#        self.x = x
#        self.y = y
#    
#    def __repr__(self) -> str:
#        #return f'{self.__class__.__name__}}({self.x}, {self.y})'
        
#p1 = Point2D(0, 0)
#p2 = Point2D(1, 0)

#print(p1, p2)