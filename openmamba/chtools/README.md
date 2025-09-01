# Installare un rootfs-base

Questa per me è una nuova avventura, spero rapida.

Remastersys, systemback ed anche penguins-eggs fanno un percorso del tutto opposto - e più semplice - ma storicamente __è nato prima l'uovo e poi la gallina__ ed è stato ed è comune e necessario partire da un rootfs di base e configurarlo chrooted.

D'altra parte è il modo più pratico che ho trovato per ottenere una openmamba "naked" e, mi è stato suggerito direttamente dall'autore.

Quindi, partiamo scaricando **openmamba-rootfs-base-en-snapshot-20250815.x86_64.tar.xz** dal sito di [opemamba](https://openmamba.org/it/Scarica/).

# Cosa manca a rootfs?
Per installare rootfs utilizzeremo una live, la prima volta ho usato la live openmamba-lxqt, successivamente le varie naked prodotte.

In primo luogo, questo è un lavoro fatto su una VM, fregandosene di quello che c'era dentro - in effetti è stata/sono state create appositamnte - farlo direttamente su un PC - non è cosa ne' buone , ne' giusta, ed in ogni caso NON seguite questa procedura.

Avviata la live, ci troveremo loggati come utente: live/evolution con diritti di root - il nostro utente fa parte del gruppo sysadmin.

Io procedo così, non sono ortodosso:
* `g4clone penguins-packs`
* `ln -s penguins-packs/openmamba/chtools t`
* `sudo t/erase-sda` (formatta il disco per BIOS)

A questo punto dobbiamo recuperare il nostro rootfs-base, lo scarico, nel mio caso dall'host.

* `scp artisan@192.168.1.2:/home/artisan/openmamba-rootfs-base-en-snapshot-20250815.x86_64.tar.xz .`

quindi creiamo un punto di mount, denomimato `naked`:
* `sudo mkdir naked`
* `sudo mount /dev/sda1 naked`
* `cd naked`
* `sudo tar -xf ../openmamba-rootfs-base-en-snapshot-20250815.x86_64.tar.xz`

Stiamo a buon punto, il nostro sistema è sul disco, manca di renderlo "vivo".

* `t/bind-naked`

Ora abbiamo i nostri filesystem virtuali, presenti. Ma non basta. occorre un kernel.

## kernel
```
dnf install kernel e2fsprogs
```

## Qualche comodità minina... a scelta
```
dnf install  nano tzdata
```

## fstab
Edit `/etc/fstab` ed aggiungi:
```
/dev/sda1    /    exts    defaults    0  2
```

## grub-install
```
sudo grub-install --target=i386-pc /dev/sda
```

## password
Per non rimanere "fregati" impostate una password a root.
```
passwd
```

## Uscita e riavvio
Usciamo dalla chroot con `exit` e riavviamo. 

Se nulla     è andato storto, avremo un sistema, minimale funzionante.


