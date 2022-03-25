ifeq ($(BINDIR),)
BINDIR := bin
endif

ifeq ($(DESTDIR),)
DESTDIR := ${HOME}
endif

all:
	gcc -o hello-world hello-world.c

clean:
	rm -f hello-world

install:
	mkdir -p $(DESTDIR)/$(BINDIR)
	install -m 0755 hello-world $(DESTDIR)/$(BINDIR)/hello-world

check: all
	./hello-world | grep -q 'Hello, Brand New World'

