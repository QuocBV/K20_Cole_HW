FROM python:3-slim

WORKDIR /app

# Copy file dependency trước để tận dụng cache
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy toàn bộ mã nguồn
COPY . .

# Expose port Flask
EXPOSE 5000

CMD ["python", "app.py"]
