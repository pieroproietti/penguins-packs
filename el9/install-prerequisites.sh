echo "Adding epel-release..."
sudo dnf install epel-release -y
dnf config-manager --set-enabled crb
dnf -y update
dnf config-manager --set-enabled crb
echo "Adding rpm.nodesource.com... "
curl -fsSL https://rpm.nodesource.com/setup_20.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh


