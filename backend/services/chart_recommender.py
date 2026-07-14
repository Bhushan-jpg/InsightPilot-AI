from services.chart_utils import *

class ChartRecommender:

    def __init__(self, df):

        self.df = df

        self.dataset_type = detect_dataset_type(df)

        self.summary = dataset_summary(df)

        self.recommendations = []


    # -----------------------------------
    # Main Function
    # -----------------------------------

    def recommend(self):

        if not can_generate_charts(self.df):

            return []

        if self.dataset_type == "airline":

            self._recommend_airline()

        elif self.dataset_type == "sales":

            self._recommend_sales()

        elif self.dataset_type == "employee":

            self._recommend_employee()

        elif self.dataset_type == "amazon":

            self._recommend_amazon()

        elif self.dataset_type == "hospital":

            self._recommend_hospital()

        elif self.dataset_type == "banking":

            self._recommend_banking()

        else:

            self._recommend_generic()

        return self.recommendations


    # -----------------------------------
    # Add Chart
    # -----------------------------------

    def add(self, chart):

        self.recommendations.append(chart)


    # -----------------------------------
    # Airline
    # -----------------------------------

    def _recommend_airline(self):

        charts = recommend_charts(self.df)

        for chart in charts:

            self.add(chart)


    # -----------------------------------
    # Sales
    # -----------------------------------

    def _recommend_sales(self):

        charts = recommend_charts(self.df)

        for chart in charts:

            self.add(chart)


    # -----------------------------------
    # Employee
    # -----------------------------------

    def _recommend_employee(self):

        charts = recommend_charts(self.df)

        for chart in charts:

            self.add(chart)
                # -----------------------------------
    # Amazon Dataset
    # -----------------------------------

    def _recommend_amazon(self):

        charts = recommend_charts(self.df)

        for chart in charts:

            self.add(chart)


    # -----------------------------------
    # Hospital Dataset
    # -----------------------------------

    def _recommend_hospital(self):

        charts = recommend_charts(self.df)

        for chart in charts:

            self.add(chart)


    # -----------------------------------
    # Banking Dataset
    # -----------------------------------

    def _recommend_banking(self):

        charts = recommend_charts(self.df)

        for chart in charts:

            self.add(chart)


    # -----------------------------------
    # Generic Dataset
    # -----------------------------------

    def _recommend_generic(self):

        charts = recommend_charts(self.df)

        for chart in charts:

            self.add(chart)


    # -----------------------------------
    # Return Best Charts
    # -----------------------------------

    def top_recommendations(self, limit=6):

        charts = sorted(

            self.recommendations,

            key=lambda x: x["priority"]

        )

        return charts[:limit]


    # -----------------------------------
    # Debug Information
    # -----------------------------------

    def info(self):

        return {

            "dataset": self.dataset_type,

            "summary": self.summary,

            "recommended_charts": len(self.recommendations),

            "charts": self.recommendations

        }