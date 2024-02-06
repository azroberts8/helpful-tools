# Basic LAMP Stack

This template is for quickly prototyping and deploying basic LAMP (Linux, Apache, MariaDB, PHP) stack projects. This template **is not** intended for use in real world applications but rather small scale development and testing cases such as hackathon projects and CTF problems.

## Usage
This image can be ran as a development environment or a deployment server. When you build the image it takes a snapshot of the contents in the `setup` and `static` directories. Any changes made in these directories after the image is built will not be reflected when the container is run in deployment. When running as development, changes made in the `static` directory will be available automatically without rebuilding the image or restarting the container.

`setup/` - contains shell scripts and SQL files for setting up the databases and tables and populating them with data.
`static/` - contains all web content to be hosted including html files, php files, images, scripts, and stylesheets.

### Building The Image
```bash
docker build -t lamp-server .
```

### Running Container as Development Environment
```bash
docker run -d -p 8080:80 -v ./static:/var/www/html --name lamp-dev lamp-server
```

#### Access SQL Shell In Devlopment Environment
```bash
docker exec -it lamp-dev mysql
```

### Running Container as Deployment
Always make sure to rebuild the image before running as deployment to apply changes from any files.
```bash
docker run -d -p 8081:80 --name lamp-deploy lamp-server
```