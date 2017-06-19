import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

# Read data into a dataframe
df = pd.read_csv('/Users/maanavkhaitan/Downloads/Nerf Projectile Data.csv', usecols=['Angle', 'Average Distance'])
df = df.dropna()


# Fit model to data
parameters = np.polyfit(df['Angle'], df['Average Distance'], 3)

#Generate angles from -40 to 90
angles = np.arange(-40,90)

# Set y coordinates for regression model
y_data = np.polyval(parameters, angles)

#Creates two empty lists that will be filled by user's angles and corresponding distances
user_angles = []
user_distances = []

def plot_data():
# PLots model and data
	plt.plot(angles, y_data, label='Fit')
	plt.scatter(df['Angle'], df['Average Distance'], label='Raw Data', color='r')
	plt.scatter(user_angles, user_distances, label='Your angles', color='g')
	plt.title('Polynomial Regression: Angle vs Distance')
	plt.xlabel('Angle')
	plt.ylabel('Distance')
	plt.legend(loc=2)
	plt.show()


def ask_user():
# Asks user for an angle and prints result
	user_angle = raw_input('Please enter an angle:')

	# If user angle is a number
	try:

		user_angle = float(user_angle)
		# Append user angle to list of user angles
		user_angles.append(user_angle)

		# Print Model formula
		print 'Formula for Model:'
		print np.poly1d(parameters)

		# Calculate distance corresponding to user angle
		dist = np.polyval(parameters, user_angle)

		# Append this distance to list of user distances
		user_distances.append(dist)

		# Print distance in feet and inches
		feet = int(dist) / 12
		inches = dist%12
		print 'Distance at %s degrees: %s feet %s inches' % (user_angle, feet, inches)

		# Ask if user wants to enter another angle
		user_again = raw_input('Would you like to enter another angle? (y/n)')
		if user_again=='y':
			ask_user()
		else:
			print 'Thank you for using our service today!'

			# Plot model, user's angles, and data here
			print 'The plot for the model, your angles, and the training data has been created.'
			plot_data()

	# If user angle is not a number		
	except ValueError:
		print 'Invalid Angle.'
		ask_user()

# Initialize ask_user function when program starts
#ask_user()

# Calculate Training Error
temp_rmse = []
predictions = np.polyval(parameters, [-40,-20,0,20,40,60,80])
correct_data = [61,177.33,196.33,680.33,651,534.67,24.67]
for i in range(0,len(predictions)):
	temp_rmse.append((predictions[i]-correct_data[i])**2)
print 'Training Data: ' + str(((sum(temp_rmse))/7)**0.5)

#Calculate Testing Error
temp_test = []
predictions_test = np.polyval(parameters, [-30, -10, 10, 30, 50, 70, 90])
correct_test = [116,246,539.67,733.67,652,303.67,0]
for i in range(0,len(predictions_test)):
	temp_test.append((predictions_test[i]-correct_test[i])**2)
print 'Testing Data: ' + str(((sum(temp_test))/7)**0.5)

plt.plot(angles, y_data, label='Fit')
plt.scatter(df['Angle'], df['Average Distance'], label='Training Data', color='r')
#plt.scatter(user_angles, user_distances, label='Your angles', color='g')
plt.scatter([-30, -10, 10, 30, 50, 70, 90], [116,246,539.67,733.67,652,303.67,0], label='Test Data', color='r')
plt.scatter([-30, -10, 10, 30, 50, 70, 90], predictions_test, label='Test Predictions', color='g')
plt.scatter([-40,-20,0,20,40,60,80], predictions, label='Training Predictions', color='g')
plt.title('Polynomial Regression: Angle vs Distance')
plt.xlabel('Angle')
plt.ylabel('Distance')
plt.legend(loc='lower left')
plt.show()






