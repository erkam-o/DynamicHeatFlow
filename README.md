# DynamicHeatFlow
Calculation of Dynamic Heat Flow in Walls

Engin Bagda, Milan Dlabal, Erkam Talha Öztürk

Full report of the program can be found here.

Assessment of the energy balance of buildings depends on estimations of the temperature driven dynamic heat flow through walls between inside and outside. ISO 13790:2008-03-01 “Energy performance of buildings – Calculation of energy use for space heating and cooling” mentions different methods to calculate the dynamic heat transfer in walls at hourly changing temperatures.
In this work the Crank-Nicolson Method in combination with the Thomas algorithm is used to calculate dynamic heat transfer through walls.

The Python code CRANK_01.py (version 2020.07.05) is an example to calculate the temperature change in a wall of cellular concrete with 0.2m thickness in time steps of 60 seconds, when the temperature on one side decreases from 20°C to 0°C. The elements have a thickness of 0.01 m and the wall is virtually divided in 20 elements. The code contains an output command where the temperatures in the first and last 4 elements i[0], i[1], i[2], i[3], i[16], i[17], i[18], i[19] are printed for each time step. The first lines are important to control whether the system is oscillating or not.
Steady state is reached when the temperature differences between all layers are the same. In the example this is at minute 1402 where the temperature of the element i[1] is stable at 18.9°C to one decimal place. The time to reach the steady state depends on the accuracy.

The Python code CRANK_02.py (version 2020.07.05) is an example to calculate the temperature change in a wall consisting of two different materials in time steps of 60 seconds. The wall consists of 0.2 m cellular concrete, 0.05 m expanded polystyrene (EPS) and is virtually divided into 25 elements of 0.01 m thickness. The temperature in the element i[n-1] decreases from 20 °C to 0 °C.
The output command prints the temperatures in the first and last 4 elements i[0], i[1], i[2], i[3], i[16], i[17], i[18], i[19] and the heat flows between the elements i[0]-i[1], i[1]-i[2], i[2]- i[3], i[3]-i[4], i[20]-i[21], i[21]-i[22], i[22]-i[23] and i[23]-i[24].


Calculation of convection induced dynamic heat flow in walls

Full report of the program can be found here.

The energy balance of a building and the thermal comfort inside are depending on the surrounding air temperatures and their changes. Daily changing air temperatures cause dynamic heat flows in walls. This work explains the calculation of dynamic heat flows in walls with the Crank-Nicolson method in combination with the Biot number. The Biot number is a dimensionless quantity, expressing the ratio of the heat transfer from inside a body to the surface and from the surface to the surrounding air.
The Python code BIOT_01.py is an example to calculate dynamic heat flow and temperature profile in a wall after an abrupt outside temperature change from 20°C to 0°C. The example uses a wall consisting of 0.2 m cellular concrete and 0.05 m expanded polystyrene. It is analysed when the system is mathematically settled and stable, the results are controlled with the static heat equation.
The Python code BIOT_02.py is an example to calculate dynamic temperature profiles and heat flows in a wall when the air temperature changes periodically with a cosine step function. The cosine function simulates the hourly temperature changes in a period of 24 hours. The influence of the thermal conductivity and heat capacity on lag and damping of the temperature amplitude are analysed.
