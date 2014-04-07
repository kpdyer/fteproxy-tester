gnulinux-i386:
	@cd tests/gnulinux-i386; \
	vagrant up

clean:
	@cd $(BUILD_DIR_ABSPATH)/gnulinux-i386; \
	vagrant destroy -f
	@cd $(BUILD_DIR_ABSPATH)/gnulinux-i386; \
	rm -rvf .vagrant
