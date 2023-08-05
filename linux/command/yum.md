# yum

1. 升级python导致yum 出错

   ```shell
   sed -i '1c #!\/usr\/bin\/python2.7' /usr/bin/yum
   sed -i '1c #!\/usr\/bin\/python2.7' /usr/libexec/urlgrabber-ext-downn
   ```
