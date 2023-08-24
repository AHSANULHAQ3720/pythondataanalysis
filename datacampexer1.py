# You are about to import your first file from the web! The flat file you will import will be 'winequality-red.csv' from the University of California, Irvine's Machine Learning repository. The flat file contains tabular data of physiochemical properties of red wine, such as pH, alcohol content and citric acid content, along with wine quality rating.
# The URL of the file is
# https://assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'
# After you import it, you'll check your working directory to confirm that it is there and then you'll load it into a pandas DataFrame.

from urllib.request import urlretrieve
import pandas as pd
url = 'https://assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'

urlretrieve(url,"whilesourcecsv.csv")

df = pd.read_csv('whilesourcecsv.csv',sep=',')

print(df.head())
