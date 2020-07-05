# CRANK_02.py
# Calculation of Dynamic Heat Flow
# Example 2 in Bagda, Dlabal, Öztürk
# Calculation of temperature change and dynamic heat flow in a wall of cellular concrete
# and expanded polystyrene at  20 °C, if one side is cooled down to  0 °C.
# System design by Engin Bagda, Python programming by Erkam Talha Öztürk
# Version 2020_07_05

# Crank Nicolson function
def CrankNicolson():
    e[0] = 0
    f[0] = Temp[0]
    for i in range (1, n-1, 1):
        r = Lambda[i]*dTime / (Wkap[i]*Rho[i]*x[i]*x[i])
        K1 = Lambda[i-1]*x[i] / (Lambda[i]*x[i-1])
        K2 = Lambda[i]*x[i+1] / (Lambda[i+1]*x[i])
        g1 = r * (1 - K1) / (1 + K1)
        g2 = r * (1 - K2) / (1 + K2)
        a = r - g1
        b = 2 + (2*r) - g1 + g2
        c = r + g2
        d = (a * Temp[i-1]) + (2-(2*r)+g1-g2) * Temp[i] + (c*Temp[i+1])
        e[i] = c / (b - (a*e[i-1]))
        f[i] = (d + a*f[i-1]) / (b - a*e[i-1])

# Thomas algorithm
def ThomasAlgorithm():
    for i in range (n-2, 0, -1):
        Temp[i] = (e[i]*Temp[i+1]) + f[i]

# Calculation Heat Flow
def HeatFlowF():
    for i in range (0, n-1, 1):
        dTemp = float(Temp[i] - Temp[i+1])
        HF_1 = float(x[i]/(2*Lambda[i]))
        HF_2 = float(x[i+1]/(2*Lambda[i+1]))
        HeatFlow[i] = float(dTemp / (HF_1 + HF_2))

# Definitions
import numpy as arr # to set up arrays
global x, e, f, HeatFlow, n, dTime, Temp, Lambda, Rho, Wkap # global variables

n1 = 20 # layers for cellular concrete
n2 = 5 # layers for expanded polystyrene
n = n1 + n2 # index for layers from i=[0] to i=[n1+n2-1]

x = arr.empty(n)
e = arr.empty(n)
f = arr.empty(n)
Temp = arr.empty(n)
Lambda = arr.empty(n)
Rho = arr.empty(n)
Wkap = arr.empty(n)
HeatFlow = arr.empty(n)

# Set up of conditions and material properties

dTime = 60.00 # duration of the steps (s)

# Cellular concrete
for i in range (0, n1, 1): # n, because string stops at i=[n1-1]
    x[i] = 0.010 # thickness of each element
    Lambda[i] = 0.160 # thermal conductivity (W/m/K)
    Rho[i] = 550  # density (kg/m3)
    Wkap[i] = 1000 # heat capacity (Joule/m3)
    Temp[i] = 20 #°C, primary definition

# Expanded polystyrene
for i in range (n1, n, 1): # n, because string stops at i = [n1+n2-1]
    x[i] = 0.010 # thickness of each element
    Lambda[i] = 0.035 # thermal canductivity (W/m/K)
    Rho[i] = 15  # density (kg/m3)
    Wkap[i] = 1400 # heat capacity (Joule/m3)
    Temp[i] = 20 #°C, primary definition

# Main run
for Time in range (0, 5400, 1): # amount of time steps: 90 hours x  60 Minutes
    Temp[n-1] = 0 # °C new temperature after 1 Minute
    CrankNicolson()
    ThomasAlgorithm()
    HeatFlowF()
    print("%4.0f, %8.1f, %8.1f, %8.1f, %8.1f, %8.1f, %6.1f " % (Time, Temp[0], Temp[1], Temp[2], Temp[n - 3], Temp[n - 2], Temp[n - 1]))
    print("%4.0f, %8.2f, %8.2f, %8.2f, %8.2f, %8.2f, %6.1f " % (Time, HeatFlow[1], HeatFlow[2], HeatFlow[3], HeatFlow[n-4], HeatFlow[n-3], HeatFlow[n-2]))
    print()
# End of run
