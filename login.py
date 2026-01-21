import time
from datetime import datetime

# ============================
# CONFIGURAÇÕES
# ============================

MAX_TENTATIVAS = 3
DELAY_TENTATIVAS = 2
LOG_FILE = "security.log"

# ============================
# BASE DE USUÁRIOS (SIMULADA)
# ============================

usuarios = {
    "admin": {
        "senha": "admin123",
        "tentativas": MAX_TENTATIVAS,
        "bloqueado": False,
        "ip": "10.0.0.1"
    },
    "joao": {
        "senha": "joao123",
        "tentativas": MAX_TENTATIVAS,
        "bloqueado": False,
        "ip": "192.168.1.10"
    }
}

# ============================
# FUNÇÕES DE SEGURANÇA
# ============================

def registrar_log(evento):
    data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as log:
        log.write(f"{data_hora} | {evento}\n")

def alertar_soc(usuario, ip):
    print(f"[ALERTA SOC] Usuário '{usuario}' bloqueado | IP {ip}")
    registrar_log(f"ALERTA SOC | usuario={usuario} ip={ip}")

def autenticar(nome_usuario, senha_digitada):
    # Verifica se o usuário existe
    if nome_usuario not in usuarios:
        registrar_log(f"Tentativa com usuário inexistente: {nome_usuario}")
        return False, "Usuário não encontrado"

    usuario = usuarios[nome_usuario]

    # Verifica se está bloqueado
    if usuario["bloqueado"]:
        return False, "Usuário bloqueado"

   # Verifica senha
    if senha_digitada == usuario["senha"]:
    usuario["tentativas"] = MAX_TENTATIVAS  # reset após sucesso
    registrar_log(f"Login OK | usuario={nome_usuario} ip={usuario['ip']}")
    return True, "Login autorizado"


    # Falha de login
    usuario["tentativas"] -= 1
    registrar_log(
        f"Falha login | usuario={nome_usuario} ip={usuario['ip']} "
        f"tentativas_restantes={usuario['tentativas']}"
    )

    # Bloqueio
    if usuario["tentativas"] == 0:
        usuario["bloqueado"] = True
        registrar_log(
            f"USUÁRIO BLOQUEADO | usuario={nome_usuario} ip={usuario['ip']}"
        )
        alertar_soc(nome_usuario, usuario["ip"])

    return False, "Senha incorreta"

# ============================
# SIMULAÇÃO DE LOGIN
# ============================

print("=== Sistema de Login Seguro (Multiusuário) ===")

# Simulando tentativas
tentativas_simuladas = [
    ("admin", "1234"),
    ("admin", "root"),
    ("admin", "admin123"),
    ("joao", "errada"),
    ("joao", "errada"),
    ("joao", "errada")
]

for nome, senha in tentativas_simuladas:
    sucesso, mensagem = autenticar(nome, senha)
    print(f"[{nome}] {mensagem}")

    if not sucesso:
        time.sleep(DELAY_TENTATIVAS)

print("Sistema finalizado.")
