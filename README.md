## Example: How To build rpm package

#### Prepare build tools
	sudo yum install gcc rpm-build rpm-devel rpmlint make bash \
		coreutils diffutils patch rpmdevtools

#### Checkout sources
	cd $HOME
	mkdir rpmbuild
	git clone https://github.com/avekceeb/rpmbuild-sample .

#### Build
	rpmbuild -ba SPECS/hello-world.spec

#### Install
	sudo rpm -ihv RPMS/x86_64/hello-world-1.1-1.el8.x86_64.rpm

#### Check and Remove
	hello-world
	sudo rpm -ev hello-world

## Build and install without rpm
    make
    make DESTDIR=/opt BINDIR=hello-world/bin install

