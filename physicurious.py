#####################
### 1D Kinematics ###
#####################

def avg_speed(distance, elapsed_time, distance_unit="m", time_unit="s"):
	''' Takes in the distance and elapsed time as floats. Returns the speed.
	Default unit of speed is meters per second (m/s). 
	Both distance and elapsed time must be positive for consistency with the laws of physics.
	This is a scalar value because it has no direction associated with it.'''

	# Take the absolute value of both distance and time in case the user enters negatives.
	avg_speed = (abs(distance) / abs(elapsed_time))

	print ""
	print "Avg. Speed: " + str(avg_speed) + distance_unit + "/" + time_unit + " (Remember to adjust for sig figs!)"

	return avg_speed


# avg_speed(500.0, 60)


def distance(speed, elapsed_time, distance_unit="m", time_unit="s"):
	''' Takes in the speed and elapsed time as floats. Time must be positive. Returns the distance traveled.
	Default unit of speed is meters per second (m/s).'''

	# Take the absolute value of time in case user enters a negative.
	distance = (speed * abs(elapsed_time))

	print ""
	print "Distance: " + str(distance) + distance_unit + " (Remember to adjust for sig figs!)"

	return distance


# distance(8.33, 5)


def elapsed_time_spd(distance, speed, distance_unit="m", time_unit="s"):
	''' Takes in the distance and speed as floats. Distance must be positive. Returns the elapsed time.
	Default unit of speed is meters per second (m/s).'''

	# Take the absolute value of distance in case user enters a negative.
	time_spd = (abs(distance) / speed)

	print ""
	print "Time: " + str(time_spd) + time_unit + " (Remember to adjust for sig figs!)"

	return time_spd


# elapsed_time_spd(500.0, 8.33)


def displacement(x0, x1, unit="m"):
	''' Takes in an object's initial & final positions (x0, x1) as floats. 
	Returns the object's displacement (change in position).
	Arguments x0 and x1 may be positive or negative.
	This is a vector value because it has a direction and sign (+ or -) associated with it.
	Default unit of measurement is meters (m).'''

	displacement = (x1 - x0)

	print ""
	print "Displacement: " + str(displacement) + unit + " (Remember to adjust for sig figs!)"

	return displacement


# displacement(1.0, 2.0, "km")


def avg_velocity(displacement, elapsed_time, displ_unit="m", time_unit="s"):
	''' Takes in displacement (change in position) and elapsed time as floats. Returns average velocity.
	Describes how fast and in what direction an object is moving. This is a vector value. 
	Default unit of velocity is meters per second (m/s).'''

	avg_velocity = (displacement / elapsed_time)

	print ""
	print "Avg. Velocity: " + str(avg_velocity) + displ_unit + "/" + time_unit + " (Remember to adjust for sig figs!)"

	return avg_velocity

# If you already calculated the displacement, call the function like this:
# avg_velocity(3.0, 50)

# If you haven't yet calculated the displacement, call the function like this:
# avg_velocity(displacement(5.0, 8.0), 50)


def elapsed_time_vel(displacement, avg_velocity, displ_unit="m", time_unit="s"):
	''' Takes in displacement and average velocity as floats. Returns elapsed time. 
	Default unit of displacement is meters (m) and avg_velocity is meters per second (m/s).'''

	time_vel = (displacement / avg_velocity)

	print ""
	print "Elapsed Time: " + str(time_vel) + time_unit + " (Remember to adjust for sig figs!)"

	return time_vel


# If you already calculated the displacement and average velocity, call the function like this:
# elapsed_time_vel(3.0, 6.0)

# If you haven't yet calculated the displacement, call the function like this:
# elapsed_time_vel(displacement(5.0, 8.0), 6.0)


# This involves coding calculus concepts, which I am researching
def instant_velocity():

	#https://www.reddit.com/r/learnpython/comments/1813fo/calculus_limit_calculator_in_python/

	pass


def change_in_velocity(v0, v1, distance_unit="m", time_unit="s"):
	''' Takes in the initial and final velocities (v0, v1) as floats and returns the change in velocity.
	Default unit of velocity is meters per second (m/s).'''

	change_vel = (v1 - v0)

	print ""
	print "Change in Velocity: " + str(change_vel) + distance_unit + "/" + time_unit + " (Remember to adjust for sig figs!)"

	return change_vel


# change_in_velocity(2.0, 5.0)


# If acceleration is CONSTANT, the instantaneous and average velocities are equivalent
def avg_acceleration(change_in_velocity, elapsed_time, distance_unit="m", time_unit="s"):
	''' Takes in the change in velocity and the elapsed time as floats and returns the avg acceleration.
	Avg. acceleration can be pos, neg or zero. Acceleration is a 1D vector (ie: it has a speed & direction)
	Default unit of acceleration is meters per second per second (m/s^2 or m/s**2). '''

	avg_accel = (change_in_velocity / elapsed_time)

	print ""
	print "Avg. Acceleration: " + str(avg_accel) + distance_unit + "/" + time_unit + "^2 (Remember to adjust for sig figs!)"

	return avg_accel


# If you already calculated the change in velocity and elapsed time, call the function like this:
# avg_acceleration(10.0, 5.0)

# If you haven't yet calculated the change in velocity, call the function like this:
# avg_acceleration(change_in_velocity(3.0, 13.0), 5.0)


# This involves coding calculus concepts, which I am researching
# If acceleration is CONSTANT, the instantaneous and average velocities are equivalent
def instant_accel():

	#https://www.reddit.com/r/learnpython/comments/1813fo/calculus_limit_calculator_in_python/

	pass


def velocity_const_accel(v0, acceleration, elapsed_time, distance_unit="m", time_unit="s"):
	'''Takes in initial velocity (v0), acceleration and elapsed time as floats. 
	Returns the final velocity at the final point in time.
	Remember: with constant accel, instantaneous accel = avg acceleration.'''

	vf =  (v0 + (acceleration * elapsed_time))

	print ""
	print "Constant Motion Velocity: " + str(vf) + distance_unit + "/" + time_unit + " (Remember to adjust for sig figs!)"

	return vf


velocity_const_accel(0.0, 3.2, 10.0)

# left off here
# velocity_const_accel(0.0, avg_acceleration(change_in_velocity()), 60.0)
