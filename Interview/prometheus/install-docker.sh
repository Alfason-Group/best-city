#!/bin/bash

echo "Updating system packages..."
if [ -f /etc/system-release ] && grep -q "Amazon Linux 2" /etc/system-release; then
    sudo yum update -y >/dev/null 2>&1
else
    sudo dnf update -y >/dev/null 2>&1
fi

echo "Installing Docker..."
if [ -f /etc/system-release ] && grep -q "Amazon Linux 2" /etc/system-release; then
    sudo amazon-linux-extras install docker -y >/dev/null 2>&1
else
    sudo dnf install docker -y >/dev/null 2>&1
fi

echo "Starting Docker service..."
sudo systemctl start docker >/dev/null 2>&1

echo "Enabling Docker service on boot..."
sudo systemctl enable docker >/dev/null 2>&1

echo "Adding current user to docker group..."
sudo usermod -aG docker $USER >/dev/null 2>&1
newgrp docker

echo "Docker installation completed."

sudo curl -L https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose