# 0x09. Web infrastructure design

## File 0:
* [0-simple_web_stack](./0-simple_web_stack) - one server web infrastructure that hosts the website that is reachable via www.foobar.com.
* 1 server
* 1 web server (Nginx)
* 1 application server
* 1 application files (your code base)
* 1 database (MySQL)
* 1 domain name foobar.com configured with a www record that points to your server IP 8.8.8.8

## File 1: 
* [1-distributed_web_infrastructure](./1-distributed_web_infrastructure) - a three server web infrastructure that hosts the website www.foobar.com.
* 2 servers
* 1 web server (Nginx)
* 1 application server
* 1 load-balancer (HAproxy)
* 1 set of application files (your code base)
* 1 database (MySQL)

## File 2:
* [2-secured_and_monitored_web_infrastructure](./2-secured_and_monitored_web_infrastructure) - a three server web infrastructure that hosts the website www.foobar.com, it must be secured, serve encrypted traffic, and be monitored.
* 3 firewalls
* 1 SSL certificate to serve www.foobar.com over HTTPS
* 3 monitoring clients (data collector for Sumologic or other monitoring services)

## File 3:
* [3-scale_up](./3-scale_up) - [Application server vs web server](https://alx-intranet.hbtn.io/rltoken/toFi_SdFHyi2MaELB8ekqw)
* 1 server
* 1 load-balancer (HAproxy) configured as cluster with the other one
* Split components (web server, application server, database) with their own server
