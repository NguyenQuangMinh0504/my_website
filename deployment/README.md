# Hướng dẫn deploy code lên server
## 1. Thay IP trong file hosts.ini bằng public IP của server
## 2. Cài đặt các package cần thiết
````
ansible-playbook -i hosts.ini install_necessary.ansible.yaml
````
### Các package tải
- git: Clone repo từ github về server
- python3-mysqldb: Dùng bởi MySQL collection ansible
- lsof: Check port
- python3-venv, virtualenv: Set up python virtual environment
- openresty: Webserver
- python3-pip: Dùng để tải các package qua pip
## 3. Update code lên server bằng github
````
ansible-playbook -i hosts.ini synchronize_code.ansible.yaml
````
Clone code từ repo về folder `/opt/my_website/`
## 4. Chạy webserver
````
ansible-playbook -i hosts.ini run_server.ansible.yaml
````
Tạo thư mục chứa log rồi chạy Openresty web server với file config trong folder github `web_server`
## 5. Chạy Gunicorn server
````
ansible-playbook -i hosts.ini run_django_application.ansible.yaml
````
Tạo python virtual environment rồi chạy gunicorn server