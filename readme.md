##Neural Network - Perceptron
####By David Anthony Bell
#### An entry level perceptron based Neural Network, heavily inspired by:
####https://www.youtube.com/watch?v=kft1AJ9WVDk
#### The input shows that if the array starts with a 1, the output is 1.
###Example set
INPUTS | INPUTS | INPUTS | OUTPUT
--- | --- | --- | ---
0 | 0 | 1 | 0 
1 | 1 | 1 | 1 
1 | 0 | 1 | 1 
0 | 1 | 1 | 0 
#### This simple model learns this through utilisation of the sigmoid function.
#### Run, and observe 'Outputs after training' - note their value are close to training outputs (line 22, perceptron.py) .
#### Adjust range in line 31 in perceptron.py for greater accuracy - though do note, output will never exactly be 1. 