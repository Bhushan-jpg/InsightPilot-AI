import pandas as pd
import numpy as np


# =====================================================
# Professional Color Palette
# =====================================================

COLORS = [
    "#4F46E5",   # Indigo
    "#2563EB",   # Blue
    "#10B981",   # Green
    "#F59E0B",   # Orange
    "#EF4444",   # Red
    "#8B5CF6",   # Purple
    "#06B6D4",   # Cyan
    "#84CC16"    # Lime
]


# =====================================================
# Convert column name into readable text
# =====================================================

def pretty_name(name):

    return (
        str(name)
        .replace("_", " ")
        .replace("-", " ")
        .title()
    )


# =====================================================
# Safe Percentage Calculator
# =====================================================

def percentage(value, total):

    if total == 0:
        return 0

    return round((value / total) * 100, 1)


# =====================================================
# Smart Number Formatter
# =====================================================

def format_number(value):

    value = float(value)

    if value >= 1_000_000_000:
        return f"{value/1_000_000_000:.1f}B"

    if value >= 1_000_000:
        return f"{value/1_000_000:.1f}M"

    if value >= 1000:
        return f"{value/1000:.1f}K"

    return f"{value:,.2f}"


# =====================================================
# Detect Best Numeric Column
# =====================================================

def get_best_numeric(df):

    numeric = df.select_dtypes(include=np.number).columns.tolist()

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
        "score"

    ]

    for keyword in priority:

        for col in numeric:

            if keyword in col.lower():
                return col

    return numeric[0]


# =====================================================
# Detect Best Category Column
# =====================================================

def get_best_category(df):

    categories = []

    for col in df.columns:

        if df[col].dtype == object:

            if "id" in col.lower():
                continue

            if df[col].nunique() <= 30:
                categories.append(col)

    if not categories:
        return None

    priority = [

        "city",
        "state",
        "country",
        "product",
        "category",
        "department",
        "segment",
        "customer",
        "gender",
        "hospital",
        "disease"

    ]

    for keyword in priority:

        for col in categories:

            if keyword in col.lower():
                return col

    return categories[0]


# =====================================================
# Detect Date Column
# =====================================================

def get_date_column(df):

    for col in df.columns:

        if "date" in col.lower():

            try:

                df[col] = pd.to_datetime(df[col])

                return col

            except:

                pass

    return None
# =====================================================
# AI Insight Generator
# =====================================================

def build_insight(chart_data, category, value):

    if chart_data.empty:
        return "No meaningful insight could be generated."

    highest = chart_data.iloc[0]
    lowest = chart_data.iloc[-1]

    total = chart_data[value].sum()

    highest_percent = percentage(highest[value], total)
    lowest_percent = percentage(lowest[value], total)

    if len(chart_data) > 1:

        second = chart_data.iloc[1]

        difference = highest[value] - second[value]

        return (

            f"{highest[category]} leads with "

            f"{format_number(highest[value])} "

            f"({highest_percent}% of the total). "

            f"It performs "

            f"{format_number(difference)} "

            f"better than "

            f"{second[category]}. "

            f"{lowest[category]} contributes only "

            f"{lowest_percent}%."

        )

    return (

        f"{highest[category]} contributes "

        f"{highest_percent}% "

        "of the total value."

    )


# =====================================================
# AI Recommendation Generator
# =====================================================

def build_recommendation(chart_data, category):

    if len(chart_data) < 2:

        return (

            "Continue monitoring this metric "

            "to maintain business performance."

        )

    highest = chart_data.iloc[0]
    lowest = chart_data.iloc[-1]

    return (

        f"{highest[category]} performs the best. "

        f"Study the factors behind its success "

        f"and apply similar strategies to "

        f"{lowest[category]}. "

        "Improving lower-performing categories "

        "can increase overall business growth."

    )


# =====================================================
# Build AI Explanation
# =====================================================

def build_explanation(chart_type, value, category=None):

    if chart_type == "bar":

        return (

            f"This chart compares total "

            f"{pretty_name(value).lower()} "

            f"across different "

            f"{pretty_name(category).lower()}. "

            "Higher bars indicate stronger performance."

        )

    elif chart_type == "pie":

        return (

            "This chart shows how each category "

            "contributes to the overall total. "

            "Larger slices represent a bigger contribution."

        )

    elif chart_type == "line":

        return (

            "This chart tracks business performance "

            "over time. Rising values indicate growth, "

            "while falling values may require attention."

        )

    elif chart_type == "histogram":

        return (

            "This chart shows how records are "

            "distributed across different value ranges."

        )

    return "AI explanation unavailable."
    # =====================================================
# Create Professional Bar Chart
# =====================================================

def create_bar_chart(df, category, value):

    chart_data = (

        df.groupby(category)[value]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()

    )

    return {

        "title":
        f"Top {pretty_name(category)} by {pretty_name(value)}",

        "subtitle":
        f"Top 10 {pretty_name(category).lower()} ranked by total {pretty_name(value).lower()}.",

        "type":"bar",

        "color":COLORS[0],

        "x":category,

        "y":value,

        "data":
        chart_data.fillna("").to_dict("records"),

        "explanation":
        build_explanation(
            "bar",
            value,
            category
        ),

        "insight":
        build_insight(
            chart_data,
            category,
            value
        ),

        "recommendation":
        build_recommendation(
            chart_data,
            category
        )

    }


# =====================================================
# Create Professional Pie Chart
# =====================================================

def create_pie_chart(df, category, value):

    chart_data = (

        df.groupby(category)[value]
        .sum()
        .sort_values(ascending=False)
        .head(6)
        .reset_index()

    )

    total = chart_data[value].sum()

    chart_data["Percentage"] = (

        chart_data[value]
        / total
        * 100

    ).round(1)

    return {

        "title":
        f"{pretty_name(value)} Distribution",

        "subtitle":
        f"Percentage contribution by {pretty_name(category).lower()}.",

        "type":"pie",

        "color":COLORS[1],

        "x":category,

        "y":value,

        "data":
        chart_data.fillna("").to_dict("records"),

        "explanation":
        build_explanation(
            "pie",
            value,
            category
        ),

        "insight":
        build_insight(
            chart_data,
            category,
            value
        ),

        "recommendation":
        build_recommendation(
            chart_data,
            category
        )

    }
    # =====================================================
# Create Professional Line Chart
# =====================================================

def create_line_chart(df, date_col, value):

    try:

        temp = df.copy()

        temp[date_col] = pd.to_datetime(temp[date_col])

        chart_data = (

            temp.groupby(date_col)[value]
            .sum()
            .reset_index()

        )

        chart_data[date_col] = chart_data[date_col].dt.strftime("%Y-%m-%d")

        return {

            "title":
            f"{pretty_name(value)} Trend",

            "subtitle":
            "Business performance over time.",

            "type":"line",

            "color":COLORS[2],

            "x":date_col,

            "y":value,

            "data":
            chart_data.to_dict("records"),

            "explanation":
            build_explanation(
                "line",
                value
            ),

            "insight":
            (
                f"The highest recorded "
                f"{pretty_name(value).lower()} was "
                f"{format_number(chart_data[value].max())}."
            ),

            "recommendation":
            (
                "Monitor long-term trends to identify "
                "seasonality and support future planning."
            )

        }

    except:

        return None


# =====================================================
# Create Professional Histogram
# =====================================================

def create_histogram(df, value):

    temp = df[[value]].dropna()

    temp["Range"] = pd.cut(
        temp[value],
        bins=6
    )

    chart_data = (

        temp.groupby("Range")
        .size()
        .reset_index(name="Count")

    )

    labels = []

    for interval in chart_data["Range"]:

        left = int(interval.left)
        right = int(interval.right)

        labels.append(

            f"{format_number(left)} - {format_number(right)}"

        )

    chart_data["Range"] = labels

    return {

        "title":
        f"Distribution of {pretty_name(value)}",

        "subtitle":
        "Shows how records are spread.",

        "type":"bar",

        "color":COLORS[3],

        "x":"Range",

        "y":"Count",

        "data":
        chart_data.to_dict("records"),

        "explanation":
        build_explanation(
            "histogram",
            value
        ),

        "insight":
        (
            "Most records are concentrated "
            "within a small number of value ranges."
        ),

        "recommendation":
        (
            "Investigate unusually high or low values "
            "to detect outliers."
        )

    }


# =====================================================
# Generate AI Charts
# =====================================================

def generate_ai_charts(df):

    charts = []

    if df is None or df.empty:
        return charts

    value_col = get_best_numeric(df)
    category_col = get_best_category(df)
    date_col = get_date_column(df)

    if value_col is None:
        return charts

    # ---------------- BAR ----------------

    if category_col:

        try:

            charts.append(

                create_bar_chart(
                    df,
                    category_col,
                    value_col
                )

            )

        except Exception:

            pass

    # ---------------- PIE ----------------

    if category_col:

        try:

            charts.append(

                create_pie_chart(
                    df,
                    category_col,
                    value_col
                )

            )

        except Exception:

            pass

    # ---------------- LINE ----------------

    if date_col:

        try:

            line_chart = create_line_chart(
                df,
                date_col,
                value_col
            )

            if line_chart:

                charts.append(line_chart)

        except Exception:

            pass

    # ---------------- HISTOGRAM ----------------

    try:

        charts.append(

            create_histogram(
                df,
                value_col
            )

        )

    except Exception:

        pass

    # Add IDs

    for i, chart in enumerate(charts):

        chart["id"] = i + 1

    return charts