from pyhive import hive

def get_data():
    # 请根据实际情况修改 host、port、username、database
    conn = hive.Connection(
        host='your_hive_host',      # Hive服务器地址
        port=10000,                 # Hive端口，默认10000
        username='your_username',   # 用户名
        database='your_database'    # 数据库名
    )
    cursor = conn.cursor()
    # 示例SQL，请根据实际表结构修改
    cursor.execute("""
        SELECT 
            SUM(sales) as sales, 
            COUNT(order_id) as orders, 
            COUNT(DISTINCT user_id) as users 
        FROM orders
    """)
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    # 返回字典
    return {
        "sales": result[0],
        "orders": result[1],
        "users": result[2]
    }