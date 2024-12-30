# Python Docker Container

## Table Of Contents

# Run Python Docker Container

- Define `Dockerfile` in thr root directory with the following contents:

  ```Dockerfile
      # Use an official Python runtime as the base image
      FROM python:3.12.0

      # Set the working directory inside the container
      WORKDIR /app

      # Copy the current directory contents into the container at /app
      COPY . /app

      # Install any needed packages specified in requirements.txt
      RUN pip install -r requirements.txt

      # Define the default command to run when the container starts
      CMD ["python", "app.py"]
  ```

- Where:
  - `FROM:` Specifies the base image, in this case, Python 3.12.0
  - `WORKDIR:` Sets the working directory within the container to `/app`.
  - `COPY:` Copies the local files and directories into the container.
  - `RUN:` Installs Python dependencies defined in `requirements.txt`.
  - `CMD:` Specifies the default command to run the Python application when a container is started.

# Resources and Further Reading
