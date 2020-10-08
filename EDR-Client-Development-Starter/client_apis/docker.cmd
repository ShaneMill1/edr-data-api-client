docker build -t edr-client .
docker run -d -p 5000:80 edr-client
