# Basic LAMP Stack

## Building The Image
```bash
docker build -t lamp-server .
```

## Running Container as Development Environment
```bash
docker run -d -p 8080:80 -v ./static:/var/www/html --name lamp-development lamp-server
```

### Access SQL Shell In Devlopment Environment
```bash
docker exec -it lamp-development mysql
```

## Running Container as Deployment
Always make sure to rebuild the image before running as deployment to apply changes from any files.
```bash
docker run -d -p 8081:80 --name lamp-deployment lamp-server
```