import random

class hangman:
    word_list = ["awkward","bagpipes","banjo","bungler","croquet","crypt","dwarves","fervid","fishhook","fjord","gazebo","gypsy","haiku","haphazard","hyphen","ivory","jazzy","jiffy","jinx","jukebox","kayak","kiosk","klutz","memento","mystify","numbskull","ostracize","oxygen","pajama","phlegm","pixel","polka","quad","quip","rhythmic","rogue","sphinx","squawk","swivel","toady","twelfth","unzip","waxy","wildebeest","yacht","zealous","zigzag","zippy","zombie"]
    HANGMANPICS = ['''
       +---+

       |   |

           |

           |

           |

           |

     =========''', '''

       +---+

       |   |

       O   |

           |

           |

           |

     =========''', '''

       +---+

       |   |

       O   |

       |   |

           |

           |

     =========''', '''

       +---+

       |   |

       O   |

      /|   |

           |

           |

     =========''', '''

       +---+

       |   |

       O   |

      /|\  |

           |

           |

     =========''', '''

       +---+

       |   |

       O   |

      /|\  |

      /    |

           |

     =========''', '''

       +---+

       |   |

       O   |

      /|\  |

      / \  |

           |

    =========''']

    def __init__(self,word):
        self.score = 0
        self.word = list(word)
        self.output = ["_"]*len(word)
        self.counter = 0
        self.stored_index = []
        print (self.word)

    def calculate(self,letter):
        if letter in self.word:
            array = [pos for pos, char in enumerate(self.word) if char == letter]
            for i in array:
                self.output[i] = self.word[i]
            print ("".join(self.output))
            return True
        else:
            print (self.HANGMANPICS[self.counter])
            if self.counter == 6:
                print ("Sorry you loose. The correct word was %s" % "".join(self.word))
            return False

    def get_input(self):
        while True:
            guess = input()
            guess = guess.lower()
            if len(guess) != 1:
                print('Please enter a single letter.')
                continue
            elif guess not in 'abcdefghijklmnopqrstuvwxyz':
                print('Please enter a LETTER.')
                continue
            else:
                break
        return guess

    def play(self):
        while (self.counter <= 6):
            print("Please enter your letter \n")
            n = self.get_input()
            if n in self.stored_index:
                print ("Sorry you guessed it already \n")
                continue
            returns = self.calculate(n)
            if returns == True:
                if (self.output == self.word):
                    print("Congratulations, you won \n")
                    break
                else:
                    self.stored_index.append(n)
                    continue
            self.stored_index.append(n)
            self.counter += 1
        self.stored_index = []

if __name__ == "__main__":
    while True:
        print ("Welcome to Hangman. Please enter your letter to begin \n")
        abc = hangman(random.choice(hangman.word_list))
        abc.play()
        print ("Do you want to play again? y/n? \n")
        choice = input()
        if choice == "y":
            continue
        else:
            break

