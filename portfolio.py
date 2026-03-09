from flask import Flask, render_template, request, redirect
import csv
# from pyexpat.errors import messages


app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('D:\\Pycharm\\PythonProject\\ZTMprojects\\project3\\database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n\nemail:{email}\nsubject:{subject}\nmessage:{message}')

def write_to_csv(data):
    with open('D:\\Pycharm\\PythonProject\\ZTMprojects\\project3\\database.csv', mode='a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', lineterminator='\n', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong, try again'

# @app.route('/index.html')
# def my_index():
#     return r.ender_template('index.html')
#
# @app.route('/works.html')
# def my_works():
#     return render_template('works.html')
#
# @app.route('/about.html')
# def my_about():
#     return render_template('about.html')
#
# @app.route('/contact.html')
# def my_contact():
#     return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)