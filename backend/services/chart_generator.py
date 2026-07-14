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

    priority = [
        "category",
        "product",
        "region",
        "payment",
        "status",
        "department",
        "segment",
        "city",
        "state",
        "country",
        "gender",
        "hospital",
        "disease"
    ]

    # First search by important names
    for word in priority:
        for col in df.columns:

            if word in col.lower():
                return col

    # Otherwise use any object column
    for col in df.columns:

        if (
            df[col].dtype == object
            and "id" not in col.lower()
        ):
            return col

    return None
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
# Professional Bar Chart (Version 2)
# =====================================================

def create_bar_chart(df, category, value):

    # ------------------------------------------------
    # Aggregate Data
    # ------------------------------------------------

    chart_data = (

        df
        .groupby(category, as_index=False)[value]
        .sum()
        .sort_values(
            by=value,
            ascending=False
        )

    )

    chart_data = chart_data.dropna()

    # ------------------------------------------------
    # Top 10 + Others
    # ------------------------------------------------

    if len(chart_data) > 10:

        top10 = chart_data.head(10)

        others = chart_data.iloc[10:][value].sum()

        if others > 0:

            others_row = pd.DataFrame({

                category: ["Others"],

                value: [others]

            })

            chart_data = pd.concat(
                [top10, others_row],
                ignore_index=True
            )

        else:

            chart_data = top10

    chart_data = chart_data.reset_index(drop=True)

    # ------------------------------------------------
    # Statistics
    # ------------------------------------------------

    highest = chart_data.iloc[0]

    lowest = chart_data.iloc[-1]

    total = chart_data[value].sum()

    average = chart_data[value].mean()

    highest_percentage = round(

        highest[value] / total * 100,

        2

    )

    lowest_percentage = round(

        lowest[value] / total * 100,

        2

    )

    # ------------------------------------------------
    # Orientation
    # ------------------------------------------------

    horizontal = False

    if len(chart_data) >= 6:

        horizontal = True

    if chart_data[category].astype(str).str.len().max() > 12:

        horizontal = True

    # ------------------------------------------------
    # Build Chart
    # ------------------------------------------------

    return {

        "title":

        f"Top {len(chart_data)} {pretty_name(category)} by {pretty_name(value)}",

        "subtitle":

        f"Ranked comparison based on total {pretty_name(value).lower()}.",

        "type":"bar",

        "horizontal":horizontal,

        "color":COLORS[0],

        "x":category,

        "y":value,

        "data":

        chart_data.fillna("").to_dict("records"),

        "explanation":

        (

            f"This chart ranks "

            f"{pretty_name(category).lower()} "

            f"using total "

            f"{pretty_name(value).lower()}."

        ),

        "insight":

        (

            f"{highest[category]} "

            f"contributes "

            f"{highest_percentage}% "

            f"of the displayed total. "

            f"The average "

            f"{pretty_name(value).lower()} "

            f"is "

            f"{format_number(average)}."

        ),

        "recommendation":

        (

            f"Study the success factors of "

            f"{highest[category]} "

            f"and improve lower-performing "

            f"{pretty_name(category).lower()} "

            f"such as "

            f"{lowest[category]} "

            f"({lowest_percentage}% contribution)."

        )

    }# =====================================================
# Create Professional Pie Chart
# =====================================================

def create_pie_chart(df, category, value):

    # -------------------------------------------------
    # Aggregate
    # -------------------------------------------------

    chart_data = (

        df
        .groupby(category, as_index=False)[value]
        .sum()
        .sort_values(
            by=value,
            ascending=False
        )

    )

    chart_data = chart_data.dropna()

    # -------------------------------------------------
    # Top 5 + Others
    # -------------------------------------------------

    if len(chart_data) > 5:

        top5 = chart_data.head(5)

        others_total = chart_data.iloc[5:][value].sum()

        if others_total > 0:

            others = pd.DataFrame({

                category: ["Others"],

                value: [others_total]

            })

            chart_data = pd.concat(
                [top5, others],
                ignore_index=True
            )

        else:

            chart_data = top5

    chart_data = chart_data.reset_index(drop=True)

    # -------------------------------------------------
    # Percentages
    # -------------------------------------------------

    total = chart_data[value].sum()

    chart_data["Percentage"] = (

        chart_data[value]
        / total
        * 100

    ).round(2)

    highest = chart_data.iloc[0]

    lowest = chart_data.iloc[-1]

    # -------------------------------------------------
    # Build Chart
    # -------------------------------------------------

    return {

        "title":

        f"{pretty_name(category)} Share",

        "subtitle":

        f"Contribution of each {pretty_name(category).lower()} to total {pretty_name(value).lower()}.",

        "type":"pie",

        "color":COLORS[1],

        "x":category,

        "y":value,

        "data":

        chart_data.fillna("").to_dict("records"),

        "explanation":

        (

            f"This pie chart shows how total "

            f"{pretty_name(value).lower()} "

            f"is distributed across "

            f"{pretty_name(category).lower()}."

        ),

        "insight":

        (

            f"{highest[category]} "

            f"is the largest contributor "

            f"with "

            f"{highest['Percentage']}% "

            f"of the total."

        ),

        "recommendation":

        (

            f"Focus on maintaining the performance of "

            f"{highest[category]} "

            f"while improving lower-contributing "

            f"{pretty_name(category).lower()} "

            f"such as "

            f"{lowest[category]}."

        )

    } # =====================================================
# Create Professional Line Chart (Monthly Trend)
# =====================================================

def create_line_chart(df, date_col, value):

    try:

        temp = df.copy()
        temp[date_col] = pd.to_datetime(temp[date_col])

        # --------------------------------------------------
        # Decide aggregation level
        # --------------------------------------------------

        total_days = (temp[date_col].max() - temp[date_col].min()).days

        if total_days > 730:

            temp["Period"] = temp[date_col].dt.to_period("Y").astype(str)

        elif total_days > 90:

            temp["Period"] = temp[date_col].dt.to_period("M").astype(str)

        elif total_days > 14:

            temp["Period"] = temp[date_col].dt.to_period("W").astype(str)

        else:

            temp["Period"] = temp[date_col].dt.strftime("%d %b")

        # --------------------------------------------------
        # Choose aggregation automatically
        # --------------------------------------------------

        SUM_COLUMNS = [

            "sales",
            "revenue",
            "profit",
            "quantity",
            "cost",
            "price",
            "amount",
            "income",
            "expense"

        ]

        use_sum = any(word in value.lower() for word in SUM_COLUMNS)

        if use_sum:

            chart_data = (

                temp.groupby("Period")[value]
                .sum()
                .reset_index()

            )

            title = f"{pretty_name(value)} Trend"

            subtitle = "Total values across time."

        else:

            chart_data = (

                temp.groupby("Period")[value]
                .mean()
                .reset_index()

            )

            title = f"Average {pretty_name(value)} Trend"

            subtitle = "Average values across time."

        # --------------------------------------------------

        highest = chart_data.loc[chart_data[value].idxmax()]
        lowest = chart_data.loc[chart_data[value].idxmin()]
        average = chart_data[value].mean()

        return {

            "title": title,

            "subtitle": subtitle,

            "type": "line",

            "color": COLORS[2],

            "x": "Period",

            "y": value,

            "data": chart_data.to_dict("records"),

            "explanation":
                f"This chart shows how {pretty_name(value).lower()} changes over time.",

            "insight":
                (
                    f"Highest value occurred during {highest['Period']} "
                    f"({format_number(highest[value])}). "
                    f"Lowest value occurred during {lowest['Period']} "
                    f"({format_number(lowest[value])}). "
                    f"Average value: {format_number(average)}."
                ),

            "recommendation":
                (
                    "Investigate periods with unusually high or low values "
                    "to understand business drivers and seasonality."
                )

        }

    except Exception as e:

        print("Line Chart Error:", e)

        return None
# =====================================================
# Create Professional Histogram
# =====================================================

def create_histogram(df, value):

    temp = df[[value]].dropna()

    if temp.empty:
        return None

    # -----------------------------------------
    # Dynamic bins
    # -----------------------------------------

    n = len(temp)

    bins = max(6, min(15, int(np.sqrt(n))))

    temp["Range"] = pd.cut(
        temp[value],
        bins=bins
    )

    chart_data = (

        temp
        .groupby("Range")
        .size()
        .reset_index(name="Count")

    )

    labels = []

    for interval in chart_data["Range"]:

        left = interval.left
        right = interval.right

        labels.append(

            f"{format_number(left)} - {format_number(right)}"

        )

    chart_data["Range"] = labels

    # -----------------------------------------
    # Statistics
    # -----------------------------------------

    mean_value = temp[value].mean()

    median_value = temp[value].median()

    minimum = temp[value].min()

    maximum = temp[value].max()

    std = temp[value].std()

    highest_bin = chart_data.loc[
        chart_data["Count"].idxmax()
    ]

    # -----------------------------------------
    # Build chart
    # -----------------------------------------

    return {

        "title":

        f"{pretty_name(value)} Distribution",

        "subtitle":

        "Frequency of records across value ranges.",

        "type":"bar",

        "color":COLORS[3],

        "x":"Range",

        "y":"Count",

        "data":

        chart_data.to_dict("records"),

        "explanation":

        (

            f"This histogram shows how "

            f"{pretty_name(value).lower()} "

            f"is distributed across different value ranges."

        ),

        "insight":

        (

            f"Most records fall within "

            f"{highest_bin['Range']}. "

            f"The average value is "

            f"{format_number(mean_value)}, "

            f"while the median is "

            f"{format_number(median_value)}."

        ),

        "recommendation":

        (

            f"Review values outside the normal range "

            f"({format_number(minimum)} - "

            f"{format_number(maximum)}) "

            f"to identify unusual observations or business opportunities."

        ),

        "statistics":{

            "mean":float(mean_value),

            "median":float(median_value),

            "min":float(minimum),

            "max":float(maximum),

            "std":float(std)

        }

    }
# =====================================================
# Generate AI Charts
# =====================================================

def generate_ai_charts(df):

    charts = []

    if df is None or df.empty:
        print("Dataset is empty.")
        return charts

    value_col = get_best_numeric(df)
    category_col = get_best_category(df)
    date_col = get_date_column(df)

    print("\n================ DATASET INFO ================")
    print("Rows           :", len(df))
    print("Columns        :", list(df.columns))
    print("Value Column   :", value_col)
    print("Category Column:", category_col)
    print("Date Column    :", date_col)
    print("==============================================\n")

    if value_col is None:
        print("No numeric column found.")
        return charts

    # ---------------- BAR ----------------

    if category_col:

        try:

            print("Creating Bar Chart...")

            bar_chart = create_bar_chart(
                df,
                category_col,
                value_col
            )

            if bar_chart:
                charts.append(bar_chart)
                print("✓ Bar Chart Added")
            else:
                print("✗ Bar Chart Returned None")

        except Exception as e:

            print("Bar Chart Error:", e)

    else:

        print("No category column for Bar Chart")

    # ---------------- PIE ----------------

    if category_col:

        try:

            print("Creating Pie Chart...")

            pie_chart = create_pie_chart(
                df,
                category_col,
                value_col
            )

            if pie_chart:
                charts.append(pie_chart)
                print("✓ Pie Chart Added")
            else:
                print("✗ Pie Chart Returned None")

        except Exception as e:

            print("Pie Chart Error:", e)

    else:

        print("No category column for Pie Chart")

    # ---------------- LINE ----------------

    if date_col:

        try:

            print("Creating Line Chart...")

            line_chart = create_line_chart(
                df,
                date_col,
                value_col
            )

            if line_chart:
                charts.append(line_chart)
                print("✓ Line Chart Added")
            else:
                print("✗ Line Chart Returned None")

        except Exception as e:

            print("Line Chart Error:", e)

    else:

        print("No date column for Line Chart")

    # ---------------- HISTOGRAM ----------------

    try:

        print("Creating Histogram...")

        histogram = create_histogram(
            df,
            value_col
        )

        if histogram:
            charts.append(histogram)
            print("✓ Histogram Added")
        else:
            print("✗ Histogram Returned None")

    except Exception as e:

        print("Histogram Error:", e)

    # Remove invalid charts

    charts = [c for c in charts if c is not None]

    # Add IDs

    for i, chart in enumerate(charts):
        chart["id"] = i + 1

    print("\n============= FINAL CHARTS =================")

    for chart in charts:
        print(f"{chart['id']}. {chart['type']} -> {chart['title']}")

    print("Total Charts:", len(charts))
    print("============================================\n")

    return charts