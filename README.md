# Source code của website <a>saugau.com</a>
## 1. Project layout
- <strong>deployment</strong>: Chứa các ansible playbook dùng để deploy lên remote server
- <strong>django_my_website</strong> Chứa code website viết bằng framework Django, tạo bằng lệnh `django-admin start project django_my_website`
- web_server: Chứa file config NGINX webserver và thư mục certs website.
- databases: Chứa các file backup database và ảnh cấu trúc db.
## 2. Cấu trúc website
NGINX/Openresty -> Gunicorn -> Django web application
## 3. Chạy development server
### Cách 1: Dùng Docker
```
docker compose up
```
### Cách 2: Không dùng Docker
- Tạo virtual environment
```
python3 -m venv ./venv
source venv/bin/activate
pip3 install -r django_my_website/requirements.txt
```
- Import database
```
mysql -u root -p < databases/all_data.sql
```
- Chạy development server
```
cd django_my_website
python manage.py runserver
```