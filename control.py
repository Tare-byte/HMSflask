from flask import Flask, render_template, redirect, request
from hms import mydb, mycursor

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/patients')
def patients():
    return render_template('patients.html')


@app.route('/patient_reg', methods=['POST', 'GET'])
def system():
    if request.method == 'GET':
        return render_template('patient_reg.html')
    if request.method == 'POST':
        _name = request.form['name']
        _email = request.form['email']
        _password = request.form['password']
        _age = request.form['age']
        _phoneNumber = request.form['Phone_number']
        _gender = request.form['gender']
        sql = 'INSERT INTO PATIENT(name, email, password, Age, Phone_number, Gender) VALUES(%s, %s, %s, %s, %s, %s)'
        val = (_name, _email, _password, _age, _phoneNumber, _gender)
        mycursor.execute(sql, val)
        mydb.commit()
        return redirect('/login')


@app.route('/login', methods=(['GET', 'POST']))
def login():
    message = ''
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        _loginemail = request.form['email']
        _loginpassword = request.form['password']
        mycursor.execute(f'SELECT * FROM PATIENT WHERE email = "{_loginemail}" AND password = "{_loginpassword}"')
        verify = mycursor.fetchone()
       # print(verify)
        if verify:
           # return redirect(f"/patient/{verify['patient_id']}")
            return render_template('patient.html', patient = verify)
        else:
            message = 'failed to login'
            return render_template('login.html', msg = message)
        

@app.route('/patient/<int:id>')
def patient(id):

    print(patient)
    return render_template('patient.html', patient = patient)

@app.route('/it')
def it():
    # mycursor.execute(f'SELECT * FROM PATIENT WHERE patient_id="{id}"')
    # patient = mycursor.fetchone()
    # print(patient)
    return render_template('patient.html')


@app.route('/doctor-login', methods=(['GET', 'POST']))
def doc_login():
    message = ''
    if request.method == 'GET':
        return render_template('doctor-login.html')
    if request.method == 'POST':
        _loginemail = request.form['email']
        _loginpassword = request.form['password']
        mycursor.execute(f'SELECT * FROM DOCTORS WHERE email = "{_loginemail}" AND password = "{_loginpassword}"')
        verify = mycursor.fetchone()
        print(verify)
        if verify:
            return redirect(f"/doctor/{verify['DOCTOR_ID']}")
        else:
            message = 'failed to login'
    return render_template('doctor-login.html', msg = message)
        


@app.route('/doctor/<int:id>')
def doctor(id):
    mycursor.execute(f'SELECT * FROM DOCTORS WHERE DOCTOR_ID="{id}"')
    doctor = mycursor.fetchone()
    print(doctor)
    return render_template('doctor.html', doctor = doctor)

@app.route('/appointments', methods=(['GET', 'POST']))
def appointments():
    message = ''
    if request.method == 'GET':
        return render_template('appointments.html')
    if request.method == 'POST':
        _requesterId = int(request.form['id'])
        mycursor.execute(f'SELECT * FROM PATIENT WHERE patient_id = {_requesterId}')
        patient = mycursor.fetchone()

        if patient:
            # sql = 'INSERT INTO APPOINTMENTS(patient) VALUES(%s)'
            # val = (patient['patient_id'])
            # mycursor.execute(sql, val)
            mycursor.execute(f'INSERT INTO APPOINTMENTS(patient) VALUES({patient["patient_id"]})')
            mydb.commit()
            return redirect(f"/patient/{patient['patient_id']}")
        else:
            message = 'Use a valid patient id'
            return render_template('appointments.html', msg = message)
        


@app.route('/appointmentsmsg', methods=(['GET', 'POST']))
def gotomsg():
    return render_template('appointmentsmsg.html')
        


    


if __name__=='__main__':
    app.run()