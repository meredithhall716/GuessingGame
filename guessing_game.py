class GuessingGame:  

    def __init__(self, answer_number):
        self.answer_number = 10
        self.is_solved = False
   
    def guess(self, user_guess):
        if user_guess == self.answer_number:
            self.is_solved = True
            return 'correct'
        elif user_guess < self.answer_number:
            return 'low'
        else: return 'high'
    
    def solved(self):
        return self.is_solved
    
game = GuessingGame(10)

print(game.guess(10))