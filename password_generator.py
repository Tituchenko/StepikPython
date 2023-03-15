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