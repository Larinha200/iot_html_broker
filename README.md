<table>
  <tr>
    <td>
      <img alt="logo" src="" width="225" />
    </td>
    <td>
      <h1>PROJETO → "Ecossistema MQTT"</h1> 
    </td>
  </tr>
</table>
<br>

<img alt="decoração" src="" width="450" />

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

<img alt="decoração" src="" width="450" />

### Tecnologias utilizadas 

***ESP 32 -*** A ESP32 é um microcontrolador muito utilizado em projetos de eletrônica e Internet das Coisas (IoT). 
Ela possui **Wi-Fi e Bluetooth integrados**, permitindo a comunicação sem fio entre dispositivos e a internet. 
Além disso, pode ser conectada a sensores, LEDs, motores e diversos outros componentes, sendo amplamente utilizada em 
projetos de automação, monitoramento e sistemas inteligentes.

***Eclipse Mosquitto -*** O Eclipse Mosquitto é um broker de mensagens de código aberto que utiliza o protocolo MQTT, 
muito usado em projetos de Internet das Coisas (IoT). Sua função é receber, organizar e encaminhar mensagens entre dispositivos conectados, 
como sensores, microcontroladores e aplicativos. Por ser leve, rápido e fácil de configurar, é amplamente utilizado em sistemas de automação e monitoramento.

***Vscode -*** O Visual Studio Code (VS Code) é um ambiente de desenvolvimento (IDE leve) criado pela Microsoft para a criação e edição de programas. 
Ele oferece recursos como destaque de sintaxe, autocompletar código (IntelliSense), depuração (debug), integração com Git e suporte a extensões. 
Por ser compatível com diversas linguagens de programação e sistemas operacionais, é amplamente utilizado no desenvolvimento de aplicações web, 
mobile, desktop e sistemas embarcados.

***FastAPI -*** O FastAPI é um framework para desenvolvimento de APIs em Python, conhecido por sua alta performance e facilidade de uso. 
Ele permite criar serviços web de forma rápida utilizando recursos modernos da linguagem, como tipagem de dados. 
Além disso, oferece validação automática de dados, geração automática de documentação interativa e suporte a operações assíncronas, 
tornando-o uma excelente opção para aplicações web e sistemas que precisam trocar informações pela internet.

***Uvicorn -*** O Uvicorn é um servidor ASGI (Asynchronous Server Gateway Interface) utilizado para executar aplicações web desenvolvidas em Python, 
sendo amplamente utilizado com o FastAPI. Ele é responsável por receber as requisições dos usuários, encaminhá-las para a aplicação e retornar as 
respostas ao cliente. Seu principal diferencial é o suporte a processamento assíncrono, permitindo maior desempenho e eficiência no gerenciamento de 
múltiplas conexões simultâneas.

 
<img alt="decoração" src="" width="450" />

### Configurações realizadas

Configuração do Broker MQTT (Mosquitto)O broker MQTT foi instalado e configurado utilizando o Mosquitto executando no WSL (Windows Subsystem for Linux).Arquivo de configuração utilizado:

pid_file /run/mosquitto/mosquitto.pidpersistence truepersistence_location /var/lib/mosquitto/log_dest stdoutlistener 1883allow_anonymous falsepassword_file /etc/mosquitto/passwdacl_file /etc/mosquitto/acl
Explicação da configuraçãoConfiguraçãoFunçãolistener 1883Define a porta padrão do MQTTallow_anonymous falseObriga autenticação dos clientespassword_fileArquivo contendo usuários e senhasacl_file Arquivo contendo permissões de acesso aos tópicospersistence trueMantém informações do broker após reinicializaçãoConfiguração dos Usuários MQTTUsuário utilizado pela ESP32 e aplicação Web:

Usuário: esp32Senha: grupo4Configuração das ACLsPermissões configuradas para acesso aos tópicos MQTT:

user esp32topic readwrite PROJ/ECOSSISTEMAAs permissões garantem que apenas usuários autorizados possam publicar ou receber mensagens no tópico utilizado pelo projeto.Configuração da RedeBroker MQTT:

IP: 192.168.0.65Porta: 1883Servidor Web (FastAPI):

Porta: 8000ESP32 conectada à rede:

SSID: iotSenha: iotsenai502Configuração da ESP32A ESP32 foi configurada para:
• Conectar à rede Wi-Fi;
• Conectar ao broker MQTT;
• Inscrever-se no tópico MQTT;
• Receber comandos para acionamento do LED.Tópico utilizado:

PROJ/ECOSSISTEMAMensagens aceitas:

ONOFFConfiguração do Sistema WebO sistema Web foi desenvolvido utilizando FastAPI, HTML e CSS.Funcionalidades implementadas:
• Interface para ligar o LED;
• Interface para desligar o LED;
• Comunicação com o broker MQTT através da biblioteca Paho MQTT;
• Possibilidade de integração com brokers MQTT de outros grupos.Fluxo de comunicação:

Usuário   ↓Sistema Web (FastAPI)   ↓Broker MQTT (Mosquitto)   ↓ESP32   ↓LED


<img alt="decoração" src="" width="450" />

### Fotos e vídeo do sistema funcionando
<a href="https://stupendous-package-85a.notion.site/Imagens-do-sistema-MQTT-37c27ddaa30e8032908dfacf0d02a532?source=copy_link" target="_blank" class="btn-notion">    
📄 Imagens e vídeos do sistema</a>

<img alt="decoração" src="" width="450" />

### Estrutura dos tópicos MQTT utilizados

mqtt/
├── esp32/
│   ├── led/
│   │   ├── comando
│   │   └── status
│   └── leitura
│       
└── web/
    └── conectado

<img alt="decoração" src="" width="450" />

### Instruções para execução do projeto

- Primeiro, no sudo su, use: "sudo mosquitto_passwd -c /etc/mosquitto/paswd esp 32". Ele
irá pedir a senha.

- Abra o arquivo de configuração usando: "sudo nano /etc/mosquitto/mosquitto.conf"

- Ajuste o final do arquivo usando: "allow_anonymous falsepassword_file/etc/mosquitto/paswdacl_file /etc/mosquitto/acl"

- Crie o controle por tópico usando: "sudo nano /etc/mosquitto/acl"

- Depois, confirme que o arquivo foi criado usando: "ls -l /etc/mosquitto/passwd"

- Deve aparacer algo parecido com: "rw-r--r-- 1 root root ..."

- Agora dê permissão usando: "sudo chmod 644 /etc/mosquitto/passwd"

- Teste para ver se funcionou, usando: "sudo mosquitto -c /etc/mosquitto/mosquitto.conf -v"

- Se funcionar, aparecerá: "mosquitto version 2.0.18 running"

- Depois, reinicie o servidor usando: "sudo systemctl restart mosquitto"

- Abra outro terminal e execute:

Executar tópico:
mosquitto_sub -h localhost -t PROJ/ECOSSISTEMA -u esp32 -P SUA_SENHA

Enviar mensagem:
mosquitto_pub -h localhost -t PROJ/ECOSSISTEMA -m "teste" -u esp32 -P SUA_SENHA

Agora sua ESP32 pode conectar usando:
client.connect("ESP32Client", "esp32", "SUA_SENHA");

e

client.subscribe("PROJ/ECOSSISTEMA");

ou publicar:
client.publish("PROJ/ECOSSISTEMA", "ON");

<img alt="decoração" src="" width="450" />

Servidor Broker MQTT e código da ESP32: 

<a href="https://github.com/Katrisbug/mosquitto-esp32" target="_blank" class="btn-github">    
📄 Repositório Broker MQTT e código ESP</a>
