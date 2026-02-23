# Use an official Node.js runtime as a parent image
FROM node:20-alpine

# Set work directory
WORKDIR /app/health_front

# Copy package.json and package-lock.json to install dependencies
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code
COPY . .

# Expose port
EXPOSE 3000

# Start the development server
CMD ["npm", "start"]
