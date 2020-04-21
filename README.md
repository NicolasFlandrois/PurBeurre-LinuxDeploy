# Pur-Beurre Linux Deployment
OC - Project 10 [Fork of P08]- Deployment of a Django Application on a Linux Server.

![](https://img.shields.io/badge/Python-%3E%3D3.7-yellow.svg)  ![](https://img.shields.io/badge/Django-2.2.8-brightgreen.svg) ![](https://img.shields.io/badge/local%20database-MySQL-blue.svg)

-----------------------

This project offers a plateform for people in need of a snack, but are looking for something healthy.

A quick search can be done from the main page, and the site offers a list of substitutes in the same category, ordered from the best nutriscore to the worst.

If the user created its account and profile, it can also add a product to its favourites.

----------------------

This project is a fork of "Pur Beurre" project (P08), and is managed to be deployed on Linux Cloud Computing plateform.

(Changes from previous Dev project, this fork is the Production project. Continuous Integration is ensured by a TRAVIS CI script. Also the database changed for MySQL. All other aspects of Deployments are not registered here, but on its Linux Server. Deployement used Nginx, Gunicorn, Supervisor, Linux Server Ubuntu 19.10, Postfix, Django and Python 3.7)

----------------------

In order to ease the database update, a custom command has been created.
This command will automatically update the products, checking and avoiding duplicates.

    python manage.py update_snacks

