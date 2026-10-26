# start with a lightweight python image
# This gives our conatiner a python runtime
FROM python:3.14-slim

# set the working diectory inside the conatiner
WORKDIR /app

# copy the dependency list before copying application code
COPY requirement.txt .

# Avoid retaining pip's download cache in the image
RUN pip install --no-cache-dir -r requirement.txt


# copy the application code aand saved model into app
COPY . .

# document the port used by FastAPI applicaiotn
EXPOSE 8000


# start the api server when the conatiner launches
# 0.0.0.0 allows connections throught the conatiner's network interface
CMD ["uvicorn","main:app","--host","0.0.0.0","--port","8000"]


