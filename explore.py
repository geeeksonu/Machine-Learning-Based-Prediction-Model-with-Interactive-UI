import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Function to shorten categories based on a cutoff value
def reduce_categories(category_counts, cutoff):
    reduced_categories = {}
    for category, count in category_counts.items():
        reduced_categories[category] = category if count >= cutoff else 'Other'
    return reduced_categories


# Function to clean years of professional coding experience
def filter_experience(x):
    return 50 if x == 'More than 50 years' else (0.5 if x == 'Less than 1 year' else float(x))


# Function to clean education level
def filter_education(x):
    return (
        'Bachelor’s degree' if 'Bachelor’s degree' in x else
        'Master’s degree' if 'Master’s degree' in x else
        'Post grad' if 'Professional degree' in x or 'Other doctoral' in x else
        'Less than a Bachelors'
    )


@st.cache
def load_data():
    df = pd.read_csv("survey_results_public.csv")
    df = (df[['Country', 'EdLevel', 'YearsCodePro', 'Employment', 'ConvertedComp']]
          .dropna()
          .query('Employment == "Employed full-time"')
          .drop('Employment', axis=1))

    country_counts = df['Country'].value_counts()
    country_map = reduce_categories(country_counts, 400)
    df['Country'] = df['Country'].map(country_map)

    df = (df[df['ConvertedComp'].notnull()]
          .query('10000 <= ConvertedComp <= 250000 and Country != "Other"'))

    df['YearsCodePro'] = df['YearsCodePro'].apply(filter_experience)
    df['EdLevel'] = df['EdLevel'].apply(filter_education)
    df.rename(columns={'ConvertedComp': 'Salary'}, inplace=True)
    
    return df

df = load_data()


def show_exp_pg():
    st.title("Exploring Software Engineer Salaries")
    st.write("Analysis of Stack Overflow Developer Survey 2023")
    
        # Assuming df is your DataFrame containing the data
    salary_by_country = df.groupby("Country")["Salary"].mean().reset_index()

    # Create the choropleth map
    fig12 = px.choropleth(salary_by_country, locations="Country", locationmode='country names',
                        color="Salary", hover_name="Country", hover_data=["Salary"],
                        color_continuous_scale='Viridis', title="Average Salary by Country")

    # Update layout for better readability
    fig12.update_geos(projection_type="natural earth", showcoastlines=True, coastlinecolor="DarkBlue",
                    showland=True, landcolor="LightGreen", showocean=True, oceancolor="LightBlue")

    # Display the choropleth map in Streamlit
    st.write("Geographical Heatmap of Average Salary by Country")
    st.plotly_chart(fig12)

        # Assuming df is your DataFrame containing the data
    country_data = df["Country"].value_counts().reset_index()
    country_data.columns = ["Country", "Count"]

    # Create the treemap chart
    fig = px.treemap(country_data, path=["Country"], values="Count")

    # Display the treemap chart in Streamlit
    st.write("Treemap Chart to explore different countries")
    st.plotly_chart(fig)

    
        # Preparing the data
    country_data = df["Country"].value_counts().reset_index()
    country_data.columns = ['Country', 'Count']
    country_counts_df = pd.DataFrame(country_data['Count']).T  # Transpose to make each country a column

    # Create the heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(country_counts_df, annot=True, cmap='viridis', fmt='g')
    plt.title('Heatmap of Developer Distribution by Country')
    plt.xlabel('Country Index')
    plt.ylabel('Count')
    
    # Mean Salary Based On Country
    st.write(" Avg Salary per counrty ")
    salary_by_country = df.groupby(["Country"])["Salary"].mean().sort_values(ascending=True)
    st.bar_chart(salary_by_country)

    # Mean Salary Based On Experience
    st.write("Avg  Salary Based On Experience")
    salary_by_experience = df.groupby(["YearsCodePro"])["Salary"].mean().sort_values(ascending=True)
    st.line_chart(salary_by_experience)

    # Mean Salary Based On Education Level
    st.write("Avg Salary Based On Education Level")
    salary_by_education = df.groupby(["EdLevel"])["Salary"].mean().sort_values(ascending=True)
    st.bar_chart(salary_by_education)
