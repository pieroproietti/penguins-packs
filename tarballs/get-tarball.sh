#!/bin/bash
if [ -z "$1" ]; then
    VERSION="10.0.59"
else
    VERSION="$1"
fi
VERSIONS=$1
#wget https://penguins-eggs.net/basket/index.php?p=packages%2Ftarballs&get=penguins-eggs-tarball-1${VERSION}-linux-x64.tar.gz
wget https://penguins-eggs.net/basket/packages/tarballs/penguins-eggs-tarball-10.0.59-1-linux-x64.tar.gz
