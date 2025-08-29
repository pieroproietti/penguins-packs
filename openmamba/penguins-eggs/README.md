# penguins-eggs

```
sudo dnf install rpm-build gcc-c++ pnpm
```

il percorso è /usr/src/RPM

```
rpm --eval '%_topdir'
rpm --eval '%_sourcedir'
rpm --eval '%_download_cmd'
```


# creare patch
```
git format-patch -2 HEAD
```

# applicare patch
cp 0* .
