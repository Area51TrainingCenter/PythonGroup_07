from random import choice

sustantivos = ['perro', 'gato', 'cerdo', 'muchacho', 'auto']
adjetivos = ['alegre', 'triste', 'emocionado', 'tranquilo']
verbos = ['saltó', 'jugó', 'mordió', 'corrió', 'gritó']

sustantivo = choice(sustantivos)
sustantivo2 = choice(sustantivos)
adjetivos = choice(adjetivos)
verbo = choice(verbos)

print('El {} {} al {} y fue {}.'.format(sustantivo, verbo, sustantivo2, adjetivos))
