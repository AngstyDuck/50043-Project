import statistics
import numpy as np

def pearsonCoefficient(x,y):
    xBar = statistics.mean(x)
    yBar = statistics.mean(y)
    x = np.matrix(x)
    y = np.matrix(y)
    numerator = np.multiply(np.subtract(x,xBar),np.subtract(y,yBar)).sum()
    denominator = (np.square(np.subtract(x,xBar)).sum()*np.square(np.subtract(y,yBar)).sum())
    return(numerator/denominator)