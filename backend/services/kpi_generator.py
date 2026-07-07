import pandas as pd


def format_number(num):
    """
    Convert large numbers into a readable format.
    """

    num = float(num)

    if num >= 10000000:
        return f"₹{num / 10000000:.2f} Cr"

    elif num >= 100000:
        return f"₹{num / 100000:.2f} Lakh"

    elif num >= 1000:
        return f"₹{num / 1000:.2f} K"

    else:
        return f"₹{num:.2f}"


def generate_kpis(df):

    kpis = []

    # -----------------------------
    # Generic KPIs
    # -----------------------------

    kpis.append({
        "title": "📄 Total Records",
        "value": f"{len(df):,}",
        "description": "Total rows in dataset"
    })

    kpis.append({
        "title": "📋 Total Columns",
        "value": len(df.columns),
        "description": "Available fields"
    })

    # -----------------------------
    # Sales KPIs
    # -----------------------------

    sales_keywords = [
        "sales",
        "revenue",
        "amount",
        "price",
        "profit"
    ]

    for col in df.columns:

        if any(keyword in col.lower() for keyword in sales_keywords):

            total_sales = df[col].sum()
            avg_sales = df[col].mean()

            kpis.append({

                "title": "💰 Total Sales",

                "value": format_number(total_sales),

                "description": "Overall sales generated"

            })

            kpis.append({

                "title": "📈 Average Sale",

                "value": format_number(avg_sales),

                "description": "Average value per transaction"

            })

            break

    # -----------------------------
    # Customers
    # -----------------------------

    for col in df.columns:

        if "customer" in col.lower():

            kpis.append({

                "title": "👥 Customers",

                "value": f"{df[col].nunique():,}",

                "description": "Unique customers"

            })

            break

    # -----------------------------
    # Cities
    # -----------------------------

    for col in df.columns:

        if "city" in col.lower():

            kpis.append({

                "title": "🏙 Cities",

                "value": df[col].nunique(),

                "description": "Business locations"

            })

            break

    # -----------------------------
    # Date Range
    # -----------------------------

    for col in df.columns:

        if "date" in col.lower():

            try:

                dates = pd.to_datetime(df[col])

                kpis.append({

                    "title": "📅 Date Range",

                    "value": f"{dates.min().year} - {dates.max().year}",

                    "description": "Years covered"

                })

            except:
                pass

            break

    return kpis