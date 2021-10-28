class Atm(object):
    def __init__(self,cardNumber, pinNumber):
        self.cardNumber = cardNumber
        self.pinNumber = pinNumber

    def card(self):
        print("the card number is  " + str(self.cardNumber))

    def pin(self):
        print("the pin number is  " + str(self.pinNumber))

card1= Atm("00112233","6789")
card2= Atm("99887766", "4321")

card1.card()
card1.pin()