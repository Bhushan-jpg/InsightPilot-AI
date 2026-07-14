import pandas as pd
import numpy as np


# -----------------------------------------
# Pretty Column Name
# -----------------------------------------

def pretty_name(name):

    return (
        str(name)
        .replace("_", " ")
        .replace("-", " ")
        .title()
    )


# -----------------------------------------
# Detect Numeric Columns
# -----------------------------------------

def get_numeric_columns(df):

    return df.select_dtypes(
        include=np.number
    ).columns.tolist()


# -----------------------------------------
# Detect Category Columns
# -----------------------------------------

def get_category_columns(df):

    cols = []

    for col in df.columns:

        if df[col].dtype == object:

            if "id" in col.lower():
                continue

            cols.append(col)

    return cols


# -----------------------------------------
# Detect Date Columns
# -----------------------------------------

def get_date_columns(df):

    dates = []

    for col in df.columns:

        if "date" in col.lower():

            try:

                pd.to_datetime(df[col])

                dates.append(col)

            except:

                pass

    return dates


# -----------------------------------------
# Detect Boolean Columns
# -----------------------------------------

def get_boolean_columns(df):

    cols = []

    for col in df.columns:

        if str(df[col].dtype) == "bool":

            cols.append(col)

    return cols


# -----------------------------------------
# Detect Low Cardinality Columns
# Good for Pie Charts
# -----------------------------------------

def get_low_cardinality(df):

    cols = []

    for col in df.columns:

        if df[col].dtype == object:

            unique = df[col].nunique()

            if unique <= 8:

                cols.append(col)

    return cols


# -----------------------------------------
# Detect High Cardinality Columns
# Good for Top 10 Bar Charts
# -----------------------------------------

def get_high_cardinality(df):

    cols = []

    for col in df.columns:

        if df[col].dtype == object:

            unique = df[col].nunique()

            if unique > 8:

                cols.append(col)

    return cols
# -----------------------------------------
# Best Numeric Column
# -----------------------------------------

def get_best_numeric(df):

    numeric = get_numeric_columns(df)

    if not numeric:
        return None

    priority = [
        "sales",
        "revenue",
        "profit",
        "amount",
        "price",
        "cost",
        "income",
        "quantity",
        "total",
        "value",
        "score",
        "salary",
        "ticketprice",
        "fare"
    ]

    for keyword in priority:

        for col in numeric:

            if keyword in col.lower():

                return col

    return numeric[0]


# -----------------------------------------
# Second Numeric Column
# -----------------------------------------

def get_second_numeric(df, first):

    numeric = get_numeric_columns(df)

    for col in numeric:

        if col != first:

            return col

    return None


# -----------------------------------------
# Best Category Column
# -----------------------------------------

def get_best_category(df):

    categories = get_category_columns(df)

    if not categories:
        return None

    priority = [

        "category",
        "product",
        "department",
        "airline",
        "brand",
        "region",
        "city",
        "country",
        "route",
        "status",
        "gender",
        "customer",
        "employee",
        "doctor",
        "disease"

    ]

    for keyword in priority:

        for col in categories:

            if keyword in col.lower():

                return col

    return categories[0]


# -----------------------------------------
# Best Date Column
# -----------------------------------------

def get_best_date(df):

    dates = get_date_columns(df)

    if not dates:
        return None

    return dates[0]


# -----------------------------------------
# Dataset Type Detection
# -----------------------------------------

def detect_dataset_type(df):

    cols = [c.lower() for c in df.columns]

    airline = [
        "airline",
        "flight",
        "airport",
        "route",
        "ticket",
        "booking"
    ]

    sales = [
        "sales",
        "revenue",
        "profit",
        "customer",
        "product"
    ]

    employee = [
        "employee",
        "department",
        "salary",
        "experience",
        "designation"
    ]

    amazon = [
        "brand",
        "rating",
        "review",
        "price",
        "discount"
    ]

    hospital = [
        "patient",
        "doctor",
        "hospital",
        "disease"
    ]

    banking = [
        "loan",
        "balance",
        "account",
        "branch"
    ]

    if any(word in " ".join(cols) for word in airline):
        return "airline"

    if any(word in " ".join(cols) for word in employee):
        return "employee"

    if any(word in " ".join(cols) for word in amazon):
        return "amazon"

    if any(word in " ".join(cols) for word in hospital):
        return "hospital"

    if any(word in " ".join(cols) for word in banking):
        return "banking"

    if any(word in " ".join(cols) for word in sales):
        return "sales"

    return "generic"
# -----------------------------------------
# Aggregate Date by Month
# -----------------------------------------

def aggregate_by_month(df, date_col, value_col):

    temp = df.copy()

    temp[date_col] = pd.to_datetime(
        temp[date_col],
        errors="coerce"
    )

    temp = temp.dropna(subset=[date_col])

    temp["Month"] = temp[date_col].dt.strftime("%b %Y")

    result = (
        temp.groupby("Month")[value_col]
        .sum()
        .reset_index()
    )

    return result


# -----------------------------------------
# Top N Categories
# -----------------------------------------

def top_categories(df, category, value, top=10):

    result = (
        df.groupby(category)[value]
        .sum()
        .sort_values(ascending=False)
        .head(top)
        .reset_index()
    )

    return result


# -----------------------------------------
# Bottom N Categories
# -----------------------------------------

def bottom_categories(df, category, value, bottom=10):

    result = (
        df.groupby(category)[value]
        .sum()
        .sort_values()
        .head(bottom)
        .reset_index()
    )

    return result


# -----------------------------------------
# Pie Chart Data
# Top 5 + Others
# -----------------------------------------

def pie_data(df, category, value):

    grouped = (
        df.groupby(category)[value]
        .sum()
        .sort_values(ascending=False)
    )

    top5 = grouped.head(5)

    others = grouped.iloc[5:].sum()

    result = top5.reset_index()

    if others > 0:

        result.loc[len(result)] = [
            "Others",
            others
        ]

    return result


# -----------------------------------------
# Histogram Data
# -----------------------------------------

def histogram_data(df, value, bins=10):

    temp = df[[value]].dropna()

    temp["Range"] = pd.cut(
        temp[value],
        bins=bins
    )

    result = (
        temp.groupby("Range")
        .size()
        .reset_index(name="Count")
    )

    result["Range"] = result["Range"].astype(str)

    return result


# -----------------------------------------
# Remove Missing Values
# -----------------------------------------

def clean_dataframe(df):

    return df.dropna(how="all")


# -----------------------------------------
# Sort Descending
# -----------------------------------------

def sort_desc(df, column):

    return (
        df.sort_values(
            column,
            ascending=False
        )
        .reset_index(drop=True)
    )


# -----------------------------------------
# Sort Ascending
# -----------------------------------------

def sort_asc(df, column):

    return (
        df.sort_values(
            column
        )
        .reset_index(drop=True)
    )
# -----------------------------------------
# Smart Chart Recommendation Rules
# -----------------------------------------

def recommend_charts(df):

    recommendations = []

    numeric = get_numeric_columns(df)
    categories = get_category_columns(df)
    dates = get_date_columns(df)

    low_cardinality = get_low_cardinality(df)
    high_cardinality = get_high_cardinality(df)

    # -------------------------------------
    # Line Chart
    # -------------------------------------

    if len(dates) > 0 and len(numeric) > 0:

        recommendations.append({

            "chart": "line",

            "date": get_best_date(df),

            "value": get_best_numeric(df),

            "priority": 1

        })

    # -------------------------------------
    # Bar Chart
    # -------------------------------------

    if len(categories) > 0 and len(numeric) > 0:

        recommendations.append({

            "chart": "bar",

            "category": get_best_category(df),

            "value": get_best_numeric(df),

            "priority": 2

        })

    # -------------------------------------
    # Pie Chart
    # -------------------------------------

    if len(low_cardinality) > 0 and len(numeric) > 0:

        recommendations.append({

            "chart": "pie",

            "category": low_cardinality[0],

            "value": get_best_numeric(df),

            "priority": 3

        })

    # -------------------------------------
    # Histogram
    # -------------------------------------

    if len(numeric) > 0:

        recommendations.append({

            "chart": "histogram",

            "value": get_best_numeric(df),

            "priority": 4

        })

    # -------------------------------------
    # Horizontal Bar
    # -------------------------------------

    if len(high_cardinality) > 0 and len(numeric) > 0:

        recommendations.append({

            "chart": "horizontal_bar",

            "category": high_cardinality[0],

            "value": get_best_numeric(df),

            "priority": 5

        })

    return sorted(

        recommendations,

        key=lambda x: x["priority"]

    )


# -----------------------------------------
# Dataset Summary
# -----------------------------------------

def dataset_summary(df):

    return {

        "rows": len(df),

        "columns": len(df.columns),

        "numeric_columns": len(get_numeric_columns(df)),

        "category_columns": len(get_category_columns(df)),

        "date_columns": len(get_date_columns(df)),

        "dataset_type": detect_dataset_type(df)

    }


# -----------------------------------------
# Ready Check
# -----------------------------------------

def can_generate_charts(df):

    return len(get_numeric_columns(df)) > 0