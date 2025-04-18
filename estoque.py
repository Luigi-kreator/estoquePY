lista = []
#FUNÇÕES PARA O PROGRAMA
def adicionarProduto():
    nome =  input('digite o nome do produto: ')
    for i in range(len(lista)):
      if nome == (lista[i]['nome']):
        print('Ok, verificamos que este produto já existe em estoque.')
        novaQuant = int(input('Digite a adição de quantidade deste produto: '))
        lista[i]['quantidade'] += novaQuant
        return print('informação atualizada')
    preco = float(input('digite o preço deste Produto: '))   
    quant = int(input('digite a quantidade que terá deste Produto em estoque: '))
    produto={
        'nome': nome,
        'preço': preco,
        'quantidade': quant
    }    
    lista.append(produto)
    return print('Produto adicionado com sucesso')
 
def venderProduto():
    if (len(lista)) == 0:
      return print('Não Existe Nenhum Produto a venda')
    nome = input('Digite o nome do produto a ser vendido: ')
    for i in range(len(lista)):
        if nome == lista[i]['nome']:
          quant = int(input(f'Digite a quantidade de {nome} a ser vendido: '))
          if quant <= lista[i]['quantidade']:
            lista[i]['quantidade'] -= quant
            return print(f'Venda realizada com sucesso!')
          else:
             return print('Quantidade em estoque Insuficiente')
    else:
           return print('O produto não existe em estoque(Ou está digitado de forma incorreta)')
       
def valorTotal():
    if (len(lista)) == 0:
        print('Não tem nenhum produto em estoque')
    else:
      valorTotal = 0
      for i in range (len(lista)):
         valorTotal += (lista[i]['preço'] * lista[i]['quantidade'])      
      return print(f'O valor Total em produto no estoque atualmente é: {valorTotal}')    
 
def listarProduto():
    if (len(lista)) == 0:
        print('Não tem nenhum produto na lista')
    for i in range(len(lista)):
      print(f'Nome do produto: {lista[i]['nome']}, Preço: {lista[i]['preço']}, Quantidade: {lista[i]['quantidade']}')
   
while True:
    print('\n[Gerenciador de Estoque de produto]\n[1 - Adicionar um produto]\n[2 - Vender produtos]\n[3 - Valor Total]\n[4 - Lista de produtos]\n[5 - Sair do Sistema]')
 
    escolha = int(input('Escolha uma opção para continuar: \n'))
   
    if escolha == 1:
      adicionarProduto()
    elif escolha == 2:
      venderProduto()
    elif escolha == 3:
      valorTotal()
    elif escolha == 4:
      listarProduto()
    elif escolha == 5:
      print('Saindo do Sistema...')
      break    
    else:
      print('Opção invalida, escolha outro numero entre 1 a 5')
#DESENVOLVIDO POR LUIGI HISATSUGA PEREIRA