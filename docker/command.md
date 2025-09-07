

# Update system
  sudo apt update -y
  sudo apt upgrade -y

# Install dependencies
  sudo apt install apt-transport-https ca-certificates curl software-properties-common -y

# Add Docker GPG key
  curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/docker.gpg

# Add Docker repository
  sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"

# Install Docker Engine
  sudo apt update -y
  sudo apt install docker-ce docker-ce-cli containerd.io -y

# Start & Enable Docker
  sudo systemctl start docker
  sudo systemctl enable docker

# Allow Docker without sudo (optional)
  sudo usermod -aG docker $USER
  newgrp docker

# Verify installation
  docker --version
  docker run hello-world
