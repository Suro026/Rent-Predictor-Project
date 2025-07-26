# 🏠 House Rent Predictor

This project uses a machine learning model to predict house and flat rents based on a variety of features. This is the core prediction engine for a future interactive chatbot application.

## ✨ Features

-   **Predicts Monthly Rent:** Estimates rent based on features like city, size, BHK, and furnishing status.
-   **Trained Model:** Uses a Random Forest Regressor model trained on a real-world dataset.
-   **Ready for Use:** The trained model is saved and can be loaded for predictions.

## 💻 Tech Stack

-   **Python**
-   **Pandas** for data manipulation
-   **Scikit-learn** for modeling
-   **Pickle** for saving the model

## 🚀 Setup and Usage

To get a local copy up and running, follow these simple steps.

### Prerequisites

You need Git and Git LFS installed on your computer.

### Installation & Setup

1.  **Clone the repository** (replace `YourUsername/Your-Repo-Name.git` with your actual repo URL):
    ```sh
    git clone [https://github.com/YourUsername/Your-Repo-Name.git](https://github.com/YourUsername/Your-Repo-Name.git)
    ```
2.  **Navigate into the project folder:**
    ```sh
    cd Your-Repo-Name
    ```
3.  **Install Git LFS** to download the large model file:
    ```sh
    git lfs pull
    ```
4.  **Install required packages:**
    ```sh
    pip install pandas scikit-learn
    ```

### Running the Test Script

To test the model with a sample prediction, run the following command in your terminal:

```sh
python test_model.py
