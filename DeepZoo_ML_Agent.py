import os
os.system("pip install --ignore-installed  git+https://github.com/williamedwardhahn/DeepZoo")
from DeepZoo import *

env = start("Fox1")

for i in range(10):

    action = np.array([[1,0,0,0]])
    
    state,reward = step(env,action)

    plt.imshow(state)
    plt.show()

    
    
    
    
    
    
    
    
    
    
    
    
    
