# Use an official Python runtime as a parent image
FROM ubuntu:latest

RUN apt-get update && apt-get install -y nginx python3

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .
COPY sigmacodes.tech.config /etc/nginx/sites-avaialable/sigmacodes.tech.config
RUN ln -s /etc/nginx/sites-available/sigmacodes.tech.config /etc/nginx/sites-enabled/sigmacodes.tech.config
# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

ENV SECRET_KEY=b7a436bc0a0b2ab30b1065cf586368635660156f994067b4c2f17ca6aba79399e066296b00c0a6134b7105bca3f894ccad08
RUN gunicorn -c gunicorn.config.py
RUN serive nginx start
# Expose the port that the application will listen on
EXPOSE 80



# Set the command to run when the container starts
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

