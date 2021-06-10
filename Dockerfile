# we want containers
# containers are isolated processes
# to create a container, you need a container image, 
#   aka Docker image, aka image
#   the image will have the data needed to create the container
#       especially the initial state of the filesystem
# containers are ephemeral (arguably), created and destroyed as needed
#   they are a copy of a running program
# images are immutable, they are more reusable and permanent
#   images are used to make new containers
# Think of the image as an exe file and the container as an active process
# to create an image you build a Dockerfile
#   like recipe/instruction to build an image layer-by-layer
#       the instructions themselves are run in a container for that purpose

# step 1 of any Dockerfile: select base image for the build
#   generally download a base image from a docker registry
#       Docker Hub: hub.docker.com; docker.io
#   choosing a base image: consider...
#       1) needed dependencies already included as much as possible
#       2) officially supported/well-maintained with updates, etc.
#           - tag of an image can recieve new images to update it
#

# becaus we picked the "3" tag, it will eventually point to the newest
# version of python3 when it gets added to the base image associated with the tag
FROM python:3

# two most common commands:
#   COPY: copy files from outside the image into the image
#   RUN:  run a shell command inside the image
#       e.g., install something with apt

WORKDIR /app

COPY requirements.txt *.py ./
RUN apt update && \
    apt install nano

RUN python3.9 -m venv venv
RUN venv/bin/python3.9 -m pip install -r requirements.txt

# RUN commands executes when the image is being built

# CMD lines set the default startup executable when you run the container
CMD ["venv/bin/python3.9", "-m", "AssetManagement"]
# each CMD argument as a separate entitiy in the array structure

# when you run 'docker build', the first argument is the 'build context'
# the first thing that happens is to upload the build context, then go line-by-line
# the Default location for a Dockerfile is <build contex>/Dockerfile
#   can override with -f option

# this will copy the entire buid context directory into the container
COPY . ./
# don't copy extra things into the container; don't pollute the container
# use '.dockerignore' to ignore things from the build context
# putting it last here helps the build use more cached portions before getting to the changes


RUN bash write_test.sh >> setup_log.txt \
    && bash copy_test.sh >> setup_log.txt\
    && bash append_test.sh >> setup_log.txt