# Installazione XFCE su openmamba

Per partire pulito, sto utilizzando una immagine live in formato ISO [`eggs-of_openmamba-naked_ ... .iso`](https://drive.google.com/drive/folders/1-7LbgkKIrp8hUFTbO3qGtPKzaHter6RM) preparata con [penguins-eggs](https://github.com/pieroproietti/penguins-eggs) a partire da una installazione vergine fatta con
**openmamba-rootfs-base-en-snapshot-20250815.x86_64.tar.xz**.

PS: La procedura di pacchettizzazione che utilizzo per il tool `penguins-eggs` è nella cartella [openmamba/penguins-eggs](https://github.com/pieroproietti/penguins-packs/tree/master/openmamba/penguins-eggs) del repository [penguins-packs](https://github.com/pieroproietti/penguins-packs). Ha ancora qualche asperità - in particolare non sono riuscito a capire come fargli scaricare automaticamente i sorgenti dal mio repository, ma lo faccio preventivamente con lo script `./d`, quindi `./b` per build e `./c` per pulire.

Sulla stessa repository. sotto [openmamba/chtools](https://github.com/pieroproietti/penguins-packs/tree/master/openmamba/chtools) è descritta la procedura che ho seguito per installare il rootfs-base e che può essere - pure questa - migliorata.

Come detto, non sono esattamente un ortodosso, chiedo venia.

Per installare il sistema, basta inserire l'immagine `eggs-of_openmamba-naked_ ... .iso` ed avviare il sistema da quest'ultimo.

E' presente un autologin su live e le istruzioni per l'installazione, sono presentate direttamente a video ma - in sostanza - basta digitare:

```
sudo eggs install -u
```

Al riavvio ci potremmo loggare con:
* artisan/evolution 
* root/evolution

## [bin](./bin/)
script di installazione

## [logs](./logs/)
E' la copia della cartella `/var/log/lightdm`

## [packages](./packages/)
Sono i pacchetti creati da Silvan Calarco per lo scopo.