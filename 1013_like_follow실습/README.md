### 1. 가상환경 생성 

```bash
$ python -m venv venv
```

### 2. 가상환경 활성화

```bash
$ source venv/Scripts/activate # Windows
$ source venv/bin/activate # Mac
```

### 3. 가상환경 비활성화

```bash
$ deactivate
```

### 4. requirements.txt 목록 설치

```bash
$ pip install -r requirements.txt
```

### 5. django 애플리케이션 생성

```bash
$ python manage.py startapp articles
# 1. INSTALLED_APPS에 앱을 등록
# 2. urls.py에 path 등록
# 3. views.py에 함수 생성
# 4. template 생성
```

### 6. django 서버 실행

```bash
$ python manage.py runserver
```