FROM openjdk:8

# Defining MYSQL_URL
ARG MYSQL_URL=jdbc:mysql://localhost/petclinic
ENV MYSQL_URL $MYSQL_URL

# Get sources
RUN mkdir /app
RUN git clone https://github.com/spring-projects/spring-petclinic.git /app/petclinic
WORKDIR /app/petclinic
RUN sed -ic 's/database=h2/database=mysql/g' src/main/resources/application.properties
RUN echo 'spring.profiles.active=mysql' >> src/main/resources/application.properties
# Expose App on port 8080
EXPOSE 8080

# Starting app
CMD ./mvnw spring-boot:run
