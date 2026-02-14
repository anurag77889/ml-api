import numpy as np
from sklearn.linear_model import LogisticRegression
import pickle

X = np.array([
    [25, 50000],
    [45, 80000],
    [22, 20000],
    [35, 120000],
    [50, 150000]
])

# 0 = low risk, 1 = high risk
y = np.array([0, 1, 0, 1, 1])

model = LogisticRegression()
model.fit(X, y)


# Save model 
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved as model.pkl")