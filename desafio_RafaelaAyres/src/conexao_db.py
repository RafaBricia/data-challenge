from sqlalchemy import create_engine

def get_engine():
    return create_engine(
        "mysql+pymysql://looqbox-challenge:looq-challenge@35.199.115.174/looqbox-challenge"
    )

