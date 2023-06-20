from flask import jsonify, request, Flask, session
from flask_cors import CORS
import uuid

app = Flask(__name__)
app.config["DEBUG"] = True
CORS(app)

all_mems = [
    { 'id': 11, 'name': 'Member A', 'image': '../assets/1.jpg', 'additionalinfo': 'hereiam@gmail.com' },
    { 'id': 21, 'name': 'Member B', 'image': '../assets/2.jpg', 'additionalinfo': '+ 49 160 1234567' },
    { 'id': 31, 'name': 'Member C', 'image': '../assets/3.jpg', 'additionalinfo': 'Dev Ops' },
    { 'id': 41, 'name': 'Member D','image': '../assets/4.jpg', 'additionalinfo': 'Software Developer' },
    { 'id': 51, 'name': 'Member E','image': '../assets/5.jpg', 'additionalinfo': 'Admin' },
    { 'id': 61, 'name': 'Member F','image': '../assets/6.jpg', 'additionalinfo': 'Scrum Master' },
    { 'id': 71, 'name': 'Member G','image': '../assets/7.jpg', 'additionalinfo': 'Linux Professional' },
    { 'id': 81, 'name': 'Member H','image': '../assets/8.jpg', 'additionalinfo': 'Available' },
    { 'id': 91, 'name': 'Member I','image': '../assets/9.jpg', 'additionalinfo': 'Meeting due to 12p.m.' },
    { 'id': 13, 'name': 'Member J','image': '../assets/10.jpg', 'additionalinfo': 'not Available' },
    { 'id': 12, 'name': 'Member K','image': '../assets/11.jpg', 'additionalinfo': 'Painting' },
    { 'id': 16, 'name': 'Member L','image': '../assets/12.jpg', 'additionalinfo': 'Terraform' },
    { 'id': 18, 'name': 'Member M','image': '../assets/13.jpg', 'additionalinfo': 'Ansible' },
]


@app.route('/', methods=['GET'])
def get_all_mems():
    return jsonify(all_mems)

@app.route('/mems', methods=['GET'])
def mems():
    return jsonify(all_mems)

@app.route('/members', methods=['POST'])
def create_member():
    data = request.get_json()
    random_id = max(m['id'] for m in all_mems) + 1
    new_mem = {'id': random_id, 'name': data['name']}
    all_mems.append(new_mem)
    return jsonify(new_mem)

@app.route('/detail/<id>', methods=['GET'])
def detail(id):
    for x in all_mems:
        if int(x['id']) == int(id):
            return jsonify(x)

    return "Record not found", 400

@app.route('/update', methods=['POST'])
def update():
    data = request.get_json()
    for x in all_mems:
        if x['id'] == data['id']:
            x['name'] = data['name']
            return jsonify(x)

    return "Not found", 400

@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    if not all_mems:
        random_id = 1
    else:
        random_id = max(m['id'] for m in all_mems) + 1
    new_mem = {'id': random_id, 'name': data['name']}
    all_mems.append(new_mem)
    return jsonify(new_mem)

@app.route('/delete/<id>', methods=['DELETE'])
def delete_mem(id):
    global all_mems
    all_mems = [m for m in all_mems if m['id'] != int(id)]
    return jsonify({'message': 'Record deleted successfully'})

if __name__ == '__main__':
    app.run()
