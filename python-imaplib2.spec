Name:		python-imaplib2
Version:	3.6
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/i/imaplib2/imaplib2-%{version}.tar.gz
Summary:	A threaded Python IMAP4 client.
URL:		https://pypi.org/project/imaplib2/
License:	MIT
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pip)
BuildArch:	noarch

%description
A threaded Python IMAP4 client.

%prep
%autosetup -p1 -n imaplib2-%{version}

%build
%py_build

%install
%py_install

%files
%{py_sitedir}/imaplib2
%{py_sitedir}/imaplib2-*.*-info
