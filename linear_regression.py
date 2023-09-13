#Language: Python
#Author: Cerberus16731

"""
                                                                      --DOCSTRING--
This program takes data from the attached csv dataset and performs linear regression on salary and years of experience. 
Linear regression has been implemented from scratch without machine learning librarie like scikit-learn or tensorflow.
Pandas is being used for using the csv file and removing nan.
Numpy is being used for faster processing.
Matplotlib is being used to plot graphs.
"""

#importing dependancies
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

#linear regression for x,y both numbers
def linear_regression(x,y):
    xnew = np.array(range(int(min(x)),int(max(x))))
    x,y = np.array(x),np.array(y)
    m = np.sum((x-(np.average(x)))*(y))/np.sum((x-np.average(x))*(x-np.average(x)))
    c = np.average(y) - m*np.average(x)
    ynew = (m*xnew) + c
    return xnew, ynew
   
def main():
     data = pd.read_csv(r"Kaggle_Salary_Data.csv").dropna()
     #if this gives you file does not exist error goto current working directory and put the csv file there
     xin,yin = list(data.loc[:,"Years of Experience"]),list(data.loc[:,"Salary"])
     x,y = linear_regression(xin,yin)
     plt.plot(x,y,color = "red")
     plt.scatter(xin,yin,color="blue")
     plt.show()

    

if __name__ == '__main__':
     main()