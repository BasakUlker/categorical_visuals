import sys
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

if len(sys.argv) < 2:
    print("Error: Please send a dataset. e.g: python main.py dataset.csv")
    sys.exit(1)

file_path = sys.argv[1]

if not os.path.exists(file_path):
    print(f"Error: File is not found: {file_path}")
    sys.exit(1)

df = pd.read_csv(file_path)
#df.fillna(df.mean(), inplace=True)

print("Dataset is successfully uploaded.")

categorical_columns = df.select_dtypes(include = ["object"]).columns

print("Categorical Variables:")
print(categorical_columns)

chart_type = input("Enter the type of graphic: (Catagorical, Histogram)")
selected_columns = input("Enter the categorical variables you want to visualize, separated by commas: ").split(",")
'''
for col in selected_columns:
    col = col.strip()
    if col in df.columns:
        plt.figure(figsize=(10,5))
        df[col].value_counts().plot(kind="bar", color="red")
        plt.title(f"Distribution of {col}")
        plt.xlabel(col)
        plt.ylabel("Count")
        plt.xticks(rotation=45)
        plt.show()
    else:
        print(f"Warning: '{col}' is not found.")
'''

def plot_categorical_distribution(df, selected_columns, top_n = 10):
    
    
    for column in selected_columns:
        
        if column not in df.columns:
            print(f"Warning: '{column}' is not found.")
            continue
        
        if df[column].dtype not in ["object", "category"]:
            print(f"Warning: '{column}' is not a categoric variable.")
        
        plt.figure(figsize=(12, 6))
        
        sns.set_style("whitegrid")

        data = df[column].value_counts().nlargest(top_n)

        sns.barplot(x=data.index, y=data.values, palette="coolwarm")

        plt.xticks(rotation=45)
        plt.xlabel(column)
        plt.ylabel("Count")
        plt.title(f"Distribution of {column}")
        plt.show()

def plot_histogram_distribution(df, selected_columns):
    
    for column in selected_columns:
        if column not in df.columns:
            print(f"Warning: '{column}' is not found.")
            continue
        
        plt.figure(figsize=(10,5))
        sns.histplot(df[column], kde=True)
        plt.xticks(rotation=45)
        plt.title(f"Histogram for {column}")
        plt.show()


if chart_type == "Categorical" or chart_type == "categorical":
    plot_categorical_distribution(df, selected_columns)

if chart_type == "Histogram" or chart_type == "histogram":
    plot_histogram_distribution(df, selected_columns)

