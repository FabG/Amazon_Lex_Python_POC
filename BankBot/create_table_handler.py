import sys
import logging
import rds_config
import pymysql

#rds settings
rds_host    = rds_config.DB_ENDPOINT
name        = rds_config.DB_USERNAME
password    = rds_config.DB_PASSWORD
db_name     = rds_config.DB_NAME

logger = logging.getLogger()
logger.setLevel(logging.INFO)

conn = None

def openConnection():
    global conn
    logger.info("Connecting to RDS MySQL (host: %s)" % rds_host)
    try:
        if(conn is None):
            conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
        elif(not conn.open):
            conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
    except:
        logger.error("ERROR: Unexpected error: Could not connect to MySql instance.")
        sys.exit()

    logger.info("SUCCESS: Connection to RDS mysql instance succeeded")


def create_table(event):
    """
    This function creates a Table and add data to mysql RDS instance
    """
    try:
        openConnection()
        result = []

        with conn.cursor() as cur:
            sql = "create table if not exists Users (userid  int NOT NULL, name varchar(255) NOT NULL, PRIMARY KEY (userid))"
            cur.execute(sql)
            logger.info("Users Table created if any")

            cur.execute('insert into Users (userid, name) values(%s, %s)' % (event['id'], event['name']))
            logger.info("InsertedUser ID: %s and Name: %s" % (event['id'], event['name']))

            conn.commit()
            cur.execute("select * from Users")
            result = cur.fetchall()
            logger.info("result from select * from Users: ")
            logger.info(result)
        conn.commit()
        conn.close()

    except Exception as e:
        print(e)
        logger.error("ERROR: Unexpected error: Could not connect to MySql instance.")



def handler(event, context):
    create_table(event)
