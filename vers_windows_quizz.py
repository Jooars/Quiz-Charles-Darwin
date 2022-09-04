import vers_mobile_Tools
import os
import random
import time


def q1():

    asks.append(1)


    os.system("cls")


    vers_mobile_Tools.Title(f"\033[33m{len(asks)}° Pergunta:\033[m Charles Darwin disse mesmo que nós, seres humanos, evoluímos dos macacos?")
    p = vers_mobile_Tools.quiz(["Sim"], "Não")


    if p == True:
        corrects.append(1)
    elif p == False:
        wrongs.append(1)

    input("Pressione ENTER para continuar...")
    print("Aguarde...")



def q2():


    os.system("cls")

    asks.append(1)
    vers_mobile_Tools.Title(f"\033[33m{len(asks)}° Pergunta\033[m: Qual era o nome do clube que Charles Darwin frquentava que provava comidas exóticas")
    p = vers_mobile_Tools.quiz(["Awesome Club", "Eating Club", "Greediness Club"], "Glutton Club")

    if p == True:
        corrects.append(1)
    elif p == False:
        wrongs.append(1)

    input("Pressione ENTER para continuar...")
    print("Aguarde...")



def q3():

    os.system("cls")
 

    asks.append(1)
    vers_mobile_Tools.Title(f"\033[33m{len(asks)}° Pergunta\033[m: Segundo Charles Darwin, qual era a melhor carne que ele já comeu?")
    p = vers_mobile_Tools.quiz(["Rato", "Tatu", "Capivara"], "Um roedor desconhecido")

    if p == True:
        corrects.append(1)
    elif p == False:
        wrongs.append(1)

    input("Pressione ENTER para continuar...")
    print("Aguarde...")



def q4():

    os.system("cls")


    asks.append(1)
    vers_mobile_Tools.Title(f"\033[33m{len(asks)}° Pergunta:\033[m  Quando nasceu Charles Darwin?")
    p = vers_mobile_Tools.quiz(["15 de novembro de 1809", "Ningúem sabe", "25 de abril de 1996"], "12 de fevereiro de 1809")

    if p == True:
        corrects.append(1)
    elif p == False:
        wrongs.append(1)

    input("Pressione ENTER para continuar...")
    print("Aguarde...")



def q5():
 
    os.system("cls")

    asks.append(1)
    vers_mobile_Tools.Title(f"\033[33m{len(asks)}° Pergunta:\033[m Quantos anos Charles Darwin tinha quando sua mãe faleceu?")
    p = vers_mobile_Tools.quiz(["17 anos", "9 anos", "7 anos"], "8 anos")

    if p == True:
        corrects.append(1)
    elif p == False:
        wrongs.append(1)

    input("Pressione ENTER para continuar...")
    print("Aguarde...")



def q6():
    os.system("cls")

    asks.append(1)
    vers_mobile_Tools.Title(f"\033[33m{len(asks)}° Pergunta:\033[m A espedição HMS Beagle tinha como objetivo:")
    p = vers_mobile_Tools.quiz(["Essa expedição não existiu", "Apenas explorar áreas desconhecidas", "Charles Darwin precisava de alguns dia de descanço, e assim foi ele e alguns amigos"], "Coletar espécies de animais e plantas, além de mapear costas, que eram desconhecidas dos britânicos da época.")

    if p == True:
        corrects.append(1)
    elif p == False:
        wrongs.append(1)
    
    input("Pressione ENTER para continuar...")
    print("Aguarde...")



def q7():

    os.system("cls")


    asks.append(1)
    vers_mobile_Tools.Title(f"\033[33m{len(asks)}° Pergunta:\033[m Das alternativas a seguir, perto de qual dessas pessoas Charles Darwin foi sepultado?")
    p = vers_mobile_Tools.quiz(["Marie Curie", "Albert Einstein", "Niels Bohr"], "Isaac Newton")

    if p == True:
        corrects.append(1)
    elif p == False:
        wrongs.append(1)

    input("Pressione ENTER para continuar...")
    print("Aguarde...")


def q8():

    os.system("cls")

    asks.append(1)
    vers_mobile_Tools.Title(f"\033[33m{len(asks)}° Pergunta:\033[m De qual doença Charles Darwin sofria?")
    p = vers_mobile_Tools.quiz(["influenza", "Varíola", "Cólera", "Febre amarela"], "Chagas") 

    if p == True:
        corrects.append(1)
    elif p == False:
        wrongs.append(1)

    input("Pressione ENTER para continuar...")
    print("Aguarde...")       
    
os.system("cls")

vers_mobile_Tools.Title("Bem-vindo(a) a meu quiz, O assunto é Charles Darwin, então, se divirta!")

time.sleep(3)

os.system("clear")

questions = [1, 2, 3, 4, 5, 6, 7, 8]

corrects = []

asks = []

wrongs = []


random.shuffle(questions)
for q in questions:

    if q == 1:
        q1()

    elif q == 2:
        q2()
    
    elif q == 3:
        q3()
    
    elif q == 4:
        q4()
    
    elif q == 5:
        q5()
    
    elif q == 6:
        q6()

    elif q == 7:
        q7()
    
    elif q == 8:
        q8()

os.system("clear")

print()
print("-"*30)
print(f"Você \033[32mACERTOU\033[m: \t\t\033[4m{len(corrects)}\033[m")
print(f"e \033[31mERROU\033[m: \t\t\033[4m{len(wrongs)}\033[m")
print(f"Total de \033[33mperguntas\033[m: \t\033[4m{len(asks)}\033[m")
print("-"*30)
print()




#🦆