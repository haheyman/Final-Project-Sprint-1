# Import necessary modules
import flask
from flask import jsonify, request
import creds
from sql import create_connection, execute_read_query

# Initialize Flask app
app = flask.Flask(__name__)
app.config["DEBUG"] = True

# API endpoint to get one facility by ID
@app.route('/api/facilities/get', methods=['GET'])
def api_get_facility():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return 'Error: No ID is provided!'
    myCreds = creds.Creds()
    conn = create_connection(myCreds.hostname, myCreds.uname, myCreds.passwd, myCreds.dbname)
    sql ="select * from facility"
    users = execute_read_query(conn, sql)
    results = []
    for user in users:
        if user['id']== id:
            results.append(user)
    return jsonify(results)

# API endpoint to get all facilities
@app.route('/api/facilities/get/all', methods=['GET'])
def api_get_all_facilities():
    myCreds = creds.Creds()
    conn = create_connection(myCreds.hostname, myCreds.uname, myCreds.passwd, myCreds.dbname)
    if conn is not None:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM facility")
        facilities = cursor.fetchall()
        conn.close()
        return jsonify(facilities)
    else:
        return "Error connecting to database."

# API endpoint to add a new facility
@app.route('/api/facilities/post', methods=['POST'])
def api_add_facility():
    data = request.get_json()
    name = data['name']

    myCreds = creds.Creds()
    conn = create_connection(myCreds.hostname, myCreds.uname, myCreds.passwd, myCreds.dbname)
    if conn is not None:
        cursor=conn.cursor()
        cursor.execute("INSERT INTO facility (name) VALUES (%s)", 
                       (name))
        conn.commit()
        conn.close()
        return "Facility added successfully"
    else:
        return "Error connecting to database"

# API endpoint to update an existing facility
@app.route('/api/facilities/put', methods=['PUT'])
def api_update_facility():
    data = request.get_json()
    id = data['id']
    name = data['name']

    myCreds = creds.Creds()
    conn = create_connection(myCreds.hostname, myCreds.uname, myCreds.passwd, myCreds.dbname)
    if conn is not None:
        cursor = conn.cursor()
        cursor.execute("UPDATE facility SET name=%s WHERE id=%s",
                       (name, id))
        conn.commit()
        conn.close()
        return "Facility updated successfully."
    else:
        return "Error connecting to database."

# API endpoint to delete a facility
@app.route('/api/facilities/delete', methods=['DELETE'])
def api_delete_facility():
    data = request.get_json()
    id = data['id']

    myCreds = creds.Creds()
    conn = create_connection(myCreds.hostname, myCreds.uname, myCreds.passwd, myCreds.dbname)
    if conn is not None:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM facility WHERE id=%s", (id,))
        conn.commit()
        conn.close()
        return "Facility deleted successfully."
    else:
        return "Error connecting to database."

# API endpoint to get one classroom by ID
@app.route('/api/classrooms/get', methods=['GET'])
def api_get_classroom():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return 'Error: No ID is provided!'
    myCreds = creds.Creds()
    conn = create_connection(myCreds.hostname, myCreds.uname, myCreds.passwd, myCreds.dbname)
    sql ="select * from classroom"
    users = execute_read_query(conn, sql)
    results = []
    for user in users:
        if user['id']== id:
            results.append(user)
    return jsonify(results)

# API endpoint to get all classrooms
@app.route('/api/classrooms/get/all', methods=['GET'])
def api_get_all_classrooms():
    myCreds = creds.Creds()
    conn = create_connection(myCreds.hostname, myCreds.uname, myCreds.passwd, myCreds.dbname)
    if conn is not None:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM classroom")
        classrooms = cursor.fetchall()
        conn.close()
        return jsonify(classrooms)
    else:
        return "Error connecting to database."

# API endpoint to add a new classroom
@app.route('/api/classrooms/post', methods=['POST'])
def api_add_classroom():
    data = request.get_json()
    capacity = data['capacity']
    name = data['name']
    facilityid = data['facility_id']

    myCreds = creds.Creds()
    conn = create_connection(myCreds.hostname, myCreds.uname, myCreds.passwd, myCreds.dbname)
    if conn is not None:
        cursor=conn.cursor()
        cursor.execute("INSERT INTO classroom (capacity, name, facility_id) VALUES (%s, %s, %s)", 
                       (capacity, name, facilityid))
        conn.commit()
        conn.close()
        return "Classroom added successfully"
    else:
        return "Error connecting to database"

# API endpoint to update an existing classroom
@app.route('/api/classrooms/put', methods=['PUT'])
def api_update_classroom():
    data = request.get_json()
    id = data['id']
    capacity = data['capicity']
    name = data['name']
    facilityid = data['facility_id']
    
    myCreds = creds.Creds()
    conn = create_connection(myCreds.hostname, myCreds.uname, myCreds.passwd, myCreds.dbname)
    if conn is not None:
        cursor = conn.cursor()
        cursor.execute("UPDATE classroom SET capacity=%s, name=%s, facility_id=%s WHERE id=%s",
                       (capacity, name, facilityid, id))
        conn.commit()
        conn.close()
        return "Classroom updated successfully."
    else:
        return "Error connecting to database."

# API endpoint to delete a classroom
@app.route('/api/classrooms/delete', methods=['DELETE'])
def api_delete_classroom():
    data = request.get_json()
    id = data['id']

    myCreds = creds.Creds()
    conn = create_connection(myCreds.hostname, myCreds.uname, myCreds.passwd, myCreds.dbname)
    if conn is not None:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM classroom WHERE id=%s", (id,))
        conn.commit()
        conn.close()
        return "Classroom deleted successfully."
    else:
        return "Error connecting to database."

# API endpoint to get one teacher by ID
@app.route('/api/teachers/get', methods=['GET'])
def api_get_teacher():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return 'Error: No ID is provided!'
    myCreds = creds.Creds()
    conn = create_connection(myCreds.hostname, myCreds.uname, myCreds.passwd, myCreds.dbname)
    sql ="select * from teacher"
    users = execute_read_query(conn, sql)
    results = []
    for user in users:
        if user['id']== id:
            results.append(user)
    return jsonify(results)

# API endpoint to get all teachers
@app.route('/api/teachers/get/all', methods=['GET'])
def api_get_all_teachers():
    myCreds = creds.Creds()
    conn = create_connection(myCreds.hostname, myCreds.uname, myCreds.passwd, myCreds.dbname)
    if conn is not None:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM teacher")
        teachers = cursor.fetchall()
        conn.close()
        return jsonify(teachers)
    else:
        return "Error connecting to database."

# API endpoint to add a new teacher
@app.route('/api/teachers/post', methods=['POST'])
def api_add_teacher():
    data = request.get_json()
    firstname = data['firstname']
    lastname = data['lastname']
    room = data['room']

    myCreds = creds.Creds()
    conn = create_connection(myCreds.hostname, myCreds.uname, myCreds.passwd, myCreds.dbname)
    if conn is not None:
        cursor=conn.cursor()
        cursor.execute("INSERT INTO teacher (firstname, lastname, room) VALUES (%s, %s, %s)", 
                       (firstname, lastname, room))
        conn.commit()
        conn.close()
        return "Teacher added successfully"
    else:
        return "Error connecting to database"

# API endpoint to update an existing teacher
@app.route('/api/teachers/put', methods=['PUT'])
def api_update_teacher():
    data = request.get_json()
    id = data['id']
    firstname = data['firstname']
    lastname = data['lastname']
    room = data['room']
    
    myCreds = creds.Creds()
    conn = create_connection(myCreds.hostname, myCreds.uname, myCreds.passwd, myCreds.dbname)
    if conn is not None:
        cursor = conn.cursor()
        cursor.execute("UPDATE teacher SET firstname=%s, lastname=%s, room=%s WHERE id=%s",
                       (firstname, lastname, room, id))
        conn.commit()
        conn.close()
        return "Teacher updated successfully."
    else:
        return "Error connecting to database."

# API endpoint to delete a teacher
@app.route('/api/teachers/delete', methods=['DELETE'])
def api_delete_teacher():
    data = request.get_json()
    id = data['id']

    myCreds = creds.Creds()
    conn = create_connection(myCreds.hostname, myCreds.uname, myCreds.passwd, myCreds.dbname)
    if conn is not None:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM teacher WHERE id=%s", (id,))
        conn.commit()
        conn.close()
        return "Teacher deleted successfully."
    else:
        return "Error connecting to database."

# API endpoint to get one child by ID
@app.route('/api/children/get', methods=['GET'])
def api_get_child():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return 'Error: No ID is provided!'
    myCreds = creds.Creds()
    conn = create_connection(myCreds.hostname, myCreds.uname, myCreds.passwd, myCreds.dbname)
    sql ="select * from child"
    users = execute_read_query(conn, sql)
    results = []
    for user in users:
        if user['id']== id:
            results.append(user)
    return jsonify(results)

# API endpoint to get all children
@app.route('/api/children/get/all', methods=['GET'])
def api_get_all_children():
    myCreds = creds.Creds()
    conn = create_connection(myCreds.hostname, myCreds.uname, myCreds.passwd, myCreds.dbname)
    if conn is not None:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM child")
        children = cursor.fetchall()
        conn.close()
        return jsonify(children)
    else:
        return "Error connecting to database."

# API endpoint to add a new child
@app.route('/api/children/post', methods=['POST'])
def api_add_child():
    data = request.get_json()
    firstname = data['firstname']
    lastname = data['lastname']
    age = data['age']
    room = data['room']

    myCreds = creds.Creds()
    conn = create_connection(myCreds.hostname, myCreds.uname, myCreds.passwd, myCreds.dbname)
    if conn is not None:
        cursor=conn.cursor()
        cursor.execute("INSERT INTO child (firstname, lastname, age, room) VALUES (%s, %s, %s, %s)", 
                       (firstname, lastname, age, room))
        conn.commit()
        conn.close()
        return "Child added successfully"
    else:
        return "Error connecting to database"

# API endpoint to update an existing child
@app.route('/api/children/put', methods=['PUT'])
def api_update_child():
    data = request.get_json()
    id = data['id']
    firstname = data['firstname']
    lastname = data['lastname']
    age = data['age']
    room = data['room']
    
    myCreds = creds.Creds()
    conn = create_connection(myCreds.hostname, myCreds.uname, myCreds.passwd, myCreds.dbname)
    if conn is not None:
        cursor = conn.cursor()
        cursor.execute("UPDATE teacher SET firstname=%s, lastname=%s, age=%s, room=%s WHERE id=%s",
                       (firstname, lastname, age, room, id))
        conn.commit()
        conn.close()
        return "Teacher updated successfully."
    else:
        return "Error connecting to database."

# API endpoint to delete a child
@app.route('/api/children/delete', methods=['DELETE'])
def api_delete_child():
    data = request.get_json()
    id = data['id']

    myCreds = creds.Creds()
    conn = create_connection(myCreds.hostname, myCreds.uname, myCreds.passwd, myCreds.dbname)
    if conn is not None:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM child WHERE id=%s", (id,))
        conn.commit()
        conn.close()
        return "Child deleted successfully."
    else:
        return "Error connecting to database."

# Simple login API
@app.route('/api/login', methods=['POST'])
def api_login():
    mylogincreds = creds.Creds()
    data = request.get_json()
    username = data['username']
    password = data['password']

    # Check if username and password match the default values
    if username == mylogincreds.login_user and password == mylogincreds.login_pass:
        return jsonify({'message': 'Login successful'})
    else:
        return jsonify({'message': 'Login failed. Invalid username or password'})

# Run the Flask application
if __name__ == '__main__':
    app.run()
