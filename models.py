# models.py
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

# SQLAlchemy 초기화
db = SQLAlchemy()

# 사용자 모델 정의
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

# 설문조사 모델 정의
class Survey(db.Model):
    __tablename__ = 'surveys'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    question = db.Column(db.String(300), nullable=False)
    answer = db.Column(db.String(50), nullable=False)

    user = db.relationship('User', backref=db.backref('surveys', lazy=True))

# ESG 평가 결과 모델 정의
class Evaluation(db.Model):
    __tablename__ = 'evaluations'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    overall_score = db.Column(db.Integer, nullable=False)
    e_score = db.Column(db.Integer, nullable=False)
    s_score = db.Column(db.Integer, nullable=False)
    g_score = db.Column(db.Integer, nullable=False)

    user = db.relationship('User', backref=db.backref('evaluations', lazy=True))
