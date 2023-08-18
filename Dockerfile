FROM --platform=$BUILDPLATFORM python:3.11
EXPOSE 8000
WORKDIR /app
COPY ./django_my_website/requirements.txt /app
RUN pip3 install -r requirements.txt --no-cache-dir
COPY ./django_my_website /app/
ENTRYPOINT ["python3"]
CMD ["manage.py", "runserver", "0.0.0.0:8000"]