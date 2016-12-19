import numpy as np
def polyfit(x, y, degree):
    results={}

    coeffs=np.polyfit(x, y, degree)
     # Polynominal Coefficients
    results['polynominal']=coeffs.tolist()

    # r-squared
    p = np.poly1d(coeffs)
    # fit values, and mean
    yhat = p(x)                         # or [p(z) for z in x]
    ybar = np.sum(y)/len(y)          # or sum(y)/len(y)
    ssreg = np.sum((yhat-ybar)**2)   # or sum([ (yihat - ybar)**2 for yihat in yhat])
    sstot = np.sum((y - ybar)**2)    # or sum([ (yi - ybar)**2 for yi in y])
    results['determination'] = ssreg / sstot


    return results
x=[14345,212343,3323434,445667,523324]
y=[2367.988,3234.899,4554.998,6344.9888,8886.654]
print(polyfit(x, y, 2))