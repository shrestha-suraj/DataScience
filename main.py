
from __future__ import division
import numpy as np
import neuro

input =[[0.0,0.0,1.0,1.0,1.0,
         1.0,0.0,0.0,1.0,0.0,
         0.0,1.0,0.0,0.0,0.0,
         1.0,0.0,1.0,0.0,1.0,
         0.0,1.0,0.0,0.0,0.0]]

traget=[[1.0]]
reps=1000
network=[]
network=neuro.setup_network(input)
neuro.train(network,input,traget,reps)
neuro.writeNetworkToFile("myNetwork.net",network)
test_input=[1.0,1.0,1.0,1.0,1.0,
            1.0,1.0,1.0,1.0,1.0,
            0.0,1.0,0.0,0.0,0.0,
            1.0,0.0,1.0,1.0,1.0,
            1.0,1.0,0.1,0.0,1.0]
pred=neuro.predict(network,test_input)
pred=round(pred)
if pred==1:
    print "It is a maze"
else:
    print "It is not a maze"
