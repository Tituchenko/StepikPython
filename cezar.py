# Шифр цезаря

lowercase_letters_eng='abcdefghijklmnopqrstuvwxyz'
uppercase_letters_eng='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

lowercase_letters_rus="абвгдежзийклмнопрстуфхцчшщъыьэюя"
uppercase_letters_rus="АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"



def code (text,key,lowercase_letters,uppercase_letters):
    result=""
    power=len(uppercase_letters)
    for c in text:
        if c in lowercase_letters:
            if (lowercase_letters.index(c)+key)>=0:
                result+=lowercase_letters[(lowercase_letters.index(c)+key)%power]
            else:
                result += lowercase_letters[(lowercase_letters.index(c) + key) % -power]
        elif c in uppercase_letters:
            if (uppercase_letters.index(c) + key)>=0:
                result += uppercase_letters[(uppercase_letters.index(c) + key) % power]
            else:
                result += uppercase_letters[(uppercase_letters.index(c) + key) % -power]
        else:
            result+=c
    return result

def decode (text,key,lowercase_letters,uppercase_letters):
    return code (text,-key,lowercase_letters,uppercase_letters)


def get_user_info(text,aproved_val):
    print (text+" "+str(aproved_val))
    result=""
    while (not result.lower() in aproved_val):
        result=input()
        if (not result.lower() in aproved_val):
            print ("Введите "+aproved_val)
    return result.lower()

def get_int(text):
    print (text)
    result=""
    while (not result.isdigit()):
        result=input()
        if not result.isdigit():
            print ("Введите число!")
    return int(result)

# type=get_user_info("Введите направление", ['code','decode'])
#
# if get_user_info("Введите язык", ['rus','eng'])=='rus':
#     lowercase=lowercase_letters_rus
#     uppercase=uppercase_letters_rus
# else:
#     lowercase = lowercase_letters_eng
#     uppercase = uppercase_letters_eng
#
# key=get_int("Введите ключ")
#
# print ('Введите текст')
# text=input()
#
# if type=='code':
#     print(code(text,key,lowercase,uppercase))
# else:
#     print(decode(text, key, lowercase, uppercase))
#
# for i in range(30):
#     print(decode(text, i, lowercase, uppercase))

def get_key(s,lowercase,uppercase):
    key=0
    for c in s:
        if c in lowercase or c in uppercase:
            key+=1
    return key


text=input()
words=text.split()
result=[]
for word in words:
    result.append(code(word,get_key(word,lowercase_letters_eng,uppercase_letters_eng),lowercase_letters_eng,uppercase_letters_eng))
print (" ".join(result))