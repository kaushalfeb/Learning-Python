import random

class Deck():
    def __init__(self):
        self.cards = {
            'King of Club':10,'Queen of Club':10,'Jack of Club':10,'Ace of Club':1,'2 of Club':2,'3 of Club':3,'4 of Club':4,'5 of Club':5,'6 of Club':6,'7 of Club':7,'8 of Club':8,'9 of Club':9,'10 of Club':10,
            'King of Spade':10,'Queen of Spade':10,'Jack of Spade':10,'Ace of Spade':1,'2 of Spade':2,'3 of Spade':3,'4 of Spade':4,'5 of Spade':5,'6 of Spade':6,'7 of Spade':7,'8 of Spade':8,'9 of Spade':9,'10 of Spade':10,
            'King of Diamond':10,'Queen of Diamond':10,'Jack of Diamond':10,'Ace of Diamond':1,'2 of Diamond':2,'3 of Diamond':3,'4 of Diamond':4,'5 of Diamond':5,'6 of Diamond':6,'7 of Diamond':7,'8 of Diamond':8,'9 of Diamond':9,'10 of Diamond':10,
            'King of Heart':10,'Queen of Heart':10,'Jack of Heart':10,'Ace of Heart':1,'2 of Heart':2,'3 of Heart':3,'4 of Heart':4,'5 of Heart':5,'6 of Heart':6,'7 of Heart':7,'8 of Heart':8,'9 of Heart':9,'10 of Heart':10
                     }
        
    def get_card(self):
        name_of_cards = list(self.cards.keys()) 
        opted_card = random.choice(name_of_cards)
        val = self.cards[opted_card] # store the opted card into a variable
        self.cards.pop(opted_card) # Delete the card from deck to maintain accuracy in gameplay
        
        return opted_card,val

class Player(Deck):
    bankroll = 100
    d = Deck()
    pcards = {}
    
    def __init__(self):
            pass
        
    def carder(self):      
        #Pull two cards from deck and store in Player's collection 
        
        card_1 = self.d.get_card()
        card_2 = self.d.get_card()
        
        self.pcards[card_1[0]] = card_1[1]
        self.pcards[card_2[0]] = card_2[1]
       
    def hit(self):
    
        #Pull another card from deck and put in pcards
    
        card_3 = self.d.get_card()
        self.pcards[card_3[0]] = card_3[1]
        print(card_3[0])
        
    def stay(self):
        pass #do nothing
    
    def show_balance(self):
        print(f"You have ${self.bankroll} in your bankroll")
    
    def show_cards(self):
        sel_car = []
        for key in self.pcards.keys():
            sel_car.append(key)
        return sel_car

    def points(self):
        p_total =0
        for val in self.pcards.values():
            p_total = p_total + val
        return p_total

class Dealer(Deck):
    d = Deck()
    d_cards = {}
    
    def __init__(self):
        pass

    def carder(self):
        #Pull two cards from deck and store in Dealer's collection 
        
        card_1 = self.d.get_card()
        card_2 = self.d.get_card()
        
        self.d_cards[card_1[0]] = card_1[1]
        self.d_cards[card_2[0]] = card_2[1]
    
    def hit(self):
    
        #Pull another card from deck and put in d_cards
    
        card_3 = self.d.get_card()
        self.d_cards[card_3[0]] = card_3[1]
        print(card_3[0])
    
    def show_cards(self):
        sel_car = []
        for key in self.d_cards.keys():
            sel_car.append(key)
        return sel_car
        
    def stay(self):
        pass

    def points(self):
        d_total =0
        for val in self.d_cards.values():
            d_total = d_total + val
        return d_total

class Gameplay():
        
    def game(self):
        
        self.alan = Player()
        self.enigma = Dealer()
        self.ch_points = 0
        self.en_points = 0
        self.alan.carder()
        self.enigma.carder()
        self.flag = True

        print('\nWelcome to BlackJack game \n\nPlayer 1 goes first\n')
       
        while True:
            print(f'Player 1 you have\n{self.alan.show_cards()}\n')
            try:
                ans = int(input('Player Do you want to Hit or Stay\n1.Hit \n2.Stay\n3.End Game\n'))
            except:
                print('Choose 1 or 2')
                continue
            
            if ans == 1:
                self.alan.hit()
                self.ch_points = self.alan.points() 
                print(f"Player 1 points are {self.ch_points}")
               
               # Check whether points exceed the limit
                
                if self.ch_points == 21:
                    print("Player won")
                    self.flag = False
                    break
                elif self.ch_points > 21:
                    print("Player Busted\nComputer Won!")
                    self.flag = False
                    break
                continue


            elif ans == 2:
                print(f"Player 1 points are {self.alan.points()}")
                self.alan.stay()
                break
            elif ans == 3:
                self.flag = False
                break
            else:
                print('Wrong Input')
                continue
            
        print("\nIt is now Enigma's turn\n")
        
        while self.flag:
            
            print(f'Computer you have\n{self.enigma.show_cards()}\n')
            
            try:
                ans = int(input('Computer Do you want to Hit or Stay\n1.Hit \n2.Stay\n3.End Game\n'))
            except:
                print('Choose 1 or 2')
                continue
            
            #Check whether computer is already leading
            if self.en_points > self.ch_points:
                print("\nComputer won")
                break


            if ans == 1:
                self.enigma.hit()
               
                self.en_points = self.enigma.points() 
                print(f"Computer points are {self.en_points}")
               
               # Check whether points exceed the limit
                if self.en_points > 21 :
                    print("\nComputer Busted\nPlayer won!")
                    break
                continue

            elif ans == 2:
                print(f"computer points are {self.enigma.points()}")
                self.enigma.stay()
                if self.en_points < self.ch_points:
                    print("\nComputer busted\tPlayer Won")
                
                else:
                    print("Computer won")
                break

            elif ans == 3:
                break
            else:
                print('Wrong Input')
                continue
        
        print('Game is Over')
        
g = Gameplay()
g.game()