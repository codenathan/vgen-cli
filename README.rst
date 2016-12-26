vgen-cli
========

Automated virtual host generator


Purpose
-------

To provide a single line command line tool to setup/archive virtual host files for apache/nginx web servers.

Usage
-----

* Install Package Using pip install -e .

* Configure config file vgen/config.py

Docs
----

```
vgen

Usage:
  vgen create HOST [-p=<package>] [-u=<username>] [-d]
  vgen archive HOST
  vgen -h | --help
  vgen --version

Arguments:
  HOST  fully qualified domain name

Options:
  -h --help                        Show this screen.
  --version                        Show version.
  -p                               Optional - framework/application to install i.e wordpress/laravel/codeigniter
  -u                               Optional - Use different username
  -d                               Optional - Create Database

Examples:
  vgen create stage.vgen.com
  vgen create dev.vgen.com --p=laravel --u=vgen
  vgen archive www.vgen.com

```


Credits
-------

Base on Randall Degges(@rdegges) skele-cli https://github.com/rdegges/skele-cli