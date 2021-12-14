# kell: deck(dictionary) kartya value
# kell egy list a handben levo kartyaknak
#  oszto def ami ki is veszi a kartyat a deckbol es bele teszi a handbe 
#  kell egy fugveny ami megmeri a kartya erteket es megnezi hogy nem tobb e 21 nél --> ha tobb akkor print vege es futtassa ujra 
# EZ AZ EGESZ PEDIG EGY WHILE LOOPBA KENE HOGY FUSSON 

# import random




import random


class Black_Jack():
    def __init__(self,name, value):
        self.name = name 
        self.value = value
        

tref2 = Black_Jack('tref2',2)
tref3 = Black_Jack('tref3',3)
tref4 = Black_Jack('tref4',4)
tref5 = Black_Jack('tref5',5)
tref6 = Black_Jack('tref6',6)
tref7 = Black_Jack('tref7',7)
tref8 = Black_Jack('tref8',8)
tref9 = Black_Jack('tref9',9)
tref10 = Black_Jack('tref10',10)
trefjubi = Black_Jack('tref jubi',10)
trefdama = Black_Jack('tref dáma',10)
trefkiraly = Black_Jack('tref király',10)
trefasz = Black_Jack('tref ász',10)


deck = [tref2, tref3, tref4, tref5, tref6, tref7, tref8, tref9, tref10, trefjubi ,trefkiraly, trefdama, trefasz]

dealerhand = random.choice(deck)
personhand = random.choice(deck)
pv = int(list((personhand.value)))
dv = int(list((dealerhand.value)))
print(f'a kezedben {personhand.name} van aminek az értéke {personhand.value}. A dealer kezében pedig {dealerhand.name} van aminek az értéke {dealerhand.value} ')
input('akarod folytatni (I/N)')
if input == 'I':
    pv = pv + personhand.value
print(pv)
    
    













# hozaado = random.choice(deck)
# hand.append(hozaado)


# import random

# deck_dictionari = {
#     'tref2' : 2,
#     'tref3' : 3,
#     'tref4' : 4,
#     'tref5' : 5,
#     'tref6' : 6,
#     'tref7' : 7,
#     'tref8' : 8,
#     'tref9' : 9,
#     'tref10' : 10,
#     'trefjubi' : 10,
#     'trefdama' : 10,
#     'trefkiraly' : 10,
#     'trefasz' : 10,
# }



# hand = []

# deck_list = list(deck_dictionari.items())

# adding = hand.append(random.choice(deck_list))

# with open('jatekos pontok.txt', 'w') as file:
#     iras = str(hand) 
#     line1 = file.write(iras)
    



# # print(line1)
# hand = []
# while input('játék kezdete'):
#     if input('elsolap') == True:
#         kartya = random.choice(list(deck_dictionari.items()))
#         hand.append(kartya)
#     input(f"a kartyaid szama{hand}, akarsz tovabb menni?")
#     if input == 'nem':
#         print(f'a végeredményed {hand}')
#     else:
#         input('akarsz még játszani?')
#     exit




