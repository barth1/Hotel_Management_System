# Backend
import sqlite3
# function to create field on the database
from sqlite3.dbapi2 import Connection


def data_base():
    go_to = sqlite3.connect("booking.db")
    allow = go_to.cursor()
    allow.execute("CREATE TABLE IF NOT EXISTS booking(id INTEGER PRIMARY KEY,cusID text, Firstname text, surname text, Address text, Gender text,\
     Mobile text, Nationality text, DateIn text, DateOut text, Email text, proveofID text)")
    go_to.commit()
    go_to.close()


# function to add inputted record to the data base
def add_hotel_rec(cusID, Firstname, surname, Address, Gender, Mobile, Nationality, DateIn, DateOut, Email, proveofID):
    go_to = sqlite3.connect("booking.db")
    allow = go_to.cursor()
    allow.execute("INSERT INTO booking  VALUES (NULL, ?,?,?,?,?,?,?,?,?,?,?)",(cusID, Firstname, surname, Address, Gender, Mobile, Nationality, DateIn, DateOut, Email, proveofID))
    go_to.commit()
    go_to.close()


# function to view and select data *(i.e  all)
def view_data():
    go_to = sqlite3.connect("booking.db")
    allow = go_to.cursor()
    allow.execute("SELECT* FROM booking ")
    view = allow.fetchall()
    go_to.close()
    return view


# function to delete selected record
def delete_rec(id):
    go_to = sqlite3.connect("booking.db")
    allow = go_to.cursor()
    allow.execute("DELETE FROM booking WHERE (id)=?", (id,))
    go_to.commit()
    go_to.close()


# function to search selected data
def search_data(cusID='', Firstname='', surname='', Address='', Gender='', Mobile='', Nationality='', DateIn='',
                DateOut='', Email='', proveofID=''):
    go_to = sqlite3.connect("booking.db")
    allow = go_to.cursor()
    allow.execute("SELECT* FROM booking WHERE cusID=? OR Firstname=? OR surname=? OR Address=? OR Gender=? OR Mobile=? OR Nationality=? OR DateIn=? OR DateOut=? OR Email=? OR proveofID=?", \
        (cusID, Firstname, surname, Address, Gender, Mobile, Nationality, DateIn, DateOut, Email, proveofID))
    view = allow.fetchall()
    go_to.close()
    return view


# funtion to update records of the data
def update_data(id, cusID='', Firstname='', surname='', Address='', Gender='', Mobile='', Nationality='', DateIn='',
                DateOut='', Email='', proveofID=''):
    go_to = sqlite3.connect("booking.db")
    allow = go_to.cursor()
    allow.execute(
        "UPDATE  booking SET cusID=?, Firstname=? , surname=? , Address=? , Gender=? , Mobile=? , Nationality=? , DateIn=? , DateOut=? ,Email=? , provofID=?, WHERE id=?",
        (cusID, Firstname, surname, Address, Gender, Mobile, Nationality, DateIn, DateOut, Email, proveofID, id))
    go_to.commit()
    go_to.close()


data_base()
