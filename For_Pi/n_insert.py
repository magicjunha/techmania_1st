import pymysql.cursors
 


class ReturnValue(object):
    def __init__(self, y0,y1,y2):
        self.y0 = y0
        self.y1 = y1
        self.y2 = y2


class DB_Insert:

    def __init__(self):
        print("Insert Obj create")

    def my_insert(SiteName,SensorName,SensingValue):
        try:
            conn = pymysql.connect(host='localhost',
                                   user='test',
                                   password='test777',
                                   db='testdb')
            with conn.cursor() as cursor:
                sql = """insert into sensing_data (site_name, sensor_name,sensing_value, end_date ) values (%s,%s,%s, NOW())"""
                print(sql)
                cursor.execute(sql,(SiteName, SensorName, SensingValue))
                #cursor.execute(sql,('sejong', 'soil_sensor',0.32))
            conn.commit()
    
            with conn.cursor() as cursor:
                sql = 'SELECT * FROM sensing_data WHERE sensor_name = %s'
                cursor.execute(sql, ('soil_sensor',))
                #result = cursor.fetchone()
                result = cursor.fetchall()
                for row in result:
                    print(result)
                    # (1, 'test@test.com', 'my-passwd')
        finally:
            conn.close()
            #return 999  이경 우실행 됨
