#!/bin/bash
if [ -z "$1" ]; then
    VERSION="10.0.59"
else
    VERSION="$1"
fi
VERSIONS=$1
wget https://drive.google.com/drive/folders/1ECZnKQg4r08TyUT9yHPsZMlzuNeLP5e5/penguins-eggs-tarball-${VERSION}-1-linux-x64.tar.gz