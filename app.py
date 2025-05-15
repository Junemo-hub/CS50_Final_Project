from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from models import db, User, Survey, Evaluation
from forms import LoginForm, RegisterForm, SurveyForm
from werkzeug.security import generate_password_hash, check_password_hash
import os


# Flask App 초기화
app = Flask(__name__)
app.secret_key = 'supersecretkey'

# ✅ Flask의 instance 폴더가 없으면 생성
if not os.path.exists(app.instance_path):
    os.makedirs(app.instance_path)

# ✅ DB 설정 (Flask 권장 경로인 instance 폴더에 생성)
db_path = os.path.join(app.instance_path, 'database.db')
print(f"📌 Database path: {db_path}")  # 경로 확인용 출력

# SQLite Database 설정
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_path}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# app에 SQLAlchemy 등록
db.init_app(app)

# 데이터베이스 생성
with app.app_context():
    db.create_all()
    print(f"✅ Database has been created successfully at {db_path}")

# 메인 페이지 (로그인 페이지로 리다이렉트)
@app.route('/')
def index():
    if 'username' in session:
        return render_template('index.html', username=session['username'])
    else:
        return render_template('index.html', username=None)

# 로그인 페이지
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        print("🔎 username:", username)
        print("🔍 user from DB:", user)

        if user:
            print("🧪 checking password...")
            print("✅ match?", check_password_hash(user.password, password))

        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            session['username'] = user.username
            flash('Login successful!', 'success')
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error="Invalid username or password.")

    return render_template("login.html")


# 회원가입 페이지
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # 비밀번호 해싱
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        
        # 중복 사용자명 체크
        if User.query.filter_by(username=username).first():
            return render_template('register.html', error="Username already exists.")
        
        # 사용자 생성
        new_user = User(username=username, password=hashed_password)
        
        try:
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('login'))
        except:
            return render_template('register.html', error="There was an issue creating your account.")
    
    return render_template('register.html')

# Survey page
@app.route('/survey', methods=['GET', 'POST'])
def survey():
    if 'user_id' not in session:
        flash('Please log in to take the survey.', 'warning')
        return redirect(url_for('login'))

    form = SurveyForm()

    if form.validate_on_submit():
        new_survey = Survey(
            user_id=session['user_id'],
            question=form.question.data,
            answer=form.answer.data
        )
        db.session.add(new_survey)
        db.session.commit()
        flash('Survey submitted successfully!', 'success')
        return redirect(url_for('result'))

    return render_template('survey.html', form=form)

#survey - submit
@app.route('/submit-survey', methods=['POST'])
def submit_survey():
    if 'user_id' not in session:
        flash('Please log in.', 'warning')
        return redirect(url_for('login'))

    for question_key in request.form:
        answer = request.form[question_key]
        new_response = Survey(
            user_id=session['user_id'],
            question=question_key,
            answer=answer
        )
        db.session.add(new_response)

    db.session.commit()
    flash('Survey submitted successfully.', 'success')
    return redirect(url_for('result'))

def calculate_scores(responses: dict):
    e_questions = [k for k in responses if k.startswith('question_e')]
    s_questions = [k for k in responses if k.startswith('question_s')]
    g_questions = [k for k in responses if k.startswith('question_g')]

    def score_section(keys):
        score = 0
        for key in keys:
            answer = responses[key]
            if answer == 'Y':
                score += 1
            elif answer == 'Idontknow':
                score += 0  # 반영 안 하거나 반영 정도 선택 가능
        return round((score / len(keys)) * 100)

    e_score = score_section(e_questions)
    s_score = score_section(s_questions)
    g_score = score_section(g_questions)

    overall = round((e_score + s_score + g_score) / 3)

    return overall, e_score, s_score, g_score

@app.route('/result')
def result():
    if 'user_id' not in session:
        flash('Please log in first.', 'warning')
        return redirect(url_for('login'))

    # DB에서 해당 사용자의 응답 불러오기
    user_id = session['user_id']
    responses_query = Survey.query.filter_by(user_id=user_id).all()

    # 응답 딕셔너리로 변환
    responses = {resp.question: resp.answer for resp in responses_query}

    # 점수 계산
    overall_score, e_score, s_score, g_score = calculate_scores(responses)

    # 결과 페이지에 점수 전달
    return render_template(
        'result.html',
        overall_score=overall_score,
        e_score=e_score,
        s_score=s_score,
        g_score=g_score
    )

# 로그아웃 처리
@app.route('/logout')
def logout():
    session.clear()  # 모든 세션 정보 삭제
    return redirect(url_for('index'))  # 로그아웃 후 메인 페이지로 리다이렉트


# 마지막에 둬야 하는 데 정확히는 모르겠음.
if __name__ == '__main__':
    app.run(debug=True)

