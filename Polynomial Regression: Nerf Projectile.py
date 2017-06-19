import pandas as pd
import numpy as np
from sklearn import tree
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestRegressor
import scipy.optimize as spo
import matplotlib.pyplot as plt

# Read data into a dataframe
df = pd.read_csv('/Users/maanavkhaitan/Downloads/Nerf Projectile Data.csv', usecols=['Angle', 'Average Distance'])
#benchmark = df.shape(0) * 0.8
df = df.dropna()


# Fit model to data
parameters = np.polyfit(df['Angle'], df['Average Distance'], 3)
angles = np.arange(-40,90)
y_data = np.polyval(parameters, angles)

def ask_user():
# Asks user for an angle and prints result
	user_angle = raw_input('Please enter an angle:')
	if user_angle.isdigit():
		print 'Formula for Model:'
		print np.poly1d(parameters)
		dist = np.polyval(parameters, int(user_angle))
		feet = int(dist) / 12
		inches = dist%12
		print 'Distance at %s degrees: %s feet %s inches' % (user_angle, feet, inches)

	else:
		print 'Invalid Angle.'
		ask_user()

ask_user()


# PLots model and data
plt.plot(angles, y_data, label='Fit')
plt.scatter(df['Angle'], df['Average Distance'], label='Raw Data', color='r')
plt.title('Polynomial Regression: Angle vs Average Distance')
plt.legend(loc=2)
plt.show()



