import re

def coleta_logs():
    logs = """
    2023-10-15 14:23:45 - INFO - Usuário "joao123" fez login com sucesso.
    2023-10-15 14:24:00 - INFO - Usuário "joao123" fez logout com sucesso.
    2023-10-15 14:24:10 - ERROR - Falha ao conectar ao banco de dados.
    2023-10-15 14:25:00 - INFO - Usuário "maria456" fez login com sucesso.
    2023-10-15 14:25:30 - INFO - Usuário "maria456" fez logout com sucesso.
    2023-10-15 14:30:00 - WARNING - Disco quase cheio.
    2023-10-15 14:35:00 - INFO - Usuário "admin" fez login com sucesso.
    2023-10-15 14:35:30 - INFO - Usuário "admin" fez logout com sucesso.
    2023-10-15 14:40:00 - ERROR - Tentativa de login falhou para "hacker".
    2023-10-15 14:46:00 - CRITICAL - Servidor fora do ar.
    """
    with open("log.txt", "w") as file:
        file.write(logs)
    print("Logs coletados e salvos em 'log.txt'.")

# Outras funções (ingestao, pre_processamento, etc.) devem estar definidas aqui
# Para simplificar, vou assumir que elas existem e funcionam

def valida_automato_pilha(logs):
    # Simula uma pilha para validar correspondência de login/logout
    pilha = []
    padrao_login = r"INFO - Usuário \"[a-zA-Z0-9]+\" fez login"
    padrao_logout = r"INFO - Usuário \"[a-zA-Z0-9]+\" fez logout"
    
    for linha in logs.splitlines():
        if re.search(padrao_login, linha):
            match = re.search(r"\"(.+?)\"", linha)
            if match:
                usuario = match.group(1)
                pilha.append(usuario)
                print(f"Empilhando: {usuario}")
            else:
                print(f"Erro: Não foi possível extrair usuário de '{linha}'")
        elif re.search(padrao_logout, linha):
            match = re.search(r"\"(.+?)\"", linha)
            if match:
                usuario = match.group(1)
                if pilha and pilha[-1] == usuario:
                    pilha.pop()
                    print(f"Desempilhando: {usuario}")
                else:
                    print(f"Erro: Logout de {usuario} sem login correspondente")
            else:
                print(f"Erro: Não foi possível extrair usuário de '{linha}'")
    
    if not pilha:
        print("Validação com autômato de pilha: Todos os logins têm logout correspondente.")
        return True
    else:
        print(f"Erro: {len(pilha)} login(s) sem logout correspondente: {pilha}")
        return False

# Função main
def main():
    coleta_logs()
    # Aqui você chamaria as outras funções (ingestao, pre_processamento, etc.)
    # Para testar só a validação, vamos focar nela por enquanto
    with open("log.txt", "r") as file:
        logs = file.read()
    valida_automato_pilha(logs)

if __name__ == "__main__":
    main()