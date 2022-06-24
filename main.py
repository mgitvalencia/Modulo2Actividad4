import requests
import json
import argparse
from respuesta import guarda_estado, guarda_datos, prepara_json


parser = argparse.ArgumentParser(description="Invocación de servicios con recursos con representación JSON")
parser.add_argument("-m", "--method", type=str, choices=['GET', 'POST', 'PUT', 'DELETE'], required=True, help="Método que se usará para llamar al API")
parser.add_argument("-r", "--resource", type=str, choices=['posts', 'comments'], required=True , help="Recurso sobre el que se realiza la operación")
parser.add_argument("-i", "--resource_id", type=str, default="", required=False, help=" Identificador único del recurso")


""" Para hacer debugger
parser = argparse.ArgumentParser(description="Invocación de servicios con recursos con representación JSON")
parser.add_argument("-m", "--method", type=str, default="GET", choices=['GET', 'POST', 'PUT', 'DELETE'], required=False, help="Método que se usará para llamar al API")
parser.add_argument("-r", "--resource", type=str, default="posts", choices=['post', 'comments'], required=False , help="Recurso sobre el que se realiza la operación")
parser.add_argument("-i", "--resource_id", type=str, default="20", required=False, help=" Identificador único del recurso")
"""

args = parser.parse_args()

print(args.method)
print(args.resource)
print(args.resource_id)


with open('config.json') as file:
    data = json.load(file)
file.close()

url = data["url"]
time_out = data["request_time_out"]
res_data = data["response_data"]
res_status = data["response_status"]

print(url)
print(time_out)
print(res_data)
print(res_status)
print(url + args.resource)

if (args.method == "GET"):
    if(args.resource_id != ""):
       path = url + args.resource + "/" + args.resource_id
    else:    
       path = url + args.resource


    headers = {'Content-type': ''}
    response = requests.get(path, verify=False, headers=headers)
    guarda_datos(res_data, response)
    json_data = prepara_json(args.method, path, response)
    guarda_estado(res_status, json_data)

    print(response.headers['Content-Type'])

   






"""
response = requests.get("https://jsonplaceholder.typicode.com/todos/1").text
objeto = json.loads(response)
print()
print(objeto)
print()
print(response)
print()
print ("Titulo: " + objeto["title"])
print()
"""