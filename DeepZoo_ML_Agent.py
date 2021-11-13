# import os
# os.system("pip install --ignore-installed  git+https://github.com/williamedwardhahn/DeepZoo")
# Action Vector: 
# Dim0 -> 1 Foward / 2 Reverse, 
# Dim1 -> 1 Strafe Right / 2 Strafe Left, 
# Dim2 -> 1 Turn Counter / 2 Turn Clock, 
# Dim3 -> 0 Null / 1 Null
#########################################
from DeepZoo import *

env = start("Fox2")

for i in range(10):

    action = np.array([[1,0,0,0]])      
    
    state,reward = step(env,action)

    plot(state)
    print(reward)
