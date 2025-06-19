# Use the official MongoDB image
FROM mongo:latest

# Set environment variables (optional)
ENV MONGO_INITDB_ROOT_USERNAME=admin
ENV MONGO_INITDB_ROOT_PASSWORD=admin123
ENV MONGO_INITDB_DATABASE=examdb

# Copy initialization scripts if needed
COPY init-db.js /docker-entrypoint-initdb.d/

# Expose MongoDB default port
EXPOSE 27017