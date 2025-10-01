#25/09/2025
'''
1 - João quer adicionar mais três frutas novas ao seu sistema.
2 - Ele também deseja aumentar o preço das frutas existentes em 20%.
3 - João quer incluir mais 20 produtos de cada.
4 - João vendeu todas as maçãs.
'''


loja_frutas = {
    'maça': {'preço': 3.50,
             'quantidade':10},
    'banana': {'preço': 3.50,
             'quantidade':10},
    'uva': {'preço': 3.50,
            'quantidade':10},
}

#R:João quer adicionar mais três frutas novas ao seu sistema.
loja_frutas.update({'limão':{'preço': 3.50,'quantidade':10},
                   'laranja': {'preço': 3.50,'quantidade':10},
                    'abacaxi':{'preço': 3.50,'quantidade':10}})
print(loja_frutas)

#R2: Ele também deseja aumentar o preço das frutas existentes em 20%.
for k,v in loja_frutas.items():
      loja_frutas.get(k)['preco']*=1.15
print(loja_frutas)


#R3: João quer incluir mais 20 produtos de cada.
for k,v in loja_frutas.items():
      loja_frutas.get(k)['quantidade']+=20
print(loja_frutas)

#R4: João vendeu todas as maçãs.
loja_frutas.pop('maça')
