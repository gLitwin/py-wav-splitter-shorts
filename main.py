
#! README:
#CO'MO SE USA ESTE SCRIPT?
#PARA EJECUTARLO, EL ARCHIVO MAIN.PY TIENE QUE ESTAR EN UNA CARPETA DONDE EXISTAN OTRAS DOS CARPETAS
#LLAMADAS "input" Y "output", por ejemplo:
#
# - mi-carpeta
#     L main.py
#     L input
#     L output
#
# con la terminal nos paramos sobre "mi-carpeta" y corremos el comando "python main.py" (o el python que corresponda)
# el programa tomara' todos los archivos .wav de la carpeta input y dejara' los segmentos de cada uno en la carpeta output
# ejemplo:
# 
# - mi-carpeta
#     L main.py
#     L input
#        L mi-cancion.wav
#     L output
#        L mi-cancion--segmento-0-50seg.wav
#        L mi-cancion--segmento-1-50seg.wav
#        L mi-cancion--segmento-1-50seg.wav
#
#!fin README.



from pydub import AudioSegment
import math
import glob

print(glob.glob("/home/adam/*"))


def main():
    #PARAMETROS DE EJECUCIO'N
    #MODIFICAR A GUSTO
    flag_segmentar_final_residual=True
    largo_shorts_segundos=50
    input_folder = './input'
    output_folder = './output'

    #FIN DE LOS PARAMETROS DE EJECUCIO'N
    #HACIA ABAJO NO MODIFICAR
    print('\n\nParámetros de ejecución:')
    print(f'\tflag_segmentar_final_residual: {flag_segmentar_final_residual};\n\tlargo_shorts_segundos: \t{largo_shorts_segundos};\n\tinput_folder: \t{input_folder};\n\toutput_folder: \t{output_folder}')
    print('\npuede modificar los parámetros en las primeras lineas de la funcion main en el archivo main.py')
    files_to_input = glob.glob(f'{input_folder}/*.wav')
    print('\nA procesar:')
    print(tomar_archivos_sin_extension_forEach(files_to_input))
    for audio_url in files_to_input:
        audio_nombre = tomar_archivo_sin_extension(audio_url)
        print('\nProcesando:')
        print(audio_nombre)
        main_body(audio_nombre, flag_segmentar_final_residual,largo_shorts_segundos, output_folder, input_folder)

def tomar_archivo_sin_extension(url):
    url = url.split('\\')
    archivo_sin_extension = url[len(url)-1].split('.')[0]
    return archivo_sin_extension

def tomar_archivos_sin_extension_forEach(url_array):
    array_final = []
    for url in url_array:
        array_final.append(tomar_archivo_sin_extension(url))
    return array_final

def main_body(audio_nombre, flag_segmentar_final_residual, largo_shorts_segundos, directorio_destino, directorio_origen,):
    audio_url = f'{directorio_origen}/{audio_nombre}.wav'
    audio = AudioSegment.from_file(audio_url)
    audio_length = math.trunc(len(audio) / (1000*largo_shorts_segundos)) #cuántos segmentos pueden sacarse
    print('Nro de iteraciones:')
    print(math.ceil(len(audio) / (1000*largo_shorts_segundos)))
    print('INICIO')
    for i in range(0, audio_length):
        nombre = f'{audio_nombre}--segmento{i}-{largo_shorts_segundos}seg.wav'
        inicio = i*largo_shorts_segundos
        fin = inicio + largo_shorts_segundos
        print(f'\n{inicio,fin}')
        cortar_segmento_wav(audio_url, directorio_destino, nombre, inicio, fin )
    if(flag_segmentar_final_residual and isinstance(len(audio), int)):
        i = math.trunc(len(audio) / (1000*largo_shorts_segundos))
        inicio = i*largo_shorts_segundos
        fin = len(audio)/1000
        nombre = f'{audio_nombre}--segmento{i}-{math.trunc(fin-inicio)}seg.wav'
        print(f'\n{inicio,fin}')
        cortar_segmento_wav(audio_url,directorio_destino, nombre,inicio,fin)
    print('FIN')
    return

def cortar_segmento_wav(audio_url, directorio_destino, nombre, inicio, fin):
    t1 = inicio * 1000 #Works in milliseconds
    t2 = fin * 1000
    newAudio = AudioSegment.from_wav(audio_url) #WAV
    newAudio = newAudio[t1:t2]
    newAudio.export(f'{directorio_destino}/{nombre}', format="wav")
    print(nombre)

if __name__ == "__main__":
    main()
"""     # total arguments
    n = len(sys.argv)
    print("\nTotal arguments passed:", n)
    # Arguments passed
    print("\nName of Python script:", sys.argv[0])
    print("\nArguments passed:", end = " ")
    for i in range(1, n):
        print(sys.argv[i], end = " ")
    main(sys.argv[1], sys.argv[2]) """