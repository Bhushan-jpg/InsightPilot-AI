def detect_schema(df):

    schema = {}

    columns = [col.lower() for col in df.columns]

    BUSINESS_FIELDS = {

        "customer": [
            "customer",
            "customer id",
            "customer name",
            "client"
        ],

        "product": [
            "product",
            "product name",
            "item"
        ],

        "city": [
            "city",
            "location",
            "state"
        ],

        "category": [
            "category",
            "segment"
        ],

        "date": [
            "date",
            "order date",
            "invoice date"
        ],

        "sales": [
            "sales",
            "revenue",
            "amount"
        ],

        "quantity": [
            "quantity",
            "qty"
        ],

        "profit": [
            "profit"
        ],

        "price": [
            "price"
        ],

        "cost": [
            "cost"
        ]

    }

    for field, keywords in BUSINESS_FIELDS.items():

        for keyword in keywords:

            for i, column in enumerate(columns):

                if keyword in column:

                    schema[field] = df.columns[i]

                    break

            if field in schema:
                break

    return schema