
import Jogo_Adivinhação
import Jogo_Forca

print('Jogador(a) bem vindo ao menu de jogos')
print('')
print('Por gentileza,escolha uma das opções de jogos:')
print('')
print('1- Adivinhação')
print('2- Forca')
print('')
jogo_escolhido = int(input('Qual sua escolha:'))

if (jogo_escolhido == 1):
  print('')
  print('loading...')
  print('')
  Jogo_Adivinhação.jogo_adivinhação()
elif (jogo_escolhido == 2):
  print('')
  print('loading...')
  print('')
  Jogo_Forca.jogo_forca()
