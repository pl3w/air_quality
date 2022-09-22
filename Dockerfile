FROM python:3.9

RUN mkdir /api

COPY /src/fastapi_demo /api/

WORKDIR /api/

RUN pip install --no-cache-dir --upgrade -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]