from flask.json import jsonify
from Analysis.gramatica import parser
from Environment.Contexto import listaErrores ,resultJolc , tablaSimbolos
from flask import Flask, request
from flask_cors import CORS
import json
from werkzeug.wrappers import response
from Environment.Environment import Environment


app = Flask(__name__)
CORS(app)

cors = CORS(app, resources = {
    r"/*":{
        "origins": "*"
    }
})


@app.route('/compile', methods=['POST'])
def getInterpreter():
    try:
        codigo = request.get_json()["jolc"]
         
        executeRoout(True, codigo)
         
          # resultJolc = ""        
        return  jsonify({
            'resultado' : returnOutput(resultJolc),
            'errores' : listaErrores,
            'simbolos': tablaSimbolos
            }) 
    except:
        print("Error interno")

def main():
    f = open("./entrada.txt", "r")
    input = f.read()
    parser.parse(input)
    print("---------------------- ERRORES ------------")
    print(listaErrores)
    print("------------")
    print(returnOutput(resultJolc))

#Funcion para ejecutar el codigo  true = parse , false = ast
def executeRoout(mode, input):
    raiz = parser.parse(input)
    #if mode:
    #    parent =  Environment(None)
    #    for ins in raiz:
    #        ins.execute(parent)
    #else:
    #    print("Ejeutar el getDot")          

#Funcion para devolver el resultado como un string 
def returnOutput(lista):
    temp = "------------------ Resultado ---------------- \n"
    for a  in lista:
        temp += a
    return temp

if __name__ == "__main__":
    main()
    app.run(port=8000, debug=True)