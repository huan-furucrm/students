1. Cấu trúc ban đầu:
bookstore:
    Dockerfile
    requirement.txt
    docker-compose.yml
    README.md
2. Khởi tạo project
    docker-compose run web django-admin startproject bookstore_project .
3. Cấu trúc project sau khi thực hiện lệnh ở trên:
bookstore:
    bookstore_project:
        __init__.py
        asgi.py
        settings.py
        urls.py
        wsgi.py
    db.sqlite3
    docker-compose.yml
    Dockerfile
    manage.py
    README.md
    requirements.txt
4. Thực hiện chạy project
    docker-compose up
    Sau khi chạy lệnh có thể truy cập thông qua địa chỉ: http://localhost:8000

# Project Setup

## 1. Initial Structure

📂 __bookstore/__

- 📄 `Dockerfile`
- 📄 `requirement.txt`
- 📄 `docker-compose.yml`
- 📄 `README.md`

## 2. Initialize Project

Run the following command to start a Django project:

```bash
docker-compose run web django-admin startproject bookstore_project .
```

## 3. Cấu trúc project sau khi thực hiện lệnh ở trên:
📂 __bookstore/__

   📂 __bookstore_project/__

   📄 `__init__.py`
   📄 `asgi.py.txt`
📄 `docker-compose.yml`
📄 `README.md`
