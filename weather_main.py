import configparser import ConfigParser
import sys
from textwrap import dedent

from weather import WeatherProviderFactory

def main():
    if len(sys.argv) < 2:
        print('Positional argument "city" is required.', file=sys.stderr)
        sys.exit(1)
    
    config = ConfigParser()
    config.read('config.ini')
    
    provider_name = config.get('main', 'provider_class')
    parameters = dict(config.items(provider_name))
    #print(provider_name, parameters)
    provider = WeatherProviderFactory.create(provider_name, ** parameters)
    #print(provider)
    city = sys.argv[1]
    info = provider.get_weather(city)
    
    
if __name__ == '__main__':
    main()