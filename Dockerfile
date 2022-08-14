FROM python

WORKDIR /usr/src/
ENV PYTHONPATH=/usr/src

COPY . /usr/src

RUN pip install -r requirements.txt