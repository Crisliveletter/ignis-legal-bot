FROM rasa/rasa:3.6.0-full
WORKDIR /app
COPY . /app
COPY models /app/models
EXPOSE 5005
CMD ["run", "--enable-api", "--cors", "*"]
