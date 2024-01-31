
from flask import Flask, render_template, request, abort, redirect, url_for
from werkzeug.exceptions import MethodNotAllowed
import os
import platform
import socket
import subprocess
from db_function import *


app = Flask(__name__)


#################### User Function #####################
def system_information():

    output = subprocess.check_output("uname -r", shell=True)
    return (
        platform.node(),
        socket.gethostbyname(socket.gethostname()),
        output.decode("utf-8").split("\n")[0],
        os.getenv('NODE_NAME')
    )


def get_envs():
    return (
        os.getenv('dbname'),
        os.getenv('dbuser'),
        os.getenv('dbpassword'),
        os.getenv('dbhost'),
        os.getenv('dbport'),
    )

#################### Route #####################


@app.route('/', methods=['GET', 'POST'])
def index():
    info = system_information()
    if db_status():

        users = get_user()

        if request.method == "POST":

            id = request.form['user-id']
            name = request.form['first-lastname']
            department = request.form['department']
            username = request.form['username']
            password = request.form['password']

            if id != "" and name != "" and department != "" and username != "" and password != "":
                add_user(id, name, department, username, password)
            else:
                pass

            return redirect('/')

        else:

            return render_template(
                'adduser.html', hostname=info[0], ipaddress=info[1], kernel=info[2], version='1.1', worker=info[3], users=users,
                dbuser=get_envs()[0], dbname=get_envs()[1], dbpassword=get_envs()[2], dbhost=get_envs()[3], dbport=get_envs()[4])

    else:
        users = ()
        return render_template(
            'adduser.html', hostname=info[0], ipaddress=info[1], kernel=info[2], version='1.1', worker=info[3], users=users,
            dbuser=get_envs()[0], dbname=get_envs()[1], dbpassword=get_envs()[
                2], dbhost=get_envs()[3], dbport=get_envs()[4],
            db_status='[ db connection failed ]')


@app.route('/delete-user', methods=['GET', 'POST'])
def page_delete_user():
    info = system_information()
    if db_status():
        users = get_user()
        if request.method == "POST" and request.form['Delete'] == "Delete":
            username = request.form['username']

            if username != "":
                delete_user(username)
            else:
                pass

            return redirect('/delete-user')

        else:
            return render_template(
                'deleteuser.html', hostname=info[0], ipaddress=info[1], kernel=info[2], version='1.1', worker=info[3], users=users,
                dbuser=get_envs()[0], dbname=get_envs()[1], dbpassword=get_envs()[2], dbhost=get_envs()[3], dbport=get_envs()[4])

    else:
        users = ()
        return render_template(
            'deleteuser.html', hostname=info[0], ipaddress=info[1], kernel=info[2], version='1.1', worker=info[3], users=users,
            dbuser=get_envs()[0], dbname=get_envs()[1], dbpassword=get_envs()[
                2], dbhost=get_envs()[3], dbport=get_envs()[4],
            db_status='[ db connection failed ]')


@app.route('/change-password', methods=['GET', 'POST'])
def page_change_password():

    info = system_information()

    if db_status():
        users = get_user()
        if request.method == "POST" and request.form['Change'] == "Change":
            username = request.form['username']
            new_password = request.form['password']

            if username != "" and new_password != "":
                update_password(username, new_password)
            else:
                pass

            return redirect('/change-password')

        else:
            return render_template(
                'updatepassword.html', hostname=info[0], ipaddress=info[1], kernel=info[2], version='1.1', worker=info[3], users=users,
                dbuser=get_envs()[0], dbname=get_envs()[1], dbpassword=get_envs()[2], dbhost=get_envs()[3], dbport=get_envs()[4])

    else:
        users = ()
        return render_template(
            'updatepassword.html', hostname=info[0], ipaddress=info[1], kernel=info[2], version='1.1', worker=info[3], users=users,
            dbuser=get_envs()[0], dbname=get_envs()[1], dbpassword=get_envs()[
                2], dbhost=get_envs()[3], dbport=get_envs()[4],
            db_status='[ db connection failed ]')


@app.route('/health-check', methods=['GET'])
def heal_check():
    if db_status():
        return "OK.\n"
    else:
        return "Database connection error.\n", 500


@app.route('/health-check2', methods=['GET'])
def heal_check2():
    if db_status():
        return "OK.\n"
    else:
        abort(404)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=31000, debug=True)
