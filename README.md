fteproxy-tester
===============

This is a project that helps test fteproxy under a range of conditions.

The following platforms are supported via VirtualBox.

* Debian 7.1.0 (32-bit)
* Debian 7.1.0 (64-bit)
* Ubuntu 12.04 (32-bit)
* Ubuntu 12.04 (64-bit)
* Ubuntu 14.04 (32-bit)
* Ubuntu 14.04 (64-bit)
* OSX 10.6+
* Windows XP (32-bit)
* Windows 7 (64-bit)
* Windows 8.1 (64-bit)

Example
-------

```console
$ python main.py
config                install_method	result
debian-7.1.0-i386     pip               SUCCESS
debian-7.1.0-i386     tar               SUCCESS
debian-7.1.0-amd64    pip               SUCCESS
debian-7.1.0-amd64    tar               SUCCESS
...
windows-xp-i386       zip               SUCCESS
windows-7-amd64       zip               SUCCESS
windows-81-amd64      zip               SUCCESS
```
