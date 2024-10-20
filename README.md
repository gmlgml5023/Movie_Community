# Movie_Community

## 프로젝트 개요
- 커뮤니티 웹서비스의 모델 관계 및 인증 시스템 구성 단계
- 영화 데이터의 생성, 조회, 수정, 삭제가 가능한 애플리케이션
- 로그인, 로그아웃, 회원가입이 가능한 애플리케이션
- 영화, 댓글, 회원간의 모델 관계가 형성된 애플리케이션

## 개발도구
- Visual Studio Code
- Google Chrome
- Django 4.2.11


# 초기 설정
- git clone
- 가상환경 생성 : `python -m venv venv`
- 가상환경 실행 on : `source venv/Scripts/activate`
- 라이브러리 설치 : `pip install -r requirements.txt`
- 설계도생성 및 이식 : `python manage.py makemigrations`, `python manage.py migrate`
- dumpdata 로드 : `python manage.py loaddata users.json movies.json comments.json`
- dumpdata 저장
  - `python -Xutf8 manage.py dumpdata --indent 4 movies.movie > movies.json`
  - `python -Xutf8 manage.py dumpdata --indent 4 movies.comment > comments.json`
  - `python -Xutf8 manage.py dumpdata --indent 4 accounts.user > users.json`

# workflow
- models (accounts, movies, ) 설계
- forms.py (movies, ) 작성
- base templates 작성
  - Bootstrap ㅇ
  - navigator ㅇ
- applications
  - accounts
    - login
    - logout
    - signup
    - update
    - delete
    - change_password
    - profile
    - follow
  - movies
    - index ㅇ
    - create ㅇ
    - detail ㅇ
    - update ㅇ
    - delete ㅇ
    - comments_create ㅇ
    - comments_delete ㅇ
    - likes ㅇ
  - dumpdata 생성
  - 


  # 에러사항
  - 로그인 후 에러
  