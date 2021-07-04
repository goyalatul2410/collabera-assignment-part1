FROM python:3

RUN pip3 install requests

RUN mkdir /app
WORKDIR /app
COPY . .

CMD ["get_mac_details.py"]

ENTRYPOINT ["python3"]