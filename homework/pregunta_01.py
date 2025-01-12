# pylint: disable=import-outside-toplevel

import pandas as pd
import matplotlib.pyplot as plt
import os
from glob import glob

def pregunta_01():
    '''
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    '''
    def create_ouptput_directory(output_directory: str):    # Función auxiliar para crear y limpiar el directorio de salida
        if os.path.exists(output_directory):
            for file in glob(f'{output_directory}/*'):
                os.remove(file)
            os.rmdir(output_directory)
        os.makedirs(output_directory)
    in_path = 'files/input'                                 # Path del directorio de inputs
    out_path = 'files/plots'                                # Path del directorio de outputs

    df = pd.read_csv(f'{in_path}/news.csv', index_col = 0)  # Importar el dataset

    plt.figure()                                            # Creación de una nueva figura
    colors = dict(zip(df.columns,                           # Diccionario para colores de líneas
                      ['dimgray', 'grey', 'tab:blue', 'lightgrey']))
    zorder = dict(zip(df.columns,                           # Diccionario para orden de 'importancia' de líneas
                      [1,1,2,1]))
    linewidths = dict(zip(df.columns,                       # Diccionario para el grosor de líneas
                          [2,2,3,2]))
    for col in df.columns:                                  # Iterar sobre las columnas del directorio
        plt.plot(df[col],                                   # Crear una nueva línea con la columna
                 color = colors[col],                       # Añadir color según el diccionario de colores
                 label = col,                               # Asignar a la línea el nombre de la columna
                 zorder = zorder[col],                      # Añadir el orden de 'importancia' de la línea
                 linewidth = linewidths[col])               # Añadir el grosor de la línea
    
    plt.title('How people get their news', fontsize = 16)   # Añadir título al gráfico

    plt.gca().spines['top'].set_visible(False)              # Hacer invisible el eje horizontal superior
    plt.gca().spines['left'].set_visible(False)             # Hacer invisible el eje vertical izquierdo
    plt.gca().spines['right'].set_visible(False)            # Hacer invisible el eje vertical derecho
    plt.gca().axes.get_yaxis().set_visible(False)           # Hacer invisible el eje Y (números y métricas)
    
    first_year = df.index[0]                                # Extraer el primer año del dataset
    last_year = df.index[-1]                                # Extraer el último año del dataset
    for col in df.columns:                                  # Iterar sobre las columnas del dataset
        plt.scatter(x = first_year,                         # Añadir una marca en cada comienzo de línea
                    y = df[col][first_year],
                    color = colors[col],                    # Añadir el mismo color de la línea a la marca
                    zorder = zorder[col])                   # Añadir el orden de 'importancia' a la marca
        
        plt.text(x = first_year - 0.2,                      # Añadir texto a la marca
                 y = df[col][first_year],
                 s = col + ' ' + str(df[col][first_year]) + '%',
                 ha = 'right',                              # Alinear el texto a la izquierda del punto (x,y)
                 va = 'center',                             # Alinear el texto verticalmente al centro
                 color = colors[col])                       # Añadir el mismo color de la marca al texto
        
        plt.scatter(x = last_year,                          # Añadir una marca al final de cada línea
                    y = df[col][last_year],
                    color = colors[col],                    # Añadir el mismo color de la línea a la marca
                    zorder = zorder[col])                   # Añadir el orden de 'importancia' a la marca
        
        plt.text(x = last_year + 0.2,                       # Añadir texto a la marca
                 y = df[col][last_year],
                 s = str(df[col][last_year]) + '%',
                 ha = 'left',                               # Alinear el texto a la derecha del punto (x,y)
                 va = 'center',                             # Alinear el texto verticalmente al centro
                 color = colors[col])                       # Añadir el mismo color de la marca al texto
        
    plt.tight_layout()                                      # Ajustar el tamaño de la figura a los elementos de la misma
    create_ouptput_directory(out_path)                      # Creación y limpieza del directorio de salida
    plt.savefig(f'{out_path}/news.png')                     # Guardar el gráfico