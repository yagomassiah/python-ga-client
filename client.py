import requests
import json
from read_maze import Maze
import matplotlib.pyplot as plt
import numpy as np

""" plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show() """
print("something")

URL = 'http://localhost:3000/labirinto-genetico/'

Labirinto = Maze(r'M1.txt').oficial

payload =  {'labirinto': Labirinto} 


r = requests.post(url = URL, json = payload) 
data = r.json() 
plt.plot(data['nGeracoes'], data['fitnessGeral'])
plt.plot(data['nGeracoes'], data['fitnessDoMeio'])
plt.plot(data['nGeracoes'], data['mediaFitness'])
plt.ylabel('Fitness')
plt.xlabel('Gerações')
plt.show()


#a = np.asarray([ data['fitnessGeral'], data['fitnessDoMeio'], data['mediaFitness'] ])
a =  [ data['fitnessGeral'], data['fitnessDoMeio'], data['mediaFitness'] ]
np.savetxt("dados.csv", a, delimiter=",")

print(data['elite'])