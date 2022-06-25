import json

def guarda_datos(archivo, mensaje):
    with open(archivo, 'w', encoding=mensaje.encoding) as file:
       json.dump(json.loads(mensaje.text), file, indent=4)
    file.close

def guarda_estado(archivo, mensaje):
    with open(archivo, 'w') as file:
       json.dump(mensaje, file, indent=4)
    file.close

def prepara_json(metodo, path, response):
    json_data = {}
    json_data['method'] = metodo
    json_data['url'] = path
    json_data['status'] = response.status_code
    json_data['content-type'] = response.headers['Content-Type'].split(';')[0]
    json_data['encoding'] = response.encoding
    return(json_data)

