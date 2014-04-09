all: debian-7.1.0-amd64 debian-7.1.0-i386 ubuntu-12.04-i386

debian-7.1.0-amd64:
	@cd tests/debian-7.1.0-amd64; \
	vagrant up

debian-7.1.0-i386:
	@cd tests/debian-7.1.0-i386; \
	vagrant up

ubuntu-12.04-i386:
	@cd tests/ubuntu-12.04-i386; \
	vagrant up

clean:
	@cd tests/debian-7.1.0-amd64; \
	vagrant destroy -f
	@cd tests/debian-7.1.0-i386; \
	vagrant destroy -f
	@cd tests/ubuntu-12.04-i386; \
	vagrant destroy -f
