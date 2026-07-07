import pandas as pd


def generate_insights(df):

    findings = []
    recommendations = []

    # Dataset Size
    findings.append(
        f"The dataset contains {df.shape[0]:,} rows and {df.shape[1]} columns."
    )

    # Missing Values
    missing = int(df.isnull().sum().sum())

    if missing == 0:
        findings.append(
            "The dataset has no missing values."
        )
    else:
        findings.append(
            f"The dataset contains {missing} missing values."
        )
        recommendations.append(
            "Handle missing values before performing advanced analysis."
        )

    # Duplicate Records
    duplicates = int(df.duplicated().sum())

    if duplicates == 0:
        findings.append(
            "No duplicate records were found."
        )
    else:
        findings.append(
            f"{duplicates} duplicate records were found."
        )
        recommendations.append(
            "Remove duplicate records to improve data quality."
        )

    # Numeric Columns
    numeric_cols = df.select_dtypes(include=["number"]).columns

    for col in numeric_cols:

        findings.append(
            f"The average {col} is {round(df[col].mean(),2)}."
        )

        recommendations.append(
            f"Monitor the {col} metric regularly to identify trends and improve decision-making."
        )

    # Categorical Columns
    categorical_cols = df.select_dtypes(
        include=["object", "category"]
    ).columns

    for col in categorical_cols:

        findings.append(
            f"{col} contains {df[col].nunique()} unique values."
        )

    # General Recommendation
    recommendations.append(
        "Use Smart Charts to identify important business trends."
    )

    recommendations.append(
        "Use the AI Chat to ask questions about your dataset in simple language."
    )

    return {
        "findings": findings,
        "recommendations": recommendations
    }