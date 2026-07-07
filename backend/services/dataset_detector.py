def detect_dataset_type(df):

    columns = [c.lower() for c in df.columns]

    # Sales
    if any(x in columns for x in ["sales", "revenue", "profit", "price", "quantity"]):
        return {
            "type": "Sales Analytics",
            "icon": "🛒",
            "confidence": 98
        }

    # Banking
    if any(x in columns for x in ["balance", "transaction_amount", "account_type"]):
        return {
            "type": "Banking Analytics",
            "icon": "🏦",
            "confidence": 98
        }

    # HR
    if any(x in columns for x in ["salary", "employee", "department"]):
        return {
            "type": "HR Analytics",
            "icon": "👨‍💼",
            "confidence": 97
        }

    # Healthcare
    if any(x in columns for x in ["patient", "hospital", "diagnosis"]):
        return {
            "type": "Healthcare Analytics",
            "icon": "🏥",
            "confidence": 96
        }

    return {
        "type": "General Dataset",
        "icon": "📊",
        "confidence": 90
    }