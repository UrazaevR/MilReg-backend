# Use an official, lightweight Python runtime as a parent image
FROM python:latest

# Set the working directory in the container
WORKDIR /app

# Set environment variables to optimize Python behavior
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Copy only the requirements file first to leverage Docker cache
COPY ./requirements.txt .

# Install dependencies without storing pip cache to keep image small
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port FastAPI runs on
EXPOSE 8000

# Start Uvicorn, binding to 0.0.0.0 so external traffic can reach it
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
