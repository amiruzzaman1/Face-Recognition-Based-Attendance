import csv
class Mark_Attendance:
    def __init__(self,csv_filename):
        self.csv_filename = csv_filename

    
    def write_csv_header(self,id,date,staff_name,time,status):
        self.id = id
        self.date = date
        self.staff_name = staff_name
        self.time = time
        self.status = status
        f = open(self.csv_filename, "w+",newline='')
        writer = csv.DictWriter(f, fieldnames=[self.id,self.staff_name,self.date,self.time,self.status])
        writer.writeheader()
        f.close()

    def append_csv_rows(self,records):
        self.records = records
        with open(self.csv_filename, 'a+',newline='') as f_object: 
            writer_object = csv.writer(f_object) 
        
            writer_object.writerow(self.records) 
        
            f_object.close() 
    
    

