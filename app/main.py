import read_csv as rc
import utils 
import charts


def run():
    # Obtención de los datos
    data = rc.read_csv('py-project/app/data.csv')

    # Gráfico bar de población según país.
    country = input('Type Country => ').title().strip()
    filter = utils.population_by_country(data, country)
    cou_anos, cou_population = utils.get_population(filter)
    charts.generate_bar_chart(cou_anos, cou_population, country)

    # Porcentaje de la población en el mundo.
    filtrar = input('¿Desea filtrar por continente? Si o no -> ').lower()
    if filtrar == 'si':
        continent = input('Escribir el continente -> ').title().strip()
        data = utils.country_by_continent(data, continent)
    country = list(map(lambda x : x['Country/Territory'], data))
    percentage = list(map(lambda x : x['World Population Percentage'], data))   
    charts.generate_pie_chart(country, percentage)


if __name__ == '__main__':
    run()