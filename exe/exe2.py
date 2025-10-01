# Aula 18/09/2025
#Criar a lojinha de carros, com marca, valor, cor e depois adicionar um aumento de preço de 15% no valor dos itens

loja_carro ={
    'gol':{
        'preco':20000,
        'cor': 'vermelho'
    },
    'uno':{
        'preco':30000,
        'cor': 'vermelho'
    }
}

for k,v in loja_carro.items():
      loja_carro.get(k)['preco']*=1.15
print(loja_carro)