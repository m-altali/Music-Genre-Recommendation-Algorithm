import pandas as pd  # importing pandas library
from sklearn.tree import DecisionTreeClassifier  # importing the decision tree from sci kit learn
from sklearn.model_selection import train_test_split  # importing train_test_split function,
# This function splits data into train & test sets

# from sklearn.metrics import accuracy_score  # importing the accuracy_score function to evaluate algorithm accuracy
music_data = pd.read_csv('Updatedmusic.csv')  # reading the data set

x_data = music_data.drop(columns=['genre'])  # separating the input and response data
y_data = music_data['genre']
x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.2)
# in the line above, we are separating the training and testing data

algorithm = DecisionTreeClassifier()  # making an instance of the decision tree classifier
# this algorithm type goes through a tree of decisions, at each branch, decides by using log regression and thresholds

algorithm.fit(x_train, y_train)  # training the data
# predictions = algorithm.predict(x_test)  #this line and the one below are lines I used to evaluate the models accuracy
# score = accuracy_score(y_test, predictions)

# uncomment lines 5, 16 and 17 to display this models accuracy, which should be around 90-99%

print('Welcome to MichaelMusicApp\nTo begin, please enter the following info')
print('Begin by entering your region,'
      '\n1 -- U.S'
      '\n2 -- Canada'
      '\n3 -- Peru'
      '\n4 -- China'
      '\n5 -- South Korea'
      '\n6 -- South Africa'
      '\n7 -- Brazil'
      '\n8 -- Mexico'
      '\n9 -- India'
      '\n10 -- Australia'
      '\n11 -- U.K'
      '\n12 -- Germany'
      '\n13 -- Poland'
      '\n14 -- Japan'
      '\n15 -- France')
countryNumber = int(input('Enter your Country Number: '))  # Asking using for their region
# Below is a while loop that prevents user from entering incorrect values

while countryNumber <= 0 or countryNumber > 15:
    print('Sorry, this app is currently only available for one of the countries above')
    countryNumber = int(input('Enter your Country Number: '))
gender = input('Gender(M/F): ')  # asking the user for their gender

# Below is a while loop like above, keeps looping until user enters a m or f
# Note: I made it so it doesn't matter if the user chooses to write upper or lower case, it'll still work
genderNumber = 0  # defining the variable for users gender, it will be changed in the next few lines
while gender != 'M' or gender != 'm' or gender != 'F' or gender != 'f':
    if gender == 'M' or gender == 'm':
        genderNumber = 1
        break
    elif gender == 'F' or gender == 'f':
        genderNumber = 0
        break
    else:
        print('Please enter one of the options in letter form')
        gender = input('gender(M/F): ')
age = int(input('Age: '))  # asks user for their age
while age <= 0 or age > 100:
    print('Please enter a valid age')
    age = int(input('Age: '))
# the loop above makes sure they input a valid age

predictions = algorithm.predict([[countryNumber, age, genderNumber]])  # we now ask the model to make a prediction
print('You should try listening to: ' + predictions)  # display the prediction for the user

# user should now have a valid genre to listen to based on popular music for their demographic
