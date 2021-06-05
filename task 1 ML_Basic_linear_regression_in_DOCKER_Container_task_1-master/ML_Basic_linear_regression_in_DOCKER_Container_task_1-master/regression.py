 
from sklearn.linear_model import LinearRegression
 
import pandas
#fetching data from Book1.csv file for data set
db=pandas.read_csv("SalaryData.csv")


#x is faeture  ie independent variable
x=db["YearsExperience"]


#x is target  ie dependent variable
y=db["Salary"]

#converting x and y into numpy format
x=x.values
y=y.values

#making 2d array
x=x.reshape(-1,1)
y=y.reshape(-1,1)

#model creation
mind=LinearRegression()

#linear function 
#weight calculated
#model trained with feature ie x and target ie y
mind.fit(x,y)
mind.predict([[9.5]])

#to save the model called mind here for future use or refernecs
import joblib
joblib.dump(mind,'model.pk1')
