def population_by_country(data, country):
    result = list(filter(lambda x: x['Country/Territory'] == country, data))[0]
    return result

def get_population(country):
    dict = {
        '1970': country['1970 Population'],
        '1980': country['1980 Population'],
        '1990': country['1990 Population'],
        '2000': country['2000 Population'],
        '2010': country['2010 Population'],
        '2015': country['2015 Population'],
        '2020': country['2020 Population'],
        '2022': country['2022 Population']
    }
    keys = list(dict.keys())
    values = dict.values()
    values = list(map(lambda x : int(x), values))
    return keys, values

def country_by_continent(data, continent):
    result = list(filter(lambda x: x['Continent'] == continent, data))
    return result