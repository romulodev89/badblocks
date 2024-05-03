#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Romulo Pavanello
Script para verificar setores defeituosos (bad blocks) em um disco rígido
"""

import subprocess
import sys

def verificar_badblocks(device):
    # Verificar se o script está sendo executado como root
    if not subprocess.check_call(['id', '-u']) == 0:
        print("Este script precisa ser executado como root")
        sys.exit(1)

    # Verificar se o argumento (caminho do dispositivo) foi fornecido
    if len(device) == 0:
        print("Uso: {} <caminho_do_dispositivo>".format(sys.argv[0]))
        sys.exit(1)

    print("Iniciando verificação de setores defeituosos...\n")

    # Executar badblocks com opções de verificação
    comando = ["badblocks", "-sv", "-c", "1024", device]
    resultado = subprocess.run(comando)

    print("\nVerificação de setores defeituosos concluída.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: {} <caminho_do_dispositivo>".format(sys.argv[0]))
        sys.exit(1)
    
    verificar_badblocks(sys.argv[1])
