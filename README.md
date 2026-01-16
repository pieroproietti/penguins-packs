# penguins-packs

This repository started as `penguins-eggs-pkgbuilds` and included package creation for Arch and Manjaro. Later the package creation for AlpineLinux was included, finally the rpm packages for AlmaLinux/Rock, fedora, Openmamba and OpenSuSE were included.

There is no need to use this repository for the creation of DEB packages, which is done directly from penguins-eggs sources, using the command: `pnpm deb`

## AlmaLinux/RockyLinux (RPM)
* `cd el9/penguins-eggs`
* `./clean|./build`

## Alpine Linux (APK)
* See: [penguins-alpine](https://github.com/pieroproietti/penguins-alpine).

## ArchLinux [aur] (PKGBUILD)
* `cd aur/penguins/eggs`
* `./clean|./build`

[calamares](./aur/calamares)
* `cd aur/calamares`
* `./clean|./build`

#### Instructions
[Publish package to AUR](./PUBLISH.md), link to 
[penguins-eggs on AUR](https://aur.archlinux.org/packages/penguins-eggs)

## Fedora  (RPM)
* `cd fedora/penguins-eggs`
* `./clean|./build`

## Manjaro (PKGBUILD)
* `cd manjaro/penguins-eggs`
* `./clean|./build`

[penguins-eggs on Manjaro community](https://gitlab.manjaro.org/packages/community/penguins-eggs)

## Openmamba (RPM)
* `cd openmamba/penguins-eggs`
* `./c|./d|./b`