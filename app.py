from flask import Flask, jsonify, send_file, render_template
from flask_cors import CORS
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from PIL import Image
import os
import random
import io

app = Flask(__name__)
CORS(app)

# Настройка базы данных
Base = declarative_base()
engine = create_engine('sqlite:///db.sqlite3')
Session = sessionmaker(bind=engine)
session = Session()

# Модель аватара
class Avatar(Base):
    __tablename__ = 'avatars'
    id = Column(Integer, primary_key=True)
    filename = Column(String, unique=True)

Base.metadata.create_all(engine)

# Путь к папке с аватарками
AVATAR_FOLDER = 'static/avatars/'

def populate_db():
    session = Session()
    files_in_directory = set(os.listdir(AVATAR_FOLDER))

    for filename in files_in_directory:
        if filename.endswith(('png', 'jpg', 'jpeg', 'webp')):
            if not session.query(Avatar).filter_by(filename=filename).first():
                new_avatar = Avatar(filename=filename)
                session.add(new_avatar)
                print(f"Added {filename} to the database.")

    avatars_in_db = session.query(Avatar).all()
    for avatar in avatars_in_db:
        if avatar.filename not in files_in_directory:
            session.delete(avatar)
            print(f"Deleted {avatar.filename} from the database.")

    session.commit()
    print("Database population complete.")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/random-avatar')
def random_avatar():
    avatars = session.query(Avatar).all()
    if not avatars:
        return jsonify({'success': False, 'message': 'No avatars available'}), 404

    avatar = random.choice(avatars)
    return jsonify({'id': avatar.id, 'filename': avatar.filename})

@app.route('/download/<int:avatar_id>/<format>/<int:width>/<int:height>')
def download(avatar_id, format, width, height):
    if width > 1000 or height > 1000:
        return jsonify({'success': False, 'message': 'Maximum allowed dimensions are 1000x1000'}), 400
    
    avatar = session.query(Avatar).filter_by(id=avatar_id).first()
    if avatar:
        filepath = os.path.join(AVATAR_FOLDER, avatar.filename)
        img = Image.open(filepath)
        img = img.resize((width, height))
        
        img_io = io.BytesIO()
        img.save(img_io, format)
        img_io.seek(0)
        
        return send_file(img_io, mimetype=f'image/{format}', as_attachment=True, download_name=f"{os.path.splitext(avatar.filename)[0]}_{width}x{height}.{format}")
    return jsonify({'success': False, 'message': 'Avatar not found'}), 404

if __name__ == '__main__':
    if not os.path.exists(AVATAR_FOLDER):
        os.makedirs(AVATAR_FOLDER)
    populate_db()
    app.run(debug=True)
