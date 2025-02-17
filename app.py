from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_cors import CORS
import datetime

# Flask uygulaması
app = Flask(__name__)
CORS(app)

# Veritabanı konfigürasyonu (SQLite, PostgreSQL veya MySQL)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'  # PostgreSQL: 'postgresql://user:pass@localhost/dbname'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'supersecretkey'  # Güvenlik için değiştir!

# Kütüphaneleri bağla
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# Kullanıcı Modeli
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

# Görev Modeli
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    done = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# Veritabanını oluştur
with app.app_context():
    db.create_all()

# Kullanıcı Kaydı
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    new_user = User(username=data['username'], password=hashed_password)
    
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "Kullanıcı oluşturuldu!"}), 201

# Kullanıcı Girişi (JWT Token Döner)
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    
    if user and bcrypt.check_password_hash(user.password, data['password']):
        access_token = create_access_token(identity=user.id, expires_delta=datetime.timedelta(hours=1))
        return jsonify(access_token=access_token)
    
    return jsonify({"message": "Geçersiz kimlik bilgileri!"}), 401

# Görevleri Listele (Sadece Giriş Yapan Kullanıcının)
@app.route('/tasks', methods=['GET'])
@jwt_required()
def get_tasks():
    user_id = get_jwt_identity()
    tasks = Task.query.filter_by(user_id=user_id).all()
    
    return jsonify([{"id": task.id, "title": task.title, "done": task.done} for task in tasks])

# Yeni Görev Ekle
@app.route('/tasks', methods=['POST'])
@jwt_required()
def add_task():
    user_id = get_jwt_identity()
    data = request.get_json()
    new_task = Task(title=data['title'], done=False, user_id=user_id)
    
    db.session.add(new_task)
    db.session.commit()
    
    return jsonify({"message": "Görev eklendi!"}), 201

# Görev Güncelle
@app.route('/tasks/<int:task_id>', methods=['PUT'])
@jwt_required()
def update_task(task_id):
    user_id = get_jwt_identity()
    task = Task.query.filter_by(id=task_id, user_id=user_id).first()
    
    if not task:
        return jsonify({"message": "Görev bulunamadı!"}), 404

    data = request.get_json()
    task.title = data.get("title", task.title)
    task.done = data.get("done", task.done)

    db.session.commit()
    return jsonify({"message": "Görev güncellendi!"})

# Görev Sil
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
@jwt_required()
def delete_task(task_id):
    user_id = get_jwt_identity()
    task = Task.query.filter_by(id=task_id, user_id=user_id).first()

    if not task:
        return jsonify({"message": "Görev bulunamadı!"}), 404

    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": "Görev silindi!"})

# Uygulamayı Çalıştır
if __name__ == '__main__':
    app.run(debug=True)
