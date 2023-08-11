# Source code của website <a>saugau.com</a>
## 1. Project layout
- <strong>deployment</strong>: Chứa các ansible playbook dùng để deploy lên remote server
- <strong>website_on_thi_dai_hoc</strong> Chứa các API 

Các lệnh chạy 
```
python manage.py runserver
openresty -p `pwd` -c nginx.conf -s reload
uvicorn main:app --reload --port 8001
```
