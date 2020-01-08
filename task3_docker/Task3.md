#   Task 3

****
##  Task 3A
### 1.    Explain the difference between an image and a container
Image consists of layers of changes applied to a base image. A copy of an image is manifested as a container. There can be many containers running the same image.

### 2.    Give some advantages of using containers
Containers are supported by a strong community, have faster development time, low footprint on server, ease of migration, can build image upon another image, version control, and can be used to replace scripts, don’t need the same OS as host.

### 3.    How can security of containers be compromised?
Intrinsic security of kernel and support for namespaces, loopholes in container configuration file, “hardening” security features of kernels and how they interact with others.

### 4.    How is Docker different from Vagrant?
Docker is an open platform for building, shipping and running distributed applications. Provides containers with host machine. Vagrant is used for workflow of development projects. It provisions any machine with a typical virtual machine.


****
##  Task 3B
### 1. Install Docker on your local machine
##### Docker is already installed on the Virtual Machine
For Windows:
- Click on this [link](https://docs.docker.com/v17.09/docker-for-windows/install/#download-docker-for-windows). Select on **Get Docker for Windoes (Stable)**. This is the Windows installer for Docker Desktop (Windows).
- Navigate to your **Downloads** directory (or whichever directory you've downloaded the installer into). Double-click `Docker Desktop Installer.exe`
- Follow the Install Wizard to accept the license, authorise the installer, and proceed with the install.
- Click **Finish** on the setup complete dialog to launch Docker.
- To start Docker, search for **Docker** in the Start Bar and click on the results. When the whale in the status bar, Docker is ready to be accessed from any terminal window.

For Mac:
-   Click on this [link](https://docs.docker.com/v17.09/docker-for-mac/install/). Select on **Get Docker for Mac (Stable)**. This is the installer for Docker Desktop (Mac)
-   Navigate to the directory you've installed Docker in. Double click on `Docker.dmg` to open the installer. Drag the whale to the Applications folder.
-   Doucle click `Docker.app` in Applications to start Docker.
-   You will be asked to authorise Docker with your system password after launching it. Privileged access is needed to install networking components and links to Docker apps.
-   The whale in the status bar will indicate that Docker is running and accessible from a terminal.

### 2. Pull the rocker/rstudio image to your local machine
-   Navigate to the [rocker/rstudio](https://hub.docker.com/r/rocker/rstudio/) page on DockerHub.
-   In a Terminal, type `docker pull rocker/rstudio` to pull the image.

### 3. Create a container for the image
-   Type in the following in your Terminal:
       `docker run --rm -p 8787:8787 -e PASSWORD=yourpasswordhere rocker/rstudio`
-   `docker run`    processes images in isolated containers
-   `--rm`  Clean up. Docker automatically cleans up the container and removes the file system when the container exits
-   `-p 8787:8787` publishes exposed ports to host interfaces
-   `-e` Environment variable. You can set the PASSWORD as any password that you prefer

### 4. Access the application from your browser.
-   In your browser, navigate to [localhost:8787](localhost:8787).
-   Log in with the username `rstudio` and type in the password you've set.
-   You can now access the rocker/rstudio image
-   To end the session, `Ctrl+C` into the Terminal.
-   To stop and remove the container type in `docker ps -a` into the Terminal to list out all containers. Under the `CONTAINER_ID` column, select the container ID of the rocker/rstudio container.
-   In the Terminal, type in `docker container stop CONTAINER_ID` to stop and remove the rocker/rstudio container from your machine.
-   Since we've added the `--rm` flag when building the container, Docker will automatically remove the container once it is stopped. You can check through `docker ps -a` just to be sure. 
****
##  Task 3C
### 1. Set up a docker-compose file for the image in Task 3B
-   In a Terminal, create a new file called `docker-compose.yml`
    For Windows: `New-Item docker-compose.yml` <br />
    For Mac and Ununtu VM: `touch docker-compose.yml`
-   Open `docker-compose.yml` in your favourite text editor and type in the following:
    ```
    #Build image with version 3.7
    version: '3.7'
    services:
        #Uses RStudio as a service
        rstudio:
            environment:
                #Environment Variables (username, password)
                - USER=rstudio
                - PASSWORD=<your_password_here>
            image: rocker/rstudio
            ports:
                - 8787:8787
    ```
-   Save `docker-compose.yml`

### 2. Demonstrate that containers can be started up with docker-compose
-   In a Terminal, navigate to the directory containing the docker-compose file.
-   Build the container using the command line `docker-compose up` in the Terminal
-   Access the container through [localhost:8787](localhost:8787)
-   To end the session `Ctrl+C` into the Terminal
-   To stop the container `docker-compose down` in the Terminal
