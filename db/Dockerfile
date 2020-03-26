FROM postgres

EXPOSE 5430

COPY ./datasets/winequality.csv /

ADD ./db-init/ /docker-entrypoint-initdb.d/