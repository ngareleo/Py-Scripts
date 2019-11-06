
import time
from itertools import permutations

def setup():
    passwd = input("Enter password :\t")
    with open('passw-file.txt','a+') as f:
        f.write("\n" + passwd)


def brute_password(password_file,char_limit):
    with open(password_file,'r') as f:
        corredt_passowrd = list(f)[-1]
    #check the password type
    try:
        passwd_int = int(corredt_passowrd) * 0 == 0
    except:
        passwd_int = False
    BRUTE_INT(corredt_passowrd,char_limit) if passwd_int == True else BRTUTE_STR(corredt_passowrd,char_limit)


def BRUTE_INT(passcode,char_limit):#Character limit is 10 Characters
    start = time.clock()

    for i in range(10**char_limit):
        print(f"Attempt == {i}")
        if str(i) == passcode:
            print(f"Paswsord is {i}\nTime taken is {time.clock() - start}")
            result_file = open('result.txt','a')
            result_file.write("\n\nTime taken is " + str(time.clock() - start) +"\nPassword disccovered is " + str(i))
            return 0


def BRTUTE_STR(passcode,char_limit):
    start = time.clock()
    for passwd in range(char_limit):
        all_char_list = []
        for all in range(32,123):
            if all in range(33,48) or all in range(58,64) or all in range(91,97):
                pass
            else:
                all_char_list.append(chr(all))
        for len in range(char_limit):
            for passwd in permutations(all_char_list,len):
                    final_passwd = ""
                    for i in passwd:
                        final_passwd += i
                    print(f"Attempt == {final_passwd}")
                    if str(final_passwd) == passcode:
                        print(f"Password is {final_passwd}\nTime taken is {time.clock() - start}")
                        result_file = open('result.txt','a')
                        result_file.write("\n\nTime taken is " + str(time.clock() - start) +"\nPassword disccovered is " + str(final_passwd))
                        return 0
setup()
brute_password('./passw-file.txt',10)
