from flask import Flask, request, jsonify # type: ignore
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

API_TOKEN = os.getenv("API_TOKEN")

DEBUG = os.getenv("DEBUG", "False") == "True"
PORT = int(os.getenv("PORT", 5000))


# 🧹 Função de tratamento
def tratar_relato(texto: str) -> str:

    if not texto:
        return ""

    # Normaliza quebras de linha
    texto = texto.replace("\r\n", "\n").replace("\r", "\n")

    # Remove espaços extras mantendo estrutura
    linhas = [linha.strip() for linha in texto.split("\n")]

    texto = "\n".join(linhas)

    return texto


# 🔐 Middleware de autenticação
def validar_token():

    auth_header = request.headers.get("Authorization")

    if not auth_header:
        return False

    if auth_header != f"Bearer {API_TOKEN}":
        return False

    return True


# 🌐 Endpoint
@app.route("/tratar-relato", methods=["POST"])
def tratar():

    if not validar_token():
        return jsonify({
            "erro": "Não autorizado"
        }), 401

    texto = request.data.decode("utf-8")

    if not texto:
        return jsonify({
            "erro": "Texto vazio"
        }), 400

    texto_tratado = tratar_relato(texto)

    return jsonify({
        "relato_tratado": texto_tratado
    })


# ▶️ Rodar servidor
if __name__ == "__main__":

    app.run(host="0.0.0.0", port=PORT, debug=DEBUG)