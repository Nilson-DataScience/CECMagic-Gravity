# Aula 10/09/2025

# Treinamento para manipular dicionario



loja_frutas = {
    'maca': {'preco': 3.50,
             'quantidade':10},
    'banana': {'preco': 3.50,
             'quantidade':10},
    'uva': {'preco': 3.50,
            'quantidade':10},
}

# função get: método usado para acessar o valor em um dicionário ->
preco_uva = loja_frutas.get('uva',{})
#print('Uva:',preco_uva)

# função update: método usado para atualizar os valores do dicionário
loja_frutas.update({'uva': 8.90,'tomate':10})
print(loja_frutas,'#tomate adicionado')

# função pop: método para  remover uma chave
#específica de um dicionário e retornar
#o valor associado a ela.
loja_frutas.pop('tomate')
print(loja_frutas,'#tomate removido')