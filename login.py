# ============================
# Secure Login Simulation
# Uso educacional
# ============================

# Credenciais corretas (simulação)
USUARIO_CORRETO = "admin"
SENHA_CORRETA = "admin123"

# Número máximo de tentativas
tentativas = 3

def registrar_log(mensagem):
    """
    Simula o registro de eventos de segurança
    """
    print(f"[LOG] {mensagem}")

# Loop principal de login
while tentativas > 0:
    try:
        # Simulando entrada do usuário
        usuario = "admin"
        senha = "1234"  # senha errada propositalmente

        # Verificação de credenciais
        if usuario == USUARIO_CORRETO and senha == SENHA_CORRETA:
            print("Login autorizado")
            registrar_log("Login realizado com sucesso")
            break
        else:
            tentativas -= 1
            print(f"Tentativas restantes: {tentativas}")
            registrar_log("Falha de login")

    except Exception as erro:
        # Tratamento de erro inesperado
        registrar_log(f"Erro inesperado: {erro}")

# Se todas as tentativas forem usadas
if tentativas == 0:
    print("Conta bloqueada")
    registrar_log("Conta bloqueada por excesso de tentativas")
