# Генерация пароля
import random

def get_int(text):
    print (text)
    result=""
    while (not result.isdigit()):
        result=input()
        if not result.isdigit():
            print ("Введите число!")
    return int(result)

def get_boolean(text):
    print (text+" (y/n)")
    result=""
    while (not result.lower() in ['y','n']):
        result=input()
        if (not result.lower() in ['y','n']):
            print ("Введите 'y' или 'n'")
    return result.lower()=='y'

def generate_password(length,chars):
    password=""
    for i in range(length):
        password+=random.choice(chars)
    return password


digits='0123456789'
lowercase_letters='abcdefghijklmnopqrstuvwxyz'
uppercase_letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation='!#$%&*+-=?@^_.'
bad_char='l1Lo0O'
chars=''
# Количество паролей для генерации;
num_pass=get_int("Количество паролей для генерации")
# Длину одного пароля;
len_pass=get_int("Длина пароля")
# Включать ли цифры 0123456789?
has_digit=get_boolean("Включать ли цифры 0123456789?")
# Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?
has_upper=get_boolean("Включать ли буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?")
# Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz?
has_lower=get_boolean("Включать ли буквы abcdefghijklmnopqrstuvwxyz?")
# Включать ли символы !#$%&*+-=?@^_?
has_symbol=get_boolean("Включать ли символы !#$%&*+-=?@^_?")
# Исключать ли неоднозначные символы il1Lo0O?
del_bed_char=get_boolean("Исключать ли неоднозначные символы il1Lo0O?")

if (has_digit):
    chars+=digits
if (has_upper):
    chars+=uppercase_letters
if (has_lower):
    chars+=lowercase_letters
if (has_symbol):
    chars+=punctuation
if (del_bed_char):
    for c in bad_char:
        chars.replace(c,"")

for _ in range(num_pass):
    password=generate_password(len_pass,chars)
    print (password)