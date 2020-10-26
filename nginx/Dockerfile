FROM api-container:latest as api
FROM nginx:latest

USER root

COPY nginx.conf /etc/nginx/nginx.conf
COPY my_nginx.conf /etc/nginx/sites-available/

RUN mkdir -p /etc/nginx/sites-enabled/ \
&&  ln -s /etc/nginx/sites-available/my_nginx.conf /etc/nginx/sites-enabled/

# RUN mkdir -p /etc/nginx/sites-enabled/ \
#     && ln -s /etc/nginx/sites-available/my_nginx.conf /etc/nginx/sites-enabled/ \
#     && rm /etc/nginx/conf.d/default.conf

COPY --from=api /docker_api/static /var/www/static

CMD ["nginx", "-g", "daemon off;"]
