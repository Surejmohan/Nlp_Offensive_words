FROM python:3.6 as intermediate

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install wheel
RUN pip install -r requirements.txt
RUN pip3 install torch --extra-index-url https://download.pytorch.org/whl/cpu --no-cache-dir

FROM python:3.6

# copy the python packages from the intermediate image
COPY --from=intermediate /usr/local/lib/python3.6/site-packages/ /usr/local/lib/python3.6/site-packages/
ENV PYTHONUNBUFFERED 1

WORKDIR /src

COPY . .

EXPOSE 5000

CMD ["python3", "./app.py"]
