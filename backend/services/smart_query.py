import pandas as pd


# =====================================================
# Helper Functions
# =====================================================

CATEGORY_KEYWORDS = {
    "city": ["city", "location", "state"],
    "customer": ["customer", "customer name", "client"],
    "product": ["product", "product name", "item"],
    "category": ["category", "segment"],
    "region": ["region"],
}

NUMERIC_KEYWORDS = {
    "sales": ["sales", "revenue", "amount"],
    "profit": ["profit"],
    "quantity": ["quantity", "qty"],
    "price": ["price"],
    "cost": ["cost"],
    "balance": ["balance"],
}


def find_category_column(df, question):

    cols = [c.lower() for c in df.columns]

    for key, words in CATEGORY_KEYWORDS.items():

        if any(word in question for word in words):

            for i, col in enumerate(cols):

                if any(word in col for word in words):
                    return df.columns[i]

    return None


def find_numeric_column(df, question):

    numeric_cols = df.select_dtypes(include="number").columns

    for key, words in NUMERIC_KEYWORDS.items():

        if any(word in question for word in words):

            for col in numeric_cols:

                if any(word in col.lower() for word in words):
                    return col

    # fallback
    if len(numeric_cols) > 0:
        return numeric_cols[0]

    return None


# =====================================================
# Main Smart Query
# =====================================================

def smart_query(question, df):

    question = question.lower().strip()

    # -----------------------------------
    # Dataset Info
    # -----------------------------------

    if "row" in question or "record" in question:
        return f"The dataset contains {len(df):,} records."

    if "column name" in question:
        return "Columns:\n\n" + ", ".join(df.columns)

    if "column" in question:
        return f"The dataset contains {len(df.columns)} columns."

    if "missing" in question or "null" in question:
        return f"The dataset contains {df.isnull().sum().sum()} missing values."

    if "duplicate" in question:
        return f"The dataset contains {df.duplicated().sum()} duplicate records."

    # -----------------------------------
    # Statistics
    # -----------------------------------

    num_col = find_numeric_column(df, question)

    if num_col is not None:

        if "average" in question or "mean" in question:
            return f"The average {num_col} is {df[num_col].mean():,.2f}."

        if "total" in question or "sum" in question:
            return f"The total {num_col} is {df[num_col].sum():,.2f}."

        if "maximum" in question or "max" in question:
            return f"The maximum {num_col} is {df[num_col].max():,.2f}."

        if "minimum" in question or "min" in question:
            return f"The minimum {num_col} is {df[num_col].min():,.2f}."

    # -----------------------------------
    # Business Questions
    # -----------------------------------

    cat_col = find_category_column(df, question)

    if cat_col is not None and num_col is not None:

        grouped = (
            df.groupby(cat_col)[num_col]
            .sum()
            .sort_values(ascending=False)
        )

        # Highest
        if (
            "highest" in question
            or "top" in question
            or "most" in question
            or "best" in question
        ):

            winner = grouped.index[0]
            value = grouped.iloc[0]

            return (
                f"{winner} has the highest {num_col} "
                f"({value:,.2f})."
            )

        # Lowest
        if "lowest" in question:

            grouped = grouped.sort_values()

            winner = grouped.index[0]
            value = grouped.iloc[0]

            return (
                f"{winner} has the lowest {num_col} "
                f"({value:,.2f})."
            )

        # Top 5
        if "top 5" in question:

            top5 = grouped.head(5)

            text = f"Top 5 {cat_col} by {num_col}:\n\n"

            for i, (name, value) in enumerate(top5.items(), start=1):
                text += f"{i}. {name} - {value:,.2f}\n"

            return text

    # -----------------------------------
    # Not Found
    # -----------------------------------

    return None