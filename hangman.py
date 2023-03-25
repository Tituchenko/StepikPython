import random
word_list=["березка","стол","солнце","небо","звезды","удача","волшебник","питон","колдун","гвоздь","яблоко"]

def get_word():
    return random.choice(word_list).upper()

# функция получения текущего состояния
def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]

def play(word):
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False  # сигнальная метка
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6  # количество попыток
    print ("Давайте играть в угадайку слов!")
    while (tries>0):
        print (display_hangman(tries))
        print (word_completion)
        print ("Введите букву или слово")
        s=input().upper()
        if len(s)>1:
            if (s!=word):
                if s in guessed_words:
                    print ("Это слово уже было")
                else:
                    guessed_words.append(s)
                    print ("Не угадал")
                    tries-=1
            else:
                print ("Ты выиграл!")
                break
        else:
            if s in guessed_letters:
                print ("Такая буква была!")
            else:
                if s in word:
                    for i,c in enumerate(word):
                        if c==s:
                            word_completion=word_completion[:i]+c+word_completion[i+1:]
                else:
                    guessed_letters.append(s)
                    tries-=1
    else:
        print ("Ты проиграл")
        print(f"Слово:{word}")

        print (display_hangman(tries))

play(get_word())