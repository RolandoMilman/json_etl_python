# JSON ETL [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

import json


def serializar():
    print("Funcion que genera un archivo JSON")
    # JSON Serialize
    # Armar un JSON que represente los datos personales
    # de su persona (puede invitar los datos sino quiere exponer
    # información confidencial)

    # Debe armar un JSON que tenga como datos
    # nombre, apellido, DNI
    # Dentro debe tener una lista donde coloque cantidad de elementos de vestir
    # ejemplo -->
    #  { "prenda": "zapatilla", "cantidad": 4 }
    #  { "prenda": "remeras", "cantidad": 12 }
    # Que su lista de prendas dentro del JSON tenga al menos 2 prendas

    # json_data = {...}

    # Una vez que finalice el JSON realice un "dump" para almacenarlo en
    # un archivo que usted defina

    # Observe el archivo y verifique que se almaceno lo deseado
    # Generar un json y almacenarlo en archivo (dump)

    cliente1 = {
                  "nombre": "Max",
                  "apellido": "Power",
                  "dni": "12589666",
                  "vestidor": [
                      {
                       "prenda": "remera",
                       "cantidad": "2"
                      },
                      {
                       "prenda": "pantalón",
                       "cantidad": "2"
                      }
                      ]
                   }

    cliente2 = {
                "nombre": "Jorge",
                "apellido": "Mendieta",
                "dni": "23659855",
                "vestidor": [
                    {
                    "prenda": "camisa",
                    "cantidad": "3"
                    },
                    {
                    "prenda": "pullover",
                    "cantidad": "2"
                    },
                    {
                    "prenda": "campera",
                    "cantidad": "1"
                    }
                    ]
                }

    cliente3 = {
        "nombre": "Alejandro",
        "apellido": "Saponare",
        "dni": "125888566",
        "vestidor": [
            {
            "prenda": "bufanda",
            "cantidad": "1"
            },
            {
            "prenda": "media",
            "cantidad": "3"
            },
            {
            "prenda": "pantalón",
            "cantidad": "1"
            }
            ]
        }

    json_test = {"max": cliente1, "jorge": cliente2, "alejandro": cliente3}

    print('Imprimir json como un objeto')
    print(json_test)

    # Leer json y grabarlo en un archivo json
    
    with open('mi_json.json', 'w') as jsonfile:
        data = [json_test]
        json.dump(data, jsonfile, indent=4)


def deserializar():
    print("Funcion que lee un archivo JSON")
    # JSON Deserialize
    # Basado en la función  anterior debe abrir y leer el contenido
    # del archivo y guardarlo en un objeto JSON utilizando el método
    # load()

    # Luego debe convertir ese JSON data en json_string utilizando
    # el método "dumps" y finalmente imprimir en pantalla el resultado
    # Recuerde utilizar indent=4 para poder observar mejor el resultado
    # en pantalla y comparelo contra el JSON que generó en la función anterior
  
    # Leer json y mostrarlo por pantalla
    
    with open('mi_json.json', 'r') as jsonfile:
        json_data = json.load(jsonfile)
    
    print('Mostrar el contenido del archivo mi_json')
    print(json.dumps(json_data, indent=4))

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    serializar()
    deserializar()

    print("terminamos")