FROM eclipse-temurin:17-jdk

WORKDIR /app

COPY Application.java .

RUN javac Application.java

EXPOSE 8080

CMD ["java", "Application"]
