import joblib
name = input('Enter your name : ')
num = float(input('Enter year of experience : '))
model = joblib.load('model.pk1')
print()
print('Name               : ' ,name)
print('Year_of_Experience : ', num)
output = model.predict([[num]])
print('Salary you will recive per month : ',output)
