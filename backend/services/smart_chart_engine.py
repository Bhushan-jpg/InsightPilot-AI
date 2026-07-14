import pandas as pd

from services.chart_recommender import ChartRecommender

from services.chart_utils import *

from services.chart_generator import (
    create_bar_chart,
    create_line_chart,
    create_pie_chart,
    create_histogram
)


class SmartChartEngine:

    def __init__(self, df):

        self.df = df

        self.charts = []

        self.recommender = ChartRecommender(df)

        self.recommendations = self.recommender.recommend()


    # -----------------------------------------
    # Main Function
    # -----------------------------------------

    def generate(self):

        if self.df is None or self.df.empty:

            return []

        for chart in self.recommendations:

            chart_type = chart["chart"]

            try:

                if chart_type == "line":

                    self.build_line(chart)

                elif chart_type == "bar":

                    self.build_bar(chart)

                elif chart_type == "pie":

                    self.build_pie(chart)

                elif chart_type == "histogram":

                    self.build_histogram(chart)

                elif chart_type == "horizontal_bar":

                    self.build_horizontal_bar(chart)

            except Exception as e:

                print("Chart Error :", e)

        for i, chart in enumerate(self.charts):

            chart["id"] = i + 1

        return self.charts
        # -----------------------------------------
    # Build Line Chart
    # -----------------------------------------

    def build_line(self, recommendation):

        date_col = recommendation["date"]

        value_col = recommendation["value"]

        chart = create_line_chart(

            self.df,

            date_col,

            value_col

        )

        if chart:

            self.charts.append(chart)


    # -----------------------------------------
    # Build Bar Chart
    # -----------------------------------------

    def build_bar(self, recommendation):

        category = recommendation["category"]

        value = recommendation["value"]

        chart = create_bar_chart(

            self.df,

            category,

            value

        )

        if chart:

            self.charts.append(chart)


    # -----------------------------------------
    # Build Horizontal Bar
    # -----------------------------------------

    def build_horizontal_bar(self, recommendation):

        category = recommendation["category"]

        value = recommendation["value"]

        chart = create_bar_chart(

            self.df,

            category,

            value

        )

        if chart:

            chart["title"] = "Top 10 " + pretty_name(category)

            chart["subtitle"] = (

                "Highest performing "

                + pretty_name(category).lower()

            )

            chart["horizontal"] = True

            self.charts.append(chart)
                # -----------------------------------------
    # Build Pie Chart
    # -----------------------------------------

    def build_pie(self, recommendation):

        category = recommendation["category"]

        value = recommendation["value"]

        data = pie_data(

            self.df,

            category,

            value

        )

        chart = {

            "title": f"{pretty_name(category)} Distribution",

            "subtitle": "Top categories by contribution",

            "type": "pie",

            "x": category,

            "y": value,

            "data": data.to_dict("records"),

            "explanation":
            f"This chart shows how {pretty_name(value).lower()} is distributed across different {pretty_name(category).lower()}.",

            "insight":
            f"The top 5 {pretty_name(category).lower()} contribute most of the overall value.",

            "recommendation":
            f"Focus on the highest contributing {pretty_name(category).lower()} while improving the lower-performing ones."

        }

        self.charts.append(chart)


    # -----------------------------------------
    # Build Histogram
    # -----------------------------------------

    def build_histogram(self, recommendation):

        value = recommendation["value"]

        data = histogram_data(

            self.df,

            value

        )

        chart = {

            "title": f"{pretty_name(value)} Distribution",

            "subtitle": "Value distribution",

            "type": "bar",

            "x": "Range",

            "y": "Count",

            "data": data.to_dict("records"),

            "explanation":
            f"This chart explains how {pretty_name(value).lower()} values are distributed.",

            "insight":
            "Most records fall within a limited number of value ranges.",

            "recommendation":
            "Investigate unusually high and unusually low values."

        }

        self.charts.append(chart)
            # -----------------------------------------
    # Enhance Charts with AI Metadata
    # -----------------------------------------

    def enhance_charts(self):

        dataset = detect_dataset_type(self.df)

        for chart in self.charts:

            chart["dataset"] = dataset

            chart["confidence"] = "High"

            chart["generated_by"] = "InsightPilot AI"

            chart["ai"] = {

                "summary":
                chart.get(
                    "explanation",
                    ""
                ),

                "insight":
                chart.get(
                    "insight",
                    ""
                ),

                "recommendation":
                chart.get(
                    "recommendation",
                    ""
                )

            }

        return self.charts


    # -----------------------------------------
    # Final Output
    # -----------------------------------------

    def build(self):

        charts = self.generate()

        charts = self.enhance_charts()

        return charts