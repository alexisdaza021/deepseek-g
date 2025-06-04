import requests
import json

# 🔑 Tu clave API de OpenRouter
api_key = "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"

# ✍️ Mensaje del usuario (prompt)
user_input = input("Escribe tu mensaje para DeepSeek:\n> ")

# Configuración de la solicitud
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

payload = {
    "model": "deepseek/deepseek-r1-0528-qwen3-8b:free",
    "messages": [
        {"role": "user", "content": user_input}
    ]
}

# Enviar solicitud a OpenRouter
response = requests.post(
    "https://openrouter.ai/api/v1/chat/completions",
    headers=headers,
    data=json.dumps(payload)
)

# Procesar la respuesta
if response.status_code == 200:
    data = response.json()
    if "choices" in data and len(data["choices"]) > 0:
        print("\n🧠 Respuesta de DeepSeek:\n")
        print(data["choices"][0]["message"]["content"])
    else:
        print("⚠️ No se recibió una respuesta válida.")
else:
    print(f"🔴 Error {response.status_code}: {response.text}")
