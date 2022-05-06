# problema 6 hewel.ochoa@utp.ac.pa
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

lector = pd.read_csv('DatasaurusDozen.csv', header=0)

take_nom = lector['dataset']
CoordDino = lector[take_nom == 'dino']
CoordAway = lector[take_nom == 'away']
CoordHlin = lector[take_nom == 'h_lines']
CoordVlin = lector[take_nom == 'v_line']
CoordXshape = lector[take_nom == 'x_shape']
CoordStar = lector[take_nom == 'star']
CoordHigLin = lector[take_nom == 'high_lines']
CoordDots = lector[take_nom == 'dots']
CoordCircle = lector[take_nom == 'circle']
CoordBull = lector[take_nom == 'bullseye']
CoordSlantU = lector[take_nom == 'slant_up']
CoordSlantD = lector[take_nom == 'slant_down']
CoordWide = lector[take_nom == 'wide_lines']


#---el arreglo contiene los calculos de las 12+1 formas['promedioX','promedioY','varianzaX','varianzay','correlacion de x y']
mediDino = [np.mean(CoordDino['x']),np.mean(CoordDino['y']),np.std(CoordDino['x']),np.std(CoordDino['y']),np.corrcoef(CoordDino['x'],CoordDino['y'])]
mediAway = [np.mean(CoordAway['x']),np.mean(CoordAway['y']),np.std(CoordAway['x']),np.std(CoordAway['y']),np.corrcoef(CoordAway['x'],CoordAway['y'])]
mediHlin = [np.mean(CoordHlin['x']),np.mean(CoordHlin['y']),np.std(CoordHlin['x']),np.std(CoordHlin['y']),np.corrcoef(CoordHlin['x'],CoordHlin['y'])]
mediVlin = [np.mean(CoordVlin['x']),np.mean(CoordVlin['y']),np.std(CoordVlin['x']),np.std(CoordVlin['y']),np.corrcoef(CoordVlin['x'],CoordVlin['y'])]
mediXshape = [np.mean(CoordXshape['x']),np.mean(CoordXshape['y']),np.std(CoordXshape['x']),np.std(CoordXshape['y']),np.corrcoef(CoordXshape['x'],CoordXshape['y'])]
mediStar = [np.mean(CoordStar['x']),np.mean(CoordStar['y']),np.std(CoordStar['x']),np.std(CoordStar['y']),np.corrcoef(CoordStar['x'],CoordStar['y'])]
mediHigLin = [np.mean(CoordHigLin['x']),np.mean(CoordHigLin['y']),np.std(CoordHigLin['x']),np.std(CoordHigLin['y']),np.corrcoef(CoordHigLin['x'],CoordHigLin['y'])]
mediDots = [np.mean(CoordDots['x']),np.mean(CoordDots['y']),np.std(CoordDots['x']),np.std(CoordDots['y']),np.corrcoef(CoordDots['x'],CoordDots['y'])]
mediCircle = [np.mean(CoordCircle['x']),np.mean(CoordCircle['y']),np.std(CoordCircle['x']),np.std(CoordCircle['y']),np.corrcoef(CoordCircle['x'],CoordCircle['y'])]
mediBull = [np.mean(CoordBull['x']),np.mean(CoordBull['y']),np.std(CoordBull['x']),np.std(CoordBull['y']),np.corrcoef(CoordBull['x'],CoordBull['y'])]
mediSlantU = [np.mean(CoordSlantU['x']),np.mean(CoordSlantU['y']),np.std(CoordSlantU['x']),np.std(CoordSlantU['y']),np.corrcoef(CoordSlantU['x'],CoordSlantU['y'])]
mediSlantD = [np.mean(CoordSlantD['x']),np.mean(CoordSlantD['y']),np.std(CoordSlantD['x']),np.std(CoordSlantD['y']),np.corrcoef(CoordSlantD['x'],CoordSlantD['y'])]
mediWide = [np.mean(CoordWide['x']),np.mean(CoordWide['y']),np.std(CoordWide['x']),np.std(CoordWide['y']),np.corrcoef(CoordWide['x'],CoordWide['y'])]

#--------muestra dos graficas una del datasaurio y la otra de 3x4 para las otras 12

plt.subplot(1,2,1)
plt.figure(figsize=(4,4))
plt.scatter(CoordDino['x'], CoordDino['y'], label = 'dino', color = 'green')
plt.grid()
plt.title('grafica del datasaurus')
plt.legend()
plt.show()

plt.subplot(2,1,2)
plt.figure(figsize=(3,4))
plt.scatter(CoordStar['x'], CoordStar['y'], label = 'star', color = 'blue')
plt.grid()
plt.title('grafica de la dozena')
plt.legend()
plt.show()

