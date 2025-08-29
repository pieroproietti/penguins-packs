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

# per non impazzire...
```
mkdir -p ~/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}
echo '%_topdir %(echo $HOME)/rpmbuild' > ~/.rpmmacros
echo '%_download_cmd /usr/bin/wget -O %{O} %{U}' >> ~/.rpmmacros
```

# creare patch
```
git format-patch -2 HEAD
```

# applicare patch
cp 0* .
