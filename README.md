🖊️ Handwritten Digit Recognizer

A machine learning project that classifies handwritten digits (0–9) using a Decision Tree Classifier. The model is trained on the MNIST dataset provided in the Kaggle Digit Recognizer competition and optimized using GridSearchCV for hyperparameter tuning.

##kaggle score = 0.87142##

📌 Features

* Train a Decision Tree classifier on the MNIST dataset
* Hyperparameter tuning using GridSearchCV
* 5-Fold Cross Validation
* Predict handwritten digits from unseen test images
* Generate a Kaggle-compatible submission.csv
* Visualize predicted digits using Matplotlib

📂 Dataset

This project uses the Digit Recognizer dataset from Kaggle.

* train.csv – Contains 42,000 labeled handwritten digit images.
* test.csv – Contains 28,000 unlabeled images used for competition submissions.

Each image is represented as 784 pixel values (28 × 28 grayscale image).

🛠️ Technologies Used

* Python
* NumPy
* Pandas
* Matplotlib
* Scikit-learn

🚀 Machine Learning Workflow

1. Load the training and testing datasets.
2. Separate features and labels.
3. Train a DecisionTreeClassifier.
4. Perform hyperparameter tuning using GridSearchCV.
5. Select the best-performing model using 5-fold cross-validation.
6. Predict labels for the test dataset.
7. Generate a submission.csv file for Kaggle.

⚙️ Hyperparameters Tuned

* criterion
* max_depth
* min_samples_split
* min_samples_leaf

📈 Results

* Model: Decision Tree Classifier
* Hyperparameter Tuning: GridSearchCV
* Cross Validation: 5-Fold
* Kaggle Public Leaderboard Score: 0.87142

📁 Project Structure

Digit Recognizer/
│
├── digit-recognizer/
│   ├── train.csv
│   └── test.csv
│
├── main.py
├── submission.csv
└── README.md

▶️ How to Run

1. Clone the repository.

git clone <https://github.com/ankurgithb/handwritten-digit-recognizer>

2. Install the required libraries.

pip install pandas numpy matplotlib scikit-learn

3. Run the project.

python main.py

After training, the program will generate a submission.csv file that can be uploaded to the Kaggle Digit Recognizer competition.

🎯 Future Improvements

* Implement Random Forest Classifier
* Try K-Nearest Neighbors (KNN)
* Experiment with Support Vector Machines (SVM)
* Build a Neural Network using TensorFlow or PyTorch
* Improve accuracy using Convolutional Neural Networks (CNNs)

📚 What I Learned

* Data preprocessing with Pandas
* Decision Tree Classification
* Hyperparameter tuning with GridSearchCV
* Cross Validation
* Model evaluation
* Creating Kaggle competition submissions
* End-to-end machine learning workflow

👨‍💻 Author

Ankur Joshi

If you found this project helpful, feel free to ⭐ the repository.
