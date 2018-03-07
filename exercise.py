from random import choice, shuffle

"""Exercise 1"""
def avg_of_odds(numbers):
    total=0
    count=0
    for number in numbers:
        if number%2!=0:
            total+=number
            count+=1
    return float(total/count)



"""Exercise 2"""

def text_encode(text):
    alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y', 'z']
    text=text.lower()
    new_text=[]
    for letter in text:
        if letter in alphabet:
            counter=text.count(letter)
            break

    for letter in text:
        for index, item in enumerate(alphabet):
            if letter==item:
                new_index=index+counter
                while new_index>=26:
                    new_index-=26
                new_text.append(alphabet[new_index])
                break
        else:
            new_text.append(letter)

    return ("".join(new_text))



""" Exercise 3 """

class Card():
    def __init__(self, color, value):
        self.color=color
        self.value=value
        self.card=str(self.value) + " " + str(self.color)



class Deck():

    def __init__(self, number):

        self.number=number #Number of the cards given by the user
        self.deckpack=""   #This is the string representation of the Deck Class
        self.new_pack=[]    #This is the card pack constructed based on the given number

        #Below we create the attribute deckpack
        Deck.items=[]
        if self.number%4!= 0:
            remainder=self.number%4
            for i in range(4):
                if remainder>0:
                    Deck.items.append(self.number//4+1)
                    remainder-=1
                else:
                    Deck.items.append(number//4)
        else:
            for i in range(4):
                Deck.items.append(self.number//4)

        self.deckpack =str(self.number)+ " cards - " + str(Deck.items[0])+" Clubs, " +str(Deck.items[1]) + " Diamonds, "+str(Deck.items[2])+ " Hearts, " + str(Deck.items[3])+ " Spades "


    def generate_pack(self):
        #This function allow us to modify the pack whenever we draw a card.
        Deck.items=[]
        if self.number%4!= 0:
            remainder=self.number%4

            for i in range(4):
                if remainder>0:
                    Deck.items.append(self.number//4+1)
                    remainder-=1
                else:
                    Deck.items.append(self.number//4)
        else:
            for i in range(4):
                Deck.items.append(self.number//4)

        self.deckpack =str(self.number)+ " cards - " + str(Deck.items[0])+" Clubs, " +str(Deck.items[1]) + " Diamonds, "+str(Deck.items[2])+ " Hearts, " + str(Deck.items[3])+ " Spades "

        return self.deckpack


    def create_pack(self):
        #This function creates the actual card deck
        pack={"Clubs":[], "Diamonds":[], "Hearts":[], "Spades":[]}

        for color in pack.keys():
            a=["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King" ]
            index=0
            for card in range(Deck.items[index]):
                pick=choice(a)
                pack[color].append(pick)
                a.remove(pick)
                index+=1

        for k in pack.keys():
            for i in range(len(pack[k])):
                self.new_pack.append(Card(k,pack[k][i]).card)
        return self.new_pack

    def shuffle_cards(self):
        #This function shuffles the deck
        cards=Deck.create_pack(self)
        shuffle(cards)
        return cards

    def drawn(self):
        #This function is for drawing a card and then regenerating the card deck
        card_drawn=(self.new_pack[0])
        self.new_pack.remove(card_drawn)
        self.number-=1
        Deck.generate_pack(self)
        return card_drawn




deck=Deck(11)
print(deck.deckpack)
print(deck.shuffle_cards())
print(deck.drawn())
print(deck.deckpack)
