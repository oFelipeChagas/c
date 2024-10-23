# Conversatórium

Olá! Eu sou uma inteligência artificial e estou ajudando no desenvolvimento do Conversatórium, um projeto fascinante que está evoluindo através de um processo de colaboração entre humanos e IA.

## Sobre o Projeto

O Conversatórium é uma plataforma web em desenvolvimento que visa criar um espaço para conversas significativas e troca de ideias. O projeto agora inclui as seguintes características:

- Uma interface responsiva e amigável
- Um sistema de chat integrado com IA usando o modelo Llama 2
- Integração com banco de dados MySQL para armazenamento de conversas
- Potencial para futuras integrações com APIs de inteligência artificial

## Processo de Desenvolvimento

O desenvolvimento do Conversatórium está ocorrendo através de um diálogo interativo entre um desenvolvedor humano e eu, uma IA. O processo envolve:

1. O humano propõe ideias ou solicita funcionalidades
2. Eu ofereço sugestões de implementação e código
3. O humano revisa, aceita ou solicita modificações
4. Iteramos sobre o código e o design até chegarmos a um resultado satisfatório

Este método permite uma combinação única de criatividade humana e eficiência computacional da IA.

## Mudanças Recentes

Nas últimas atualizações, realizamos as seguintes implementações:

1. Integração com o Ollama para usar o modelo Llama 2
2. Implementação de um sistema de chat que se comunica com o Llama 2
3. Adição de funcionalidade para salvar conversas no banco de dados MySQL
4. Melhoria na exibição das respostas do chat, incluindo formatação de quebras de linha
5. Otimização do processamento das respostas do modelo Llama 2

## Configuração do Projeto

Para configurar o projeto, siga estes passos:

1. Clone o repositório
2. Crie um ambiente virtual: `python -m venv venv`
3. Ative o ambiente virtual:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`
4. Instale as dependências: `pip install -r requirements.txt`
5. Configure o banco de dados MySQL conforme especificado no arquivo `app.py`
6. Certifique-se de que o Ollama está instalado e rodando com o modelo Llama 2
7. Execute o aplicativo Flask: `flask run`

## Manual de Instalação Detalhado

Siga estas etapas para configurar o Conversatórium em seu ambiente local:

### 1. Pré-requisitos

Certifique-se de ter instalado:
- Python 3.7 ou superior
- pip (gerenciador de pacotes do Python)
- MySQL Server
- Git
- Ollama com o modelo llama2:latest

### 2. Clonar o Repositório

1. Abra um terminal ou prompt de comando.
2. Navegue até o diretório onde deseja clonar o projeto.
3. Execute o comando:
   ```
   git clone https://github.com/oFelipeChagas/c.git
   cd c
   ```

### 3. Configurar o Ambiente Virtual

1. Crie um ambiente virtual:
   - No Windows:
     ```
     python -m venv venv
     ```
   - No macOS/Linux:
     ```
     python3 -m venv venv
     ```

2. Ative o ambiente virtual:
   - No Windows:
     ```
     venv\Scripts\activate
     ```
   - No macOS/Linux:
     ```
     source venv/bin/activate
     ```

### 4. Instalar Dependências

1. Com o ambiente virtual ativado, instale as dependências:
   ```
   pip install -r requirements.txt
   ```

### 5. Configurar o Banco de Dados MySQL

1. Abra o MySQL Workbench ou seu cliente MySQL preferido.
2. Execute os seguintes comandos SQL:
   ```sql
   CREATE DATABASE conversatorium_db;
   USE conversatorium_db;

   CREATE TABLE conversations (
       id INT AUTO_INCREMENT PRIMARY KEY,
       user_input TEXT,
       ai_response TEXT,
       timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
   );
   ```

3. Abra o arquivo `app.py` e atualize as configurações do banco de dados:
   ```python
   db_config = {
       'host': 'localhost',
       'user': 'seu_usuario_mysql',
       'password': 'sua_senha_mysql',
       'database': 'conversatorium_db'
   }
   ```

### 6. Configurar o Ollama

1. Certifique-se de que o Ollama está instalado em seu sistema.
2. Abra um novo terminal e execute:
   ```
   ollama run llama2:latest
   ```
   Mantenha este terminal aberto enquanto estiver usando o Conversatórium.

### 7. Executar o Aplicativo

1. No terminal onde o ambiente virtual está ativado, execute:
   ```
   flask run
   ```

2. Abra um navegador e acesse `http://127.0.0.1:5000`

### 8. Solução de Problemas

- Se encontrar erros relacionados a importações no Python, verifique se todas as dependências foram instaladas corretamente.
- Se houver problemas de conexão com o banco de dados, verifique as credenciais e certifique-se de que o servidor MySQL está em execução.
- Se o Ollama não responder, verifique se ele está rodando em um terminal separado.

### 9. Desenvolvimento

- Para fazer alterações no código, edite os arquivos na pasta do projeto.
- Após fazer alterações, reinicie o servidor Flask para que elas tenham efeito.

Parabéns! Você agora deve ter o Conversatórium rodando em seu ambiente local. Se encontrar algum problema durante a instalação, não hesite em buscar ajuda ou consultar a documentação das ferramentas utilizadas.

## Próximos Passos

Os próximos passos para o desenvolvimento incluem:

- Refinamento da integração com o Llama 2
- Melhoria da interface do usuário
- Implementação de autenticação de usuários
- Expansão das funcionalidades do chat

---

Este README será atualizado conforme o projeto evolui. Estou entusiasmada para ver como o Conversatórium se desenvolverá e como poderei contribuir para seu crescimento!
