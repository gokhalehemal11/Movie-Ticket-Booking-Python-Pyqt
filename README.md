# Movie-Ticket-Booking-Python-Pyqt
Movie ticket booking system using python and pyqt4

------------------------------------------------------------------------------------------------------------------------------------
1) System is created using pyqt4 and python and linked with Mysql Database
2) A .ui extension (user interface file) is created using pyqt4/ pyqt5 and coverted to python file .py extension using following command:
    > pyuic4 -o file_name.py file_name.ui
3) Then funcationalities are added according to application requirements which are 
  - Book Ticket
  - Cancel Ticket
  - Show status of Booked tickets
  - Logout
-----------------------------------------------------------------------------------------------------------------------------------  
4)  To run the application clone all files into a single folder 
5) Create database named "mini" and password "pkg" or change connectivity to mysql module in each python file to your requirement
6) In mysql create following tables:

      +------------------+
      | Tables_in_mini   |
      +------------------+
      | 3idiots_booking  |
      | J2CE_booking     |
      | logged_users     |
      | sairat_booking   |
      | user_information |
      +------------------+
7) Following should be table description :

mysql> desc user_information;
+------------+-------------+------+-----+---------+-------+
| Field      | Type        | Null | Key | Default | Extra |
+------------+-------------+------+-----+---------+-------+
| user_id    | varchar(50) | NO   | PRI | NULL    |       |
| user_name  | varchar(50) | NO   |     | NULL    |       |
| user_phone | int(50)     | NO   |     | NULL    |       |
| password   | varchar(50) | NO   |     | NULL    |       |
+------------+-------------+------+-----+---------+-------+


mysql> desc logged_users;
+----------+-------------+------+-----+---------+-------+
| Field    | Type        | Null | Key | Default | Extra |
+----------+-------------+------+-----+---------+-------+
| user_id  | varchar(50) | YES  |     | NULL    |       |
| password | varchar(50) | YES  |     | NULL    |       |
| status   | varchar(50) | YES  |     | NULL    |       |
+----------+-------------+------+-----+---------+-------+

mysql> desc 3idiots_booking;
+---------+-------------+------+-----+---------+-------+
| Field   | Type        | Null | Key | Default | Extra |
+---------+-------------+------+-----+---------+-------+
| user_id | varchar(50) | YES  |     | NULL    |       |
| seats   | varchar(50) | YES  |     | NULL    |       |
| time    | varchar(50) | YES  |     | NULL    |       |
+---------+-------------+------+-----+---------+-------+

mysql> desc J2CE_booking;
+---------+-------------+------+-----+---------+-------+
| Field   | Type        | Null | Key | Default | Extra |
+---------+-------------+------+-----+---------+-------+
| user_id | varchar(50) | YES  |     | NULL    |       |
| seats   | varchar(50) | YES  |     | NULL    |       |
| time    | varchar(50) | YES  |     | NULL    |       |
+---------+-------------+------+-----+---------+-------+

mysql> desc sairat_booking;
+---------+-------------+------+-----+---------+-------+
| Field   | Type        | Null | Key | Default | Extra |
+---------+-------------+------+-----+---------+-------+
| user_id | varchar(50) | YES  |     | NULL    |       |
| seats   | varchar(50) | YES  |     | NULL    |       |
| time    | varchar(50) | YES  |     | NULL    |       |
+---------+-------------+------+-----+---------+-------+

---------------------------------------------------------------------------------------------------------------------------------
8) Once these tables are ready according to your requirements, specify path to your folder in command line
9) Run command:
      >python login1.py
10) And you are good to go !





