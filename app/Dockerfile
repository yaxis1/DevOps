# Step 1: Import the Os
from ubuntu:latest

# Step 2: Install pip, Python, uwsgi 
RUN apt-get update && apt-get install -y --no-install-recommends \
#    gnupg2\
    python3.5 \
    python3-pip \
    uwsgi \
	gunicorn \
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Step 4: Create a Work Directory
WORKDIR /app

# Step 5: copy all Project Files
COPY . /app

# Step 3: Install the requirements
RUN pip3 install -r requirements.txt 

# Step 6:  run the command to start uWSGI
CMD ["uwsgi", "app.ini"]

# Step 7:  run the command to start gunicorn
#CMD ["gunicorn", "-w","2", "run:app"]