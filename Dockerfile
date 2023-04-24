FROM python

COPY ./app /app

RUN pip install -r app/requirements.txt

# RUN uvicorn app.main:app --reload --port 8000

EXPOSE 8000

CMD ["uvicorn", "app.main:app" , "--host", "0.0.0.0", "--port", "8000"]
