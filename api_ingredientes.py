# API - disponibilizar recursos ou funcionalidades
#1. Objetivo - criar API que dispnibiliza a inclusão, consulta, edicao e exclusao de receitas para determinado ingrediente
#2. URL base - https://miguelyogui.pythonanywhere.com/
#3. Endpoint - Endereços consumíveis
    # #- https://miguelyogui.pythonanywhere.com/ingredientes (GET) mostra todos
    # #- https://miguelyogui.pythonanywhere.com/ingredientes (POST)
    # #- https://miguelyogui.pythonanywhere.com/ingredientes/id (GET)
    # #- https://miguelyogui.pythonanywhere.com/ingredientes/id (PUT)
    # #- https://miguelyogui.pythonanywhere.com/ingredientes/id (DELETE)
#4. QUais recursos disponibilizar - ingredientes, receita gerada por IA para o ingredientes solicitado

# Repositório da API: https://github.com/miguelyogui/projetoSDW2023
#sdw2023_api_url = 'https://miguelyogui.pythonanywhere.com/'
#dw2023_api_url = 'localhost:5000/'


from flask import Flask, jsonify, request

app = Flask(__name__)

#Extraia a lista de IDs de ingredientes a partir do arquivo CSV. Para cada ID, 
#faça uma requisição GET para obter os dados do ingrediente correspondente.

ingredientes = [
     {
         'id': 1,
         'ingrediente': 'Picanha',
         'receita': ""
     },
     {
         'id': 2,
         'ingrediente': 'Sal |Marinho',
         'receita': ""
     },
     {
         'id': 3,
         'ingrediente': 'Feijão',
         'receita': ""
     },
     {
         'id': 4,
         'ingrediente': 'Macarrão',
         'receita': ""
     },
     {
         'id': 5,
         'ingrediente': 'Quiabo',
         'receita': ""
     },
     {
         'id': 6,
         'ingrediente': 'Peito de Frango',
         'receita': ""
     },
     {
         'id': 7,
         'ingrediente': 'Arroz',
         'receita': ""
     },
     {
         'id': 8,
         'ingrediente': 'Tomate',
         'receita': ""
     },
     {
         'id': 9,
         'ingrediente': 'Palmito',
         'receita': ""
     },
     {
         'id': 10,
         'ingrediente': 'Salsinha',
         'receita': ""
     }
 ]

#Consultar(todos)
@app.route('/ingrediente', methods=['GET']) #URL do endpoint para visualizar todos os ingredientes - aceita somente metodo GET
def obter_ingrediente():
    return jsonify(ingredientes)

#Consultar(id)
@app.route('/ingrediente/<int:id>', methods=['GET']) #URL do endpoint para visualizar os ingredientes por id - aceita somente metodo GET
def obter_ingediente_por_id(id):
    for ingrediente in ingredientes:
        if ingrediente.get('id') == id:
            return jsonify(ingrediente)



#Incluir
@app.route('/ingrediente',methods=["POST"])
def incluir_novo_ingrediente():
    novo_ingrediente = request.get_json()
    ingredientes.append(novo_ingrediente)

    return jsonify(ingredientes)


#Editar
@app.route('/ingrediente/<int:id>', methods=['PUT'])
def editar_ingrediente_por_id(id):
    ingrediente_alterado = request.get_json()
    for indice,ingrediente in enumerate(ingredientes):
        if ingrediente.get('id') == id:
            ingredientes[indice].update(ingrediente_alterado)
            return jsonify(ingredientes[indice])



#Excluir
@app.route('/ingrediente/<int:id>',methods=['DELETE'])
def excluir_ingrediente(id):
    for indice, ingrediente in enumerate(ingredientes):
        if ingrediente.get('id') == id:
            del ingredientes[indice]
    
    return jsonify(ingredientes)
        

#Publicar na WEB porta 5000, localhost
app.run(port=5000,host='localhost',debug=True)










