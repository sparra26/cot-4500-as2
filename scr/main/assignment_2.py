import numpy as np

# Question 1
np.set_printoptions(precision=7, suppress=True, linewidth=100)
x = [3.6, 3.8, 3.9]
y = [1.675, 1.436, 1.318]
def neville(x, y, x_interp):
    n = len(x)
    p = np.zeros((n, n))
    p[:, 0] = y
    for j in range(1, n):
        for i in range(n - j):
            p[i, j] = ((x_interp - x[i + j]) * p[i, j - 1] - (x_interp - x[i]) * p[i + 1, j - 1]) / (x[i] - x[i + j])
    return p[0, n - 1]
x_interp = 3.7
result = neville(x, y, x_interp)
print(result)
print("\n")

# Question 2

# Defining the x and y data points
x = [7.2, 7.4, 7.5, 7.6]
y = [23.5492, 25.3913, 26.8224, 27.4589]
# Calculating the coefficients using Newton's Forward Method
coefficients = [] 
for i in range(len(x)): 
    coefficients.append(y[i]) 
for j in range(1, len(x)): 
    for i in range(len(x)-1, j-1, -1): 
        coefficients[i] = (coefficients[i]-coefficients[i-1])/(x[i]-x[i-j]) 
print(coefficients[1:])
print("\n")

# Question 3

# Defining the data
x = [7.2, 7.4, 7.5, 7.6]
y = [23.5492, 25.3913, 26.8224, 27.4589]
# Calculating the coefficients using Newton's Forward Method
coefficients = [] 
for i in range(len(x)): 
    coefficients.append(y[i]) 
for j in range(1, len(x)): 
    for i in range(len(x)-1, j-1, -1): 
        coefficients[i] = (coefficients[i]-coefficients[i-1])/(x[i]-x[i-j]) 
# Applying the coefficients to the polynomial
result = 0
for i in range(len(coefficients)): 
    term = coefficients[i] 
    for j in range(i): 
        term = term * (7.3 - x[j]) 
    result += term 
print(result)
print("\n")

# Question 4
def divided_difference(x, y, y_prime):
    n = len(x)
    f = np.zeros((n, n))
    f[:, 0] = y
    f[:, 1] = y_prime
    for j in range(2, n):
        for i in range(n-j+1):
            f[i, j] = (f[i+1, j-1] - f[i, j-1]) / (x[i+j-1] - x[i])
    return np.hstack((np.array([x]).T, f))
x = [3.6, 3.8, 3.9]
y = [1.675, 1.436, 1.318]
y_prime = [-1.195, -1.188, -1.182]
approximation_matrix = divided_difference(x, y, y_prime)
print(approximation_matrix)
print("\n")

# Question 5

# Definining the data
x_data = np.array([2, 5, 8, 10])
y_data = np.array([3, 5, 7, 9])
# Defining the matrix A
n = len(x_data)
A = np.zeros((n, n))
A[0, 0] = 1
A[n-1, n-1] = 1
for i in range(1, n-1):
    A[i, i-1] = x_data[i] - x_data[i-1]
    A[i, i] = 2 * (x_data[i+1] - x_data[i-1])
    A[i, i+1] = x_data[i+1] - x_data[i]
# Defining the vector b
b = np.zeros(n)
for i in range(1, n-1):
    b[i] = 3 * (y_data[i+1] - y_data[i]) / (x_data[i+1] - x_data[i]) - \
           3 * (y_data[i] - y_data[i-1]) / (x_data[i] - x_data[i-1])
# Solve for the vector x
x = np.linalg.solve(A, b)
# Print the results
print(A)
print("\n")
print(b)
print("\n")
print(x)
