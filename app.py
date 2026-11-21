
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

contacts = []

@app.route('/')
def index():
    search = request.args.get('search', '')
    if search:
        filtered = [
            c for c in contacts
            if search.lower() in c['name'].lower()
        ]
    else:
        filtered = contacts

    return render_template(
        'index.html',
        contacts=filtered,
        total=len(contacts)
    )

@app.route('/add', methods=['POST'])
def add():
    name = request.form.get('name')
    phone = request.form.get('phone')
    email = request.form.get('email')

    if name and phone:
        contacts.append({
            'name': name,
            'phone': phone,
            'email': email
        })

    return redirect(url_for('index'))

@app.route('/delete/<int:index>')
def delete(index):
    if 0 <= index < len(contacts):
        contacts.pop(index)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
