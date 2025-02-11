# Use a base Python image
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /apps

# Copy the application files into the container
COPY . /apps

# Install dependencies
RUN pip install --no-cache-dir -r requirements

# Set environment variables (optional, you can use GitHub secrets)
# ENV SUBSCRIPTION_KEY <your_subscription_key>

# Command to run the application
CMD ["python", "oagflightinfo.py"]
