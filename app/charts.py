import matplotlib.pyplot as plt

def generate_bar_chart(labels, values, country):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    
    ax.set_title(f'Grafica población {country}')
    ax.set_xlabel('label')
    ax.set_ylabel('value')
    
    plt.savefig(f'py-project/app/imgs/{country}.png')
    plt.close()

def generate_pie_chart(labels,values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')

    plt.savefig('py-project/app/imgs/pie.png')
    plt.close()


if __name__ == '__main__':
    labels = ['a', 'b', 'c']
    values = [100, 200, 80]
    generate_bar_chart(labels,values)
    generate_pie_chart(labels,values)
