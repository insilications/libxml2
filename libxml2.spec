Name     : libxml2
Version  : 2.9.3
Release  : 26
URL      : ftp://xmlsoft.org/libxml2/libxml2-2.9.3.tar.gz
Source0  : ftp://xmlsoft.org/libxml2/libxml2-2.9.3.tar.gz
Summary  : Library providing XML and HTML support
Group    : Development/Tools
License  : MIT
Requires: libxml2-bin
Requires: libxml2-python
Requires: libxml2-lib
Requires: libxml2-data
Requires: libxml2-doc
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pkgconfig(liblzma)
BuildRequires : pkgconfig(zlib)
BuildRequires : python-dev
BuildRequires : setuptools
BuildRequires : bzip2-dev
Patch1: stateless.patch

%description
This library allows to manipulate XML files. It includes support
to read, modify and write XML and HTML files. There is DTDs support
this includes parsing and validation even with complex DtDs, either
at parse time or later once the document has been modified. The output
can be a simple SAX stream or and in-memory DOM like representations.
In this case one can use the built-in XPath and XPointer implementation
to select sub nodes or ranges. A flexible Input/Output mechanism is
available, with existing HTTP and FTP modules and combined to an
URI library.

%package bin
Summary: bin components for the libxml2 package.
Group: Binaries
Requires: libxml2-data

%description bin
bin components for the libxml2 package.


%package data
Summary: data components for the libxml2 package.
Group: Data

%description data
data components for the libxml2 package.


%package dev
Summary: dev components for the libxml2 package.
Group: Development
Requires: libxml2-lib
Requires: libxml2-bin
Requires: libxml2-data
Provides: libxml2-devel

%description dev
dev components for the libxml2 package.


%package doc
Summary: doc components for the libxml2 package.
Group: Documentation

%description doc
doc components for the libxml2 package.


%package lib
Summary: lib components for the libxml2 package.
Group: Libraries
Requires: libxml2-data

%description lib
lib components for the libxml2 package.


%package python
Summary: python components for the libxml2 package.
Group: Default

%description python
python components for the libxml2 package.


%prep
%setup -q -n libxml2-2.9.3
%patch1 -p1

%build
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS1="$CFLAGS -fno-semantic-interposition -falign-functions=32 -O3 "
export CFLAGS2="$CFLAGS -fno-semantic-interposition -falign-functions=32 -O3 "
export CFLAGS="$CFLAGS -fno-semantic-interposition -falign-functions=32 -O3 -flto "
export CXXFLAGS="$CXXFLAGS -fno-semantic-interposition -falign-functions=32 -O3 -flto "


CFLAGS="$CFLAGS1 -fprofile-generate" %configure --disable-static
make V=1  %{?_smp_mflags}
make dba100000.xml
./xmllint --noout  dba100000.xml
./xmllint --stream  dba100000.xml
./xmllint --noout --valid test/valid/REC-xml-19980210.xml
./xmllint --stream --valid test/valid/REC-xml-19980210.xml
CFLAGS="$CFLAGS2 -fprofile-use" %configure --disable-static
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)
/usr/lib64/cmake/libxml2/libxml2-config.cmake
/usr/lib64/xml2Conf.sh

%files bin
%defattr(-,root,root,-)
/usr/bin/xml2-config
/usr/bin/xmlcatalog
/usr/bin/xmllint

%files data
%defattr(-,root,root,-)
/usr/share/doc/libxml2-python-2.9.3/TODO
/usr/share/doc/libxml2-python-2.9.3/examples/attribs.py
/usr/share/doc/libxml2-python-2.9.3/examples/attribs.pyc
/usr/share/doc/libxml2-python-2.9.3/examples/attribs.pyo
/usr/share/doc/libxml2-python-2.9.3/examples/build.py
/usr/share/doc/libxml2-python-2.9.3/examples/build.pyc
/usr/share/doc/libxml2-python-2.9.3/examples/build.pyo
/usr/share/doc/libxml2-python-2.9.3/examples/compareNodes.py
/usr/share/doc/libxml2-python-2.9.3/examples/compareNodes.pyc
/usr/share/doc/libxml2-python-2.9.3/examples/compareNodes.pyo
/usr/share/doc/libxml2-python-2.9.3/examples/ctxterror.py
/usr/share/doc/libxml2-python-2.9.3/examples/ctxterror.pyc
/usr/share/doc/libxml2-python-2.9.3/examples/ctxterror.pyo
/usr/share/doc/libxml2-python-2.9.3/examples/cutnpaste.py
/usr/share/doc/libxml2-python-2.9.3/examples/cutnpaste.pyc
/usr/share/doc/libxml2-python-2.9.3/examples/cutnpaste.pyo
/usr/share/doc/libxml2-python-2.9.3/examples/dtdvalid.py
/usr/share/doc/libxml2-python-2.9.3/examples/dtdvalid.pyc
/usr/share/doc/libxml2-python-2.9.3/examples/dtdvalid.pyo
/usr/share/doc/libxml2-python-2.9.3/examples/error.py
/usr/share/doc/libxml2-python-2.9.3/examples/error.pyc
/usr/share/doc/libxml2-python-2.9.3/examples/error.pyo
/usr/share/doc/libxml2-python-2.9.3/examples/inbuf.py
/usr/share/doc/libxml2-python-2.9.3/examples/inbuf.pyc
/usr/share/doc/libxml2-python-2.9.3/examples/inbuf.pyo
/usr/share/doc/libxml2-python-2.9.3/examples/indexes.py
/usr/share/doc/libxml2-python-2.9.3/examples/indexes.pyc
/usr/share/doc/libxml2-python-2.9.3/examples/indexes.pyo
/usr/share/doc/libxml2-python-2.9.3/examples/input_callback.py
/usr/share/doc/libxml2-python-2.9.3/examples/input_callback.pyc
/usr/share/doc/libxml2-python-2.9.3/examples/input_callback.pyo
/usr/share/doc/libxml2-python-2.9.3/examples/invalid.xml
/usr/share/doc/libxml2-python-2.9.3/examples/nsdel.py
/usr/share/doc/libxml2-python-2.9.3/examples/nsdel.pyc
/usr/share/doc/libxml2-python-2.9.3/examples/nsdel.pyo
/usr/share/doc/libxml2-python-2.9.3/examples/outbuf.py
/usr/share/doc/libxml2-python-2.9.3/examples/outbuf.pyc
/usr/share/doc/libxml2-python-2.9.3/examples/outbuf.pyo
/usr/share/doc/libxml2-python-2.9.3/examples/push.py
/usr/share/doc/libxml2-python-2.9.3/examples/push.pyc
/usr/share/doc/libxml2-python-2.9.3/examples/push.pyo
/usr/share/doc/libxml2-python-2.9.3/examples/pushSAX.py
/usr/share/doc/libxml2-python-2.9.3/examples/pushSAX.pyc
/usr/share/doc/libxml2-python-2.9.3/examples/pushSAX.pyo
/usr/share/doc/libxml2-python-2.9.3/examples/pushSAXhtml.py
/usr/share/doc/libxml2-python-2.9.3/examples/pushSAXhtml.pyc
/usr/share/doc/libxml2-python-2.9.3/examples/pushSAXhtml.pyo
/usr/share/doc/libxml2-python-2.9.3/examples/reader.py
/usr/share/doc/libxml2-python-2.9.3/examples/reader.pyc
/usr/share/doc/libxml2-python-2.9.3/examples/reader.pyo
/usr/share/doc/libxml2-python-2.9.3/examples/reader2.py
/usr/share/doc/libxml2-python-2.9.3/examples/reader2.pyc
/usr/share/doc/libxml2-python-2.9.3/examples/reader2.pyo
/usr/share/doc/libxml2-python-2.9.3/examples/reader3.py
/usr/share/doc/libxml2-python-2.9.3/examples/reader3.pyc
/usr/share/doc/libxml2-python-2.9.3/examples/reader3.pyo
/usr/share/doc/libxml2-python-2.9.3/examples/reader4.py
/usr/share/doc/libxml2-python-2.9.3/examples/reader4.pyc
/usr/share/doc/libxml2-python-2.9.3/examples/reader4.pyo
/usr/share/doc/libxml2-python-2.9.3/examples/reader5.py
/usr/share/doc/libxml2-python-2.9.3/examples/reader5.pyc
/usr/share/doc/libxml2-python-2.9.3/examples/reader5.pyo
/usr/share/doc/libxml2-python-2.9.3/examples/reader6.py
/usr/share/doc/libxml2-python-2.9.3/examples/reader6.pyc
/usr/share/doc/libxml2-python-2.9.3/examples/reader6.pyo
/usr/share/doc/libxml2-python-2.9.3/examples/reader7.py
/usr/share/doc/libxml2-python-2.9.3/examples/reader7.pyc
/usr/share/doc/libxml2-python-2.9.3/examples/reader7.pyo
/usr/share/doc/libxml2-python-2.9.3/examples/reader8.py
/usr/share/doc/libxml2-python-2.9.3/examples/reader8.pyc
/usr/share/doc/libxml2-python-2.9.3/examples/reader8.pyo
/usr/share/doc/libxml2-python-2.9.3/examples/readererr.py
/usr/share/doc/libxml2-python-2.9.3/examples/readererr.pyc
/usr/share/doc/libxml2-python-2.9.3/examples/readererr.pyo
/usr/share/doc/libxml2-python-2.9.3/examples/readernext.py
/usr/share/doc/libxml2-python-2.9.3/examples/readernext.pyc
/usr/share/doc/libxml2-python-2.9.3/examples/readernext.pyo
/usr/share/doc/libxml2-python-2.9.3/examples/regexp.py
/usr/share/doc/libxml2-python-2.9.3/examples/regexp.pyc
/usr/share/doc/libxml2-python-2.9.3/examples/regexp.pyo
/usr/share/doc/libxml2-python-2.9.3/examples/relaxng.py
/usr/share/doc/libxml2-python-2.9.3/examples/relaxng.pyc
/usr/share/doc/libxml2-python-2.9.3/examples/relaxng.pyo
/usr/share/doc/libxml2-python-2.9.3/examples/resolver.py
/usr/share/doc/libxml2-python-2.9.3/examples/resolver.pyc
/usr/share/doc/libxml2-python-2.9.3/examples/resolver.pyo
/usr/share/doc/libxml2-python-2.9.3/examples/schema.py
/usr/share/doc/libxml2-python-2.9.3/examples/schema.pyc
/usr/share/doc/libxml2-python-2.9.3/examples/schema.pyo
/usr/share/doc/libxml2-python-2.9.3/examples/serialize.py
/usr/share/doc/libxml2-python-2.9.3/examples/serialize.pyc
/usr/share/doc/libxml2-python-2.9.3/examples/serialize.pyo
/usr/share/doc/libxml2-python-2.9.3/examples/sync.py
/usr/share/doc/libxml2-python-2.9.3/examples/sync.pyc
/usr/share/doc/libxml2-python-2.9.3/examples/sync.pyo
/usr/share/doc/libxml2-python-2.9.3/examples/test.dtd
/usr/share/doc/libxml2-python-2.9.3/examples/thread2.py
/usr/share/doc/libxml2-python-2.9.3/examples/thread2.pyc
/usr/share/doc/libxml2-python-2.9.3/examples/thread2.pyo
/usr/share/doc/libxml2-python-2.9.3/examples/tst.py
/usr/share/doc/libxml2-python-2.9.3/examples/tst.pyc
/usr/share/doc/libxml2-python-2.9.3/examples/tst.pyo
/usr/share/doc/libxml2-python-2.9.3/examples/tst.xml
/usr/share/doc/libxml2-python-2.9.3/examples/tstLastError.py
/usr/share/doc/libxml2-python-2.9.3/examples/tstLastError.pyc
/usr/share/doc/libxml2-python-2.9.3/examples/tstLastError.pyo
/usr/share/doc/libxml2-python-2.9.3/examples/tstURI.py
/usr/share/doc/libxml2-python-2.9.3/examples/tstURI.pyc
/usr/share/doc/libxml2-python-2.9.3/examples/tstURI.pyo
/usr/share/doc/libxml2-python-2.9.3/examples/tstmem.py
/usr/share/doc/libxml2-python-2.9.3/examples/tstmem.pyc
/usr/share/doc/libxml2-python-2.9.3/examples/tstmem.pyo
/usr/share/doc/libxml2-python-2.9.3/examples/tstxpath.py
/usr/share/doc/libxml2-python-2.9.3/examples/tstxpath.pyc
/usr/share/doc/libxml2-python-2.9.3/examples/tstxpath.pyo
/usr/share/doc/libxml2-python-2.9.3/examples/valid.xml
/usr/share/doc/libxml2-python-2.9.3/examples/validDTD.py
/usr/share/doc/libxml2-python-2.9.3/examples/validDTD.pyc
/usr/share/doc/libxml2-python-2.9.3/examples/validDTD.pyo
/usr/share/doc/libxml2-python-2.9.3/examples/validRNG.py
/usr/share/doc/libxml2-python-2.9.3/examples/validRNG.pyc
/usr/share/doc/libxml2-python-2.9.3/examples/validRNG.pyo
/usr/share/doc/libxml2-python-2.9.3/examples/validSchemas.py
/usr/share/doc/libxml2-python-2.9.3/examples/validSchemas.pyc
/usr/share/doc/libxml2-python-2.9.3/examples/validSchemas.pyo
/usr/share/doc/libxml2-python-2.9.3/examples/validate.py
/usr/share/doc/libxml2-python-2.9.3/examples/validate.pyc
/usr/share/doc/libxml2-python-2.9.3/examples/validate.pyo
/usr/share/doc/libxml2-python-2.9.3/examples/walker.py
/usr/share/doc/libxml2-python-2.9.3/examples/walker.pyc
/usr/share/doc/libxml2-python-2.9.3/examples/walker.pyo
/usr/share/doc/libxml2-python-2.9.3/examples/xpath.py
/usr/share/doc/libxml2-python-2.9.3/examples/xpath.pyc
/usr/share/doc/libxml2-python-2.9.3/examples/xpath.pyo
/usr/share/doc/libxml2-python-2.9.3/examples/xpathext.py
/usr/share/doc/libxml2-python-2.9.3/examples/xpathext.pyc
/usr/share/doc/libxml2-python-2.9.3/examples/xpathext.pyo
/usr/share/doc/libxml2-python-2.9.3/examples/xpathleak.py
/usr/share/doc/libxml2-python-2.9.3/examples/xpathleak.pyc
/usr/share/doc/libxml2-python-2.9.3/examples/xpathleak.pyo
/usr/share/doc/libxml2-python-2.9.3/examples/xpathns.py
/usr/share/doc/libxml2-python-2.9.3/examples/xpathns.pyc
/usr/share/doc/libxml2-python-2.9.3/examples/xpathns.pyo
/usr/share/doc/libxml2-python-2.9.3/examples/xpathret.py
/usr/share/doc/libxml2-python-2.9.3/examples/xpathret.pyc
/usr/share/doc/libxml2-python-2.9.3/examples/xpathret.pyo

%files dev
%defattr(-,root,root,-)
/usr/include/libxml2/libxml/DOCBparser.h
/usr/include/libxml2/libxml/HTMLparser.h
/usr/include/libxml2/libxml/HTMLtree.h
/usr/include/libxml2/libxml/SAX.h
/usr/include/libxml2/libxml/SAX2.h
/usr/include/libxml2/libxml/c14n.h
/usr/include/libxml2/libxml/catalog.h
/usr/include/libxml2/libxml/chvalid.h
/usr/include/libxml2/libxml/debugXML.h
/usr/include/libxml2/libxml/dict.h
/usr/include/libxml2/libxml/encoding.h
/usr/include/libxml2/libxml/entities.h
/usr/include/libxml2/libxml/globals.h
/usr/include/libxml2/libxml/hash.h
/usr/include/libxml2/libxml/list.h
/usr/include/libxml2/libxml/nanoftp.h
/usr/include/libxml2/libxml/nanohttp.h
/usr/include/libxml2/libxml/parser.h
/usr/include/libxml2/libxml/parserInternals.h
/usr/include/libxml2/libxml/pattern.h
/usr/include/libxml2/libxml/relaxng.h
/usr/include/libxml2/libxml/schemasInternals.h
/usr/include/libxml2/libxml/schematron.h
/usr/include/libxml2/libxml/threads.h
/usr/include/libxml2/libxml/tree.h
/usr/include/libxml2/libxml/uri.h
/usr/include/libxml2/libxml/valid.h
/usr/include/libxml2/libxml/xinclude.h
/usr/include/libxml2/libxml/xlink.h
/usr/include/libxml2/libxml/xmlIO.h
/usr/include/libxml2/libxml/xmlautomata.h
/usr/include/libxml2/libxml/xmlerror.h
/usr/include/libxml2/libxml/xmlexports.h
/usr/include/libxml2/libxml/xmlmemory.h
/usr/include/libxml2/libxml/xmlmodule.h
/usr/include/libxml2/libxml/xmlreader.h
/usr/include/libxml2/libxml/xmlregexp.h
/usr/include/libxml2/libxml/xmlsave.h
/usr/include/libxml2/libxml/xmlschemas.h
/usr/include/libxml2/libxml/xmlschemastypes.h
/usr/include/libxml2/libxml/xmlstring.h
/usr/include/libxml2/libxml/xmlunicode.h
/usr/include/libxml2/libxml/xmlversion.h
/usr/include/libxml2/libxml/xmlwriter.h
/usr/include/libxml2/libxml/xpath.h
/usr/include/libxml2/libxml/xpathInternals.h
/usr/include/libxml2/libxml/xpointer.h
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc
/usr/share/aclocal/*.m4

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/libxml2/*
%doc /usr/share/man/man1/*
%doc /usr/share/man/man3/*
/usr/share/gtk-doc/html/libxml2/general.html
/usr/share/gtk-doc/html/libxml2/home.png
/usr/share/gtk-doc/html/libxml2/index.html
/usr/share/gtk-doc/html/libxml2/left.png
/usr/share/gtk-doc/html/libxml2/libxml2-DOCBparser.html
/usr/share/gtk-doc/html/libxml2/libxml2-HTMLparser.html
/usr/share/gtk-doc/html/libxml2/libxml2-HTMLtree.html
/usr/share/gtk-doc/html/libxml2/libxml2-SAX.html
/usr/share/gtk-doc/html/libxml2/libxml2-SAX2.html
/usr/share/gtk-doc/html/libxml2/libxml2-c14n.html
/usr/share/gtk-doc/html/libxml2/libxml2-catalog.html
/usr/share/gtk-doc/html/libxml2/libxml2-chvalid.html
/usr/share/gtk-doc/html/libxml2/libxml2-debugXML.html
/usr/share/gtk-doc/html/libxml2/libxml2-dict.html
/usr/share/gtk-doc/html/libxml2/libxml2-encoding.html
/usr/share/gtk-doc/html/libxml2/libxml2-entities.html
/usr/share/gtk-doc/html/libxml2/libxml2-globals.html
/usr/share/gtk-doc/html/libxml2/libxml2-hash.html
/usr/share/gtk-doc/html/libxml2/libxml2-list.html
/usr/share/gtk-doc/html/libxml2/libxml2-nanoftp.html
/usr/share/gtk-doc/html/libxml2/libxml2-nanohttp.html
/usr/share/gtk-doc/html/libxml2/libxml2-parser.html
/usr/share/gtk-doc/html/libxml2/libxml2-parserInternals.html
/usr/share/gtk-doc/html/libxml2/libxml2-pattern.html
/usr/share/gtk-doc/html/libxml2/libxml2-relaxng.html
/usr/share/gtk-doc/html/libxml2/libxml2-schemasInternals.html
/usr/share/gtk-doc/html/libxml2/libxml2-schematron.html
/usr/share/gtk-doc/html/libxml2/libxml2-threads.html
/usr/share/gtk-doc/html/libxml2/libxml2-tree.html
/usr/share/gtk-doc/html/libxml2/libxml2-uri.html
/usr/share/gtk-doc/html/libxml2/libxml2-valid.html
/usr/share/gtk-doc/html/libxml2/libxml2-xinclude.html
/usr/share/gtk-doc/html/libxml2/libxml2-xlink.html
/usr/share/gtk-doc/html/libxml2/libxml2-xmlIO.html
/usr/share/gtk-doc/html/libxml2/libxml2-xmlautomata.html
/usr/share/gtk-doc/html/libxml2/libxml2-xmlerror.html
/usr/share/gtk-doc/html/libxml2/libxml2-xmlexports.html
/usr/share/gtk-doc/html/libxml2/libxml2-xmlmemory.html
/usr/share/gtk-doc/html/libxml2/libxml2-xmlmodule.html
/usr/share/gtk-doc/html/libxml2/libxml2-xmlreader.html
/usr/share/gtk-doc/html/libxml2/libxml2-xmlregexp.html
/usr/share/gtk-doc/html/libxml2/libxml2-xmlsave.html
/usr/share/gtk-doc/html/libxml2/libxml2-xmlschemas.html
/usr/share/gtk-doc/html/libxml2/libxml2-xmlschemastypes.html
/usr/share/gtk-doc/html/libxml2/libxml2-xmlstring.html
/usr/share/gtk-doc/html/libxml2/libxml2-xmlunicode.html
/usr/share/gtk-doc/html/libxml2/libxml2-xmlversion.html
/usr/share/gtk-doc/html/libxml2/libxml2-xmlwriter.html
/usr/share/gtk-doc/html/libxml2/libxml2-xpath.html
/usr/share/gtk-doc/html/libxml2/libxml2-xpathInternals.html
/usr/share/gtk-doc/html/libxml2/libxml2-xpointer.html
/usr/share/gtk-doc/html/libxml2/libxml2.devhelp
/usr/share/gtk-doc/html/libxml2/right.png
/usr/share/gtk-doc/html/libxml2/style.css
/usr/share/gtk-doc/html/libxml2/up.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
