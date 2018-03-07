ACLOCAL_AMFLAGS = -I m4

idldir = $(datadir)/idl/fred
dist_idl_DATA = ${srcdir}/idl/*.idl
EXTRA_DIST = contrib/fedora/fred-idl.spec $(srcdir)/doc/Doxyfile \
  $(srcdir)/doc/docbook.xsl $(srcdir)/doc/mainpage.h

include $(top_srcdir)/am_doxygen.am

if DX_COND_html
doc_DATA = @DX_DOCDIR@/html/*
$(doc_DATA): doxygen-doc
MOSTLYCLEANFILES = ${DX_CLEANFILES}
endif

all: fred_idl

fred_idl: ${dist_idl_DATA}
	omniidl -bpython -Wbmodules=fred_idl -Wbstubs=fred_idl._stubs ${dist_idl_DATA}
	find fred_idl -name \*.py -exec $(PYTHON) -mcompileall {} \;

install-exec-local: fred_idl
	install -d "$(DESTDIR)$(pkgpythondir)" && cp -r fred_idl "$(DESTDIR)$(pkgpythondir)"

uninstall-local:
	-rm -rf "$(DESTDIR)$(pkgpythondir)/fred_idl"

clean-local:
	-rm -rf fred_idl

