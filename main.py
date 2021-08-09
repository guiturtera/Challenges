print("Bruteforce")
print("Available char - a-z")# 97 - 122


def replace_str_index(text,index=0,replacement=''):
    return '%s%s%s'%(text[:index],replacement,text[index+1:])

def change_string_positions(simulated_passoword):
    startLength = len(simulated_passoword) - 1
    for i in range(startLength, -1, -1):
        current_char_number = ord(simulated_passoword[i])
        if current_char_number == 122 and i == 0:
            return True, ""
        elif current_char_number == 122:
            simulated_passoword = replace_str_index(simulated_passoword, i, chr(97))
        elif current_char_number > 96 and current_char_number < 122:
            return False, replace_str_index(simulated_passoword, i, chr(current_char_number + 1))
        else:
            raise Exception("INVALID PASSWORD!")


def check_all_keys(number_of_chars, password):
    simulated_password = chr(97) * number_of_chars
    final_index = number_of_chars - 1
    print(f"checking {number_of_chars}...")
    while True:
        print(simulated_password)
        if simulated_password == password:
            return True, simulated_password 
        #elif current_index == 0 and simulated_password[0] == 'z':
        #    print(f'did not found with {number_of_chars}')
        #    return False, ""
        else:
            finished, simulated_password = change_string_positions(simulated_password)
            if finished:
                return False, ''

def bute_force(password):   
    x = 0
    while True:
        x+= 1
        exists, key = check_all_keys(x, password)
        if exists:
            print(f'password found! {key}')
            return
        '''for index in range(26):
            senhaSimulada = replace_str_index(senhaSimulada, i, chr(97 + index))
            print(senhaSimulada)
            if senhaSimulada == keyword:
                print(f'senha é \"{senhaSimulada}\"')
                return'''

validated = False
while not validated:
    senha = str(input("insira uma senha\n"))
    if len(senha) > 0:
        validated = True
    else:
        print('write a keyword with atleast one character!')

bute_force(senha)

