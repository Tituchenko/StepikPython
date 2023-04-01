def translate_pos_sys (number,system):
    letters={"A":10,"B":11,"C":12,"D":13,"E":14,"F":15}
    result=0
    max_pow=len(number)-1
    for c in number:
        if c in letters.keys():
            cur_num=letters[c]
        else:
            cur_num=int(c)
        result+=cur_num*system**max_pow
        max_pow-=1
    return result

def translate_form10 (number,system):
    result=""
    letters = {10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"}
    while number!=0:
        cur_result=number%system
        if cur_result in letters.keys():
            result+=letters[cur_result]
        else:
            result+=str(cur_result)

        number=number//system
    return result[::-1]


def boh(number):
    b=bin(number)[2:]
    o=oct(number)[2:]
    h=hex(number)[2:].upper()
    print (b,o,h,sep="\n")

boh (int(input()))