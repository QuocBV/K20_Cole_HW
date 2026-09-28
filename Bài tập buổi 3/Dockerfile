FROM python:3.11-slim

WORKDIR /workspace

# Cài các thư viện cần thiết
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Tạo thư mục làm việc
RUN mkdir -p /workspace/notebooks /workspace/data/input /workspace/data/output

EXPOSE 8888

CMD ["jupyter", "notebook", \
     "--ip=0.0.0.0", \
     "--port=8888", \
     "--no-browser", \
     "--allow-root", \
     "--NotebookApp.token=''", \
     "--NotebookApp.password=''", \
     "--notebook-dir=/workspace"]
