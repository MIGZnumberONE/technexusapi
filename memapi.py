from flask import jsonify, request, Flask, session
from flask_cors import CORS
import uuid

app = Flask(__name__)
app.config["DEBUG"] = True
CORS(app)

all_mems = [
    { 'id': 11, 'name': 'London', 'image': '../assets/seo.jpg', 'additionalinfo': 'What 4 Party' },
    { 'id': 21, 'name': 'Paris', 'image': '../assets/callcenter.jpg', 'latitude': 48.8583, 'longitude': 2.2944, 'additionalinfo': 'One Night in Paris' },
    { 'id': 31, 'name': 'Seuol', 'image': '../assets/cyberspace.jpg', 'latitude': 37.5665, 'longitude': 126.9779, 'additionalinfo': 'What happens in Munich Stay in Seoul' },
    { 'id': 41, 'name': 'Göbekli Tepe','image': '../assets/people.jpg', 'latitude': 34.5337, 'longitude': 43.4837, 'additionalinfo': 'Harran-Ebene (Mesopotamien)' },
    { 'id': 51, 'name': 'Saint Tropez','image': '../assets/sayhi.jpeg', 'latitude': 43.2676, 'longitude': 6.6407, 'additionalinfo': 'La Citadelle' },
    { 'id': 61, 'name': 'Greenwich','image': '../assets/greenwich.jpeg', 'latitude': 51.482577, 'longitude': -0.0076, 'additionalinfo': 'Null Meridian' },
    { 'id': 71, 'name': 'Osterinseln','image': '../assets/easterisland.jpg', 'latitude': -27.0889, 'longitude': -109.3545, 'additionalinfo': 'So many people' },
    { 'id': 81, 'name': 'Groom Lake','image': '../assets/service.jpg', 'latitude': 37.2766, 'longitude': -115.7989, 'additionalinfo': 'Tikaboo Peak' },
    { 'id': 91, 'name': 'Gizeh','image': '../assets/giza.JPG', 'latitude': 29.977296, 'longitude': 31.1324, 'additionalinfo': 'As above, so below and also it looks like Speed of Light' },
    { 'id': 13, 'name': 'Sacsayhuamán, Cusco, Perú','image': '../assets/sacsay.JPG', 'latitude': -13.5098, 'longitude': -71.9816, 'additionalinfo': 'Sunny Fiesta on Juny the 24th.' },
    { 'id': 12, 'name': 'Nazca','image': '../assets/nazca.jpg', 'latitude': -14.7390, 'longitude': -75.1300, 'additionalinfo': 'Painting' },
    { 'id': 16, 'name': 'Teotihuacán','image': '../assets/laluna.jpg', 'latitude': 19.6897, 'longitude': -98.8608, 'additionalinfo': 'The Pyramid of the Sun and the "Avenue of the Dead" in Teotihuacán seen from the Pyramid of the Moon' },
    { 'id': 18, 'name': 'Baalbek, Lebanon','image': '../assets/baalbek.jpg', 'latitude': 34.0046, 'longitude': 36.2110, 'additionalinfo': 'Juniper, as many Megalith blocks as the eye can see' },
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