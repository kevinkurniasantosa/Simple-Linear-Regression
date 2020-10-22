
## A Linear Regression algorithm from scratch

## A good Linear Regression algorithm minimizes the error function or the distance from each point in the line. 
# A line with the least error is the best line that fits the data the best.

################################################################################

### Part 1 - Calculating Error/MSE

# The formula of the linear regression is: y = m*x + b OR y = a + b*x OR y = wo + w1*x, but in this case                          
# where m is the slope of the line and b is the intercept where the line crosses the y-axis

def get_y_predicted(m, b, x):
    y = m*x + b

    return y

# The calc_err function is created to calculate the error between a point and a line which return the distance between the line (the predicted value) and the point (the actual value)
# The datapoint parameter takes two input which x and y in (x, y) format

def calc_err(m, b, point):
    x, y_actual = point

    y_predicted = m*x + b
    distance = abs(y_predicted - y_actual) # the error difference between predicted value and the actual value

    return distance

# print for testing
# print(calc_err(1, 0, (3, 3)))

def calc_final_err(m, b, datapoints):
    total_error = 0

    for point in datapoints:
        each_error = calc_err(m, b, point)
        total_error += each_error
    
    return total_error

# For testing
# datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
# print(calc_final_err(1, 0, datapoints))

################################################################################

### Part 2 - Trying a bunch of slopes and intercepts (m and b)

# To find the best linear regression model, I need to find the m and b that minimizes the error the most, and thus fits the data best.

all_m = [m * 0.1 for m in range(-100, 101)]
all_b = [b * 0.1 for b in range(-200, 201)]

# Find the the smallest error by using every possible y = m*x + b by pairing all of the possible m and b. 
# Then, find out whether y = mx + b produces the smallest total error.

# To optimize the best model:
# Iterate through each element m in all_m
# For every m value, take every b value in all_b
# If the value returned from calc_final_err on this m value, this b value, and datapoints is less than our current least_error
# Set best_m and best_b to be these values, and set least_error to this error.

datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)] # where (x, y), x is the independent variable and y is the actual dependent variable value
least_error = float("inf") # set the least error as an infinite value (later will be replaced)
best_m = 0
best_b = 0
best_x = 0

for m in all_m:
    for b in all_b:
        error = calc_final_err(m, b, datapoints)

        if error < least_error:
            best_m = m 
            best_b = b
            least_error = error

print('Best M: {}, Best B: {}, Least Error: {}'.format(best_m, best_b, least_error))
print('Best Linear Regression: y = {}*x + {}'.format(round(best_m,2), round(best_b,2)))

## Part 3 - Linear regression model predicts

# Now that we have observed multiple datapoints and the line that fits the data best has an m of 0.3 and b of 1.7
# with the formula of y = 0.3x + 1.7 with a total error of 5

# Let's try what the model predicts when we define the x as 6
# In other words, I will call the get_y_predicted function that have defined earlier with the parameter:
# m = 0.3, b = 1.7, and x = 6

# x_input_value = input('Input value x: ') # in case the user wants to input
x_input_value = 6
print('The predicted value (y) is ' + str(round(get_y_predicted(best_m, best_b, x_input_value),2)))











