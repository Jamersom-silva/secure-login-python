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
        "ip": "10.0.0.1",
        "falhas": 0
    },
    "joao": {
        "senha": "joao123",
        "tentativas": MAX_TENTATIVAS_USUARIO,
        "bloqueado": False,
        "ip": "10.0.0.1",
        "falhas": 0
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
    return ip in ips and ips[ip]["bloqueado"]

def registrar_falha_ip(ip):
    if ip not in ips:
        ips[ip] = {"tentativas": 0, "bloqueado": False}

    ips[ip]["tentativas"] += 1

    if ips[ip]["tentativas"] >= MAX_TENTATIVAS_IP:
        ips[ip]["bloqueado"] = True
        registrar_log(f"IP BLOQUEADO | ip={ip}")
        alertar_soc(f"IP bloqueado por excesso de tentativas: {ip}")

def autenticar(nome_usuario, senha_digitada):
    if nome_usuario not in usuarios:
        registrar_log(f"Tentativa com usuário inexistente: {nome_usuario}")
        return False, "Usuário não encontrado"

    usuario = usuarios[nome_usuario]
    ip = usuario["ip"]

    if verificar_ip(ip):
        return False, "IP bloqueado por segurança"

    if usuario["bloqueado"]:
        return False, "Usuário bloqueado"

    if senha_digitada == usuario["senha"]:
        usuario["tentativas"] = MAX_TENTATIVAS_USUARIO
        registrar_log(f"Login OK | usuario={nome_usuario} ip={ip}")
        return True, "Login autorizado"

    # Falha
    usuario["tentativas"] -= 1
    usuario["falhas"] += 1
    registrar_falha_ip(ip)

    registrar_log(
        f"Falha login | usuario={nome_usuario} ip={ip} "
        f"tentativas_usuario={usuario['tentativas']} "
        f"tentativas_ip={ips[ip]['tentativas']}"
    )

    if usuario["tentativas"] == 0:
        usuario["bloqueado"] = True
        registrar_log(f"USUÁRIO BLOQUEADO | usuario={nome_usuario} ip={ip}")
        alertar_soc(f"Usuário bloqueado: {nome_usuario} ({ip})")

    return False, "Senha incorreta"

# ============================
# RELATÓRIO DE INCIDENTES
# ============================

def gerar_relatorio():
    print("\n===== RELATÓRIO FINAL DE SEGURANÇA =====")
    print(f"Data/Hora: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    print("Usuários bloqueados:")
    for nome, dados in usuarios.items():
        if dados["bloqueado"]:
            print(f"- {nome} | IP {dados['ip']} | Falhas: {dados['falhas']}")

    print("\nIPs bloqueados:")
    for ip, dados in ips.items():
        if dados["bloqueado"]:
            print(f"- {ip} | Tentativas: {dados['tentativas']}")

    print("\nResumo geral:")
    for nome, dados in usuarios.items():
        print(
            f"- {nome}: falhas={dados['falhas']} | "
            f"bloqueado={dados['bloqueado']}"
        )

    print("======================================")

# ============================
# SIMULAÇÃO DE LOGIN
# ============================

print("=== Sistema de Login Seguro ===")

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

# Geração do relatório
gerar_relatorio()
