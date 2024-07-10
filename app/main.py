import read_csv as rc
import utils 
import charts
import pandas as pd


def run():
    # Obtención de los datos
    df = pd.read_csv('data.csv') 

    # Gráfico bar de población según país.

    country = input('Type Country => ').title().strip()
    filter = df[df['Country/Territory'] == country]
    
    cou_anos, cou_population = utils.get_population(filter)
    charts.generate_bar_chart(cou_anos, cou_population, country)

    # Porcentaje de la población en el mundo.
    filtrar = input('¿Desea filtrar por continente? Si o no -> ').lower()
    if filtrar == 'si':
        continent = input('Escribir el continente -> ').title().strip()
        df = df[df['Continent'] == continent]
    countries = df['Country/Territory'].values
    percentages = df['World Population Percentage']   
    charts.generate_pie_chart(countries, percentages)


if __name__ == '__main__':
    run()