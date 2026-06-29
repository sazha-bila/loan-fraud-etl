import psycopg2

from src.logger import get_logger
from config.db import DB_CONFIG


logger = get_logger(__name__)

def load(df):
    conn = psycopg2.connect(**DB_CONFIG)

    cur = conn.cursor()

    for _, row in df.iterrows():
        cur.execute("""
                    INSERT INTO loans (loan_id, income, loan_amount, credit_score, fraud)
                    VALUES (%s, %s, %s, %s, %s)
                    ON CONFLICT (loan_id) DO NOTHING
        """, (
            row.loan_id,
            int(row.income),
            int(row.loan_amount),
            int(row.credit_score),
            int(row.fraud)
        ))

    conn.commit()
    cur.close()
    conn.close()

    logger.info("Load completed")
