# RHEL/ROCKY

```
sudo dnf install \
    gcc-c++ \
    make \
    rpm-build \
    rpmdevtools
```


## setxkbmap
```
sudo dnf install setxkbmap
```

### epel
We need to enable epel
```
sudo dnf install epel-release -y
```

### nodesource
We need node >18:

```
curl -fsSL https://rpm.nodesource.com/setup_22.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo dnf install -y nodejs
```

