import random

def choose_options():
    options = ('piedra','papel','tijera')
    user_option = input("Piedra, papel o tijera => ").lower()
    computer_option = random.choice(options)

    if not user_option in options:
        return(None, None)
    else:
        return(user_option, computer_option)

def reglas(usu, comp):
    score_user = 0
    score_computer = 0
    if usu == comp:
        print("¡EMPATE!")
    elif usu == 'piedra' and comp == 'tijera':
        print("¡Usuario GANÓ!")
        score_user += 1
    elif usu == 'papel' and comp == 'piedra':
        print("¡Usuario GANÓ!")
        score_user += 1
    elif usu == 'tijera' and comp == 'papel':
        print("¡Usuario GANÓ!")
        score_user += 1
    else: 
        print("Computadora gana")
        score_computer +=1
    return(score_user, score_computer)
    

def run_game():
    score_user = 0
    score_computer = 0
    puntaje = int(input("¿A cuantos puntos quieres jugar? => "))
    ronda = 0

    while score_user < puntaje and score_computer < puntaje:
        # contador ronda
        ronda += 1 
        print('*' * 10 + "\n RONDA #" + str(ronda) + "\n" + '*' * 10)

        # opciones usuario
        user_option, computer_option = choose_options()

        user = 0
        computer = 0

        if user_option == None:
            print("opción invalida")
        else:
            print('- Usuario:', user_option)
            print('- Computadora:', computer_option)

            user, computer = reglas(user_option, computer_option)

        score_user += user
        score_computer += computer

        print("El usuario tiene {} wins y la maquina tiene {} wins \n".format(score_user,score_computer))


run_game()
