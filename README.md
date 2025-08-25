# TalentScope AI 🚀

[![Python Version](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/) [![Flask Version](https://img.shields.io/badge/Flask-3.0-green.svg)](https://flask.palletsprojects.com/) [![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.5-orange.svg)](https://scikit-learn.org/) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A machine learning web application built to predict the productivity of workers in a garment manufacturing context, based on the "Productivity Prediction of Garment Employees" dataset. This tool provides a user-friendly dashboard for managers and HR professionals to input task-related parameters and receive a productivity score along with data-driven, actionable recommendations.

---

### ✨ Application Demo

![Productivity Predictor Demo GIF](https://github.com/user-attachments/assets/8062bff3-bb70-4923-9aed-ce0cdc3c44f4)


---

## 📋 Table of Contents

* [About The Project](#-about-the-project)
* [Key Features](#-key-features)
* [Project Architecture](#-project-architecture)
* [Model Performance](#-model-performance)
* [Setup and Usage](#-setup-and-usage)
* [Gallery](#-gallery)

---

## ℹ️ About The Project

This project addresses a practical challenge in the manufacturing industry: forecasting workforce productivity. Using a real-world dataset from a garment factory, this tool provides supervisors and floor managers with a data-driven estimate of team productivity based on various task and environmental parameters.

The goal is to move beyond simple historical averages and provide a more nuanced prediction that accounts for factors like task complexity (SMV), team size, and pending workload (WIP). This can help in setting realistic daily targets, identifying potentially challenging tasks, and better understanding the variables that influence performance on the factory floor.

The project is built as a complete end-to-end system, from data exploration and model training in a Jupyter Notebook to deployment as an interactive web dashboard using Flask.

---

## ⭐ Key Features

* **Systematic Workflow:** A clear separation between the data science notebook (for analysis and training) and the Flask application (for serving the model).
* **Productivity Prediction Model:** Utilizes a trained Random Forest Regressor to predict a numerical productivity score (ranging from 0 to 1).
* **Data-Based Insights:** The application provides a qualitative assessment of the predicted score ("Good," "Needs Support," etc.) and recommendations based on the user's specific inputs.
* **Interactive Web Dashboard:** A clean and modern user interface built with HTML, CSS, and JavaScript that allows for easy input of parameters and clear visualization of the results.
* **Flask-Powered Backend:** The application is served by a robust Flask backend that handles data validation and serves predictions via an API.

---

## 🏗️ Project Architecture

The project is structured to separate the data science and web deployment components for clarity and maintainability.

<img width="2506" height="731" alt="Project Architecture" src="https://github.com/user-attachments/assets/caf24b1d-781f-41ec-b001-51e84ea9f4c5" />


---

## 🎯 Model Performance

Several regression models were tested, with the **Random Forest Regressor** providing the best performance on the holdout test set.

* **Final Model:** Random Forest Regressor
* **R-squared Score:** **0.4742**
    * *This indicates that the model can explain approximately 47.4% of the variance in employee productivity, providing a solid predictive foundation.*

---

## 🚀 Setup and Usage

To get a local copy up and running, follow these steps.

### Prerequisites

* Python 3.8+
* Git

### Workflow

This project has a two-stage workflow: **Training** and **Serving**.

#### Stage 1: Train the Model

First, you need to run the data science notebook to create the trained model file.

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/theanushkatrivedi/Talent-Scope-AI.git
    cd TalentScope-AI
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # For Windows
    python -m venv .venv
    .\.venv\Scripts\Activate.ps1
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Jupyter Notebook:**
    * Open the `Training_Notebook/Employee_Prediction.ipynb` file in VS Code or Jupyter.
    * Select the virtual environment (`.venv`) as your kernel.
    * Click **"Run All"** to execute the notebook. This will create the `gwp.pkl` file inside the `Flask` folder.

#### Stage 2: Run the Web Application

Once the `gwp.pkl` model file has been created, you can start the web server.

1.  Make sure your virtual environment is still active.
2.  Navigate to the Flask directory:
    ```bash
    cd Flask
    ```
3.  Run the Flask application from the terminal:
    ```bash
    python app.py
    ```
4.  Open your web browser and navigate to `http://127.0.0.1:5000`.

---

## 📸 Gallery

![Prediction_Insights](https://github.com/user-attachments/assets/c21b8f76-5c9c-4f25-9689-62bb82aac54d)
