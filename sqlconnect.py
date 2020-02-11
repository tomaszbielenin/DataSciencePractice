import pandas as pd
import sqlalchemy as sa

engine = sa.create_engine('mssql+pyodbc://PLKTW0-APP001/Cadworx_Request?driver=SQL+Server+Native+Client+11.0', echo=True)

sql = """SELECT *
  FROM [Cadworx_Request].[dbo].[tblProjects]"""

df = pd.read_sql_query(sql, engine)
df