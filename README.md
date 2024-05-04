# Machine-Learning-Based-Prediction-Model-with-Interactive-UI(Salary Predictor)
Team Members:
Sonu Kumar
Ravulapalli Tanuja
Nakshatra Mutyam



Motivation

The goal of this project is to create a machine learning application to both facilitate learning about machine learning techniques and assist the general public. This application predicts the salary of an individual based on various factors using data from Stack Overflow, making it a practical tool for understanding potential earnings.

Problem Statement

The Salary Predictor is designed to accurately predict the actual salary of an individual based on diverse attributes, rather than categorizing income into broad ranges. This direct approach helps in precise financial planning and policy making.

Data Set

The data used in this project is sourced from the Stack Overflow Annual Developer Survey. This comprehensive dataset provides insights into the earnings and professional dynamics of the developer community globally.
Data Source: [Stack Overflow Developer Survey](https://survey.stackoverflow.co/)

Project Phases

Phase 1: Includes the details (code + report) of the Exploratory Data Analysis (EDA). This phase involves various data processing, cleaning, and exploratory techniques to analyze different attributes of the dataset.
Phase 2: Describes the application of Machine Learning models to the cleaned data, including detailed results and comparisons to identify the most effective model for the application.
Phase 3: Contains the final application (code + report), a web-based Salary Predictor developed using the chosen model. This phase also includes the code for the user interface.

Technology Used

Programming Language: Python
App Framework: Streamlit
Data Visualization: Plotly, Matplotlib, Seaborn

Installations

Install the necessary tools and libraries to run the project:

```bash
pip install streamlit matplotlib seaborn plotly pandas numpy scikit-learn
Or with Anaconda
conda install streamlit matplotlib seaborn plotly pandas numpy scikit-learn
```

Setting Up the Environment

Here are step-by-step instructions to set up the project environment:

1.Install Python Packages:
    - Use pip or conda to install the required packages as listed above.

2.Run the Application:
    Navigate to the project directory in the terminal.
    Launch the application by running:
      ```bash
      streamlit run filePath/app.py
      ```
    The application will be hosted locally and can be accessed via a web browser.

Running the Application

1.Open the project folder in Visual Studio Code or another IDE.
2.Open a terminal in the IDE.
3.Execute the following command to start the application:
   ```bash
   streamlit run filePath/app.py
   example:streamlit run c:/Users/Lenovo/Documents/FinalProject/app.py
   ```
   This will open the Salary Predictor application in your web browser, allowing you to interact with the tool.

User Interface

predict.py: The core prediction logic.
explore_page.py
