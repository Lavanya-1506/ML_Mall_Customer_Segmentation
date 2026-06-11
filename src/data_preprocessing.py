import pandas as pd


def load_data(filepath):
    return pd.read_csv(filepath)


def preprocess_data(df):

    df = df.copy()

    # Remove duplicates
    df.drop_duplicates(inplace=True)

    # Remove missing values
    df.dropna(inplace=True)

    # Encode Gender
    if "Gender" in df.columns:
        df["Gender"] = df["Gender"].map(
            {
                "Male": 1,
                "Female": 0
            }
        )

    return df


if __name__ == "__main__":

    df = load_data("../data/Mall_Customers.csv")

    processed_df = preprocess_data(df)

    processed_df.to_csv(
        "../data/processed_data.csv",
        index=False
    )

    print("Preprocessing Completed")