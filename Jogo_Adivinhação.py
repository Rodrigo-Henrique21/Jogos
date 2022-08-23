def jogo_adivinhação():

  #realiza importacao 
  
  import datetime as data
  import random
  
  
  #inicio do jogo
  print('Bem Vindo Jogador(a) ao jogo de adivinhação')
  print('por favor digite seu nome')
  
  hoje = data.date.today()
  nome_usuario = input()
  print('bem vindo:'+' '+nome_usuario+' '+'data de acesso:'+' '+str(hoje))
        
  pontuação_incial = 100
  total = 0
  max_tentativas = {}
  secredo = {}
  tentativa_restante = {}
  par = 'par'
  impar = 'impar'
  
  print('')
  print(nome_usuario+' '+'escolha um nivel de dificuldade;')
  print('')
  print('1 - Hard'+' '+'2 - Medium'+' '+'3 - Easy')
  print('')
  dificuldade = input('Qual sua escolha? ' )
  
  while (int(dificuldade) > 3 or int(dificuldade) < 1):
    #max_tentativas = range(total,5)
    #secredo = random.randrange(1,10)
    #tentativa_restante = 6
    dificuldade = input('Por gentileza selecione uma das opções:')
    continue
  
  if (int(dificuldade) == 3):
    max_tentativas = range(total,4)
    secredo = random.randrange(1,5)
    tentativa_restante = 5

  elif (int(dificuldade) == 2):
    max_tentativas = range(total,5)
    secredo = random.randrange(1,10)
    tentativa_restante = 6

  elif (int(dificuldade) == 1):
    max_tentativas = range(total,6)
    secredo = random.randrange(1,15)
    tentativa_restante = 7
    
    #comeco do loop de tentativas 
  for total in max_tentativas: 
  
    total = total +1
    tentativa_restante = tentativa_restante - 1
    tentativas_faltantes = print(nome_usuario+' '+'você tem apenas'+' '+str(tentativa_restante)+' '+ 'tentativas'+' '+'e'+' '+str(pontuação_incial)+' '+'pontos')
  
    
    print('')
    tentativa = input('por favor insira o numero:' )
  
    if (int(dificuldade) == 1):
      pontuação_restante = pontuação_incial - 30
    elif (int(dificuldade) == 2):
      pontuação_restante = pontuação_incial - 20
    else:
      pontuação_restante = pontuação_incial - 10
  
    pontuação_incial = pontuação_restante
  
    while (int(tentativa) < 1 or int(tentativa) > 15 and int(dificuldade) == 1):
      print('Insira um valor entre 1 até 15')
      tentativa = input('por favor insira o numero:' )
    while (int(tentativa) < 1 or int(tentativa) > 10 and int(dificuldade) == 2):
      print('Insira um valor entre 1 até 10')
      tentativa = input('por favor insira o numero:' )
    while (int(tentativa) < 1 or int(tentativa) > 5 and int(dificuldade) == 3):
      print('Insira um valor entre 1 até 5')
      tentativa = input('por favor insira o numero:' )
      
    else:
      input('voce digitou:'+tentativa+' '+'pressione entrer para confirmar')
      
      print('')
      
  
      if (int(tentativa) > secredo):
        print(nome_usuario +' '+'valor foi alto')
        print(str(pontuação_restante)+' '+'pontos')
      
        print('')    
        
      elif int(tentativa) < secredo:
        print('valor chutado foi menor')
        print(str(pontuação_restante)+' '+'pontos')
  
        
        print('')
        tentativas_faltantes      
      elif int(tentativa) == secredo: 
        print('parabens'+' '+ nome_usuario+' '+ 'voce ganhouu e fez'+' '+str(pontuação_restante)+' '+'pontos')
  
  
        break
  
      
      #final do jogo   
      if (tentativa_restante <= 1):
        print('total de tentativas restantes'+' '+ '{}'.format(tentativa_restante - 1))
        print('jogo encerrado, obrigado por jogar'+' '+ 'data encerramento:'+' '+ str(hoje))

if (__name__=='main'):
  jogo_adivinhação()

  
