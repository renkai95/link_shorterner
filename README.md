# link_shortener

Intro:
-------
 - Simple link shortener that will return a shortened link
 - If called with the shortened link, server will redirect to the provided link
 - App contains a nginx reverse proxy, an api layer and a database

![Architecture diagram](./docs/architecture_diagram.png)


### Running app

  ```make start``` to bring the containers up

 Call ```172.16.238.20:80``` to get a simple frontend text box to enter the link

 Call ```172.16.238.20:80/<generated_link>``` to get the link redirect



  ```make stop``` to stop the containers

  ```make clean``` to clear all images and remove any existing networks

   ```make test``` to run unit tests
