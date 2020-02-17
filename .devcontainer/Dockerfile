FROM python:3.7.6
ARG requirementsFile=src/requirements.txt

# This Dockerfile adds a non-root user with sudo access. Use the "remoteUser"
# property in devcontainer.json to use it. On Linux, the container user's GID/UIDs
# will be updated to match your local UID/GID (when using the dockerFile property).
# See https://aka.ms/vscode-remote/containers/non-root-user for details.
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN apt-get -y update && apt-get install -y apt-utils software-properties-common

# Configure apt and install packages
RUN apt-get -y update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        libmagic-dev \
        libxml2-utils \
        curl \
        sqlite3 \
        ffmpeg \
        netcat \
        git iproute2 procps lsb-release \
        gettext \
        dialog \
    # Clean up
    && apt-get autoremove -y \
    && apt-get clean -y
RUN curl -sL https://deb.nodesource.com/setup_12.x | bash -
#RUN apt-get install nodejs
#RUN npm install -g mjml@^4.2.1

# Create a non-root user to use if preferred - see https://aka.ms/vscode-remote/containers/non-root-user.
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd -s /bin/bash --uid $USER_UID --gid $USER_GID -m $USERNAME \
    # [Optional] Add sudo support for the non-root user
    && apt-get install -y sudo \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME\
    && chmod 0440 /etc/sudoers.d/$USERNAME

# Make python3 default
# RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.7 100

COPY $requirementsFile /tmp/req.txt
RUN pip install --requirement /tmp/req.txt && rm /tmp/req.txt
