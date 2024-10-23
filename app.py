from flask import Flask, render_template, request, jsonify
import requests
import mysql.connector
from mysql.connector import Error
import json

app = Flask(__name__)

# Configuração do MySQL
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '1234',
    'database': 'conversatorium_db'
}

# Função para conectar ao MySQL
def create_db_connection():
    try:
        connection = mysql.connector.connect(**db_config)
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
    return None

# Função para salvar a conversa no banco de dados
def save_conversation(user_input, ai_response):
    connection = create_db_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = "INSERT INTO conversations (user_input, ai_response) VALUES (%s, %s)"
            cursor.execute(query, (user_input, ai_response))
            connection.commit()
            print("Conversa salva no banco de dados com sucesso!")
        except Error as e:
            print(f"Erro ao salvar conversa: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']
    
    # Chamada para o Ollama
    ollama_url = "http://localhost:11434/api/generate"
    ollama_data = {
        "model": "llama2:latest",
        "prompt": user_input
    }
    
    try:
        response = requests.post(ollama_url, json=ollama_data, stream=True)
        ai_response = ""
        
        for line in response.iter_lines():
            if line:
                json_response = json.loads(line)
                if 'response' in json_response:
                    ai_response += json_response['response']
                if json_response.get('done', False):
                    break
        
        print(f"Resposta processada do Ollama: {ai_response}")
        
        # Salvar a conversa no banco de dados
        save_conversation(user_input, ai_response)
        
        return jsonify({'response': ai_response})
    except Exception as e:
        print(f"Erro ao comunicar com Ollama: {e}")
        return jsonify({'response': "Desculpe, ocorreu um erro ao processar sua mensagem."})

@app.route('/saiba-mais')
def saiba_mais():
    return render_template('saiba_mais.html')

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
