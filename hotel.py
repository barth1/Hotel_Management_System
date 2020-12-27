from tkinter import *
from tkinter import ttk
import hotelDatabase
import tkinter.messagebox
import random
from datetime import datetime
import time


# frontend

class Hotel:
    def __init__(self, root):
        self.root = root
        self.root.title('Data Base Hotel Management System')
        self.root.geometry('1350x800+0+0')

        mainframe = Frame(self.root)
        mainframe.grid()
        topframe = Frame(mainframe, width=1350, height=550, relief=RIDGE, bd=10, padx=2)
        topframe.pack(side=TOP)
        leftframe = Frame(topframe, width=400, height=550, relief=RIDGE, bd=5, padx=2)
        leftframe.pack(side=LEFT)
        rightframe = Frame(topframe, width=400, height=550, relief=RIDGE, bd=5, padx=2)
        rightframe.pack(side=RIGHT)
        rightframe1 = Frame(rightframe, width=800, height=50, relief=RIDGE, bd=5, padx=10)
        rightframe1.grid(row=0, column=0)
        rightframe2 = Frame(rightframe, width=800, height=100, relief=RIDGE, bd=5, padx=4)
        rightframe2.grid(column=0, row=1)
        rightframe3 = Frame(rightframe, width=800, height=400, relief=RIDGE, bd=5, padx=3)
        rightframe3.grid(row=3, column=0)

        bottomframe = Frame(mainframe, width=1350, height=150, relief=RIDGE, bd=10, padx=2)
        bottomframe.pack(side=BOTTOM)

        global hD
        cusID = StringVar()
        Firstname = StringVar()
        surname = StringVar()
        Address = StringVar()
        Date_of_Birth = StringVar()
        Mobile = StringVar()
        postcode = StringVar()
        Email = StringVar()
        Nationality = StringVar()
        proveofID = StringVar()
        roomtype = StringVar()
        roomexno = StringVar()
        roomno = StringVar()
        DateIn = StringVar()
        DateOut = StringVar()
        meal = StringVar()
        subtotal = StringVar()
        totaldays = StringVar()
        paidtax = StringVar()
        totalcost = StringVar()
        Gender = StringVar()

        DateIn.set(time.strftime('%d/%m/%y'))
        DateOut.set(time.strftime('%d/%m/%y'))

        x = random.randint(1197, 8744)
        ref = str(x)
        cusID.set('HOTEL_' + ref)

        def iexit():
            iexit = tkinter.messagebox.askyesno('Hotel Management', 'confirm if you want to exit')
            if iexit > 0:
                root.destroy()
                return

        def reset():
            cbo_prove_of0_id.set('')
            cbomeal.set('')
            cboroomexno.set('')
            cboroomNo.set('')
            cboroomtype.set('')

            txtDOB.delete(0, END)
            txtGender.delete(0, END)
            txtemail.delete(0, END)
            txtnationality.delete(0, END)
            txtmobile.delete(0, END)
            txtpostcode.delete(0, END)
            txtFirstname.delete(0, END)
            txtsurname.delete(0, END)
            txtAddress.delete(0, END)
            txtnoofdays.delete(0, END)
            txttotal.delete(0, END)
            txtsub.delete(0, END)
            txttax.delete(0, END)

            DateIn.set(time.strftime('%d/%m/%y'))
            DateOut.set(time.strftime('%d/%m/%y'))

            x = random.randint(1197, 8744)
            ref = str(x)
            cusID.set('HOTEL_' + ref)

        def addData():
            if (len(cusID.get()) != 0):
                hotelDatabase.add_hotel_rec(cusID.get(), Firstname.get(), surname.get(), Address.get(), Gender.get(),Mobile.get(), Nationality.get(), DateIn.get(), Email.get(), DateOut.get(),proveofID.get())

                lsthotel.delete(0, END)
                lsthotel.insert(END,(cusID.get(), Firstname.get(), surname.get(), Address.get(), Gender.get(), Mobile.get(),Nationality.get(), DateIn.get(), Email.get(), DateOut.get(), proveofID.get()))

        def displayData():
            lsthotel.delete(0, END)
            for row in hotelDatabase.view_data():
                lsthotel.insert(END, row, str(''))

        def Hotel_rec():
            searchHdb = lsthotel.curselection()[0]
            hD = lsthotel.get(searchHdb)

            txtcusID.delete(0, END)
            txtcusID.insert(END, hD)[1]
            txtFirstname.delete(0, END)
            txtFirstname.insert(END, hD)[2]
            txtsurname.delete(0, END)
            txtsurname.insert(END, hD)[3]
            txtAddress.delete(0, END)
            txtAddress.insert(END, hD)[4]
            txtGender.delete(0, END)
            txtGender.insert(END, hD)[5]
            txtmobile.delete(0, END)
            txtmobile.insert(END, hD)[6]
            txtnationality.delete(0, END)
            txtnationality.insert(END, hD)[7]
            cbo_prove_of0_id.delete(0, END)
            cbo_prove_of0_id.insert(END, hD[8])
            txtcheck_in.delete(0, END)
            txtcheck_in.insert(0, hD)[9]
            txtcheck_out.delete(0, END)
            txtcheck_out.insert(END, hD)[10]
            txtemail.delete(0, END)
            txtemail.insert(END, hD)[11]

        def deleting ():
            global hD
            ea = lsthotel.curselection()[0]
            hD = lsthotel.get(ea)
            if (len(cusID.get() )!= 0):
                hotelDatabase.delete_rec(hD[0])
                reset()
                displayData()

        def searching ():
            lsthotel.delete(0, END)
            for row in hotelDatabase.search_data(cusID.get(), Firstname.get(), surname.get(), Address.get(),Gender.get(), Mobile.get(), Nationality.get(), DateIn.get(),Email.get(), DateOut.get(), proveofID.get()):
                lsthotel.insert(END, row, str(''))

        def updating ():
            global hD
            if (len(cusID.get()) != 0):
                hotelDatabase.delete_rec(hD[0])
            if (len(cusID.get()) != 0):
                hotelDatabase.add_hotel_rec(cusID.get(), Firstname.get(), surname.get(), Address.get(), Gender.get(),Mobile.get(), Nationality.get(), DateIn.get(), Email.get(), DateOut.get(),proveofID.get())
                lsthotel.delete(0, END)
                lsthotel.insert(END(cusID.get(), Firstname.get(), surname.get(), Address.get(), Gender.get(), Mobile.get(),Nationality.get(), DateIn.get(), Email.get(), DateOut.get(), proveofID.get()))

        def totalcostandaddnew():
            addData()
            indate = DateIn.get()
            outdate = DateOut.get()
            indate = datetime.strptime(indate, '%d/%m/%y')
            outdate = datetime.strptime(outdate, '%d/%m/%y')
            totaldays.set(abs((outdate - indate).days))

            if (meal.get() == 'BreakFast' and roomtype.get() == 'Single'):
                q1 = float(17)
                q2 = float(34)
                q3 = float(totaldays.get())
                q4 = float(q1 + q2)
                q5 = float(q3 + q4)
                Tax = 'N' + str('%.2f' % ((q5) * 0.09))
                ST = 'N' + str('%.2f' % ((q5)))
                TT = 'N' + str('%.2f' % (q5 + ((q5) * 0.09)))
                paidtax.set(Tax)
                subtotal.set(ST)
                totalcost.set(TT)

            elif (meal.get() == 'BreakFast' and roomtype.get() == 'Double'):
                q1 = float(35)
                q2 = float(43)
                q3 = float(totaldays.get())
                q4 = float(q1 + q2)
                q5 = float(q3 + q4)
                Tax = 'N' + str('%.2f' % ((q5) * 0.09))
                ST = 'N' + str('%.2f' % ((q5)))
                TT = 'N' + str('%.2f' % (q5 + ((q5) * 0.09)))
                paidtax.set(Tax)
                subtotal.set(ST)
                totalcost.set(TT)

            elif (meal.get() == 'BreakFast' and roomtype.get() == 'Family'):
                q1 = float(45)
                q2 = float(63)
                q3 = float(totaldays.get())
                q4 = float(q1 + q2)
                q5 = float(q3 + q4)
                Tax = 'N' + str('%.2f' % ((q5) * 0.09))
                ST = 'N' + str('%.2f' % ((q5)))
                TT = 'N' + str('%.2f' % (q5 + ((q5) * 0.09)))
                paidtax.set(Tax)
                subtotal.set(ST)
                totalcost.set(TT)

            elif (meal.get() == 'Lunch' and roomtype.get() == 'Single'):
                q1 = float(29)
                q2 = float(37)
                q3 = float(totaldays.get())
                q4 = float(q1 + q2)
                q5 = float(q3 + q4)
                Tax = 'N' + str('%.2f' % ((q5) * 0.09))
                ST = 'N' + str('%.2f' % ((q5)))
                TT = 'N' + str('%.2f' % (q5 + ((q5) * 0.09)))
                paidtax.set(Tax)
                subtotal.set(ST)
                totalcost.set(TT)

            elif (meal.get() == 'Lunch' and roomtype.get() == 'Dougle'):
                q1 = float(37)
                q2 = float(43)
                q3 = float(totaldays.get())
                q4 = float(q1 + q2)
                q5 = float(q3 + q4)
                Tax = 'N' + str('%.2f' % ((q5) * 0.09))
                ST = 'N' + str('%.2f' % ((q5)))
                TT = 'N' + str('%.2f' % (q5 + ((q5) * 0.09)))
                paidtax.set(Tax)
                subtotal.set(ST)
                totalcost.set(TT)

            elif (meal.get() == 'Lunch' and roomtype.get() == 'Family'):
                q1 = float(46)
                q2 = float(63)
                q3 = float(totaldays.get())
                q4 = float(q1 + q2)
                q5 = float(q3 + q4)
                Tax = 'N' + str('%.2f' % ((q5) * 0.09))
                ST = 'N' + str('%.2f' % ((q5)))
                TT = 'N' + str('%.2f' % (q5 + ((q5) * 0.09)))
                paidtax.set(Tax)
                subtotal.set(ST)
                totalcost.set(TT)

            elif (meal.get() == 'Dinner' and roomtype.get() == 'Single'):
                q1 = float(28)
                q2 = float(37)
                q3 = float(totaldays.get())
                q4 = float(q1 + q2)
                q5 = float(q3 + q4)
                Tax = 'N' + str('%.2f' % ((q5) * 0.09))
                ST = 'N' + str('%.2f' % ((q5)))
                TT = 'N' + str('%.2f' % (q5 + ((q5) * 0.09)))
                paidtax.set(Tax)
                subtotal.set(ST)
                totalcost.set(TT)

            elif (meal.get() == 'Dinner' and roomtype.get() == 'Dougle'):
                q1 = float(30)
                q2 = float(43)
                q3 = float(totaldays.get())
                q4 = float(q1 + q2)
                q5 = float(q3 + q4)
                Tax = 'N' + str('%.2f' % ((q5) * 0.09))
                ST = 'N' + str('%.2f' % ((q5)))
                TT = 'N' + str('%.2f' % (q5 + ((q5) * 0.09)))
                paidtax.set(Tax)
                subtotal.set(ST)
                totalcost.set(TT)

            elif (meal.get() == 'Dinner' and roomtype.get() == 'Family'):
                q1 = float(43)
                q2 = float(63)
                q3 = float(totaldays.get())
                q4 = float(q1 + q2)
                q5 = float(q3 + q4)
                Tax = 'N' + str('%.2f' % ((q5) * 0.09))
                ST = 'N' + str('%.2f' % ((q5)))
                TT = 'N' + str('%.2f' % (q5 + ((q5) * 0.09)))
                paidtax.set(Tax)
                subtotal.set(ST)
                totalcost.set(TT)

        # ======================================widget================================================
        lblcusID = Label(leftframe, font=('arial', 12, 'bold'), text='customer ref:', padx=1)
        lblcusID.grid(column=0, row=0, sticky=W)
        txtcusID = Entry(leftframe, width=18, font=('arial', 12, 'bold'), textvariable=cusID)
        txtcusID.grid(column=1, row=0, pady=3, padx=20)

        lblFirstname = Label(leftframe, font=('arial', 12, 'bold'), text='Firstname:', padx=1)
        lblFirstname.grid(column=0, row=1, sticky=W)
        txtFirstname = Entry(leftframe, width=18, font=('arial', 12, 'bold'), textvariable=Firstname)
        txtFirstname.grid(column=1, row=1)

        lblsurname = Label(leftframe, font=('arial', 12, 'bold'), text='Surname:', padx=1)
        lblsurname.grid(column=0, row=2, sticky=W)
        txtsurname = Entry(leftframe, width=18, font=('arial', 12, 'bold'), textvariable=surname)
        txtsurname.grid(column=1, row=2, pady=3, padx=20)

        lblAddress = Label(leftframe, font=('arial', 12, 'bold'), text='Address:', padx=1, pady=2)
        lblAddress.grid(column=0, row=3, sticky=W)
        txtAddress = Entry(leftframe, width=18, font=('arial', 12, 'bold'), textvariable=Address)
        txtAddress.grid(column=1, row=3, pady=3, padx=20)

        lblDOB = Label(leftframe, font=('arial', 12, 'bold'), text='Date of Birth:', padx=2, pady=2)
        lblDOB.grid(column=0, row=4, sticky=W)
        txtDOB = Entry(leftframe, width=18, font=('arial', 12, 'bold'), textvariable=Date_of_Birth)
        txtDOB.grid(column=1, row=4, pady=3, padx=20)

        lblpostcode = Label(leftframe, font=('arial', 12, 'bold'), text='PostCode:', padx=2, pady=2)
        lblpostcode.grid(column=0, row=5, sticky=W)
        txtpostcode = Entry(leftframe, width=18, font=('arial', 12, 'bold'), textvariable=postcode)
        txtpostcode.grid(column=1, row=5, pady=3, padx=20)

        lblmobile = Label(leftframe, font=('arial', 12, 'bold'), text='Mobile No:', pady=2, padx=2)
        lblmobile.grid(column=0, row=6, sticky=W)
        txtmobile = Entry(leftframe, width=18, font=('arial', 12, 'bold'), textvariable=Mobile)
        txtmobile.grid(column=1, row=6, pady=3, padx=20)

        lblemail = Label(leftframe, font=('arial', 12, 'bold'), text='Email:', pady=2, padx=2)
        lblemail.grid(column=0, row=7, sticky=W)
        txtemail = Entry(leftframe, width=18, font=('arial', 12, 'bold'), textvariable=Email)
        txtemail.grid(column=1, row=7, pady=3, padx=20)

        lblnationality = Label(leftframe, font=('arial', 12, 'bold'), text='Nationality:', pady=2, padx=2)
        lblnationality.grid(column=0, row=8, sticky=W)
        txtnationality = Entry(leftframe, width=18, font=('arial', 12, 'bold'), textvariable=Nationality)
        txtnationality.grid(column=1, row=8, pady=3, padx=20)

        lblGender = Label(leftframe, font=('arial', 12, 'bold'), text='Gender:', pady=2, padx=2)
        lblGender.grid(column=0, row=9, sticky=W)
        txtGender = Entry(leftframe, width=18, font=('arial', 12, 'bold'), textvariable=Gender)
        txtGender.grid(column=1, row=9, pady=3, padx=20)

        lblcheck_in = Label(leftframe, font=('arial', 12, 'bold'), text='Check In Date:', pady=2, padx=1)
        lblcheck_in.grid(column=0, row=10, sticky=W)
        txtcheck_in = Entry(leftframe, width=18, font=('arial', 12, 'bold'), textvariable=DateIn)
        txtcheck_in.grid(column=1, row=10, pady=3, padx=20)

        lblcheck_out = Label(leftframe, font=('arial', 12, 'bold'), text='Check Out Date :', pady=2, padx=1)
        lblcheck_out.grid(column=0, row=11, sticky=W)
        txtcheck_out = Entry(leftframe, width=18, font=('arial', 12, 'bold'), textvariable=DateOut)
        txtcheck_out.grid(column=1, row=11, pady=3, padx=20)

        lblproveid = Label(leftframe, font=('arial', 12, 'bold'), text='Prove of ID:', pady=2, padx=2)
        lblproveid.grid(column=0, row=12, sticky=W)
        cbo_prove_of0_id = ttk.Combobox(leftframe, state='readonly', width=16, font=('arial', 12, 'bold'),
                                        textvariable=proveofID)
        cbo_prove_of0_id['value'] = ('', 'pilot licence', 'Drivers licence', 'Student ID', 'Passport')
        cbo_prove_of0_id.current(0)
        cbo_prove_of0_id.grid(column=1, row=12, pady=3, padx=2)

        lblmeal = Label(leftframe, font=('arial', 12, 'bold'), text='Meal:', pady=2, padx=2)
        lblmeal.grid(column=0, row=13, sticky=W)
        cbomeal = ttk.Combobox(leftframe, state='readonly', width=16, font=('arial', 12, 'bold'), textvariable=meal)
        cbomeal['value'] = ('', 'BreakFast', 'Lunch', 'Dinner')
        cbomeal.current(0)
        cbomeal.grid(column=1, row=13, pady=3, padx=2)

        lblroomtype = Label(leftframe, font=('arial', 12, 'bold'), text='Room Type:', pady=2, padx=2)
        lblroomtype.grid(column=0, row=14, sticky=W)
        cboroomtype = ttk.Combobox(leftframe, state='readonly', width=16, font=('arial', 12, 'bold'),
                                   textvariable=roomtype)
        cboroomtype['value'] = ('', 'Single', 'Double', 'Family')
        cboroomtype.current(0)
        cboroomtype.grid(column=1, row=14, pady=3, padx=2)

        lblroomNo = Label(leftframe, font=('arial', 12, 'bold'), text='Room Number:', pady=2, padx=2)
        lblroomNo.grid(column=0, row=15, sticky=W)
        cboroomNo = ttk.Combobox(leftframe, state='readonly', width=16, font=('arial', 12, 'bold'), textvariable=roomno)
        cboroomNo['value'] = ('', '001', '002', '003', '004', '005', '006', '007', '008', '009')
        cboroomNo.current(0)
        cboroomNo.grid(column=1, row=15, pady=3, padx=2)

        lblroomexno = Label(leftframe, font=('arial', 12, 'bold'), text='Room Ex.No:', pady=2, padx=2)
        lblroomexno.grid(column=0, row=16, sticky=W)
        cboroomexno = ttk.Combobox(leftframe, state='readonly', width=16, font=('arial', 12, 'bold'),
                                   textvariable=roomexno)
        cboroomexno['value'] = ('', '101', '102', '103', '104', '105', '106', '107')
        cboroomexno.current(0)
        cboroomexno.grid(column=1, row=16, pady=3, padx=2)
        # ==========================widget=============================================================================
        lbllabel = Label(rightframe1, width=116, font=('arial', 10, 'bold'), pady=6, padx=10,
                         text='Customer Ref\tFirstname\tSurname\tAddress\tGender\tMobile\tNationality\tProve_of_id\tDatein\tDateout\t\tEmail')
        lbllabel.grid(row=0, column=0, columnspan=17)

        scroll_bar = Scrollbar(rightframe2)
        scroll_bar.grid(row=0, column=0, sticky='ns')
        lsthotel = Listbox(rightframe2, width=105, height=14, font=('arial', 12, 'bold'), yscrollcommand=scroll_bar.set)
        lsthotel.bind('<<ListboxSelect>>', Hotel_rec)
        lsthotel.grid(column=0, row=0, padx=7, sticky='nsew')
        scroll_bar.configure(command=lsthotel.xview)
        # =========================================widget=====================================================================

        lblnoofdays = Label(rightframe3, font=('arial', 14, 'bold'), text='No. of Days:', bd=7)
        lblnoofdays.grid(column=0, row=0, sticky=W)
        txtnoofdays = Entry(rightframe3, width=76, font=('arial', 14, 'bold'), justify=LEFT, textvariable=totaldays)
        txtnoofdays.grid(column=1, row=0)

        lbltax = Label(rightframe3, font=('arial', 14, 'bold'), text='Pay Tax:', bd=7)
        lbltax.grid(column=0, row=1, sticky=W)
        txttax = Entry(rightframe3, width=76, font=('arial', 14, 'bold'), justify=LEFT, textvariable=paidtax)
        txttax.grid(column=1, row=1)

        lblsub = Label(rightframe3, font=('arial', 14, 'bold'), text='Subtotal:', bd=7)
        lblsub.grid(column=0, row=2, sticky=W)
        txtsub = Entry(rightframe3, width=76, font=('arial', 14, 'bold'), justify=LEFT, textvariable=subtotal)
        txtsub.grid(column=1, row=2)

        lbltotal = Label(rightframe3, font=('arial', 14, 'bold'), text='Total Cost:', bd=7)
        lbltotal.grid(column=0, row=3, sticky=W)
        txttotal = Entry(rightframe3, width=76, font=('arial', 14, 'bold'), justify=LEFT, textvariable=totalcost)
        txttotal.grid(column=1, row=3)

        # ================================widget button=========================================

        btnadd = Button(bottomframe, font=('arial', 16, 'bold'), width=13, height=2, text='AddNew/Total', bd=5,
                        command=totalcostandaddnew)
        btnadd.grid(column=0, row=0, padx=4, pady=1)

        btnDisplay = Button(bottomframe, font=('arial', 16, 'bold'), width=13, height=2, text='Display', bd=5,command=displayData)
        btnDisplay.grid(column=1, row=0, padx=4, pady=1)

        btnUpdate = Button(bottomframe, font=('arial', 16, 'bold'), width=13, height=2, text='Update', bd=5,command=updating)
        btnUpdate.grid(column=2, row=0, padx=4, pady=1)

        btnDelete = Button(bottomframe, font=('arial', 16, 'bold'), width=13, height=2, text='Delete', bd=5,command=deleting)
        btnDelete.grid(column=3, row=0, padx=4, pady=1)

        btnsearch = Button(bottomframe, font=('arial', 16, 'bold'), width=13, height=2, text='Search', bd=5,command=searching)
        btnsearch.grid(column=4, row=0, padx=4, pady=1)

        btnreset = Button(bottomframe, font=('arial', 16, 'bold'), width=13, height=2, text='Reset', bd=5,
                          command=reset)
        btnreset.grid(column=5, row=0, padx=4, pady=1)

        btnexit = Button(bottomframe, font=('arial', 16, 'bold'), width=13, height=2, text='Exit', bd=5, command=iexit)
        btnexit.grid(column=6, row=0, padx=4, pady=1)


if __name__ == '__main__':
    root = Tk()
    application = Hotel(root)
    mainloop()
