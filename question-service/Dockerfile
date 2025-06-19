# Use Python 3.9 as base image
FROM python:3.9-alpine

# Set working directory
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . .

# Set environment variables
ENV MONGO_URI=mongodb://admin:admin123@mongodb:27017/examdb?authSource=admin

# Expose port 5001 for the service
EXPOSE 5001

# Run the Flask app
CMD ["python", "server.py"]
