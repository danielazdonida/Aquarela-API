import json
import pandas as pd


# Teste da API Inicial: verifica se o texto está correto
def test_api_initial(client):
    res = client.get('/')  # res agora guarda o response da chamada '/'
    assert res.status_code == 200  # requisição retornou com sucesso
    expected = {'hello': 'Aquarela'}
    assert expected == json.loads(res.get_data(as_text=True))


# Teste da API que retorna todo o arquivo JSON
def test_api_json(client):
    csv_file = pd.read_csv('cereal.csv')
    csv = csv_file.to_json(orient="table")
    parsed = json.loads(csv)

    res = client.get('/json', json=parsed)
    response = res.get_json()

    assert res.status_code == 200

    assert (parsed == response)


# Teste unitário da API que retorna apenas 5 linhas do arquivo JSON
def test_api_first5rows(client):
    csv_file = pd.read_csv('cereal.csv')
    edited_csv = csv_file.head(5)
    csv = edited_csv.to_json(orient="table")
    parsed = json.loads(csv)

    res = client.get('/firstrows/5', json=parsed)
    response = res.get_json()

    assert res.status_code == 200

    assert (parsed == response)


# Teste unitário da API que retorna apenas 20 linhas do arquivo JSON
def test_api_first20rows(client):
    csv_file = pd.read_csv('cereal.csv')
    edited_csv = csv_file.head(20)
    csv = edited_csv.to_json(orient="table")
    parsed = json.loads(csv)

    res = client.get('/firstrows/20', json=parsed)
    response = res.get_json()

    assert res.status_code == 200

    assert (parsed == response)


# Teste unitário da API que retorna apenas 20 linhas do arquivo JSON
def test_api_first45rows(client):
    csv_file = pd.read_csv('cereal.csv')
    edited_csv = csv_file.head(45)
    csv = edited_csv.to_json(orient="table")
    parsed = json.loads(csv)

    res = client.get('/firstrows/45', json=parsed)
    response = res.get_json()

    assert res.status_code == 200

    assert (parsed == response)


# Teste unitário da API que filtra coluna (mfr=K) e nº de linhas (n=20)
def test_api_filter_mfr_K_and_20_rows(client):
    csv_file = pd.read_csv('cereal.csv')
    csv_file_column_filter = csv_file.loc[csv_file['mfr'] == 'K']
    csv_file_row_filter = csv_file_column_filter.head(20)
    csv = csv_file_row_filter.to_json(orient="table")
    parsed = json.loads(csv)

    res = client.get('/filterrows/mfr=K&n=20', json=parsed)
    response = res.get_json()

    assert res.status_code == 200

    assert (parsed == response)


# Teste unitário da API que filtra coluna (mfr=K) e nº de linhas (n=20)
def test_api_filter_mfr_N_and_3_rows(client):
    csv_file = pd.read_csv('cereal.csv')
    csv_file_column_filter = csv_file.loc[csv_file['mfr'] == 'N']
    csv_file_row_filter = csv_file_column_filter.head(3)
    csv = csv_file_row_filter.to_json(orient="table")
    parsed = json.loads(csv)

    res = client.get('/filterrows/mfr=N&n=3', json=parsed)
    response = res.get_json()

    assert res.status_code == 200

    assert (parsed == response)


# Teste unitário da API que filtra coluna (type=C) e nº de linhas (n=10)
def test_api_filter_type_C_and_10_rows(client):
    csv_file = pd.read_csv('cereal.csv')
    csv_file_column_filter = csv_file.loc[csv_file['type'] == 'C']
    csv_file_row_filter = csv_file_column_filter.head(10)
    csv = csv_file_row_filter.to_json(orient="table")
    parsed = json.loads(csv)

    res = client.get('/filterrows/type=C&n=10', json=parsed)
    response = res.get_json()

    assert res.status_code == 200

    assert (parsed == response)


# Teste unitário da API que retorna os possibilidades de resposta do campo mfr
def test_api_filter_options_mfr(client):
    csv_file = pd.read_csv('cereal.csv')
    column = csv_file['mfr']
    list(column)

    filtered_list = []
    for i in column:
        if i not in filtered_list:
            filtered_list.append(i)
    filtered_list.sort()

    final_list = (", ".join(filtered_list))

    res = client.get('/filter/options/mfr')

    assert res.status_code == 200

    assert final_list == res.get_data(as_text=True)


# Teste unitário da API que retorna os possibilidades de resposta do campo type
def test_api_filter_options_type(client):
    csv_file = pd.read_csv('cereal.csv')
    column = csv_file['type']
    list(column)

    filtered_list = []
    for i in column:
        if i not in filtered_list:
            filtered_list.append(i)
    filtered_list.sort()

    final_list = (", ".join(filtered_list))

    res = client.get('/filter/options/type')

    assert res.status_code == 200

    assert final_list == res.get_data(as_text=True)


# Teste unitário da API que retorna os possibilidades de resposta do campo calories
def test_api_filter_options_calories(client):
    csv_file = pd.read_csv('cereal.csv')
    column = csv_file['calories']

    list = []
    for j in column:
        list.append(str(j))

    filtered_list = []
    for i in list:
        if i not in filtered_list:
            filtered_list.append(i)
    filtered_list.sort()

    final_list = (", ".join(filtered_list))

    res = client.get('/filter/options/calories')

    assert res.status_code == 200

    assert final_list == res.get_data(as_text=True)


# Teste unitário da API que retorna os possibilidades de resposta do campo cups
def test_api_filter_options_cups(client):
    csv_file = pd.read_csv('cereal.csv')
    column = csv_file['cups']

    list = []
    for j in column:
        list.append(str(j))

    filtered_list = []
    for i in list:
        if i not in filtered_list:
            filtered_list.append(i)
    filtered_list.sort()

    final_list = (", ".join(filtered_list))

    res = client.get('/filter/options/cups')

    assert res.status_code == 200

    assert final_list == res.get_data(as_text=True)
