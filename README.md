Pay Predictor

Inspiration

The purpose of this project is to develop a machine learning application that will help the general public and make learning about machine learning techniques easier. This application is a useful tool for analyzing possible wages because it uses data from Stack Overflow to anticipate an individual's pay based on multiple characteristics.

Problem Synopsis

Rather of classifying income into wide categories, the purpose of the wage Predictor is to precisely forecast an individual's real wage based on a variety of variables. This straightforward method aids in accurate policy and budgetary planning.

Set of Data

The Stack Overflow Annual Developer Survey provided the data for this project. This extensive dataset offers insights on the global developer community's wages and professional behavior.[Stack Overflow Developer Survey] is the data source.(https://stackoverflow.co/survey)

Phases of the Project

Phase 1: Consists of the Exploratory Data Analysis (EDA) details (code + report). many data processing, cleansing, and exploratory approaches are used in this step to assess the dataset's many features.
Phase 2: Explains how Machine Learning models are applied to the cleaned data, along with comprehensive findings and comparisons to determine which model works best in this situation.
Phase 3: Consists of the completed application (report and code), which is an online Salary Predictor created with the selected model. The user interface code is also included in this phase.

Technology Employed

Python programming language; Streamlit application framework; Plotly, Matplotlib, Seaborn data visualization

Setups

bash pip install scikit-learn, pandas, numpy, seaborn, matplotlib, and streamlit
Alternatively, you can use Anaconda to install Streamlit MatplotLib Seaborn Plotly, Pandas, Numpy, and Scikit-Learn.


Configuring the Scene

The following are detailed instructions for configuring the project environment:

1. Install Python Packages: - Install the above-mentioned necessary packages using conda or pip.

2. Launch the Program:
    Open the terminal and navigate to the project directory.
    Run the following commands to open the application: bash streamlit run filePath/app.py
      
    A web browser can be used to access the locally hosted application.

Launching the Program

1. In Visual Studio Code or another IDE, open the project folder.
2. In the IDE, open a terminal.
3. To launch the application, use the following command:
   streamlit run file for bashExample:streamlit run c:/Users/Lenovo/Documents/FinalProject/app.py in Path/app.pyThis will launch your web browser and launch the Salary Predictor application, where you can use the tool.

Interface User

The main prediction logic is in predict.py and explore_page.py
