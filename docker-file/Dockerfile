# ---------- Stage 1: Build ----------
FROM python:3.10-slim AS builder

WORKDIR /app

# Install dependencies into a separate folder
RUN pip install --no-cache-dir flask --target /app/deps

# Copy app source
COPY app.py .

# ---------- Stage 2: Runtime ----------
FROM python:3.10-slim

WORKDIR /app

# Copy only what is needed from builder stage
COPY --from=builder /app/deps /usr/local/lib/python3.10/site-packages
COPY --from=builder /app/app.py .

EXPOSE 5000

CMD ["python", "app.py"]
