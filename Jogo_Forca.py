def jogo_forca():

  #realiza importacao 
    
  import datetime as data
  import random as rd
    
    
  #inicio do jogo
  print('Bem Vindo Jogador(a)')
  print('por favor digite seu nome')
    
  hoje = data.date.today()
  nome_usuario = input()
  print('bem vindo:'+' '+nome_usuario+' '+'data de acesso:'+' '+str(hoje))


  # Definindo gerador de palavras

  palavras = []
  def gerador_palavras():
      with open('palavras.txt','r') as arq:
          for i in arq:
              palavras.append(i.strip())
          arq.close()
          return 
      palavras
  gerador_palavras()

  # definindo variaveis
  numero_aleatorio = rd.randrange(1,len(palavras))
  palavra_chave = palavras[numero_aleatorio]
  saida_chave = []
  acertos = []
  total_letras = len(palavra_chave)
  chance_incial = 0
  chance_max = range(chance_incial,6)
  enforcou = False
  acertou = False   
  
  # definindo funções

  def check_len():
    for i in palavra_chave:
      saida_chave.append('_')

  check_len()

  # Printando dicas ao usuario 
  
  print('')
  print('Dicas:{}'.format(saida_chave))
  print('')

  while (not enforcou and not acertou):
    chance_incial += 1
    faltantes = total_letras - len(acertos)
    posicao_inicial = 0

    if (chance_incial == 1):
      tentativa = input('Qual letra?:').lower().strip()

    if (chance_incial > 1):
      tentativa = input('Tente Dinovo faltam apenas {}, Qual letra?:'.format(str(faltantes))).lower().strip()

    if (tentativa == palavra_chave.lower()):
      print('parabens')
      acertou = True
    elif (chance_incial >= 6):
      enforcou = True
    for letra in palavra_chave:
      if (tentativa == letra.lower()):
        saida_chave[posicao_inicial] = letra
      posicao_inicial += 1
      if (tentativa == letra.lower() and posicao_inicial not in acertos):
        acertos.append(posicao_inicial)
      if ('_' not in saida_chave):
        print(saida_chave)
        print('parabens acertou')
        acertou = True
        break
        
    if (acertou == True):
      print('Palavra secreta:{}'.format(''.join(saida_chave)))
    elif (acertou == False and enforcou == False):
      print(saida_chave)
    elif (enforcou == True):
      print('Acabaram as chances')
      print('A palavra secreta era: {}'.format(palavra_chave))
      enforcou = True
      break
      
  
    
if (__name__ == 'main'):
  jogo_forca()





