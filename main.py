import json
import pandas as pd
from flask import Flask, jsonify

csv_file = pd.read_csv('cereal.csv')  # upload do arquivo CSV que está na pasta do projeto

app = Flask(__name__)


# Fiz essa API para tentar começar a compreender os testes unitários
@app.route('/')
def api_initial():
    return jsonify({'hello': 'Aquarela'})


# API que retorna todo arquivo CSV no formato JSON
@app.route('/json', methods=['GET'])
def api_json():
    csv = csv_file.to_json(orient="table")
    parsed = json.loads(csv)
    json.dumps(parsed, indent=4)
    return jsonify(parsed)


# API que retorna as N primeiras linhas do arquivo JSON
@app.route('/firstrows/<int:n>', methods=['GET'])
def api_firstrows(n):
    edited_csv = csv_file.head(n)
    csv = edited_csv.to_json(orient="table")
    parsed = json.loads(csv)
    json.dumps(parsed, indent=4)
    return jsonify(parsed)


# API que retorna o filtro dos resultados e o número máximo de registros recebidos
@app.route('/filterrows/<field>=<string:fieldname>&n=<int:n>', methods=['GET'])
def api_filterrows(field, fieldname, n):
    csv_file_column_filter = csv_file.loc[csv_file[field] == fieldname]
    csv_file_row_filter = csv_file_column_filter.head(n)
    csv = csv_file_row_filter.to_json(orient="table")
    parsed = json.loads(csv)
    json.dumps(parsed, indent=4)
    return jsonify(parsed)


# API que retorna uma lista de valores possíveis de serem utilizados no campo escolhido
@app.route('/filter/options/<string:field>', methods=['GET'])
def api_filter_options(field):
    column = csv_file[field]

    list = []
    for j in column:
        list.append(str(j))

    filtered_list = []
    for i in list:
        if i not in filtered_list:
            filtered_list.append(i)  # cast para transformar todos os dados em strings
    filtered_list.sort()

    return (", ".join(filtered_list))


if __name__ == '__main__':
    app.run(debug=True)
