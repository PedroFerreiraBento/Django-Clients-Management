# Django-Clients-Management

Django Clients Management is a Python system for dealing with clients management.

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#django-clients-management">About The Project</a>
    </li>
    <li>
      <a href="#installation">Installation</a>
      <ul>
        <li><a href="#windows">Windows</a></li>
        <li><a href="#linux">Linux</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>

## Installation

Install the [docker](https://www.docker.com/) and [docker compose](https://docs.docker.com/compose/) to build the container.

- ### Windows:
  
  Download the [Docker Desktop](https://www.docker.com/)
  
- ### Linux:
  
  #### Uninstall old versions
    
    Older versions of Docker went by the names of docker, docker.io, or docker-engine. Uninstall any such older versions before attempting to install a new version:

    ```bash
    sudo apt-get remove docker docker-engine docker.io containerd runc
    ```
    
  ##### Set up the repository
  
  1. Update the apt package index and install packages to allow apt to use a repository over HTTPS:
  
    ```bash
    sudo apt-get update
    sudo apt-get install \
        ca-certificates \
        curl \
        gnupg \
        lsb-release
    ```
    
  2. Add Docker’s official GPG key:
  
    ```bash
    sudo mkdir -p /etc/apt/keyrings
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
    ```
    
  3. Use the following command to set up the repository:
  
    ```bash
    echo \
    "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
    $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    ```
    
  4. Install Docker Engine, containerd, and Docker Compose.
  
    ```bash
    sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin
    ```

## Usage

  1. ### Build the container
  
  ```bash
  docker-compose build
  ```
    
  2. ### Execute the database migrations
    
  ```bash
  docker-compose run web python manage.py migrate
  ```
    
  3. ### Create a super user
  
  ```bash
  docker-compose run web python manage.py createsuperuser
  ```
    
  4. ### Run the container
  
  ```bash
  docker-compose up
  ```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
