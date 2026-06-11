from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import paho.mqtt.client as mqtt

app = FastAPI()

# ==========================================
# CONFIGURAÇÕES MQTT
# ==========================================

TOPICO = "PROJ/ECOSSISTEMA"

BROKER_GRUPO = "192.168.0.65"
USUARIO_GRUPO = "esp32"
SENHA_GRUPO = "grupo4"

BROKER_OUTRO = "192.168.0.72"
USUARIO_OUTRO = "grupo1"
SENHA_OUTRO = "grupo1"
TOPICO2 = "esp32/led"

# ==========================================
# CLIENTE GRUPO
# ==========================================

cliente_grupo = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

cliente_grupo.username_pw_set(
    USUARIO_GRUPO,
    SENHA_GRUPO
)

cliente_grupo.connect(
    BROKER_GRUPO,
    1883
)

cliente_grupo.loop_start()

# ==========================================
# CLIENTE OUTRO GRUPO
# ==========================================

cliente_outro = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

outro_broker_conectado = False

try:

    cliente_outro.username_pw_set(
        USUARIO_OUTRO,
        SENHA_OUTRO
    )

    cliente_outro.connect(
        BROKER_OUTRO,
        1883,
        60
    )

    cliente_outro.loop_start()

    outro_broker_conectado = True

    print("✓ Broker do outro grupo conectado")

except Exception as e:

    print("✗ Erro ao conectar no outro broker")
    print(e)

# ==========================================
# TEMPLATES
# ==========================================

templates = Jinja2Templates(
    directory="templates"
)

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

# ==========================================
# PÁGINAS
# ==========================================

@app.get("/")
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


@app.get("/outro_broker")
async def outro_broker(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="outro_broker.html"
    )

# ==========================================
# SEU BROKER
# ==========================================

@app.post("/ligar")
def ligar():

    resultado = cliente_grupo.publish(
        TOPICO,
        "ON"
    )

    print("LIGAR:", resultado.rc)

    return RedirectResponse(
        url="/",
        status_code=303
    )


@app.post("/desligar")
def desligar():

    resultado = cliente_grupo.publish(
        TOPICO,
        "OFF"
    )

    print("DESLIGAR:", resultado.rc)

    return RedirectResponse(
        url="/",
        status_code=303
    )

# ==========================================
# OUTRO BROKER
# ==========================================

@app.post("/ligar_outro")
def ligar_outro():

    if not outro_broker_conectado:
        print("Outro broker não conectado")
        return RedirectResponse(
            url="/outro_broker",
            status_code=303
        )

    resultado = cliente_outro.publish(
        TOPICO2,
        "ON"
    )

    print("OUTRO LIGAR:", resultado.rc)

    return RedirectResponse(
        url="/outro_broker",
        status_code=303
    )


@app.post("/desligar_outro")
def desligar_outro():

    if not outro_broker_conectado:
        print("Outro broker não conectado")
        return RedirectResponse(
            url="/outro_broker",
            status_code=303
        )

    resultado = cliente_outro.publish(
        TOPICO2,
        "OFF"
    )

    print("OUTRO DESLIGAR:", resultado.rc)

    return RedirectResponse(
        url="/outro_broker",
        status_code=303
    )