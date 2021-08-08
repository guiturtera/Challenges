print("Bruteforce")
print("Available char - 97 - 122")# 97 - 122

def bute_force(keyword):   
    senhaSimulada = ""
    x = 0
    while True:
        x+= 1
        senhaSimulada = ""
        for i in range(x):
            senhaSimulada += "a"

        for length in range(x):
            charNum = x - 1
            
            for index in range(26):
                senhaSimulada = replace_str_index(senhaSimulada, length, chr(97 + index))
                print(senhaSimulada)
                if senhaSimulada == keyword:
                    print(f'senha é \"{senhaSimulada}\"')
                    return

def replace_str_index(text,index=0,replacement=''):
    return '%s%s%s'%(text[:index],replacement,text[index+1:])

senha = str(input("insira uma senha\n"))
bute_force(senha)

