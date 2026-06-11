import pandas as pd


def create_features(df):

    df = df.copy()

    # Age Category

    df["Age_Group"] = pd.cut(
        df["Age"],
        bins=[0,25,40,60,100],
        labels=[
            "Young",
            "Adult",
            "Middle Age",
            "Senior"
        ]
    )

    # Income Category

    df["Income_Group"] = pd.cut(
        df["Annual Income (k$)"],
        bins=[0,40,70,100,150],
        labels=[
            "Low",
            "Medium",
            "High",
            "Very High"
        ]
    )

    return df