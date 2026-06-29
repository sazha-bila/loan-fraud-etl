
from src.logger import get_logger

logger = get_logger(__name__)

def transform(df):
    df["fraud"] = (
        (df["loan_amount"] > df["income"] * 3) |
        (df["credit_score"] < 520) |
        (df["loan_amount"] > 15000)
    ).astype(int)

    fraud_count = df["fraud"].sum()
    
    logger.info("Transformation completed")

    return df