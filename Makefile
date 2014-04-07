all: gnulinux-i386

gnulinux-i386:
	@cd tests/gnulinux-i386; \
	vagrant up

clean:
	@cd tests/gnulinux-i386; \
	vagrant destroy -f
	@cd tests/gnulinux-i386; \
	rm -rvf .vagrant
