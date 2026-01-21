# Secure Login Simulation – Evolução do Projeto

Este repositório documenta a **evolução progressiva de um sistema de autenticação em Python**, desenvolvido com foco em **segurança defensiva (Blue Team)** e aprendizado prático de lógica aplicada à mitigação de ataques de força bruta (brute force).

O projeto foi construído de forma incremental, partindo de um **login simples** até um **sistema multiusuário com controle de tentativas, logs e alertas de segurança**, simulando práticas comuns utilizadas em ambientes reais.

---

## 🎯 Objetivo do Projeto

Demonstrar, de maneira didática e prática:

* Como ataques de brute force funcionam
* Como sistemas podem mitigar esse tipo de ataque
* Como eventos de segurança podem ser registrados e analisados
* Como evoluir um código simples para uma solução mais robusta

O foco não é ataque, mas **prevenção, detecção e análise**.

---

## 🧩 Fase 1 – Login Simples (Início da Ideia)

### 📌 Descrição

A primeira versão do projeto consistia em um **login básico com usuário e senha fixos**, apenas para simular o processo de autenticação.

### 🔐 Conceitos aplicados

* Variáveis
* Condicionais (`if / else`)
* Loop de repetição

### 🎯 Aprendizado

Compreender como funciona a validação básica de credenciais e onde surgem as primeiras vulnerabilidades, como a ausência de limite de tentativas.

---

## 🧩 Fase 2 – Limite de Tentativas e Bloqueio

### 📌 Evolução

Foi adicionado um **contador de tentativas**, limitando o número de erros permitidos antes do bloqueio do usuário.

### 🔐 Conceitos aplicados

* Controle de tentativas
* Loops (`while`)
* Lógica de bloqueio

### 🛡️ Segurança

Essa etapa introduz a **mitigação básica contra brute force**, impedindo tentativas infinitas.

---

## 🧩 Fase 3 – Tratamento de Erros e Logs

### 📌 Evolução

A aplicação passou a registrar eventos de segurança e tratar falhas de execução.

### 🔐 Conceitos aplicados

* Funções
* `try / except`
* Registro de eventos

### 🛡️ Segurança

Permite auditoria e investigação posterior, evitando que erros interrompam o sistema.

---

## 🧩 Fase 4 – Identificação por IP e Delay

### 📌 Evolução

Foi adicionada a identificação do **IP de origem** e um **delay entre tentativas**.

### 🔐 Conceitos aplicados

* Controle de origem das tentativas
* `time.sleep()`

### 🛡️ Segurança

Dificulta ataques automatizados e permite identificar padrões suspeitos por origem.

---

## 🧩 Fase 5 – Sistema Multiusuário (Versão Atual)

### 📌 Evolução Final

O sistema passou a suportar **múltiplos usuários**, cada um com controle independente de tentativas, bloqueio e IP.

### 🔐 Conceitos aplicados

* Dicionários para armazenamento de usuários
* Controle individual de estado
* Logs persistentes
* Alertas de segurança simulados

### 🛡️ Segurança

Essa versão se aproxima de um **sistema real de autenticação**, com capacidade de monitoramento e resposta a incidentes.

---

## 📂 Estrutura do Projeto

```
secure-login-python/
│
├── login.py
├── README.md
└── security.log (gerado automaticamente)
```

---

## 📄 Logs de Segurança

Os eventos de autenticação são registrados automaticamente em um arquivo de log durante a execução do sistema, simulando registros utilizados em auditorias e investigações de incidentes.

---

## 🚀 Possíveis Próximas Evoluções

* Bloqueio por endereço IP independente do usuário
* Persistência de usuários em arquivo ou banco de dados
* Análise por janela de tempo
* Geração de relatórios de incidentes
* Integração com analisador de logs

---

## ⚠️ Aviso

Este projeto possui **finalidade exclusivamente educacional**. Todos os dados e cenários são simulados e não devem ser utilizados em ambientes reais sem autorização.

---

## 👤 Autor

Projeto desenvolvido como parte do aprendizado em **Python aplicado à segurança da informação**, com foco em lógica defensiva e boas práticas de monitoramento.
