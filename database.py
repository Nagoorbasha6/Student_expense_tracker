from sqlalchemy.orm import sessionMaker,declarative_base
from sqlalchemy import create_engine
db_url="mysql+pymysql://root:@Basha143@localhost:3306/student_expense_tracker"
engine=create_engine(db_url)
sessionLocal=sessionMaker(autocommit=False,autoflush=False,bind=engine)
Base=declarative_base()