import psycopg2

conn_string = (
    "host=localhost port=5432 dbname=postgres user=postgres password=xflqm#WDZG#8341"
)
# conn = psycopg2.connect(conn_string)

try:
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="xflqm#WDZG#8341",
    )
    print("成功连接到数据库")
except psycopg2.Error as e:
    print(f"连接数据库失败: {e}")
