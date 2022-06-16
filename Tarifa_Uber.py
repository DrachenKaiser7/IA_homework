import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
import sys
'''
Entradas
1.La demanda de viajes tendrá repercusión en el precio y la demanda sera determinada por baja, media o alta 
2.Las situaciones externas como el clima y condiciones del entorno también repercuten al costo variando como condiciones de viaje: Aceptables,complicadas y extremas
3.El precio del viaje puede aumentar dependiendo de la hora y la luz siendo que en el dia el precio es bajo, en la noche y muy temprano hay un aumento medio y en la madrugada un aumento alto
Salidas
1.El porcentaje que sera el multiplicador del agregado de la tarifa dinamica 

'''
if len(sys.argv) > 3:

    dem_viaje = sys.argv[1] #Demanda de autos en viaje

    cond_viaje = sys.argv[2] #Condiciones de viaje 

    hora_viaje = sys.argv[2] #Hora de viaje
    
else:

    dem_viaje = 8

    cond_viaje = 5

    hora_viaje = 7

print("[INFO] Usando valores por defecto")

print("[INFO] Multiplicador de demanda de viaje:{}/10".format(dem_viaje))

print("[INFO] Valor de la dificultad de las condiciones de viaje :{}/10".format(cond_viaje))

print("[INFO] Valor de la dificultad de las condiciones de viaje :{}/10".format(cond_viaje))


x_dem = np.arange(0, 11, 1)

x_cond = np.arange(0, 11, 1)

x_hora = np.arange(0, 25, 1)

x_tarifa = np.arange(15, 40, 1)

qual_lo = fuzz.trimf(x_qual, [0, 0, 5]) # —- 0-1 5-0 \ (v1, 0), (v2, 1), (v3,0 )

qual_md = fuzz.trimf(x_qual, [0, 5, 10]) # 0-0 5-1 10-0 /\

qual_hi = fuzz.trimf(x_qual, [5, 10, 10])# 5-0 10-1 —- /

serv_lo = fuzz.trimf(x_serv, [0, 0, 5]) # —- 0-1 5-0 \

serv_md = fuzz.trimf(x_serv, [0, 5, 10]) # 0-0 5-1 10-0 /\

serv_hi = fuzz.trimf(x_serv, [5, 10, 10])# 5-0 10-1 —- /

tip_lo = fuzz.trimf(x_tip, [5, 5, 13]) # —- 5-1 13-0 \

tip_md = fuzz.trimf(x_tip, [5, 13, 25]) # 5-0 13-1 25-0 /\

tip_hi = fuzz.trimf(x_tip, [13, 25, 25]) # 13-0 25-1 —- /