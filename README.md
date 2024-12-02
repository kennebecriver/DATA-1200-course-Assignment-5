# DATA-1200-course-Assignment-5
A repository for DATA 1200 coursework, featuring a Python script related to Artificial Neural Networks. Includes a detailed README.md for project overview and usage instructions.

# Neural Network for Drug Classification

## Project Description
This project demonstrates the implementation of a neural network using the `scikit-learn` library to classify drugs based on a dataset. The script performs data preprocessing, model training, and evaluation to classify drugs into different categories. The dataset used in this project is `drugdataset.csv`.

---

## Getting Started

### Prerequisites
Ensure the following Python libraries are installed:
- `pandas`
- `numpy`
- `matplotlib`
- `scikit-learn`

You can install these libraries using pip:
```bash
pip install pandas numpy matplotlib scikit-learn
```

### Dataset
- Ensure the `drugdataset.csv` file is in the same directory as the script or update the file path accordingly.

---

## Installation
1. Clone the repository or download the script.
2. Place the `drugdataset.csv` file in the project directory.

---

## Usage
1. Open the script in a Python environment (e.g., Jupyter Notebook or any Python IDE).
2. Run the script step by step to:
   - Load and explore the dataset.
   - Preprocess the data (scaling and splitting).
   - Train a neural network model.
   - Evaluate the model's performance using a classification report and confusion matrix.

---

## Breakdown of the Script

1. **Load Libraries**  
   Essential libraries for data handling, visualization, and modeling are imported.

2. **Data Loading and Exploration**  
   The dataset is loaded, and its structure is analyzed using `head()` and `describe()`.

3. **Data Preprocessing**  
   - Features (`X`) and target (`y`) variables are separated.
   - Data is split into training and testing sets.
   - Features are scaled using `StandardScaler`.

4. **Model Training**  
   A neural network (`MLPClassifier`) is configured with:
   - Hidden layers: (5, 4, 5)
   - Activation function: ReLU
   - Solver: Adam
   - Maximum iterations: 10,000

5. **Model Evaluation**  
   - Predictions are made on the test data.
   - The performance is evaluated using:
     - Confusion Matrix
     - Classification Report

---

## Results
- Outputs include:
  - Confusion Matrix: Provides an overview of the model's predictions vs. actual values.
  - Classification Report: Displays precision, recall, F1-score, and support for each drug category.

---

## Deployment
This script is intended for academic purposes and is not deployed in a production environment.
