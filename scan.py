import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)
print("""
 Luka Coder

    - PORT SCANNER -
      """)
host = input("LÜTFEN İP ADRESİNİ GİRİNİZ : ")
port = int(input("TARATILACAK PORT ADRESİNİ GİRİNİZ : "))
def portScanner(port):
    if s.connect_ex((host, port)):
        print( "BU PORT KAPALI")
    else:
        print("BU PORT AÇIK")
portScanner(port)
