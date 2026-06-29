import os 



from src.extract import extract
from src.transform import transform
from src.load import load
from src.logger import get_logger


os.makedirs("logs", exist_ok=True)

logger = get_logger(__name__)

def main():

    logger.info("Pipeline started")

    df = extract()
    logger.info(f"Extracted{len(df)} rows")

    df = transform(df)
    logger.info("Transformation completed")

    load(df)
    logger.info("Data loaded succesfully")


    logger.info("Pipeline finished succesfully")

if __name__ == "__main__":
    main()
