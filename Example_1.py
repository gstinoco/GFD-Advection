"""
All the codes presented below were developed by:
    Dr. Gerardo Tinoco Guerrero
    Universidad Michoacana de San Nicolás de Hidalgo
    gerardo.tinoco@umich.mx

With the funding of:
    National Council of Humanities, Sciences and Technologies, CONAHCyT (Consejo Nacional de Humanidades, Ciencias y Tecnologías, CONAHCyT). México.
    Coordination of Scientific Research, CIC-UMSNH (Coordinación de la Investigación Científica de la Universidad Michoacana de San Nicolás de Hidalgo, CIC-UMSNH). México
    Aula CIMNE-Morelia. México

Date:
    July, 2023.

Last Modification:
    October, 2023.
"""

# Library importation
import numpy as np
from Scripts.run import run_simulation

# State the conditions for the problem.
## Problem Parameters
a = 0.3                                                                                     # Transport velocity on the x direction.
b = 0.2                                                                                     # Transport velocity on the y direction.
t = 2000                                                                                    # Number of time-steps.

## Function for the problem.
f = lambda x, y, t, a, b, c1, c2: 0.2*np.exp((-(x-c1-a*t)**2-(y-c2-b*t)**2)/.01)

# Should I save the results?
save = True

# Environment Variables for the functions
exam = 'Example 1'

# Run simulation with clouds.
data = 'Data/Clouds/'
print('Simulations for Simply Connected domains.')
run_simulation(f, a, b, t, implicit = False, data = data, exam = exam, holes = False, save = save)