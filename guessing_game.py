import random

def is_valid(str: str,max:int)->bool:
    if str.isdigit():
        if 1<=int(str)<=100:
            return True
    return False

num=random.randint(1,100)
print('Добро пожаловать в числовую угадайку')
print ('Введите правую границу:')
max=0
while True:
    max=input()
    if max.isdigit():
        max=int(max)
        if max>1:
            break

print ('Введите число:')
count_try=0
while True:
    count_try +=1
    while True:
        num_str=input()
        if is_valid(num_str,max):
            num_user=int(num_str)
            break
        else:
            print(f'А может быть все-таки введем целое число от 1 до {max}?')
    if num_user==num:
        print (f'Вы угадали, поздравляем! (попыток:{count_try})')
        print ('Сыграем еще?(y/n)')
        answer_user=''
        while answer_user not in ['y','n']:
            answer_user=input()
        if answer_user=='n':
            break
        else:
            num = random.randint(1, 100)
            print('Введите число:')
            count_try = 0
    elif num>num_user:
        print('Ваше число меньше загаданного, попробуйте еще')
    else:
        print('Ваше число больше загаданного, попробуйте еще')
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')