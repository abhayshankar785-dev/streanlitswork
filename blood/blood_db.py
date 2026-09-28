# Define a class to perform database operations on Book Table
# Create a class named BookListCreateRetrieveUpdateDelete
# Define methods
    # list() --> for reading all records
    # create() --> for creating a new record
    # retrieve() --> for reading a specific record
    # update(id,data) --> for updating a specific record
    # delete(id) --> for deleting a specific record
# -------------------------------------------------------------
import mysql.connector
class BloodListCreateRetrieveUpdateDelete:
    def __init__(self):
        self.connection=mysql.connector.connect(user="root", password="User@123", host="localhost", database="blood_db")
        print(self.connection)
        self.cursor=self.connection.cursor()
        print("Sucessfully connected")

    def get(self):
        query="select * from book"
        self.cursor.execute(query)
        records=self.cursor.fetchall()
        if records:
            # for row in records:
            #     print(row)
            return records
        else:
            print("No records found")

    def post(self,name,blood_group,phone,city,last_donation):
        query = "insert into book(id,name,blood_group,phone,city,last_donation) values(%s,%s,%s,%s,%s,%s)"
        data = (id,name,blood_group,phone,city,last_donation)
        self.cursor.execute(query, data)
        self.connection.commit()
        print("Data Inserted Sucessfully")

    def retrive(self,id):
        query = "select * from book where id=%s"
        data=(id,)
        # if there is only one element in tuple to read it in sequence just use a comma after element
        self.cursor.execute(query,data)
        record = self.cursor.fetchone()
        if record:
            # print(record)
            return record
        else:
            print("No records found")

    def put(self,id,name,blood_group,phone,city,last_donation):
        query = "update name=%s,blood_group=%s,phone=%s,city=%s,last_donation=%s where id=%s"
        data = (id,name,blood_group,phone,city,last_donation)
        self.cursor.execute(query, data)
        self.connection.commit()
        if self.cursor.rowcount > 0:
            # print("Updated Sucessfully")
            return True
        else:
            # print("No Record Found")
            return False

    def delete(self,id):
        query = "delete from donor where id=%s"
        data = (id,)
        self.cursor.execute(query, data)
        #self.connection.commit()
        if self.cursor.rowcount>0: # if no updations rowcount returns 0
            # print("Data is Deleted")
            return True
        else:
            return False
            print("No Record Found")
# book_instance=BookListCreateRetrieveUpdateDelete()
# book_instance.list()
# book_instance.create("STU","Sam",400,500,"English")
# book_instance.retrieve(2)
# book_instance.update(2,"PQR","Mike",300,400,"English")
# book_instance.delete(1)


