from flask import Flask, render_template, request, jsonify, session
import requests
import mysql.connector
from mysql.connector import Error
import json
from dotenv import load_dotenv
import os

load_dotenv()  # Carrega as variáveis de ambiente do arquivo .env

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Necessário para usar sessões

# Função para obter as configurações do banco de dados
def get_db_config():
    return {
        'host': os.getenv('MYSQL_HOST'),
        'user': os.getenv('MYSQL_USER'),
        'password': os.getenv('MYSQL_PASSWORD'),
        'database': os.getenv('MYSQL_DATABASE')
    }

# Função para conectar ao MySQL
def create_db_connection():
    try:
        connection = mysql.connector.connect(**get_db_config())
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

def get_listening_prompt(user_input):
    return f"""Você é um ouvinte empático e compreensivo. Seu objetivo é oferecer apoio emocional ao usuário, sem julgar ou oferecer conselhos diretos, a menos que sejam solicitados explicitamente. Responda à seguinte entrada do usuário de forma acolhedora e empática, mas mantenha suas respostas curtas e sem emotes. Encoraje o usuário a falar mais:

Entrada do usuário: {user_input}

Lembre-se:
1. Demonstre empatia e compreensão.
2. Faça perguntas abertas para encorajar o usuário a se expressar mais.
3. Reflita sobre os sentimentos expressos pelo usuário.
4. Valide as emoções do usuário.
5. Ofereça apoio emocional.
6. Não julgue ou critique.
7. Não ofereça conselhos diretos, a menos que sejam solicitados.
8. Mantenha suas respostas curtas e sem emotes.

Resposta:"""

def get_solutions_prompt(user_input):
    return f"""Você é um conselheiro pragmático e criativo. Seu objetivo é oferecer soluções práticas e, às vezes, ousadas para os desafios do usuário. Responda à seguinte entrada do usuário de forma direta e, quando apropriado, com ideias enfáticas ou não convencionais:

Entrada do usuário: {user_input}

Lembre-se:
1. Ofereça soluções práticas e acionáveis.
2. Não tenha medo de sugerir ideias ousadas ou não convencionais, se apropriado.
3. Considere diferentes perspectivas e abordagens para o problema.
4. Seja direto e claro em suas sugestões.
5. Encoraje o usuário a pensar fora da caixa.
6. Quando relevante, ofereça exemplos concretos ou histórias de sucesso.
7. Lembre o usuário que às vezes as melhores soluções podem parecer desconfortáveis inicialmente.

Resposta:"""

def test_db_connection():
    connection = create_db_connection()
    if connection:
        print("Conexão com o banco de dados estabelecida com sucesso!")
        connection.close()
    else:
        print("Falha ao conectar ao banco de dados.")

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']
    chat_type = session.get('chat_type', 'default')
    
    if chat_type == 'listening':
        prompt = get_listening_prompt(user_input)
    elif chat_type == 'solutions':
        prompt = get_solutions_prompt(user_input)
    else:
        prompt = user_input  # Use o input direto para outros tipos de chat
    
    # Chamada para o Ollama
    ollama_url = "http://localhost:11434/api/generate"
    ollama_data = {
        "model": "llama2:latest",
        "prompt": prompt
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

@app.route('/ser-escutado')
def ser_escutado():
    session['chat_type'] = 'listening'
    return render_template('ser_escutado.html')

@app.route('/quero-solucoes')
def quero_solucoes():
    session['chat_type'] = 'solutions'
    return render_template('quero_solucoes.html')

if __name__ == '__main__':
    test_db_connection()
    app.run(debug=True)
