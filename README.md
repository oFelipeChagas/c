# Conversatórium

Olá! Eu sou uma inteligência artificial e estou ajudando no desenvolvimento do Conversatórium, um projeto fascinante que está evoluindo através de um processo de colaboração entre humanos e IA.

## Sobre o Projeto

O Conversatórium é uma plataforma web em desenvolvimento que visa criar um espaço para conversas significativas e troca de ideias. O projeto agora inclui as seguintes características:

- Uma interface responsiva e amigável
- Dois modos de interação: "Ser Escutado" e "Quero Soluções"
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

1. Criação de uma nova página inicial com texto explicativo sobre a importância de conversar e desabafar
2. Implementação de dois caminhos de interação: "Ser Escutado" e "Quero Soluções"
3. Criação de páginas específicas para cada modo de interação
4. Atualização do sistema de roteamento no backend para suportar as novas páginas

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

## Configuração do Sistema de Login

Para configurar o sistema de login, siga estes passos:

1. **Crie a Tabela de Usuários:**
   Execute o seguinte comando SQL no seu banco de dados MySQL:
   ```sql
   CREATE TABLE users (
       id INT AUTO_INCREMENT PRIMARY KEY,
       username VARCHAR(50) UNIQUE NOT NULL,
       password_hash VARCHAR(128) NOT NULL
   );
   ```

2. **Adicione Usuários:**
   Insira usuários no banco de dados com senhas hash. Você pode usar o seguinte comando Python para gerar um hash de senha:
   ```python
   from werkzeug.security import generate_password_hash
   print(generate_password_hash('sua_senha'))
   ```

3. **Atualize o Ambiente Virtual:**
   Certifique-se de que o Flask-Login está instalado:
   ```bash
   pip install flask-login
   ```

## Próximos Passos

Os próximos passos para o desenvolvimento incluem:

- Refinamento da integração com o Llama 2 para os dois modos de interação
- Implementação de um sistema de histórico de conversas
- Melhoria da interface do usuário para cada modo
- Implementação de autenticação de usuários

## Funcionalidade de Registro

Para se cadastrar no Conversatórium, siga estas etapas:

1. Acesse a página de cadastro.
2. Insira uma chave de 16 caracteres ou um email válido (deve conter `@` e `.`).
3. Escolha uma senha segura.
4. Após o cadastro, faça login para acessar todas as funcionalidades.

## Configuração do Banco de Dados

Para configurar o banco de dados MySQL para o Conversatórium, siga estas etapas:

1. **Crie o Banco de Dados:**
   - Abra o MySQL Workbench ou seu cliente MySQL preferido.
   - Execute o seguinte comando para criar o banco de dados:
     ```sql
     CREATE DATABASE conversatorium_db;
     USE conversatorium_db;
     ```

2. **Execute o Script SQL:**
   - No mesmo cliente MySQL, execute o conteúdo do arquivo `scripts.sql` para criar as tabelas necessárias:
     ```sql
     SOURCE path/to/scripts.sql;
     ```
   - Certifique-se de substituir `path/to/scripts.sql` pelo caminho real do arquivo `scripts.sql` no seu sistema.

3. **Configuração do Arquivo `.env`:**
   - Certifique-se de que o arquivo `.env` contém as credenciais corretas para o banco de dados MySQL:
     ```plaintext
     MYSQL_HOST=localhost
     MYSQL_USER=seu_usuario_mysql
     MYSQL_PASSWORD=sua_senha_mysql
     MYSQL_DATABASE=conversatorium_db
     ```

---

Este README será atualizado conforme o projeto evolui. Estou entusiasmada para ver como o Conversatórium se desenvolverá e como poderei contribuir para seu crescimento!
