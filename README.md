# API de Tratamento de Relatos

Uma API REST desenvolvida com Flask para tratamento e normalização de relatos textuais.

A API realiza:
- normalização de quebras de linha
- remoção de espaços desnecessários
- autenticação via Bearer Token
- configuração via `.env`
- deploy simplificado com Docker

---

# 🚀 Tecnologias utilizadas

- Python 3
- Flask
- python-dotenv
- Docker
- Docker Compose
- Traefik (opcional)

---

# 📂 Estrutura do projeto

```text
message_formater/
│
├── .env
├── .dockerignore
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
└── message_formater.py
```

---

# ⚙️ Configuração do ambiente

## 1. Clone o projeto

```bash
git clone https://github.com/TsunaYoshy/message_formater.git
cd message_formater
```

---

## 2. Crie o ambiente virtual

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Instale as dependências

```bash
pip install -r requirements.txt
```

---

# 🔐 Variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
DEBUG=True
PORT=5007

API_TOKEN=seu-token-super-seguro

DOMAIN=api.seudominio.com
TRAEFIK_ENTRYPOINT=web
```

---

# ▶️ Executando localmente

```bash
python3 message_formater.py
```

A API ficará disponível em:

```text
http://localhost:5007
```

---

# 🌐 Endpoint disponível

## POST `/tratar-relato`

Endpoint responsável pelo tratamento e normalização do texto.

---

# 🔐 Autenticação

A API utiliza autenticação Bearer Token.

Header obrigatório:

```http
Authorization: Bearer SEU_TOKEN
```

---

# 📥 Exemplo de requisição com curl

```bash
curl -X POST "http://localhost:5007/tratar-relato" \
-H "Authorization: Bearer seu-token-super-seguro" \
-H "Content-Type: text/plain" \
--data "Estávamos no ponto de ônibus..."
```

---

# 📤 Exemplo de resposta

```json
{
  "relato_tratado": "Estávamos no ponto de ônibus..."
}
```

---

# 🐳 Docker

## Build da imagem

```bash
docker build -t message_formater .
```

---

## Executar container

```bash
docker compose up --build
```

---

# 🌍 Traefik

A API pode ser integrada facilmente ao Traefik utilizando labels no `docker-compose.yml`.

Exemplo:

```yaml
labels:
  - "traefik.enable=true"
  - "traefik.http.routers.message-formater.rule=Host(`${DOMAIN}`)"
  - "traefik.http.routers.message-formater.entrypoints=${TRAEFIK_ENTRYPOINT}"
  - "traefik.http.services.message-formater.loadbalancer.server.port=${PORT}"
```

---

# 🚨 Segurança

## Recomendações para produção

- Não utilizar `debug=True`
- Utilizar HTTPS
- Não expor diretamente a porta Flask
- Utilizar reverse proxy (Traefik/Nginx)
- Armazenar tokens no `.env`
- Nunca versionar o `.env`

---

# 📄 Licença

Projeto desenvolvido para fins de automação e integração de relatos textuais.