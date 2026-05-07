from flask import Flask, request, jsonify

app = Flask(__name__)

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


# 🌐 Endpoint
@app.route("/tratar-relato", methods=["POST"])
def tratar():
    data = request.get_json()

    if not data or "relato" not in data:
        return jsonify({"erro": "Campo 'relato' é obrigatório"}), 400

    texto_tratado = tratar_relato(data["relato"])

    return jsonify({
        "relato_tratado": texto_tratado
    })


# ▶️ Rodar servidor
if __name__ == "__main__":
    app.run(debug=True)