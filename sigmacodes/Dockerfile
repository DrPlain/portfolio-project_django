# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Expose the port that the application will listen on
EXPOSE 8000

RUN source .DJANGO_SECRET_KEY

# Set the command to run when the container starts
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

