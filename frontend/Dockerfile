# Step 1: Build the React App
FROM node:18-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# Step 2: Serve with Nginx
FROM nginx:alpine
COPY --from=builder /app/build /usr/share/nginx/html

# Expose port 80 (default for Nginx)
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
