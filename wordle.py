class Wordle:
    def __init__(self, answer, guesses = {k:[] for k in range(5)}, current = []):
        self.answer = answer
        self.guesses = guesses
        self.current = current
    
    def guess(self, number):
        print('')
        self.current = []
        attempt = input('What is your guess?')
        for i in range(5):
            if attempt[i] == self.answer[i]:
                self.guesses[number].append((attempt[i], 'green'))
                self.current.append('green')
            elif attempt[i] in self.answer:
                self.guesses[number].append((attempt[i], 'yellow'))
                self.current.append('yellow')
            else:
                self.guesses[number].append((attempt[i], 'black'))
                self.current.append('black')
        print(self.guesses)

    def printAnswers(self, turn):
        print('\nHere were your guesses...')
        for i in range (5):
            print(self.guesses[turn][i][1], end = ' ')
        print(' ')
        for i in range (5):
            print(self.guesses[turn][i][0], end = '      ')
        print('')
    def validate(self):
        if 'yellow' not in self.current and 'black' not in self.current:
            return True
        return False


def run():
    word = input('Enter a 5 letter word to start: ')
    while len(word) != 5:
        word = input('Please enter a 5 letter word: ')
    test = Wordle(word)
    for i in range(6):
        test.guess(i)
        test.printAnswers(i)
        if test.validate():
            return f'You won! The word was {test.answer}'
    return f'Sorry, you lost! Word was {test.answer}'

print(run())