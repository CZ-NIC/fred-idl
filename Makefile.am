ACLOCAL_AMFLAGS = -I m4

idldir = $(datadir)/idl/fred
dist_idl_DATA = ${srcdir}/idl/*.idl
EXTRA_DIST = fred-idl.spec $(srcdir)/doc/Doxyfile \
  $(srcdir)/doc/docbook.xsl $(srcdir)/doc/mainpage.h

include $(top_srcdir)/am_doxygen.am

if DX_COND_html
doc_DATA = @DX_DOCDIR@/html/*
$(doc_DATA): doxygen-doc
MOSTLYCLEANFILES = ${DX_CLEANFILES}
endif

