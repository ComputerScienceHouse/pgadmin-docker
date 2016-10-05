# pgadmin-docker
FROM centos:7
MAINTAINER Steven Mirabito (smirabito@csh.rit.edu)

# Install required packages
RUN yum -y install https://download.postgresql.org/pub/repos/yum/9.6/redhat/rhel-7-x86_64/pgdg-centos96-9.6-3.noarch.rpm && \
yum -y install epel-release && \
yum -y update && \
yum -y install pgadmin4 python-gunicorn

# Copy config file and run script into the container
COPY config_local.py run.sh /usr/lib/python2.7/site-packages/pgadmin4-web/
RUN chmod +x /usr/lib/python2.7/site-packages/pgadmin4-web/run.sh

# Create the application user and drop privileges
RUN useradd -r -d /var/lib/pgadmin -s /sbin/nologin -c "pgAdmin" pgadmin && \
mkdir -p /var/lib/pgadmin && \
chown -R pgadmin:pgadmin /var/lib/pgadmin
USER pgadmin

# Set the working directory to the pgadmin4-web root
WORKDIR /usr/lib/python2.7/site-packages/pgadmin4-web

# Run the application
CMD ./run.sh

