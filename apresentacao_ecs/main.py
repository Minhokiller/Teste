from flask import Flask, render_template, request, jsonify
import psycopg2

app = Flask(__name__)

# Configurações de conexão com o banco de dados PostgreSQL
db_host = 'postgres'
db_port = '5432'
db_name = 'postgres'
db_user = 'postgres'
db_password = 'mypassword'

# Rota principal
@app.route('/')
def index():
    # Conecta ao banco de dados
    connection = psycopg2.connect(
        host=db_host,
        port=db_port,
        dbname=db_name,
        user=db_user,
        password=db_password
    )
    cursor = connection.cursor()

    # Recupera o valor atual do contador do banco de dados
    cursor.execute("SELECT count FROM click_counter")
    count = cursor.fetchone()[0]

    # Renderiza o template index.html com a contagem atual
    return render_template('index.html', count=count)

# Rota para incrementar o contador
@app.route('/increment', methods=['POST'])
def increment():
    # Conecta ao banco de dados
    connection = psycopg2.connect(
        host=db_host,
        port=db_port,
        dbname=db_name,
        user=db_user,
        password=db_password
    )
    cursor = connection.cursor()

    # Recupera o valor atual do contador do banco de dados
    cursor.execute("SELECT count FROM click_counter")
    count = cursor.fetchone()[0]

    # Incrementa o contador
    count += 1

    # Atualiza o valor do contador no banco de dados
    cursor.execute("UPDATE click_counter SET count = %s", (count,))
    connection.commit()

    # Retorna o valor do contador atualizado como um JSON
    return jsonify(count=count)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)