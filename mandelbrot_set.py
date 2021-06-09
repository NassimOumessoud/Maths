# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 10:48:43 2021

@author: Nassim
"""

import numpy as np
import matplotlib.pyplot as plt
import time


def arithmetic(z, c):
    try:
        return z**2+c
    
    except OverflowError:
        return complex(3, 3)
    
    
def gen_random_number(high, low, amount=1):
    random = np.random.rand(amount)*(np.abs(high)+np.abs(low))+low
    return np.around(random, decimals=3)


def normalize(max_value, value):
    real = int(max_value/2 + value.real*max_value/3)
    comp = int(max_value/2 + value.imag*max_value/3)
    return real, comp

    
N = 2e8
size = 4000
maximum = 2
minimum = -1.5
image = np.ones((size, size))*1000
t_1 = time.time()


for i in range(int(N)):
    comp_number = 0
    iteration = 0
 
    real = gen_random_number(maximum, minimum)
    comp = gen_random_number(maximum, minimum)
    starting_number = complex(real, comp)
    
        
    while comp_number.real <= 2 and comp_number.imag <= 2:
        
        comp_number = arithmetic(comp_number, starting_number)
            
        if iteration == 1000:
            x, y = normalize(size, starting_number)
            image[y, x] = 0
            break
        
        iteration += 1
        
        
    if iteration >= 100:
         x, y = normalize(size, starting_number)
         image[y, x] = 1000 - iteration

     
plt.imshow(image, cmap='nipy_spectral')
plt.colorbar()

t_2 = time.time()
dt = round((t_2 - t_1)/3600, 3)
print(f'This operation took {dt} hours')
        