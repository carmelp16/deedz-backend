import psycopg
from typing import Dict, Any

# Function to execute the query
# Returns a Dict object which is a JSON of result
def execute_query(query: str, host: str, dbname: str, user: str, password: str,
                params: tuple = None, is_edit: bool = False, execute_many: bool = False) -> Dict[str,Any]:
    with psycopg.connect(host=host, dbname=dbname,
                          user=user, password=password) as conn:
        
        with conn.cursor() as cur: 
            if not execute_many:
                cur.execute(query, params) if params else cur.execute(query)
                data = cur.fetchall()
                colnames = [desc[0] for desc in cur.description]
            
            else:
                cur.executemany(query, params)
                #no need to collect cols because it is edit

            if is_edit:
                conn.commit()

    if execute_many:
        return
    result = [dict(zip(colnames, row)) for row in data]
    return result