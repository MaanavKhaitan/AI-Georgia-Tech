import pandas as pd
import numpy as np
from sklearn import tree
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestRegressor
import scipy.optimize as spo
import matplotlib.pyplot as plt

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
	if user_angle.isdigit():

		# Append user angle to list of user angles
		user_angles.append(user_angle)

		# Print Model formula
		print 'Formula for Model:'
		print np.poly1d(parameters)

		# Calculate distance corresponding to user angle
		dist = np.polyval(parameters, int(user_angle))

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
	else:
		print 'Invalid Angle.'
		ask_user()

# Initialize ask_user function when program starts
ask_user()
