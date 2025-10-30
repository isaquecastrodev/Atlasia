# main.py
"""Entrada opcional para rodar o motor localmente."""
from core.engine import handle_user_input

def repl():
    print("AtlasAI - modo REPL. Digite 'exit' para sair.")
    while True:
        cmd = input('> ')
        if cmd.lower() in ('exit', 'quit', 'sair'):
            break
        r = handle_user_input(cmd)
        print(r)

if __name__ == '__main__':
    repl()
