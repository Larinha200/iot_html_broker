<table>
  <tr>
    <td>
      <img alt="logo" src="https://github.com/user-attachments/assets/2107d297-281f-4a34-b137-d9599446a10a" width="200" />
    </td>
    <td>
      <h1>PROJETO → "Ecossistema MQTT"</h1> 
    </td>
  </tr>
</table>
<br>

### Explicação do funcionamento do sistema

O sistema desenvolvido utiliza o protocolo MQTT (Message Queuing Telemetry Transport) para realizar a comunicação entre uma aplicação web e 
uma ESP32 através de um broker MQTT. O objetivo principal é permitir o monitoramento e o controle remoto de dispositivos eletrônicos conectados à ESP32.

Inicialmente, foi instalado e configurado o broker MQTT Eclipse Mosquitto no ambiente WSL (Windows Subsystem for Linux). O broker atua como intermediário da comunicação, 
sendo responsável por receber e distribuir mensagens entre os dispositivos conectados.

A ESP32 é conectada à rede Wi-Fi e ao broker MQTT. Após estabelecer a conexão, ela permanece inscrita (subscrita) em tópicos específicos, aguardando comandos enviados pela aplicação web. 
Quando uma mensagem é publicada no tópico de comando, a ESP32 recebe essa informação e executa a ação correspondente, como ligar ou desligar um LED.

O sistema web foi desenvolvido para permitir que o usuário interaja com o dispositivo de forma simples e intuitiva. Por meio da interface, é possível enviar comandos MQTT para a ESP32 e 
visualizar o estado atual do dispositivo em tempo real. Para isso, a aplicação publica mensagens nos tópicos de comando e recebe informações através dos tópicos de status.

Quando um comando é executado pela ESP32, ela publica uma mensagem de confirmação em um tópico de status. O sistema web recebe essa mensagem e atualiza a interface, informando ao 
usuário se o dispositivo está ligado ou desligado.


## **Tecnologias utilizadas**

| **Tecnologia** | **Descrição** |
| --- | --- |
| **ESP32** | Microcontrolador com Wi-Fi e Bluetooth integrados, utilizado para controle do LED e comunicação MQTT |
| **Eclipse Mosquitto** | Broker MQTT de código aberto, responsável pelo roteamento das mensagens entre os dispositivos |
| **VS Code** | Editor de código-fonte utilizado como ambiente principal de desenvolvimento, tanto para o código da ESP32 quanto para a aplicação web |
| **PlatformIO** | Extensão do VS Code para desenvolvimento embarcado, utilizada para programar, compilar e fazer o upload do código para a ESP32 de forma simples e eficiente |
| **FastAPI** | Framework Python para criação da API web, com alta performance e suporte a operações assíncronas |
| **Uvicorn** | Servidor ASGI para execução da aplicação FastAPI, gerenciando conexões simultâneas |

## **🧠 Resumo visual da stack tecnológica**

```
Frontend (Web)      →  HTML + CSS
Backend (API)       →  FastAPI + Uvicorn (Python)
Comunicação         →  MQTT (Mosquitto Broker)
Microcontrolador    →  ESP32
IDE/Programação ESP →  VS Code + PlatformIO
```

## Configurações realizadas

### 1. Configuração do Broker MQTT (Mosquitto)

O broker MQTT foi instalado e configurado utilizando o Mosquitto executando no WSL.

Arquivo de configuração **`*(`/etc/mosquitto/mosquitto.conf`)*`**:

```
pid_file /run/mosquitto/mosquitto.pid
persistence true
persistence_location /var/lib/mosquitto/
log_dest stdout
listener 1883
allow_anonymous false
password_file /etc/mosquitto/passwd
acl_file /etc/mosquitto/acl
```

**Explicação das configurações:**

| **Configuração** | **Função** |
| --- | --- |
| `listener 1883` | Define a porta padrão do MQTT |
| `allow_anonymous false` | Obriga autenticação dos clientes |
| `password_file` | Arquivo contendo usuários e senhas |
| `acl_file` | Arquivo contendo permissões de acesso aos tópicos |
| `persistence true` | Mantém informações do broker após reinicialização |

### **2. Configuração dos Usuários MQTT**

Usuário criado para a ESP32 e aplicação Web:

```
Usuário: esp32
Senha: grupo4
```

### **3. Configuração das ACLs**

Permissões configuradas para acesso aos tópicos MQTT (`/etc/mosquitto/acl`):

```
user esp32
topic readwrite PROJ/ECOSSISTEMA
```

### **4. Configuração da Rede**

| **Componente** | **Configuração** |
| --- | --- |
| Broker MQTT IP | `192.168.0.65`  (mude de acordo com o ip da maquina que esta o broker) |
| Broker MQTT Porta | `1883` |
| Servidor Web (FastAPI) Porta | `8000` |
| Wi-Fi SSID | `iot` |
| Wi-Fi Senha | `iotsenai502` |

### **5. Configuração da ESP32**

A ESP32 foi configurada para:

- Conectar à rede Wi-Fi
- Conectar ao broker MQTT
- Inscrever-se no tópico MQTT
- Receber comandos para acionamento do LED

**Tópico utilizado:** `PROJ/ECOSSISTEMA`

**Mensagens aceitas:** `ON` / `OFF`

### **6. Configuração do Sistema Web**

O sistema Web foi desenvolvido utilizando FastAPI, HTML e CSS.

**Funcionalidades implementadas:**

- Interface para ligar o LED;
- Interface para desligar o LED;
- Comunicação com o broker MQTT através do python com o FastApi;
- Possibilidade de integração com brokers MQTT de outros grupos (ajustando as informações no código);

**Fluxo de comunicação:**

```
Usuário → Sistema Web (FastAPI) → Broker MQTT (Mosquitto) → ESP32 → LED
```

### **Fotos e vídeo do sistema funcionando**

📸 **Clique abaixo para visualizar as imagens e vídeos do sistema:**

Imagens e vídeos do sistema MQTT 

### **Estrutura dos tópicos MQTT utilizados**

```
mqtt/
├── esp32/
│   ├── led/
│   │   ├── comando
│   │   └── status
│   └── leitura
│
└── web/
    └── conectado
```

**Tópico principal utilizado no projeto:** `PROJ/ECOSSISTEMA`

### **Instruções para execução do projeto**

### **Passo 1: Configurar o Mosquitto Broker**

```bash
# Acessar como superusuário
sudo su

# Criar arquivo de senhas para o usuário esp32
sudo mosquitto_passwd -c /etc/mosquitto/passwd esp32
# (Digite a senha: grupo4)

# Editar arquivo de configuração
sudo nano /etc/mosquitto/mosquitto.conf
```

Adicione ao final do arquivo:

```
allow_anonymous false
password_file /etc/mosquitto/passwd
acl_file /etc/mosquitto/acl
```

### **Passo 2: Configurar ACL (Controle de Acesso)**

```bash
# Criar arquivo ACL
sudo nano /etc/mosquitto/acl
```

Adicione:

```
user esp32
topic readwrite PROJ/ECOSSISTEMA
```

### **Passo 3: Ajustar permissões**

```bash
# Confirmar criação do arquivo
ls -l /etc/mosquitto/passwd

#Deve aparecer algo parecido como:
 "rw-r--r-- 1 root root ..."
 
# Dar permissão adequada
sudo chmod 644 /etc/mosquitto/passwd

# Testar configuração
sudo mosquitto -c /etc/mosquitto/mosquitto.conf -v

#Se funcionar, aparecerá: 
"mosquitto versão 2.0.18 em execução"
```

### **Passo 4: Iniciar o broker**

```bash
# Reiniciar o serviço
sudo systemctl restart mosquitto
```

### **Passo 5: Testar o broker**

No terminal aonde esta o broker (subscribe), coloque para “escutar a mensagem”:

```bash
mosquitto_sub -h localhost -t PROJ/ECOSSISTEMA -u esp32 -P grupo4
```

Em outro terminal (publish), coloque para enviar a mensagem:

```
mosquitto_pub -h ***IP_DO_BROKER*** -t PROJ/ECOSSISTEMA -m "teste" -u SEU_USUARIO -P SUA_SENHA
```

| **Parâmetro** | **Significado** | **Exemplo** |
| --- | --- | --- |
| `-h` | Host (endereço do broker) | `-h 192.168.0.65` |
| `-t` | Tópico | `-t PROJ/ECOSSISTEMA` |
| `-u` | Usuário | `-u esp32` |
| `-P` | Senha | `-P grupo4` |
| `-m` | Mensagem (apenas no pub) | `-m "ON"` |
- no ***IP_DO_BROKER*** utilize o ip da maquina que esta conectada ao broker, para descobrir abra o terminal da maquina e digite ***ipconfig,***  estara ao lado de  ***Endereço IPv4. . . . . . . .  . . . . . . . : 192.168.0.137.***

### **Passo 6: Configurar a ESP32**

- Para utilizar o codigo da esp32 voce precisa que a maquina esteja usando o plataformIO, alem de nao poder misturar com o codigo da API, ***somente o codigo da ESP32.***

No código da ESP32 (***ao final do readme esta o repositorio)***, configure:

```cpp
// Conexão ao broker
client.connect("ESP32Client", "esp32", "grupo4");

// Subscribe ao tópico
client.subscribe("PROJ/ECOSSISTEMA");

// Publicar mensagem
client.publish("PROJ/ECOSSISTEMA", "ON");
```

### **Passo 7: Executar o servidor web (FastAPI)**

- para executar o servidor você fara em uma outra maquina utilizando o VS Code e o FastApi, instale as dependências e o ambiente virtual abaixo:

#### **Passo a passo no Linux/WSL ou macOS:**

```bash
# 1. Criar o ambiente virtual
python3 -m venv venv

# 2. Ativar o ambiente virtual
source venv/bin/activate

# 3. Instalar as dependências
pip install -r requirements.txt

# 4. Verificar se tudo foi instalado corretamente
pip list
```

#### **Passo a passo no Windows (PowerShell):**

```powershell
# 1. Criar o ambiente virtual
python -m venv venv

# 2. Ativar o ambiente virtual
.\venv\Scripts\Activate.ps1

# 3. Instalar as dependências
pip install -r requirements.txt

# 4. Verificar instalação
pip list
```

dentro do ambiente virtual instale:

#### **No Linux/WSL/Mac:**

```bash
# Instalar o FastAPI
pip3 install fastapi

# Instalar o servidor Uvicorn
pip3 install uvicorn[standard]

# Instalar o cliente MQTT
pip3 install paho-mqtt
```

### **No Windows:**

```bash
# Instalar o FastAPI
pip install fastapi

# Instalar o servidor Uvicorn
pip install uvicorn[standard]

# Instalar o cliente MQTT
pip install paho-mqtt
```

```bash
# Instalar dependências
pip install fastapi uvicorn paho-mqtt

# Executar o servidor
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### **Passo 8: Acessar a interface web**

Abra o navegador e acesse: `http://localhost:8000`  (troque o localhost pelo ip da maquina onde esta o código da API e HTML. **`Ex: 192.168.0.65`**)

### **Estrutura final do projeto**

```
projeto-mqtt/
│
├── venv/                       # Ambiente virtual (não versionar)
├── .env                        # Variáveis de ambiente
├── .gitignore                  # Ignorar venv, .env, etc.
├── requirements.txt            # Dependências do projeto
├── main.py                     # Código do FastAPI
├── static/
│   └── style.css               # Estilos CSS
└── templates/
    └── index.html              # Interface web
```

### **Repositórios do projeto**

| **Repositório** | **Link** |
| --- | --- |
| **Broker MQTT e código ESP32** | [github.com/Katrisbug/mosquitto-esp32](https://github.com/Katrisbug/mosquitto-esp32) |

---

📌 **Projeto desenvolvido como parte da disciplina de IoT - Ecossistema MQTT**
