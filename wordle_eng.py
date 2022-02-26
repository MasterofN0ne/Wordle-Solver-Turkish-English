class Wordle:
    def __init__(self):
        self.wordlist = [] #List we remove elements from
        with open('wordle_eng.txt') as f:
            for line in f:
                line.strip()
                line.lower()
                actual_line = line.split()

                if len(actual_line) > 1:
                    pass

                if len(line) == 6:
                    self.wordlist.append(line.strip())

        self.word_tuple = tuple(self.wordlist) #We wouldn't wanna remove elements from the list we iterate 
    
    def solver(self):
        counter = 5
        color_letters = {} #to eliminate the letters we used before we will store the letters which we mark them 'green, yellow, red'
        color_letters['g'] = []
        color_letters['y'] = []
        color_letters['r'] = []
        seen_words = set()
        

        while counter > 0:
            word = input('Kelime: ')
            colors = input('Renk kombinasyonu: ')

            

            for i in range(5): #Creating the dictionary
                if colors[i] == 'g':
                    if word[i] in seen_words:
                        continue
                    else:
                        color_letters['g'].append((i,word[i]))
                        seen_words.add(word[i])

                if colors[i] == 'y':
                    if word[i] in seen_words:
                        continue
                    else:
                        color_letters['y'].append((i,word[i]))
                        seen_words.add(word[i])

                if colors[i] == 'r':
                    if word[i] in seen_words:
                        continue
                    else:
                        color_letters['r'].append((i,word[i]))
                        seen_words.add(word[i])

            for w in self.word_tuple:
                w = w.lower()
                for key in color_letters.keys():
                    if color_letters[key] != []:
                        if key == 'g':
                            for index, letter in color_letters['g']: #color_letters['g'] = [(1,'a'),(2,'b'),(3,'c')]
                                if w[index] != letter and w in self.wordlist: # after the and part we want to check again if the word still in wordlist 
                                    self.wordlist.remove(w) # if we don't check program will try to remove the same word 
                                    break

                        if key == 'r':
                            for index, letter in color_letters['r']:
                                if letter in w and w in self.wordlist:
                                    self.wordlist.remove(w)
                                    break
                        
                        if key == 'y':
                            for index, letter in color_letters['y']:
                                if w[index] == letter and w in self.wordlist:
                                    self.wordlist.remove(w)
                                    break
                                elif letter not in w and w in self.wordlist:
                                    self.wordlist.remove(w)
                                    break
            
            print(self.wordlist)

            counter -= 1 

    

    # def another_solver(self):
    #     for i in range(5):
    #         word = input('Word: ')
    #         colors = input('Color combination: ')
    #         for w in self.word_tuple:
    #             for i in range(5):
    #                 if colors[i] == 'r' and word[i] in w:
    #                     self.wordlist.remove(w)
    #                     break

    #                 elif colors[i] == 'g' and word[i] != w[i]:
    #                     self.wordlist.remove(w)
    #                     break

    #                 elif colors[i] == 'y' and word[i] not in w:
    #                     self.wordlist.remove(w)
    #                     break

    #                 elif colors[i] == 'y' and word[i] == w[i]:
    #                     self.wordlist.remove(w)
    #                     break
    #         return self.wordlist


def wordle_eng_runner():
    w = Wordle()
    w.solver()



        



        