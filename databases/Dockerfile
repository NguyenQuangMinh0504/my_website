FROM --platform=$BUILDPLATFORM mysql:latest
ENV MYSQL_ROOT_PASSWORD=qmqmqm8c3
COPY ./all_data.sql /docker-entrypoint-initdb.d/
CMD ["mysqld"]