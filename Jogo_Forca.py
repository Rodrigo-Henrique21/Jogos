def jogo_forca():

  #realiza importacao 
    
  import datetime as data
    
    
  #inicio do jogo
  print('Bem Vindo Jogador(a)')
  print('por favor digite seu nome')
    
  hoje = data.date.today()
  nome_usuario = input()
  print('bem vindo:'+' '+nome_usuario+' '+'data de acesso:'+' '+str(hoje))
  
  # definindo palavras secretas
  def gerador_palavras():
      palavras = pd.read_excel(r'C:\palavras.xlsx',usecols = ['palavras'])
        df = pd.DataFrame(data = palavras)
        lista = df['palavras'].tolist()

  # definindo variaveis

  palavra_chave = 'Rodrigo'
  saida_chave = []
  acertos = []
  total_letras = len(palavra_chave)
  chance_incial = 0
  chance_max = range(chance_incial,6)
  enforcou = False
  acertou = False   
  
  # definindo uma compressão de lista
  
  def check_len():
   saida_chave = ['_' for i in palavra_chave]

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
      enforcou = True
      break
      
  
    
if (__name__ == 'main'):
  jogo_forca()





