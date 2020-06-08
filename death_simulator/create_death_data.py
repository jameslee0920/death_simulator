"""
Author: James Bumsoo Lee
This module is designed for the purpose of:
    1. To read in all txt files in a directory and
        concatenate to a single data frame.
    2. Create the deaths dataset of ages from 0 to 100.
To use the functions of the pandas DataFrame:
    import create_death_data
or to use only one of the functions:
    from create_death_data import combine_txt_data
Specific examples and further documentations of each functions are
included with the respective functions
Requirements:
    Python (version 3.7.4 was used on creation of this module)
    pandas (version 1.0.3 was used on creation of this module)
    numpy (version 1.18.1 was used on creation of this module)
    scikit-learn (version 0.22.1 was used on creation of this module)
"""

import os

import numpy as np
import pandas as pd
from sklearn import linear_model


def combine_txt_data(filepath):
    """
    Create a pandas DataFrame by concatenating all txt
    files from a given filepath
    Args:
        filepath (string): filepath or directory containing txt files
    Returns:
        A pandas DataFrame
    Example:
        df = combine_txt_data("../data_raw/")
    """
    df_list = []
    for file in os.listdir("../data_raw/"):
        if file.endswith(".txt"):
            df_list.append(
                pd.read_csv(
                    "../data_raw/{}".format(file), sep="\t", encoding="ISO-8859-1"
                )
            )
    return pd.concat(df_list)


def create_deaths_dataset():
    """
    Create the Deaths Dataset
    Args:
        None
    Returns:
        A pandas DataFrame
    Example:
        deaths = create_deaths_dataset()
    """
    # load raw data
    deaths = combine_txt_data("../data_raw/")
    # filter columns
    deaths = deaths[
        [
            "Single-Year Ages Code",
            "Gender",
            "Race",
            "Injury Mechanism & All Other Leading Causes",
            "Cause of death",
            "Deaths",
            "Population",
        ]
    ]
    # rename columns
    deaths.columns = [
        "age",
        "gender",
        "race",
        "mechanism_of_death",
        "cause_of_death",
        "deaths",
        "population",
    ]
    # clean data (make NA values)
    deaths = deaths.replace("Not Applicable", np.NaN)
    # convert population to float
    deaths["population"] = deaths["population"].astype("float")
    # Extrapolate linearly on each race and age
    pred_dfs = []
    for race in deaths.race.unique():
        for sex in deaths.gender.unique():
            temp_df = deaths[
                (deaths.race == race) & (deaths.gender == sex) & (deaths.age >= 70)
            ][["age", "population"]].drop_duplicates()
            reg = linear_model.LinearRegression()
            reg.fit(
                X=np.array(temp_df[temp_df.age < 85]["age"]).reshape(-1, 1),
                y=np.array(temp_df[temp_df.age < 85]["population"]),
            )
            y_pred = np.clip(
                reg.predict(np.array(temp_df[temp_df.age >= 85]["age"]).reshape(-1, 1)),
                a_min=0,
                a_max=float("inf"),
            ).round()
            x_pred = range(85, 101)
            pred_df = pd.DataFrame(
                {"age": x_pred, "pred_population": y_pred, "race": race, "gender": sex}
            )
            pred_dfs.append(pred_df)
    pred_df_full = pd.concat(pred_dfs)
    # load extrapolated dataset and replace with null population values
    deaths = deaths.merge(
        pred_df_full,
        left_on=["age", "gender", "race"],
        right_on=["age", "gender", "race"],
        how="left",
    )
    deaths["population"] = deaths["population"].mask(
        pd.isnull, deaths["pred_population"]
    )
    deaths = deaths.drop("pred_population", axis=1)
    return deaths
