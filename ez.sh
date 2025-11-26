#!/bin/bash

COMPOSE_FILE="compose.yaml"

case "$1" in

    criar)
        echo "[+] Construindo imagens..."
        docker compose -f $COMPOSE_FILE build
        echo "[+] Subindo serviços..."
        docker compose -f $COMPOSE_FILE up -d
        ;;

    iniciar)
        echo "[+] Iniciando os serviços..."
        docker compose -f $COMPOSE_FILE start
        ;;

    parar)
        echo "[+] Parando os serviços..."
        docker compose -f $COMPOSE_FILE stop
        ;;

    excluir)
        echo "[+] Excluindo os serviços..."
        docker compose -f $COMPOSE_FILE down
        ;;

    logs)
        echo "[+] Exibindo logs..."
        docker compose -f $COMPOSE_FILE logs -f
        ;;
    
    reiniciar)
        echo "[+] Reiniciando serviços..."
        docker compose -f $COMPOSE_FILE restart
        ;;
    
    *)
        echo "Uso: $0 {criar|iniciar|parar|excluir|logs|reiniciar}"
        exit 1
        ;;
esac