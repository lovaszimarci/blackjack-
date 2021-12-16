import random


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
print(f'a kezedben {personhand} van aminek az értéke {ph}. A dealer kezében pedig {dealerhand} van aminek az értéke {dh} ')
valasz = ''


while ph or dh < 21:
    valasz = input('akarod folytatni (I/N)')
    if valasz.capitalize == 'I':
        personhand = random.choice(list(deck))
        ph += deck.get(personhand)
        deck.pop(personhand)
        dealerhand = random.choice(list(deck))
        dh += deck.get(dealerhand)
        deck.pop(dealerhand)
        print(f' {personhand} et húztál. Az össz érték {ph}. A dealer {dealerhand} et húzott. A dealer értéke {dh} ')
    elif ph > 21 and dh < 21:
        print('A dealer nyert')
    elif dh > 21 and ph < 21:
        print('Te nyertél')
    elif dh == ph and ph and dh > 21:
        print('döntetlen')




   
   


