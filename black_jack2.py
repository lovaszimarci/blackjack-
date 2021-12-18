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
#a personhand kivalaszt egy random lapot a personnak a deckbol
personhand = random.choice(list(deck))
# ph a personhand erteke int be 
ph = []
# a dealerhand kivalaszt egy random lapot a dealernek a deckbol
dealerhand = random.choice(list(deck))
# a dh a dealerhand erteke intben 
dh =  []




# ez a function kiosztja a lapokat
def osztas():
    # hozza adja a ph hoz a pershonhand erteket
    ph.append(deck.get(personhand))
    #kiveszi a deckbol a person lapjat
    deck.pop(personhand)
    #ugyanez a dealerrel 
    dh.append(deck.get(dealerhand))
    deck.pop(dealerhand)
    return None


# kiijra a pontszamokat
def printpontszamok():
    return print(f'a húzott lap {dealerhand}, a lapjaid összege {ph}')







# ha nem akarsz jatszani vagy pontszamod 21 fole megy akkor megmondja hogy ki nyert 
def osszegzes():
    if sum(ph) and sum(dh) > 21:
        print('Mind a ketten veszetettek')
    elif sum(ph) < 21 and sum(dh) > 21:
        print('te nyertél')
    elif sum(dh) < 21 and sum(ph) > 21:
        print('A dealer nyert')
    elif ph == 21:
        print('blackjack!')
    return None





# megkerdezi egy inputtal hogy akarsz e jatszani
def akarszjatszanikerdojel():
    input('Akarsz tobább játszani?')
    if input == 'n':
        osszegzes()
    elif input == 'n':
        osztas()


def game():
    print('welcome to blackjack!')
    input("akarszjatszani?")
    while input == 'i':
        osztas()
        printpontszamok()
        akarszjatszanikerdojel()
    osszegzes()

    


game()