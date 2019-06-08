class Connect:
    def __init__(self,host,port,db,charset):
        self.host=host
        self.port=port
        self.db=db
        self.charset=charset
        
        
    def exec1(self,sql):
        conn=connect(self.host,self.port,self.db,self.charset)
        conn.execute(sql)
        return xxx
        
    def exec2(self,proc_name):
        conn=connect(self.host,self.port,self.db,self.charset)
        conn.call_proc(proc_name)
        return xxx
    
            
conn1=Connect('127.0.0.1',3306,'db1','utf8')
conn1.exec1('select * from tb1;')
conn1.exec2('存储过程的名字')
