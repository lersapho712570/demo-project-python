FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN apt update && apt install -y libpq-dev python3-dev

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 31000 8080

CMD [ "python", "./userapp.py" ]
