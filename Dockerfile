#Base image
FROM python:3.7-buster

#Prepare environment
RUN apt-get update && apt-get install -y pandoc
RUN pip install jupyter

#Add the script file
ADD ipymd.py /

#Execute the script file
ENTRYPOINT ["python", "./ipymd.py"]