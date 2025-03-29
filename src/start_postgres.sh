#!/bin/bash

# Configurable variables
CONTAINER_NAME="local-postgres"
POSTGRES_USER="myuser"
POSTGRES_PASSWORD="mypassword"
POSTGRES_DB="mydb"
HOST_PORT=5432
IMAGE="postgres:latest"

find . -name "__pycache__" -exec rm -rf {} +
find . -name "*.pyc" -delete
echo "✅ all pycache remove"

# Check if container already exists
if [ "$(docker ps -aq -f name=$CONTAINER_NAME)" ]; then
    echo "Stopping and removing existing container: $CONTAINER_NAME"
    docker stop $CONTAINER_NAME
    docker rm $CONTAINER_NAME
fi

# Pull latest PostgreSQL image
echo "Pulling PostgreSQL Docker image..."   
docker pull $IMAGE

# Run the container
echo "Starting PostgreSQL Docker container..."
docker run -d \
    --name $CONTAINER_NAME \
    -e POSTGRES_USER=$POSTGRES_USER \
    -e POSTGRES_PASSWORD=$POSTGRES_PASSWORD \
    -e POSTGRES_DB=$POSTGRES_DB \
    -p $HOST_PORT:5432 \
    $IMAGE

# Wait for Postgres to be ready
echo "Waiting for PostgreSQL to be ready..."
until docker exec $CONTAINER_NAME pg_isready -U $POSTGRES_USER > /dev/null 2>&1; do
    sleep 1
done

echo "✅ PostgreSQL is up and ready on localhost:$HOST_PORT"
