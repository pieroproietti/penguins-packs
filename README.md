# penguins-packs

This repository contains instructions for creating penguins-eggs packages for different distros:
- Alpine Linux (APK)
- AlmaLinux/RockyLinux (RPM)
- ArchLinux (PKGBUILD)
- Fedora (RPM)
- Manjaro (PKGBUILD)
- Openmamba (RPM)
- OpenSuSE (RPM)

It is not necessary to use this repository for package creation (DEB), which is performed directly from the penguins-eggs sources using the command: `pnpm deb`


## AlmaLinux/RockyLinux (RPM)
* `cd el9/penguins-eggs`
* `./clean|./build`

## Alpine Linux (APK)
* See: [penguins-alpine](https://github.com/pieroproietti/penguins-alpine).

## ArchLinux [aur] (PKGBUILD)
[penguins-eggs](./aur/penguins-eggs)
* `cd aur/penguins-eggs`
* `./clean|./build`

[calamares](./aur/calamares)
* `cd aur/calamares`
* `./clean|./build`

[ckbcomp](./aur/ckbcomp)
* `cd aur/ckbcomp`
* `./build`

#### Instructions
[Publish package to AUR](./PUBLISH.md), link to 
[penguins-eggs on AUR](https://aur.archlinux.org/packages/penguins-eggs)

## Fedora (RPM)
* `cd fedora/penguins-eggs`
* `./clean|./build`

## Manjaro (PKGBUILD)
* `cd manjaro/penguins-eggs`
* `./clean|./build`

[penguins-eggs on Manjaro community](https://gitlab.manjaro.org/packages/community/penguins-eggs)

## Openmamba (RPM)
* `cd openmamba/penguins-eggs`
* `./clean|./download|./build`

## OpenSuSE (RPM)
[penguins-eggs](./opensuse/penguins-eggs)
* `cd opensuse/penguins-eggs`
* `./clean|./download|./build`

[calamares](./opensuse/calamares)
* `cd opensuse/calamares`
* `./download|./build`

# Copyright and licenses

Copyright (c) 2017, 2026
[Piero Proietti](https://penguins-eggs.net/about-me.html), dual licensed under
the MIT or GPL Version 2 licenses.
