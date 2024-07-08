import sqlite3
from datetime import datetime

# Database file path
db_path = 'example.db'

# Connect to the SQLite database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create the Employees table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS Employees (
    EmpID INTEGER PRIMARY KEY,
    FirstName TEXT,
    LastName TEXT,
    StartDate DATE,
    ExitDate DATE,
    Title TEXT,
    EmployeeStatus TEXT,
    PerformanceScore INTEGER,
    SolvedNumberOfTickets INTEGER,
    TicketTimeRate REAL
)
''')
conn.commit()

# Original employees data
employees = [
    (1, 'Gencay', 'Turgut', '2020-01-01', '2021-01-01', 'Engineer', 'Active', 95, 50, 1.5),
    (2, 'Matin', 'Hüseynzade', '2019-03-01', '2022-02-01', 'Manager', 'Active', 80, 60, 1.8),
    (3, 'Cüneyd', 'Çelik', '2018-05-15', '2023-03-15', 'Technician', 'Inactive', 65, 70, 1.7),
    (4, 'Kağan', 'Yalım', '2021-06-01', None, 'Developer', 'Active', 90, 80, 1.6),
    (5, 'Emre', 'Beskan', '2017-08-10', '2022-07-10', 'Analyst', 'Inactive', 75, 90, 2.0),
    (6, 'Emre', 'Karaduman', '2016-09-20', '2021-08-20', 'Consultant', 'Inactive', 85, 40, 1.3),
    (7, 'Azad', 'Karatay', '2015-11-30', '2020-10-30', 'Engineer', 'Inactive', 70, 30, 1.2),
    (8, 'Hasan', 'Selçuk', '2014-01-01', '2019-12-01', 'Manager', 'Inactive', 60, 20, 1.1),
    (9, 'Cenk', 'Yavru', '2013-02-15', '2018-01-15', 'Developer', 'Inactive', 55, 55, 1.4),
    (10, 'Nurbala', 'Heybatov', '2012-03-20', '2017-02-20', 'Technician', 'Inactive', 50, 65, 1.9),
    (11, 'John', 'Doe', '2020-02-01', '2021-02-01', 'Engineer', 'Active', 88, 45, 1.7),
    (12, 'Jane', 'Smith', '2019-04-01', '2022-03-01', 'Manager', 'Active', 82, 50, 1.6),
    (13, 'Alice', 'Johnson', '2018-06-15', '2023-04-15', 'Technician', 'Inactive', 75, 55, 1.5),
    (14, 'Bob', 'Brown', '2021-07-01', None, 'Developer', 'Active', 90, 60, 1.8),
    (15, 'Charlie', 'Davis', '2017-09-10', '2022-08-10', 'Analyst', 'Inactive', 77, 65, 2.1),
    (16, 'David', 'Wilson', '2016-10-20', '2021-09-20', 'Consultant', 'Inactive', 85, 35, 1.2),
    (17, 'Eva', 'Garcia', '2015-12-30', '2020-11-30', 'Engineer', 'Inactive', 70, 25, 1.3),
    (18, 'Frank', 'Martinez', '2014-02-01', '2019-01-01', 'Manager', 'Inactive', 65, 30, 1.4),
    (19, 'Grace', 'Lopez', '2013-03-15', '2018-02-15', 'Developer', 'Inactive', 60, 40, 1.5),
    (20, 'Henry', 'Gonzalez', '2012-04-20', '2017-03-20', 'Technician', 'Inactive', 55, 50, 1.6),
    (21, 'Isabella', 'Anderson', '2020-05-01', '2021-04-01', 'Engineer', 'Active', 85, 60, 1.7),
    (22, 'Jack', 'Thomas', '2019-06-01', '2022-05-01', 'Manager', 'Active', 80, 55, 1.8),
    (23, 'Karen', 'Taylor', '2018-07-15', '2023-06-15', 'Technician', 'Inactive', 78, 45, 1.9),
    (24, 'Liam', 'Moore', '2021-08-01', None, 'Developer', 'Active', 88, 50, 2.0),
    (25, 'Mia', 'Jackson', '2017-10-10', '2022-09-10', 'Analyst', 'Inactive', 77, 60, 2.2),
    (26, 'Noah', 'Martin', '2016-11-20', '2021-10-20', 'Consultant', 'Inactive', 82, 35, 1.4),
    (27, 'Olivia', 'Lee', '2015-01-30', '2020-12-30', 'Engineer', 'Inactive', 75, 40, 1.5),
    (28, 'Paul', 'Perez', '2014-03-01', '2019-02-01', 'Manager', 'Inactive', 65, 50, 1.6),
    (29, 'Quinn', 'Thompson', '2013-04-15', '2018-03-15', 'Developer', 'Inactive', 60, 55, 1.7),
    (30, 'Ruby', 'White', '2012-05-20', '2017-04-20', 'Technician', 'Inactive', 55, 60, 1.8),
    (31, 'Sophia', 'Clark', '2021-06-01', None, 'Engineer', 'Active', 89, 65, 2.1),
    (32, 'James', 'Rodriguez', '2020-07-01', None, 'Manager', 'Active', 83, 70, 2.2),
    (33, 'Lily', 'Lewis', '2019-08-01', None, 'Technician', 'Active', 79, 75, 2.3),
    (34, 'Daniel', 'Walker', '2018-09-01', '2023-07-01', 'Developer', 'Inactive', 85, 80, 2.4),
    (35, 'Emma', 'Hall', '2017-10-01', '2022-08-01', 'Analyst', 'Inactive', 88, 85, 2.5),
    (36, 'Michael', 'Allen', '2016-11-01', '2021-09-01', 'Consultant', 'Inactive', 90, 90, 2.6),
    (37, 'Ava', 'Young', '2015-12-01', '2020-10-01', 'Engineer', 'Inactive', 87, 95, 2.7),
    (38, 'Ethan', 'King', '2014-01-01', '2019-12-01', 'Manager', 'Inactive', 86, 100, 2.8),
    (39, 'Chloe', 'Wright', '2013-02-01', '2018-11-01', 'Developer', 'Inactive', 80, 105, 2.9),
    (40, 'Chloe', 'Lewis', '2021-01-01', None, 'Engineer', 'Active', 100, 1000, 13.0),
]


# Insert data into the Employees table
cursor.executemany('''
INSERT INTO Employees (
    EmpID, FirstName, LastName, StartDate, ExitDate, Title, EmployeeStatus, PerformanceScore,
    SolvedNumberOfTickets, TicketTimeRate
) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
''', employees)
conn.commit()

# Close the connection
conn.close()
