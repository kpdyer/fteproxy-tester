#!/bin/sh

# This file is part of fteproxy.
#
# fteproxy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# fteproxy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with fteproxy.  If not, see <http://www.gnu.org/licenses/>.

# install tor repo
echo "deb http://deb.torproject.org/torproject.org wheezy main" >> /etc/apt/sources.list
echo "deb http://deb.torproject.org/torproject.org tor-experimental-0.2.5.x-wheezy main" >> /etc/apt/sources.list
gpg --keyserver keys.gnupg.net --recv 886DDD89
gpg --export A3C4F0F979CAA22CDBA8F512EE8CBC9E886DDD89 | sudo apt-key add -

# install fteproxy repo
echo "deb http://fteproxy.org/deb/ stable/" >> /etc/apt/sources.list
gpg --keyserver keys.gnupg.net --recv 6B898EE18FBA6390
gpg --export 6B898EE18FBA6390 | sudo apt-key add -

# do update
apt-get -y update

# install fteproxy
apt-get -y install fteproxy

# test fteproxy
fteproxy --mode test
