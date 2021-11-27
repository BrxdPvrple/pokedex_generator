FROM mysql:5.7

ENV MYSQL_ROOT_PASSWORD=password MYSQL_DATABASE=favourites

COPY CreateTable.sql /docker-entrypoint-initdb.d
