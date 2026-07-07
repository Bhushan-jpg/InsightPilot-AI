import pandas as pd


def detect_dataset_type(df):

    columns = " ".join(
        df.columns.astype(str)
    ).lower()


    if any(word in columns for word in ["sales", "revenue", "profit", "price"]):
        return "Business / Sales Dataset"

    if any(word in columns for word in ["employee", "salary", "department"]):
        return "HR Dataset"

    if any(word in columns for word in ["patient", "disease", "hospital"]):
        return "Healthcare Dataset"

    if any(word in columns for word in ["student", "grade", "marks"]):
        return "Education Dataset"


    return "General Transaction Dataset"



def analyze_columns(df):

    result = []


    for column in df.columns:

        dtype = str(df[column].dtype)


        if "datetime" in dtype:
            column_type = "Date"

        elif dtype in ["int64","float64"]:
            column_type = "Number"

        else:
            column_type = "Category"


        role = "Dimension"


        if column_type == "Number":
            role = "KPI"


        result.append(
            {
                "name": column,
                "type": column_type,
                "role": role,
                "meaning": f"{column} information"
            }
        )


    return result



def profile_dataset(df):


    profile = {

        "dataset_type":
            detect_dataset_type(df),


        "rows":
            int(df.shape[0]),


        "columns":
            int(df.shape[1]),


        "quality":
        {

            "missing_values":
                int(df.isnull().sum().sum()),


            "duplicate_rows":
                int(df.duplicated().sum())
        },


        "column_analysis":
            analyze_columns(df)

    }


    return profile