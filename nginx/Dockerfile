FROM nginx:alpine

RUN apk add --no-cache bash
COPY templates/nginx.conf.template /etc/nginx/templates/
COPY ./init-nginx.sh /docker-entrypoint.d/

RUN chmod +x /docker-entrypoint.d/init-nginx.sh