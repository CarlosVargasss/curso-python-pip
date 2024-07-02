import csv

def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        data = []
        for line in reader:
            iterable = list(zip(header, line))
            country_dict = {key : value for key, value in iterable}
            data.append(country_dict)
    return data


if __name__ == '__main__':
    data = read_csv('py-project/app/data.csv')
    print(data[0])