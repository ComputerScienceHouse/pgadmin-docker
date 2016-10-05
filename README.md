# pgAdmin Docker Image

This repository serves as the automated build repository for the [computersciencehouse/pgadmin](https://hub.docker.com/r/computersciencehouse/pgadmin) Docker image.

For more information about pgAdmin, [visit their website](https://www.pgadmin.org/).

# Usage

This image expects a number of environment variables to be set.

###### Required
* PGADMIN\_SETUP\_EMAIL - Initial administrative user email
* PGADMIN\_SETUP\_PASSWORD - Password for the initial administrative user

###### Recommended
* PGADMIN\_CSRF\_SESSION\_KEY
* PGADMIN\_SECRET\_KEY
* PGADMIN\_PASSWORD\_SALT
* PGADMIN\_MAIL\_SERVER
* PGADMIN\_MAIL\_PORT
* PGADMIN\_MAIL\_USE\_SSL
* PGADMIN\_MAIL\_USE\_TLS
* PGADMIN\_MAIL\_USERNAME
* PGADMIN\_MAIL\_PASSWORD

###### Optional
* PGADMIN\_APP\_NAME
* PGADMIN\_APP\_ICON
* PGADMIN\_SERVER\_IP
* PGADMIN\_SERVER\_PORT

