import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    database = "hospital",
    user ="root",
    password = ""
)

mycursor = mydb.cursor(dictionary=True)

mycursor.execute(
    """CREATE TABLE IF NOT EXISTS PATIENT(
        name VARCHAR(255),
        email VARCHAR(255),
        password VARCHAR(255),
        Age INT,
        Phone_number INT,
        Gender VARCHAR(100)
        )
         """
)

mycursor.execute( 
"""CREATE TABLE IF NOT EXISTS DOCTORS(
        DOCTOR_ID INT AUTO_INCREMENT,
        name VARCHAR(255),
        email VARCHAR(255),
        password VARCHAR(255),
        Age INT,
        Phone_number INT,
        Gender VARCHAR(100),
        PRIMARY KEY(DOCTOR_ID)
 ) """
)

mycursor.execute(
    """CREATE TABLE IF NOT EXISTS APPOINTMENTS(
        APPOINTMENT_ID INT AUTO_INCREMENT,
        Date VARCHAR(100),
        Time INT,
        PRIMARY KEY(APPOINTMENT_ID)
        )"""

)

# mycursor.execute(
#     """ALTER TABLE PATIENT ADD COLUMN IF NOT EXISTS(
#         patient_id int AUTO_INCREMENT,
#         appointment_time INT,
#         FOREIGN KEY(appointment_time) REFERENCES APPOINTMENTS(APPOINTMENT_ID),
#         PRIMARY KEY(patient_id)
#     )
#     """
# )

# mycursor.execute(
#     """ALTER TABLE APPOINTMENTS ADD COLUMN IF NOT EXISTS(
#         DOCTOR INT,
#         FOREIGN KEY(DOCTOR) REFERENCES DOCTORS(DOCTOR_ID)
#     )
#     """
# )

mycursor.execute(
    """ALTER TABLE APPOINTMENTS ADD COLUMN IF NOT EXISTS(
        PATIENT INT,
        FOREIGN KEY(PATIENT) REFERENCES PATIENT(patient_id)
        )"""

)


# mycursor.execute(
#     """ALTER TABLE """
# )