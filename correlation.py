'''
This refresher will help to use
numpy with data for correlation
purposes

Task:
    [ ] Use numpy with pandas
    [ ] Making sure all formats
        of variables can be used 
        with this module
'''
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

def correlate(x,y):
    '''
    To do correlation between
    two variables, we use
    
    numpy.correff() method
    
    The output would be
    an array
    '''
    return np.corrcoef(x,y)[0,1]
    
def numpy_visualize(x,y):
    '''
    Visualize two variables
    or the visualization of
    multiple variable
    '''

    matplotlib.style.use('ggplot')
    plt.scatter(x,y)
    plt.show

def pandas_visualize(x):
    '''
    Using pandas.Dataframe class to
    visualize a correlation
    '''


def multiple_visualize(x):
    '''
    this function visualize
    multiple scatterplot using
    pandas.Dataframe class

    x must be a pandas.Dataframe class
    '''

 
#	df = pd.DataFrame({'a': np.random.randint(0, 50, 1000)})
#	df['b'] = df['a'] + np.random.normal(0, 10, 1000) # positively correlated with 'a'
#	df['c'] = 100 - df['a'] + np.random.normal(0, 5, 1000) # negatively correlated with 'a'
#	df['d'] = np.random.randint(0, 50, 1000) # not correlated with 'a'
#	df.corr() using panda to find correlation

    pd.scatter_matrix(x, figsize=(6,6))
    plt.show()

def readcsv(file_location):
    '''
    using pandas to read a csv file
    using pandas.Dataframe.read_csv() function
    '''
    return pd.read_csv(file_location)

def readexcel(file_location,multi_sheets=True):
    '''
    using pandas.Dataframe.read_excel() method
    
    For multiple sheets, the list of sheets
    can be called using
    
    xls =pd.ExcelFile('location_file')
    xls.sheet_names
    '''
    
    if mutli_sheets:
        return pd.ExcelFile(file_location)
    else
        return pd.read_excel(file_location)


