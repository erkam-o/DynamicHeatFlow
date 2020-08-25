# BIOT_02.py
# Calculation of dynamic heat flow and surface temperatures of a wall in contact with air
# Example 2 in Bagda, Dlabal, Öztürk:
# Calculation of dynamic heat flow and surface temperatures of a wall at changing hourly  air temperatures
# System design by Engin Bagda, Python programming by Erkam Talha Öztürk
# Version 2020_07_15

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
import math # for cosine function
global x, e, f, HeatFlow, n, dTime, Temp, Lambda, Rho, Wkap #global variables

# Initialization values
n1 = 20 # elements for cellular concrete
n2 = 5 # elements for expanded polystyrene
n1 = n1 + 1 # one element is added  for  dummy i[0]
n2 = n2 + 1 # one element is added for dummy i[n]
n = n1 + n2 # sum of elements from i[0] to i[n1+n2-1]

x = arr.empty(n)
e = arr.empty(n)
f = arr.empty(n)
Temp = arr.empty(n)
Lambda = arr.empty(n)
Rho = arr.empty(n)
Wkap = arr.empty(n)
HeatFlow = arr.empty(n)


# Set up conditions and material properties

dTime = 60.00 # duration of the steps seconds

# Cellular concrete
for i in range (0, n1, 1): # loop stops at i[n1-1]
    x[i] = 0.010 # thickness of each element
    Lambda[i] = 0.160 # thermal conductivity W/m/K
    Rho[i] = 550  # density kg/m3
    Wkap[i] = 1000 # heat capacity Joule/m3
    Temp[i] = 20 #°C, primary definition

# Expanded polystyrene
for i in range (n1, n, 1): # loop stops at i[n1+n2-1]
    x[i] = 0.010 # thickness of each element
    Lambda[i] = 0.035 # thermal conductivity W/m/K
    Rho[i] = 15  # density kg/m3
    Wkap[i] = 1400 # Heat capacity Joule/m3
    Temp[i] = 20 #°C, primary definition

Heattrans_int = 1/0.13 # surface heat transition coefficient intern W/m2/K
Heattrans_ext = 1/0.04 # surface heat transition coefficient extern W/m2/K

Bi_int = (Heattrans_int*x[0])/(2*Lambda[0]) # Biot number intern
Bi_ext = (Heattrans_ext*x[n-1])/(2*Lambda[n-1]) # Biot number extern

# Main run

for Day in range (0, 6, 1): # calculation for days
    Sum_HeatFlow_int = 0 # to summarise the heat flow for a day intern
    Sum_HeatFlow_ext = 0 # to summarise the heat flow for a day extern

    for Hour in range (0, 24, 1): # calculation for hours

        Temp_air_int = 20
        Temp[0] = (Temp[1] * (1 - Bi_int) / (1 + Bi_int)) + (2 * Bi_int * Temp_air_int / (1 + Bi_int))

        # cosine function to oscillate Temp_air_ext with an amplitude of 6 K over 24 h around 20 °C
        Temp_air_ext = 20 - math.cos((2*math.pi/24)*Hour)*6

        Temp[n - 1] = (Temp[n - 2] * (1 - Bi_ext) / (1 + Bi_ext)) + (2 * Bi_ext * Temp_air_ext / (1 + Bi_ext))

        for Minute in range (0, 60, 1): # calculation for Minutes in steps of 60 seconds

            CrankNicolson()
            ThomasAlgorithm()
            HeatFlowF()

            Sum_HeatFlow_int = Sum_HeatFlow_int + HeatFlow[1]
            Sum_HeatFlow_ext = Sum_HeatFlow_ext + HeatFlow[n - 2]

        Temp_surface_int = (Temp[0]+Temp[1])/2
        Temp_surface_ext = (Temp[n-1]+Temp[n-2])/2

        print("%2.0f, %2.0f, %2.0f, %8.1f, %8.1f, %8.1f, %8.1f, %16.1f, %8.1f, %8.1f, %8.1f " % (Day, Hour, Minute, Temp_air_int, Temp[0], Temp_surface_int, Temp[1], Temp[n-2], Temp_surface_ext,Temp[n-1], Temp_air_ext))
        print("%30.2f, %8.2f, %26.2f, %8.2f " % (HeatFlow[1], Sum_HeatFlow_int, HeatFlow[n - 2], Sum_HeatFlow_ext))
        print()

    print()

print("Day Hour Min.  Air_int / Dummy_int / Surface_int T[1]            T[n-1] / Surface_ext / Dummy_ext / Air_ext  TEMPERATURES")
print("                         Hourly_int / Sum_int                    Hourly_ext /  Sum_ext                       HEAT FLOW")

# End of run
