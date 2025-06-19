# Use Python base image
FROM python:3.9-alpine

# Set working directory inside container
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Create pdf directory
RUN mkdir -p pdfs

# Expose port
EXPOSE 5003

# Run the application
CMD ["python", "server.py"]
