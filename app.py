players = {
    '1': {
        'nome':'Nilson',
        'idade': 24,
        'ryos': 320.50,
        'classe': 'Mago',
        'familia': 'Loki',
        'habilidades': {
            'ataque': 10,
            'defesa': 5,
            'vida': 10,
        },
        'nivel': 100,
        'xp': 0,
        'equipamentos': [0]

    },
    '2': {}
}

equipamentos = {
    '1': {
        'nome': 'Espada de Madeira',
        'classe': 'Guerreiro',
        'habilidades': {
            'ataque': 1,
            'defesa': 1,
            'vida': 0,}
        },
    '2': {
        'nome': 'Livro Velho',
        'classe': 'Mago',
        'nivel': 1,
        'habilidades': {
            'ataque': 1,
            'defesa': 0,
            'vida': 1,}
        },
    '3': {
        'nome': 'Arco de Madeira',
        'classe': 'Arqueiro',
        'habilidades': {
            'ataque': 2,
            'defesa': 0,
            'vida': 0,}
        },
}


def luta(player,monster):
  print('Você está lutando contra um',monster['nome'])
  player=player['habilidades']
  monster=monster['habilidades']
  while True:
    player['ataque'] -= monster['defesa']
    monster['ataque'] -= player['defesa']

    monster['vida'] -= player['ataque']
    player['vida'] -= monster['ataque']

    if player['vida'] <= 0:
      print('Você perdeu a luta')
      break
    elif monster['vida'] <= 0:
      print('Você ganhou a luta')
      break
 




def explorarDungeon(player):
  print('Você está explorando o Dungeon no Andar: ', player.get('dungeon'))
  luta(player,monstros.get(player['dungeon']))






def iniciar():
  print('Bem vindo ao RPG Terminal')
  id = str(input('Qual seu Id?: '))
  personagem = players[id]
  print(personagem['nome'])

  print('Menu\n1-Dungeon')
  
  escolha = input('Escolha uma opção: ')
  if escolha == '1':
    print('Você entrou no Dungeon')
    explorarDungeon(personagem)

iniciar()
