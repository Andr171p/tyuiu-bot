#!/bin/sh
envsubst '${SERVER_IP} ${WEBHOOK_PATH}' < /etc/nginx/templates/nginx.conf.template > /etc/nginx/conf.d/default.conf
exec nginx -g 'daemon off;'