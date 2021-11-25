# JSON ETL [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

import json
import requests

import matplotlib.pyplot as plt

import seaborn as sns


# Defino el estilo para todos los gráficos
sns.set_theme(style="white", context="talk")



def bar_plot(usuario, terminado, no_terminado):

    # Set up the matplotlib figure
    f, (ax1, ax2) = plt.subplots(2, 1, figsize=(7, 5), sharex=True)

    # Generate some sequential data
    
    sns.barplot(x=usuario, y= no_terminado, ax=ax1)
    ax1.axhline(0, color="k", clip_on=False)
    ax1.set_ylabel("Incompleto")

    # Center the data to make it diverging
    sns.barplot(x=usuario, y=terminado,  ax=ax2)
    ax2.axhline(0, color="k", clip_on=False)
    ax2.set_ylabel("Terminado")

    # Finalize the plot
    sns.despine(bottom=True)
    plt.setp(f.axes, yticks=[])
    plt.tight_layout(h_pad=2)


    
    plt.show()



if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    # Ejercicio de consumo de datos por API
    url = "https://jsonplaceholder.typicode.com/todos"

    # El primer paso es que copien esa URL en su explorador web
    # y analicen los datos en general:
    # 1) Observando la URL se puede ver que en total hay 200 entradas,
    # del id=1 al id=200
    # 2) Observando la URL se puede ver que en total hay 10 usuarios,
    # del userId=1 al userId=10
    # 3) En cada entrada se especifica si el usuario completó ese título,
    # mediante el campo "completed".


    # Alumno, de cada usuario en el total de las 200 entradas
    # debe contar cuantos títulos completó cada usuario (de los 10 posibles)
    # y armar un gráfico de barras resumiendo la información.
    # gráfico en el eje "x" está cada uno de los 10 usuarios y en el eje
    # "y" la cantidad de títulos completados

    # Para poder ir haciendo esto debe ir almacenando la información
    # de cada usuario a medida que "itera" en un bucle los datos
    # del JSON recolectado. Al finalizar el bucle deberá tener la data
    # de los 10 usuarios con cuantos títulos completó cada uno.

    # Debe poder graficar dicha información en un gráfico de barras.
    # En caso de no poder hacer el gráfico comience por usar print
    # para imprimir cuantos títulos completó cada usuario
    # y verifique si los primeros usuarios (mirando la página a ojo)
    # los datos recolectados son correctos.


    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    # Se puede obtener el objeto JSON de dos formas distintas
    data = json.loads(response.text)
    data = response.json()
    print('Imprimir los datos traídos de la nube')
    print(json.dumps(data, indent=4))

    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    data = response.json()
    #print(data)

    # Defino las variables y las lista que voy a utilizar
    i = 0
    userid = data[0]['userId']
    usuario = []
    terminado = []
    no_terminado = []

    usuario.append(userid)
    terminado.append(0)
    no_terminado.append(0)
           
    for user in data:
        if user['userId'] == userid:
            # No mostrar más de 2 usuarios
            # para no ocupar toda la pantalla con mensajes
            #print('El usuario {} completó {}? {}'.format(user['userId'],
            #                                          user['title'],
            #                                          user['completed']
            #                                          ))
            if(user['completed'] == True):
                terminado[i] += 1
            else:
                no_terminado[i] += 1

        else:
            #print('El usuario {} completó {}? {}'.format(user['userId'],
            #                                          user['title'],
            #                                          user['completed']
            #                                          ))
            userid = user['userId']
            print (userid)
            usuario.append(userid)
            terminado.append(0)
            no_terminado.append(0)
            i += 1
            if(user['completed'] == 'true'):
                terminado[i] = 1
                no_terminado[i] = 0
            else:
                no_terminado[i] = 1
                terminado[i] = 0
                
    bar_plot(usuario, terminado, no_terminado)


    print("terminamos")