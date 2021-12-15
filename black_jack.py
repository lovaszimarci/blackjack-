import random
# import zozi

#!
deck = {
    'tref2': 2,
    'tref3': 3,
    'tref4': 4,
    'tref5': 5,
    'terf6': 6,
    'tref7': 7,
    'tref8': 8,
    'terf9': 9,
    'tref10': 10,
    'trefjumbo': 10,
    'trefdama': 10,
    'trefkiraly': 10,
    'tefasz': 11,
    'tefasz2': 1
}

dealerhand = random.choice(list(deck))
dh = deck.get(dealerhand)
deck.pop(dealerhand)


personhand = random.choice(list(deck))
ph = deck.get(personhand)
deck.pop(personhand)
# ?
if personhand == 'tefasz' or 'tefasz2':
    pass
# ?
print(f'a kezedben {personhand} van aminek az értéke {ph}. A dealer kezében pedig {dealerhand} van aminek az értéke {dh} ')
valasz = ''
while valasz.capitalize() != 'N':
    valasz = input('akarod folytatni (I/N)')
    if valasz.capitalize() == 'I':
        personhand2 = random.choice(list(deck))
        ph += deck.get(personhand2)
        deck.pop(personhand2)
        dealerhand2 = random.choice(list(deck))
        dh += deck.get(dealerhand2)
        deck.pop(dealerhand2)
    else:
        break
    if ph > 21:
        break
    elif dh > ph and dh <= 21 or ph > 21 and dh <= 21:
        print('A dealer nyert')
    elif dh == ph and dh <= 21:
        print('döntetlen')
    elif dh and ph > 21:
        print('Mind a ketten vesztettetek')
    else:
        print('NYERTÉL')
        break
    print(f'a kezedben {personhand} es egy {personhand2} van amiknek az értéke {ph}. A dealer kezében {dealerhand} és egy {dealerhand2} van, aminek az értéke {dh}')
    valasz = input('Akarod folytatni a játékot? (I/N)')
    if valasz.capitalize() == 'I':
        personhand3 = random.choice(list(deck))
        ph += deck.get(personhand3)
        deck.pop(personhand3)
        dealerhand3 = random.choice(list(deck))
        dh += deck.get(dealerhand3)
        deck.pop(dealerhand3)
        print(f'A kezedben {personhand}, {personhand2}, és egy {personhand3} van aminek az értéke {ph}. A dealer kezében egy {dealerhand}, {dealerhand2} és egy {dealerhand3} van. Az ő értéke {dh}.')
if dh > ph and dh <= 21 or ph > 21 and dh <= 21:
    print('A dealer nyert')
elif dh == ph and dh <= 21:
    print('döntetlen')
elif dh and ph > 21:
    print('Mind a ketten vesztettetek')
else:
    print('NYERTÉL')
