def population_by_country(data, country):
    result = list(filter(lambda x: x['Country/Territory'] == country, data))[0]
    return result

def get_population(country):
    dict = {
        '1970': int(country['1970 Population'].iloc[0]),
        '1980': int(country['1980 Population'].iloc[0]),
        '1990': int(country['1990 Population'].iloc[0]),
        '2000': int(country['2000 Population'].iloc[0]),
        '2010': int(country['2010 Population'].iloc[0]),
        '2015': int(country['2015 Population'].iloc[0]),
        '2020': int(country['2020 Population'].iloc[0]),
        '2022': int(country['2022 Population'].iloc[0])
    }
    keys = dict.keys()
    values = dict.values()
    return keys, values

def country_by_continent(data, continent):
    result = list(filter(lambda x: x['Continent'] == continent, data))
    return result