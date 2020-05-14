FROM python:3

WORKDIR /usr/src/app

ENV DB_HOST=localhost
ENV DB_USER=root
ENV DB_PASSWORD=root
ENV TELEGRAM_TOKEN=00000000000000000000000
# ENV env_var_host=$DB_HOST
# ENV env_var_user=$DB_USER
# ENV env_var_password=$DB_PASSWORD
# ENV env_var_token=$TELEGRAM_TOKEN
COPY . /usr/src/app
RUN pip install --no-cache-dir -r requirements.txt


CMD [ "python", "./start.py" ]