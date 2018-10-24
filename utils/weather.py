import json
import urllib

translation_dict = {
    '0': 'Tornado',
    '1': 'Tempestade tropical',
    '2': 'Furacão',
    '3': 'Tempestades severas',
    '4': 'Trovoadas',
    '5': 'Misto de chuva e neve',
    '6': 'Misto de chuva e granizo',
    '7': 'Misto de neve e granizo',
    '8': 'Garoa congelante',
    '9': 'Garoa',
    '10': 'Chuva gelada',
    '11': 'Chuva',
    '12': 'Chuva',
    '13': 'Nevoeiro',
    '14': 'Chuva de nevoeiro',
    '15': 'Nevoeiro',
    '16': 'Neve',
    '17': 'Granizo',
    '18': 'Chuva com neve',
    '19': 'Poeira',
    '20': 'Pebuloso',
    '21': 'Neblina',
    '22': 'Enfumaçado',
    '23': 'Tempestuoso',
    '24': 'Ventoso',
    '25': 'Frio',
    '26': 'Nublado',
    '27': 'Muito nublado (noite)',
    '28': 'Muito nublado (dia)',
    '29': 'Parcialmente nublado (noite)',
    '30': 'Parcialmente nublado (dia)',
    '31': 'Céu limpo (noite)',
    '32': 'Ensolarado',
    '33': 'Claro (noite)',
    '34': 'Claro (dia)',
    '35': 'Misto de chuva e granizo',
    '36': 'Quente',
    '37': 'Trovoadas isoladas',
    '38': 'Trovoadas',
    '39': 'Trovoadas',
    '40': 'Chuvas esparsas',
    '41': 'Neve',
    '42': 'Aguaceiros de neve espalhados',
    '43': 'Neve',
    '44': 'Parcialmente nublado',
    '45': 'Trovoadas',
    '46': 'Aguaceiros de neve',
    '47': 'Trovoadas isoladas',
    '3200': 'Não disponível',
}

icon_dict = {
    '0': 'mdi-weather-windy',
    '1': 'mdi-weather-pouring',
    '2': 'mdi-weather-windy',
    '3': 'mdi-weather-lightning',
    '4': 'mdi-weather-lightning',
    '5': 'mdi-weather-snowy',
    '6': 'mdi-weather-snowy',
    '7': 'mdi-weather-snowy',
    '8': 'mdi-weather-hail',
    '9': 'mdi-weather-hail',
    '10': 'mdi-weather-pouring',
    '11': 'mdi-weather-pouring',
    '12': 'mdi-weather-pouring',
    '13': 'mdi-weather-snowy',
    '14': 'mdi-weather-rainy',
    '15': 'mdi-weather-rainy',
    '16': 'mdi-weather-snowy',
    '17': 'mdi-weather-snowy',
    '18': 'mdi-weather-snowy',
    '19': 'mdi-weather-windy',
    '20': 'mdi-weather-windy',
    '21': 'mdi-weather-windy-variant',
    '22': 'mdi-weather-windy-variant',
    '23': 'mdi-weather-lightning',
    '24': 'mdi-weather-windy',
    '25': 'mdi-weather-windy',
    '26': 'mdi-weather-cloudy',
    '27': 'mdi-weather-cloudy',
    '28': 'mdi-weather-cloudy',
    '29': 'mdi-weather-cloudy',
    '30': 'mdi-weather-cloudy',
    '31': 'mdi-weather-night',
    '32': 'mdi-weather-sunny',
    '33': 'mdi-weather-night',
    '34': 'mdi-weather-sunset',
    '35': 'mdi-weather-snowy',
    '36': 'mdi-weather-sunny',
    '37': 'mdi-weather-lightning',
    '38': 'mdi-weather-lightning',
    '39': 'mdi-weather-lightning',
    '40': 'mdi-weather-hail',
    '41': 'mdi-weather-snowy',
    '42': 'mdi-weather-snowy',
    '43': 'mdi-weather-snowy',
    '44': 'mdi-weather-cloudy',
    '45': 'mdi-weather-lightning',
    '46': 'mdi-weather-rainy',
    '47': 'mdi-weather-lightning',
    '3200': 'mdi-cloud-outline-off',
}


def get_weather_data(woeid=455863):
    try:
        baseurl = 'https://query.yahooapis.com/v1/public/yql?'
        yql_query = 'select * from weather.forecast where woeid={woeid}'.format(
            woeid=woeid
        )
        yql_url = baseurl + urllib.parse.urlencode({'q': yql_query}) + "&format=json"
        result = urllib.request.urlopen(yql_url).read()
        data = json.loads(result)
        forecast = data['query']['results']['channel']['item']['forecast'][1:8]

        city = data['query']['results']['channel']['location']['city']
        region = data['query']['results']['channel']['location']['region']

        condition_code = int(data['query']['results']['channel']['item']['condition']['code'])
        temperature_f = int(data['query']['results']['channel']['item']['condition']['temp'])

        temperature = (temperature_f - 32) / 1.8
        condition = translation_dict.get(str(condition_code))
        condition_icon = icon_dict.get(str(condition_code))

        return {
            'city': city,
            'region': region,
            'temperature': temperature,
            'condition': condition,
            'condition_icon': condition_icon,
            'forecast': forecast,
        }
    except (urllib.error.URLError, KeyError):
        pass
