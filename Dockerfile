# Use an official Python runtime environment
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy dependencies first to use Docker caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY app.py .

# Expose the network port the app runs on
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
