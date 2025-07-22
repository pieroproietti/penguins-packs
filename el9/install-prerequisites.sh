#!/bin/bash
echo "Adding epel-release..."
sudo dnf install epel-release -y
sudo dnf config-manager --set-enabled crb
echo "Adding rpm.nodesource.com... "
curl -fsSL https://rpm.nodesource.com/setup_20.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
rm nodesource_setup.sh
sudo dnf check-update
