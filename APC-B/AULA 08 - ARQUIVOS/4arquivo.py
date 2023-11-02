def validar_ip(ip):
    ip = ip.split('.')
    print(ip)

    if len(ip) != 4:
        return False
    else:
        for parte in ip:
            if int(parte) < 0 or int(parte) > 255:
                return False
    return True

arquivo = open('dados/4ip.txt')
for linha in arquivo.readlines():
    ip = linha.replace('\n','')
    print(ip, validar_ip(ip))

# print(validar_ip('200.135.80.9'))
# print(validar_ip('200.135.80.9.1'))