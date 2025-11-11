import numpy as np

# Example: we’ll try to fit y = 2x + 1
# Our goal is to find parameters w (slope) and b (intercept)
# using gradient descent to minimize the Mean Squared Error (MSE)

# Training data
X = np.array([1, 2, 3, 4, 5], dtype=float)
Y = np.array([3, 5, 7, 9, 11], dtype=float)

# Initialize parameters
w = 0.0
b = 0.0
learning_rate = 0.01
epochs = 1000

# Gradient Descent
for i in range(epochs):
    Y_pred = w * X + b
    error = Y_pred - Y

    # Compute gradients
    dw = (2/len(X)) * np.dot(error, X)
    db = (2/len(X)) * np.sum(error)

    # Update parameters
    w -= learning_rate * dw
    b -= learning_rate * db

    if i % 100 == 0:
        loss = np.mean(error**2)
        print(f"Epoch {i}: w={w:.4f}, b={b:.4f}, loss={loss:.4f}")

print(f"\nFinal parameters: w={w:.4f}, b={b:.4f}")
