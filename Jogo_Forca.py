def jogo_forca():

  #realiza importacao 
    
  import datetime as data
    
    
  #inicio do jogo
  print('Bem Vindo Jogador(a)')
  print('por favor digite seu nome')
    
  hoje = data.date.today()
  nome_usuario = input()
  print('bem vindo:'+' '+nome_usuario+' '+'data de acesso:'+' '+str(hoje))

  # definindo variaveis

  palavra_chave = 'Rodrigo'   
  chance_incial = 0
  chance_max = range(chance_incial,4)
  enforcou = False
  acertou = False      


  while (not enforcou and not acertou):
    chance_incial = chance_incial + 1
    posicao_inicial = 1

    if (chance_incial == 1):
      tentativa = input('Qual letra?:').lower().strip()

    if (chance_incial > 1):
      tentativa = input('Tente Dinovo Qual letra?:').lower().strip()

    if (tentativa == palavra_chave.lower()):
      print('parabens')
      acertou = True
    elif (chance_incial >= 4):
      enforcou = True
    for letra in palavra_chave:
      if (tentativa == letra.lower()):
        print(letra+' '+str({}).format(posicao_inicial))
      posicao_inicial = posicao_inicial + 1



    
if (__name__ == 'main'):
  jogo_forca()