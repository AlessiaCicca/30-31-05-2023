from database.DB_connect import DBConnect
from model.connessione import Connessione
from model.rivenditori import Rivenditore


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getNazione():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct gr.Country as nazione
from go_retailers gr"""


        cursor.execute(query)

        for row in cursor:
            result.append(row["nazione"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getNodi(nazione):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct gr.*
                    from go_retailers gr 
                    where gr.Country =%s
                    order by gr.Retailer_name"""

        cursor.execute(query,(nazione,))

        for row in cursor:
            result.append(Rivenditore(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllRivenditori():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct gr.*
                      from go_retailers gr 
                      
                      """

        cursor.execute(query)

        for row in cursor:
            result.append(Rivenditore(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getConnessioni(nazione,anno,n):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select t1.r1 as v1,t2.r2 as v2,count(distinct t1.p1) as peso
from (select gds.Retailer_code as r1 , gds.Product_number as p1 
from go_daily_sales gds, go_retailers gr 
where gds.Retailer_code=gr.Retailer_code
and gr.Country=%s and year(gds.`Date`)=%s) as t1,
(select gds.Retailer_code as r2 , gds.Product_number as p2 
from go_daily_sales gds, go_retailers gr 
where gds.Retailer_code=gr.Retailer_code
and gr.Country=%s and year(gds.`Date`)=%s) as t2
where t1.r1!=t2.r2 and t1.p1=t2.p2
group by t1.r1,t2.r2
having count(distinct t1.p1)>=%s"""

        cursor.execute(query,(nazione,anno,nazione,anno,n))

        for row in cursor:
            result.append(Connessione(**row))

        cursor.close()
        conn.close()
        return result
