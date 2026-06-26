import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

train_data = pd.read_csv("digit-recognizer/train.csv")
test_data = pd.read_csv("digit-recognizer/test.csv")

# print(train_data.shape)
# print(train_data.head())

X_train = train_data.iloc[:, 1:].values
y_train = train_data.iloc[:, 0].values

X_test = test_data.values

classifier = DecisionTreeClassifier(random_state=42)
classifier.fit(X_train, y_train)

# print(y_test[100])

# plt.imshow(X_test[100].reshape(28,28))
# plt.show()

prediction = classifier.predict(X_test)

print("Predicted digit:", prediction[0])

plt.imshow(X_test[0].reshape(28, 28), cmap="gray")
plt.axis("off")
plt.show()




