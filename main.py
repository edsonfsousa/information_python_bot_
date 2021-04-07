import os

def processar_resposta(resposta, nome):
    if resposta == '1':
        print(f'{os.linesep}{nome}, seu nome completo é Edson Fernandes de Sousa e ele é natural de Fortaleza no Ceará.{os.linesep}')
    elif resposta == '2':
        print(f'{os.linesep}{nome}, ele tem conhecimento em Java, JavaScript, PHP e Python.{os.linesep}')
    elif resposta == '3':
        print(f'{os.linesep}{nome}, eu fui programado com Pyhton.{os.linesep}')
    elif resposta == '4':
        print(f'{os.linesep}{nome}, além de programar que de longe é seu passatempo preferido, ele gosta de jogar xadrez, tocar guitarra e jogar vôlei.{os.linesep}')
    else:
        print('Por favor digite apenas os números permitidos: (1, 2, 3, 4)')

def start():
        # Apresentar o bot
        print('Olá!, bem vindo ao bot de informações sobre o Edson Fernandes.')
        # Pedir informações
        nome = input('Digite seu nome: ')
        email = input('Digite seu email: ')
        while True:
            # Oferecer o menu de opções
            resposta = input(f'O que gostaria de saber sobre edson?{os.linesep}[1] - Qual o nome completo de Edson e onde nasceu?{os.linesep}[2] - Quais linguagens de programação Edson sabe?{os.linesep}[3] - Edson programou esse bot com qual linguagem?{os.linesep}[4] - Quais os passatempos de Edson?{os.linesep}')
            # Processar a resposta enviada
            processar_resposta(resposta,nome)

if __name__ == '__main__':
    start()
