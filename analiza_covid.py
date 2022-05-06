#lab3 problema 5 hewel.ochoa@utp.ac.pa
import matplotlib.pyplot as plt
import csv
import numpy as np

with open('covid_panama.csv', newline='') as file:
    lector = csv.reader(file)
    # tendencia para el total de casos
    xT = []
    yT =  []
    # tendencia para los casos nuevos
    xN = []
    yN = []
    #para captar los casos nuevos del histograma
    # tambien los usare para graficas lineales....creo
    xH = []
    yH = []
    takeny = []
    """--------------capta los totales
    for row in lector:
        xT.append(np.array(row[1])) 
        yT.append(np.array(row[2]))
    -----------------------------"""
    """--------capta los casos nuevos
    for row in lector:
        xN.append(np.array(row[1])) 
        yN.append(np.array(row[3]))
    --------------------------------"""
    for row in lector:
        xH.append(np.array(row[0])) 
        yH.append(np.array(row[2]))    

    """--------------------grafica de tendencias------------------
    plt.plot(xN,yN, color = 'blue', linewidth=3, label = 'linea')
    plt.title('grafica de tendecia')"""
    
    xH.pop(0)
    yH.pop(0)
    """---------------------grafica logaritmica--------------------
    plt.plot(xN, yN)
    plt.yscale('log')
    plt.title('escala logaritmica')
    """
    """-------------histograma-------------------------------------
    plt.hist(yH,bin=len(xH), histtype='bar', rwidth=0.8, color='blue')
    plt.title('Histograma')
    ---------------------------------------------------------------"""
    fresh_par = np.polyfit(np.array(xH, dtype=int),np.array(yH, dtype=int),3)
    takeny = np.polyval(fresh_par,np.array(xH, dtype=int))
    plt.subplot(222)
    #print("todo bien")
    
    plt.plot(xH,takeny, color = 'blue', linewidth=3, label = 'linea')
    plt.grid(True)
    plt.legend()
    plt.show()