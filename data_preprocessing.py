import numpy as np
import pandas as pd


def read_csv():
    # Method to read the CSV file "Hospital_patients_datasets.csv" using pandas.
    # Returns: Pandas DataFrame containing the data from the CSV file.
    ds = pd.read_csv("Hospital_patients_datasets.csv")
    return ds

def check_duplicates():
    ds = read_csv()
    # Method to check for duplicate rows in the DataFrame.
    # Returns: The number of duplicated rows found in the DataFrame.
    return ds.duplicated().sum()

def check_null_values():
    ds = read_csv()
    # Method to check for null (missing) values in the DataFrame.
    # Returns: A pandas Series indicating the count of null values for each column in the DataFrame.
    return ds.isnull().sum()

def converting_dtype():
    ds = read_csv()
    # Method to convert 'ScheduledDay' and 'AppointmentDay' columns to datetime objects.
    # Returns: DataFrame with 'ScheduledDay' and 'AppointmentDay' columns converted to datetime objects.
    ds['ScheduledDay'] = pd.to_datetime(ds['ScheduledDay']).dt.to_period('D').dt.to_timestamp()
    ds['AppointmentDay'] = pd.to_datetime(ds['AppointmentDay']).dt.to_period('D').dt.to_timestamp()
    return ds

def rename_columns():
    ds = converting_dtype()
    # Method to rename some columns in the DataFrame.
    # Returns: DataFrame with certain column names changed to new names.
    ds = ds.rename(columns = {'Hipertension':'Hypertension', 'Handcap':'Handicap', 'SMS_received':'SMSRecevied', 'No-show':'NoShow'})
    return ds

def drop_columns():
    ds = rename_columns()
    # Method to drop unnecessary columns from the DataFrame.
    # Returns: DataFrame with specified columns dropped.
    ds = ds.drop(['PatientId', 'AppointmentID', 'Neighbourhood'], axis = 1)
    return ds

def create_bin():
    ds = drop_columns()
    #First Drop rows with Age == 0
    ds = ds[ds['Age'] != 0]
    # Generating labels for age intervals (e.g., '1 - 20', '21 - 40', etc.)
    labels = ["{0} - {1}".format(i, i + 20) for i in range(1, 118, 20)]
    # Using the pd.cut() function to categorize ages into groups(use bins = range(1, 130, 20) ,right=False and use the given labels)
    ds['Age_group'] = pd.cut(ds['Age'], bins = range(1, 130, 20), right = False, labels = labels)
    # Returning the modified dataset with assigned age groups
    return ds

def drop():
    ds = create_bin()
    # Method to drop the original 'Age' column from the DataFrame.
    ds = ds.drop('Age', axis = 1)
    # Returns: DataFrame with the 'Age' column dropped.
    return ds

def convert():
    ds = drop()
    # Method to convert 'NoShow' values into binary values (1 for 'Yes' and 0 for 'No').
    ds['NoShow'] = ds['NoShow'].replace({'Yes':1, 'No':0})
    # Returns: DataFrame with 'NoShow' column values converted to 1s and 0s.
    return ds

def export_the_dataset():
    df = convert()
    # write your code to export the cleaned dataset and set the index=false and return the same as 'df'
    df.to_csv("patients.csv", index = False)
    return df


# TASK 6: Load the Cleaned dataset 'patients.csv' to the database provided.
# follow the instruction in the Task 5 description and complete the task as per it.

# check if mysql table is created using "patients"
# Use this final dataset and upload it on the provided database for performing analysis in MySQL
# To run this task click on the terminal and click on the run project


