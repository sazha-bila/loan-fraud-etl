import pandas as pd
import random
import uuid

from src.logger import get_logger

logger = get_logger(__name__)

def extract():
    
    logger.info("Extracting data")

    data=[]

    for i in range(50):
        data.append({
            "loan_id": str(uuid.uuid4()),
            "income": random.randint(1500, 10000),
            "loan_amount": random.randint(500, 20000),
            "credit_score": random.randint(300, 850)
        })

    df = pd.DataFrame(data)

    logger.info(f"Extracted {len(df)} rows")
    
    return df