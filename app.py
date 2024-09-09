from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv
import openai
from flask_cors import CORS

# Cargar variables de entorno
load_dotenv()

# Crear el servidor Flask
app = Flask(__name__)
CORS(app)

# Configurar las credenciales de OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")
assistant_id = os.getenv("ASSISTANT_ID")

@app.route("/")
def index():
    return "Servidor Flask funcionando correctamente"

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message")

    # Aquí es donde interactuamos con la API de OpenAI
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_message,
            max_tokens=150
        )
        return jsonify({
            "response": response.choices[0].text.strip()
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
