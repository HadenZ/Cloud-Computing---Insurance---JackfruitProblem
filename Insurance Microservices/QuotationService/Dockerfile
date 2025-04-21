# Use the official Python image
FROM python:3.10

# Set working directory inside the container
WORKDIR /app

# Copy requirements first (helps Docker cache dependencies)
COPY app/requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the FastAPI app code into the container
COPY app/ app/

# Copy the .env file for environment variables
COPY .env .

# Expose port for FastAPI
EXPOSE 8000

# Run the app using Uvicorn with reload
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
