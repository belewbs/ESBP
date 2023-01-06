From python:3.10
COPY requirements.txt app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
ADD . /app
CMD ["python","/app/bot.py"]
