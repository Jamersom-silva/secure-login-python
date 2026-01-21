import time
from datetime import datetime

# ============================
# CONFIGURAÇÕES
# ============================

MAX_TENTATIVAS_USUARIO = 3
MAX_TENTATIVAS_IP = 5
DELAY_TENTATIVAS = 2
LOG_FILE = "security.log"

# ============================
# BASE DE USUÁRIOS (SIMULADA)
# ============================

usuarios = {
    "admin": {
        "senha": "admin123",
        "tentativas": MAX_TENTATIVAS_USUARIO,
        "bloqueado": False,
        "ip": "10.0.0.1"
    },
    "joao": {
        "senha": "joao123",
        "tentativas": MAX_TENTATIVAS_USUARIO,
        "bloqueado": False,
        "ip": "10.0.0.1"  # mesmo IP de propósito
    }
}

# ============================
# CONTROLE GLOBAL DE IPs
# ============================

ips = {}  # { "10.0.0.1": { "tentativas": 3, "bloqueado": False } }

# ============================
# FUNÇÕES DE SEGURANÇA
# ============================

def registrar_log(evento):
    data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as log:
        log.write(f"{data_hora} | {evento}\n")

def alertar_soc(mensagem):
    print(f"[ALERTA SOC] {mensagem}")
    registrar_log(f"ALERTA SOC | {mensagem}")

def verificar_ip(ip):
    """
    Verifica se o IP está bloqueado
    """
    if ip in ips and ips[ip]["bloqueado"]:
        return True
    return False

def registrar_falha_ip(ip):
    """
    Registra falha global por IP
    """
    if ip not in ips:
        ips[ip] = {"tentativas": 0, "bloqueado": False}

    ips[ip]["tentativas"] += 1

    if ips[ip]["tentativas"] >= MAX_TENTATIVAS_IP:
        ips[ip]["bloqueado"] = True
        registrar_log(f"IP BLOQUEADO | ip={ip}")
        alertar_soc(f"IP bloqueado por excesso de tentativas: {ip}")

def autenticar(nome_usuario, senha_digitada):
    # Usuário inexistente
    if nome_usuario not in usuarios:
        registrar_log(f"Tentativa com usuário inexistente: {nome_usuario}")
        return False, "Usuário não encontrado"

    usuario = usuarios[nome_usuario]
    ip = usuario["ip"]

    # Verifica IP bloqueado
    if verificar_ip(ip):
        return False, "IP bloqueado por segurança"

    # Verifica usuário bloqueado
    if usuario["bloqueado"]:
        return False, "Usuário bloqueado"

    # Verifica senha
    if senha_digitada == usuario["senha"]:
        usuario["tentativas"] = MAX_TENTATIVAS_USUARIO
        registrar_log(f"Login OK | usuario={nome_usuario} ip={ip}")
        return True, "Login autorizado"

    # Falha de login
    usuario["tentativas"] -= 1
    registrar_falha_ip(ip)

    registrar_log(
        f"Falha login | usuario={nome_usuario} ip={ip} "
        f"tentativas_usuario={usuario['tentativas']} "
        f"tentativas_ip={ips[ip]['tentativas']}"
    )

    # Bloqueio do usuário
    if usuario["tentativas"] == 0:
        usuario["bloqueado"] = True
        registrar_log(f"USUÁRIO BLOQUEADO | usuario={nome_usuario} ip={ip}")
        alertar_soc(f"Usuário bloqueado: {nome_usuario} ({ip})")

    return False, "Senha incorreta"

# ============================
# SIMULAÇÃO DE LOGIN
# ============================

print("=== Sistema de Login Seguro (Bloqueio Global por IP) ===")

tentativas_simuladas = [
    ("admin", "errada"),
    ("joao", "errada"),
    ("admin", "errada"),
    ("joao", "errada"),
    ("admin", "errada"),
    ("joao", "errada")
]

for nome, senha in tentativas_simuladas:
    sucesso, mensagem = autenticar(nome, senha)
    print(f"[{nome}] {mensagem}")
    time.sleep(DELAY_TENTATIVAS)

print("\nResumo de segurança:")
for ip, dados in ips.items():
    if dados["bloqueado"]:
        print(f"- IP bloqueado: {ip}")
