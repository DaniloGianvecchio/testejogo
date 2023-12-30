from PySimpleGUI import PySimpleGUI as sg

sg.theme('Reddit')
layout = [
    [sg.Text('Nome'), sg.Input(key='nome',size = (20, 1))],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*',size=(20,1))],
    [sg.Checkbox('Salvar informações')],
    [sg.Button('Entrar')]
]

janela = sg.Window('Tela de Login', layout)

while True:
    eventos, valores = janela.read()

    if eventos == sg.WINDOW_CLOSED:
        break

    if eventos == 'Entrar':
        nome_digitado = valores['nome']
        senha_digitada = valores['senha']

        # Aqui você pode adicionar a lógica de autenticação
        # Vou deixar um exemplo simples, mas você deve substituir isso por sua própria lógica de autenticação
        if nome_digitado == 'danlucas' and senha_digitada == 'danlucas123':
            janela.close()
            print('Bem-vindo!')
        else:
            print('Nome de usuário ou senha incorretos')

janela.close()

from random import randint
print('')
print('-=-'*10)
print(' Bem Vindo ao Battle Lands!!!')
print('-=-'*10)
print('')
jogador1=str(input('Jogador 1 Escolha o nome do seu personagem:'))
print('')
print('O nome do seu personagem sera {}'.format(jogador1))
print('')
print('''As classes disponiveis sao:
      
[1] guerreiro
[2] mago
[3] paladino''')
print('')
jogador1classe=str(input('Digite o nome da sua classe:'))
print('')
print('A classe do seu personagem sera {}'.format(jogador1classe))
print('')
jogador2=str(input('Jogador 2 Escolha o nome do seu personagem:'))
print('')
print('O nome do seu personagem sera {}'.format(jogador2))
print('')
print('''As classes disponiveis sao:
      
[1] guerreiro
[2] mago
[3] paladino''')
print('')
jogador2classe=str(input('Digite o nome da sua classe:'))
print('')
print('A classe do seu personagem sera {}'.format(jogador2classe))
print('')
print('=====A BATALHA VAI COMECAR=====')
print('')



dados1=int(input('jogador 1 Digite 1 para rolar o dado:'))

if dados1==1 :
   dados2=randint(1,2)
if dados2==1:
        

    mago = {'atk': 100, 'def': 40, 'hp': 250}
    guerreiro = {'atk': 80, 'def': 60, 'hp': 350}
    paladino = {'atk': 50, 'def': 80, 'hp': 450}

    if jogador1classe == 'mago':
            jogador1 = mago
    elif jogador1classe == 'guerreiro':
            jogador1 = guerreiro
    elif jogador1classe == 'paladino':
            jogador1 = paladino
    else:
        print("Classe inválida para o Jogador 1.")
    if jogador2classe == 'mago':
            jogador2 = mago
    elif jogador2classe == 'guerreiro':
            jogador2 = guerreiro
    elif jogador2classe == 'paladino':
            jogador2 = paladino
    else:
        print("Classe inválida para o Jogador 2.")

    resultado = jogador2['hp'] - (jogador1['atk'] -jogador2['def'] )
    print('')
    print('Seu ataque foi efetivo, o HP restante do seu oponente eh {}'.format(resultado))

    
else:print('Voce perdeu a vez, jogador 2 se prepare! ')


#======================================================================================


dados1=int(input('jogador 2 Digite 1 para rolar o dado:'))

if dados1==1 :
   dados2=randint(1,2)
if dados2==1:

    mago = {'atk': 100, 'def': 40, 'hp': 250}
    guerreiro = {'atk': 80, 'def': 60, 'hp': 350}
    paladino = {'atk': 50, 'def': 80, 'hp': 450}
        
    resultado = jogador1['hp'] - (jogador2['atk'] -jogador1['def'] )
    print('')
    print('Seu ataque foi efetivo, o HP restante do seu oponente eh {}'.format(resultado))
        
else:print('Voce perdeu a vez, jogador 1 se prepare! ')
      
    