#!/usr/bin/env python3

import subprocess
import sys

COMPOSE_FILE = "compose.yaml"

def run(comando):

    try:
        subprocess.run(comando, check=True)
    except subprocess.CalledProcessError:
        print("Erro de execução:", " ").join(comando)
        sys.exit(1)

def criar():
    print("[+] Construindo imagens...")
    run(["docker", "compose", "-f", COMPOSE_FILE, "build"])
    print("[+] Subindo serviços...")
    run(["docker", "compose", "-f", COMPOSE_FILE, "up", "-d"])

def iniciar():
    print('[+] Iniciando os serviços...')
    run(["docker", "compose", "-f", COMPOSE_FILE, "start"])

def parar():
    print('[+] Parando os serviços...')
    run(["docker", "compose", "-f", COMPOSE_FILE, "stop"])

def excluir():
    print('[+] Excluindo os serviços...')
    run(["docker", "compose", "-f", COMPOSE_FILE, "down"])

def logs():
    print("[+] Executando os logs dos serviços...")
    run(["docker", "compose", "-f", COMPOSE_FILE, "logs", "-f"])

def reiniciar():
    print('[+] Reiniciando todos os serviços...')
    run(["docker", "compose", "-f", COMPOSE_FILE, "restart"])

def uso():
    print('Uso: python script.py {criar|iniciar|parar|excluir|logs|reiniciar}')
    sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        uso()

    comando = sys.argv[1]

    if comando == "criar":
        criar()
    elif comando == "iniciar":
        iniciar()
    elif comando == "parar":
        parar()
    elif comando == "excluir":
        excluir()
    elif comando == "logs":
        logs()
    elif comando == "reiniciar":
        reiniciar()
    else:
        uso()