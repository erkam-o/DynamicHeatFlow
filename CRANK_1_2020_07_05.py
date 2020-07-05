# CRANK_01.py
# Calculation of Dynamic Heat Flow
# Example 1 in Bagda, Dlabal, Öztürk
# Calculation of temperature change in a wall  of cellular concrete
# at 20 °C,  if one side is cooled down to 0 °C.
# System design by Engin Bagda, Python programming by Erkam Talha Öztürk
# Version 2020_07_05

# Crank Nicolson function
def CrankNicolson():
    e[0] = 0
    f[0] = Temp[0]
    for i in range (1, n-1, 1):
        r = Lambda[i]*dTime / (Wkap[i]*Rho[i]*x[i]*x[i])
        K1 = Lambda[i-1]*x[i] / (Lambda[i]*x[i-1])
        K2 = Lambda[i]*x[i+1] / (Lambda[i+1]*x[i])
        a = r
        b = 2 + (2*r)
        c = r
        d = (a * Temp[i-1]) + (2-(2*r)) * Temp[i] + (c*Temp[i+1])
        e[i] = c / (b - (a*e[i-1]))
        f[i] = (d + a*f[i-1]) / (b - a*e[i-1])

# Thomas algorithm
def ThomasAlgorithm():
    for i in range (n-2, 0, -1):
        Temp[i] = (e[i]*Temp[i+1]) + f[i]

# Definitions
import numpy as arr # to set up arrays
global x, e, f, HeatFlow, n, dTime, Temp, Lambda, Rho, Wkap #global variables

n = 20 # index for layers

x = arr.empty(n)
e = arr.empty(n)
f = arr.empty(n)
Temp = arr.empty(n)
Lambda = arr.empty(n)
Rho = arr.empty(n)
Wkap = arr.empty(n)

# Setup of conditions and  material properties

dTime = 60.00 # s, duration of the time steps

for i in range (0, n, 1): # loop stops at i[n-1]
    x[i] = 0.010 # thickness of each element
    Lambda[i] = 0.160 # thermal conductivity (W/m/K)
    Rho[i] = 550  # density (kg/m3)
    Wkap[i] = 1000 # heat capacity (Joule/m3)
    Temp[i] = 20 #°C, primary definition

# Main run
for Time in range (0, 1440, 1): # ammount of time steps  24 hours x 60 minutes
    Temp[n-1] = 0 # °C new temperature after 1 minute (boundary condition in elemnt i[n-1]
    CrankNicolson()
    ThomasAlgorithm()
    print("%4.0f, %6.1f, %8.1f, %8.1f, %8.1f, %8.1f, %8.1f, %8.1f, %6.1f " % (Time, Temp[0], Temp[1], Temp[2], Temp[3], Temp[n-4], Temp[n-3], Temp[n-2], Temp[n-1]))
# End of run
