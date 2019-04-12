import sqlite3,sys
from random import *

connection = None
cursor = None

def define_tables():
    global connection, cursor

    agents_query=   '''
                        CREATE TABLE agents (
                                    aid INTEGER,
                                    name STRING,
                                    pwd  STRING,
                                    PRIMARY KEY (aid)
                                    );
                    '''
    customers_query=   '''
                        CREATE TABLE customers (
                                    cid INTEGER,
                                    name STRING,
                                    address STRING,
                                    pwd  STRING,
                                    PRIMARY KEY (cid)
                                    );

                    '''
    cursor.execute(agents_query)
    cursor.execute(customers_query)
    connection.commit()
    return

def insert_data():
    global connection, cursor
   insert_agents = '''
                        INSERT INTO agents(aid,name,pwd) VALUES
                            (1, 'a', '123');
                     '''

    insert_customers =  '''
                        INSERT INTO customers(cid,name,address,pwd) VALUES
                            (2, 'b','asdfas','123');
                       '''

    cursor.execute(insert_agents)
    cursor.execute(insert_customers)
    connection.commit()
    return

def log_in(choose):
    global connection,cursor
    c = cursor
    con = connection
    c.execute("select * from agents;")
    rows = c.fetchall()
    find_aid = False
    find = False
    return_value = 0
    if choose.lower() == 'a':
        #Enter agent id if choose "a"
        while not find_aid:
            count = 0
            aid = input('Please enter your agent id: ')

            #find aid in fetched data, return true if aid is find
            while count<3 and not find:
                if aid == rows[count][0]:
                    find = True
                    find_aid = True
                count+=1
            #aid didn't find, ask to sign a new one
            if not find:
                sign = input("Do you want to sign up?('y'for yes): ")
                if sign.lower() == 'y':
                    return return_value = 1
        #enter password
        password = False
        while not password:
            count = 0
            find = False
            pwd = input('Please input your password: ')
            while count < 3 and not find:
                if pwd == rows[count][2]:
                    find = True
                    return return_value
                count++
            while not found:
                wanna_quit = input('Do you want to quit,sign up or retry?(q/s/r): ')
                if wanna_quit.lower() == 'q':
                    sys.exit()
                elif wanna_quit.lower() == 's':
                    return return_value = 1
                elif wanna_quit =='r':
                    found = True


def set_up_delivery(trackingnoList):
    global connection,cursor
    c = cursor
    con = connection
    unique = False
   while not unique:
        trackingno = randint(1000,9999)
        if trackingno not in trackingnoList:
            unique = False
            trackingnoList.add(trackingno)
    set_up = False
    while not set_up:
        PickUpTime = null
        DropOffTime = null
        Oid = input("Please enter the order id you want to add into this delivery, or enter 'q' to quit: ")
        if Oid.lower == 'q':
            set_up = True
        pick_up = False
        while not pick_up:
            pickUp = input("Please enter the pickUpTime for this order('How many hours from now'): ")
            if type(pickUp)==int:
                pick_up = True
        PickUpTIme = datetime('now','+'+pickUp+'hours')
        insert_delivery = '''
                            INSERT INTO deliveries(trackingNo,oid,pickUpTime,dropOffTime) VALUES
                                (trackingno, Oid, PickUpTIme,DropOffTime);
                         '''
        cursor.execute(insert_delivery)
        connection.commit()
    return trackingnoList

def update_delivery(trackingnoList):
    global connection,cursor
    c = cursor
    con = connection
    c.execute("select * from deliveries;")
    delivery = c.fetchall()
    find_trackno = False
    c.execute("select * from orders;")
    order = c.fetchall()
    oidList=  []
    while not find_trackno:
        trackingno = input("Please enter the tracking number of the delivery you want to see: ")
        if trackingno in trackingnoList:
            find_trackno = True
    length = len(delivery)
    for x in range(0,length-1):
        if delivery[x][0]== trackingno:
            print(delivery[x])
            oidList.add(delivery[x][1])
    see_order = input("Do you want to see one of the order from orders: ('y' for yes, others for no) ")
    if see_order.lower() == 'y':
        while not find_oid:
            oid = input("Please enter the order you want to see from this delivery: ")
            if oid in oidList:
                find_oid = True
        length = len(order)
        for x in range(0,length-1):
            if oid == order[x][0]:
                print(order[x])
    remove_order =input("Do you wan to remove an order from this delivery?('y' for yes, others for no) ")
    if remove_order.lower() == 'y':
        find_order = False
        while not find_order:
            Oid = input("Enter the oid of the order you want to remove: ")
            if Oid in oidList:
                find_order = True
        cursor.exercute('DELETE from orders where oid =?;',Oid)
    change_pickup = input("Do you want to change the pick up time of this delivery?(y for yes, others for no) ")
    if change_pickup.lower()=='y':
        pick_up = False
        while not pick_up:
            pickUpTime = input("What is the new pick up time?(How many hours from now)")
            if type(pickUpTime)== int:
                pick_up = True
        PickUpTIme = datetime('now','+'+pickUp+'hours')
        data = (PickUpTime,trackingno)
        cursor.execute('UPDATE deliveries SET pickUpTime=? where trackingno=?;',data )
        change_pickup = input("Do you want to change the pick up time of this delivery?(y for yes, others for no) ")
    if change_pickup.lower()=='y':
        pick_up = False
        while not pick_up:
            pickUpTime = input("What is the new pick up time?(How many hours from now)")
            if type(pickUpTime)== int:
                pick_up = True
        PickUpTIme = datetime('now','+'+pickUpTIme+'hours')
        data = (PickUpTime,trackingno)
        cursor.execute('UPDATE deliveries SET pickUpTime=? where trackingno=?;',data )
    change_dropoff = input("Do you want to change the dropoff time of this delivery?(y for yes, others for no) ")
    if change_dropoff.lower()=='y':
        drop_off = False
        while not drop_off:
            dropOffTime = input("What is the new drop off time?(How many hours from now)")
            if type(dropOffTime)== int:
                drop_off = True
        DropOffTime = datetime('now','+'+dropOffTime+'hours')
        data = (DropOffTime,trackingno)
        cursor.execute('UPDATE deliveries SET dropOffTime=? where trackingno=?;',data )
    connection.commit()

def add_to_stock():
    global connection,cursor
    c = cursor
    con = connection
    c.execute("select * from carries;")
    carries = c.fetchall()
    length = len(olines)
    find_stock= False
    while not find_stock:
        Pid = input("Please enter the pid: ")
        Sid = input("Please enter the sid: ")
        for x in range(0,length-1):
            if Pid == carries[x][1] and Sid ==carries[x][0]:
                find_stock = True
                quantity = carries[x][2]
                uprice = carries[x][3]
    enter_number = False
    while not enter_number:
        number_to_add = input("Please enter the number of products to be added to the stock: ")
        if type(number_to_add) == int:
            enter_number = True
    quantity += number_to_add
    data = (quantity,Pid,Sid)
    cursor.execute('UPDATE carries SET qty=? where pid=? and sid = ?;',data )
    change_uprice = input("Do you want to change the unit price?('y' for yes and others for no)")
    if change_uprice.lower() == 'y':
        enter_uprice = False
        while not enter_uprice:
           new_uprice = input("Please enter the new unit price ")
            if type(new_uprice) == float:
                enter_uprice = True
        data = (new_uprice,Sid,Pid)
        cursor.execute('UPDATE carries SET uprice=? where sid=? and pid=?;',data)
    connection.commit()

def place_order(basket,cid):
    global connection,cursor
    c = cursor
    con = connection
    c.execute("select * from carries;")
    carries = c.fetchall()
    #sid,pid,quantity
    length_b = len(basket)
    length_c = len(carries)
    for x in range(0,length_b-1):
        for y in range(0,length_c-1):
            if basket[x][0]==carries[y][0] and basket[x][1]==carries[y][1]:
                if basket[x][2]> carries[y][2]:
                    print("The quantity you set for"+str(basket[x][1])+'is higher than the quantity left in stock')
                    update = False
                    while not update:
                        choose = input("Do you want to change the quantity(enter'c') or delete the product(enter'd') ")
                        if choose.lower()=='c':
                            less = False
                            while not less:
                                quantity = input("Enter the new quantity: ")
                                if quantity <= carries[y][2]:
                                    less = True
                                   update = True
                        if choose.lower()=='d':
                            basket.remove([basket[x][0],basket[x][1],basket[x][2]])
                            update = True
    Oid = randint(100,999)
    Address = c.execute['SELECT address FROM customers WHERE cid = ?;',cid]
    insert_delivery = '''
                         INSERT INTO orders(oid,cid,odate,address) VALUES (Oid,cid,datetime('now'),Address);
                      '''
    connection.commit()
    return basket


def main():
    k = True
    o = True
    while o:
        while k:
            choose = input("Please choose your role('a'for agent,'c'for customer,or'q'for quit): ")
            if choose.lower() == 'q':
                k = False
                o = False
            elif choose.lower()== 'a':
                k = False
            elif choose.lower()== 'c':
                k = False

main()