# Use official Python image as base
FROM python:3.9-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy the service files into the container
COPY . .

# Install required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the service runs on
EXPOSE 5002

# Run the Flask application
CMD ["python", "server.py"]
