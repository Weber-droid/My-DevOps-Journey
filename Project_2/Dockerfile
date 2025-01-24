FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /my_flask_app

# Copy the requirements file to the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the container
COPY ./my_flask_app /my_flask_app

# Expose the application port
EXPOSE 5000

# Set the Flask environment variable
ENV FLASK_APP=app.py

# Run the Flask app
CMD ["flask", "run", "--host=0.0.0.0"]
