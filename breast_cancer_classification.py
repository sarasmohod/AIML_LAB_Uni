
# Breast Cancer Classification using Logistic Regression
# Compatible with Visual Studio Code

# Step 1: Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    roc_curve,
    roc_auc_score
)


def main():
    # Step 2: Load the datasetpython breast_cancer_classification.py
    data = load_breast_cancer()

    X = pd.DataFrame(data.data, columns=data.feature_names)
    y = pd.Series(data.target)

    print("=" * 55)
    print("BREAST CANCER CLASSIFICATION")
    print("Using Logistic Regression")
    print("=" * 55)

    print("\nDataset loaded successfully!")
    print("Dataset shape:", X.shape)

    print("\nFirst five records:")
    print(X.head())

    print("\nTarget classes:", data.target_names)
    print("0 = Malignant")
    print("1 = Benign")

    # Step 3: Split the dataset
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y
    )

    print("\nTraining samples:", X_train.shape[0])
    print("Testing samples:", X_test.shape[0])

    # Step 4: Standardize the features
    scaler = StandardScaler()

    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Step 5: Create and train the model
    model = LogisticRegression(max_iter=5000)

    model.fit(X_train_scaled, y_train)

    print("\nModel trained successfully!")

    # Step 6: Make predictions
    y_pred = model.predict(X_test_scaled)

    # Probability of class 1 (Benign)
    y_prob = model.predict_proba(X_test_scaled)[:, 1]

    # Step 7: Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)

    print("\n" + "=" * 55)
    print("MODEL EVALUATION")
    print("=" * 55)

    print(f"\nModel Accuracy: {accuracy * 100:.2f}%")

    # Step 8: Confusion matrix
    cm = confusion_matrix(y_test, y_pred)

    print("\nConfusion Matrix:")
    print(cm)

    plt.figure(figsize=(7, 5))

    sns.heatmap(
        cm,
        annot=True,
        fmt="d",
        cmap="Blues",
        xticklabels=data.target_names,
        yticklabels=data.target_names
    )

    plt.xlabel("Predicted Class")
    plt.ylabel("Actual Class")
    plt.title("Confusion Matrix - Logistic Regression")
    plt.tight_layout()
    plt.savefig("confusion_matrix.png", dpi=300)
    plt.show()

    # Step 9: Classification report
    print("\nClassification Report:")

    print(
        classification_report(
            y_test,
            y_pred,
            labels=[0, 1],
            target_names=data.target_names,
            zero_division=0
        )
    )

    # Step 10: ROC curve and AUC score
    fpr, tpr, thresholds = roc_curve(y_test, y_prob)
    auc_score = roc_auc_score(y_test, y_prob)

    plt.figure(figsize=(7, 5))

    plt.plot(
        fpr,
        tpr,
        label=f"Logistic Regression (AUC = {auc_score:.3f})"
    )

    plt.plot(
        [0, 1],
        [0, 1],
        "k--",
        label="Random Classifier"
    )

    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("ROC Curve - Breast Cancer Classification")
    plt.legend(loc="lower right")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("roc_curve.png", dpi=300)
    plt.show()

    print(f"\nROC-AUC Score: {auc_score:.4f}")

    print("\nSaved graph files:")
    print("1. confusion_matrix.png")
    print("2. roc_curve.png")

    print("\nProgram executed successfully!")


if __name__ == "__main__":
    main()
