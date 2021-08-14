import os
import sys
from setuptools import setup, find_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')
def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.helpfullegaladviceforall',
      version='1.0.0',
      description=('A docassemble extension, based on providing helpful legal access for all people'),
      long_description='Made for SMU Lit Hackathon 2021\r\n  Team idk why\r\n  Members:\r\n    - ',
      long_description_content_type='text/markdown',
      author='Wicha',
      author_email='wichaprakhun5@gmail.com',
      license='The MIT License (MIT)',
      url='https://github.com/wiiicha/helpful-legal-access-for-all',
      packages=find_packages(),
      namespace_packages=['docassemble'],
      install_requires=['3to2>=1.1.1', 'Babel>=2.9.1', 'ConfigArgParse>=1.5.1', 'Docassemble-Flask-User>=0.6.24', 'Docassemble-Pattern>=3.6.2', 'Flask>=1.1.2', 'Flask-Babel>=2.0.0', 'Flask-Cors>=3.0.10', 'Flask-Login>=0.5.0', 'Flask-Mail>=0.9.1', 'Flask-SQLAlchemy>=2.4.4', 'Flask-SocketIO>=5.0.1', 'Flask-WTF>=0.14.3', 'Hyphenate>=1.1.0', 'Jinja2>=3.0.0', 'Mako>=1.1.4', 'Marisol>=0.3.0', 'Markdown>=3.3.4', 'MarkupSafe>=2.0.0', 'Pillow>=8.2.0', 'PyJWT>=1.7.1', 'PyLaTeX>=1.4.1', 'PyNaCl>=1.4.0', 'PyPDF2>=1.26.0', 'PySocks>=1.7.1', 'PyYAML>=5.1.2', 'Pygments>=2.0.2', 'SQLAlchemy>=0.6.9', 'SecretStorage>=3.3.1', 'SocksiPy-branch>=1.01', 'WTForms>=2.3.3', 'Werkzeug>=2.0.0', 'XlsxWriter>=1.4.3', 'acme>=1.18.0', 'airtable-python-wrapper>=0.15.2', 'alembic>=0.1.1', 'aloe>=0.2.0', 'amqp>=5.0.6', 'ansicolors>=1.1.8', 'asn1crypto>=1.4.0', 'astunparse>=1.6.3', 'atomicwrites>=1.4.0', 'attrs>=21.2.0', 'azure-common>=1.1.27', 'azure-core>=1.13.0', 'azure-identity>=1.5.0', 'azure-keyvault-secrets>=4.2.0', 'azure-nspkg>=3.0.2', 'azure-storage-blob>=12.8.1', 'bcrypt>=3.2.0', 'beautifulsoup4>=4.9.3', 'bidict>=0.21.2', 'billiard>=3.6.4.0', 'bleach>=3.3.0', 'blinker>=1.4', 'boto>=2.49.0', 'boto3>=1.17.71', 'botocore>=1.20.71', 'cachetools>=4.2.2', 'celery>=5.0.5', 'certbot>=1.15.0', 'certbot-apache>=1.15.0', 'certbot-nginx>=1.15.0', 'certifi>=2020.12.5', 'cffi>=1.14.5', 'chardet>=4.0.0', 'charset-normalizer>=0.1.8', 'click>=7.1.2', 'click-didyoumean>=0.0.3', 'click-plugins>=1.1.1', 'click-repl>=0.1.6', 'colorama>=0.4.4', 'configobj>=5.0.6', 'configparser>=5.0.2', 'convertapi>=1.4.0', 'crayons>=0.4.0', 'cryptography>=3.4.7', 'da-pkg-resources>=0.0.1', 'distro>=1.6.0', 'dnspython>=1.16.0', 'docassemble-textstat>=0.7.1', 'docassemble.demo>=1.2.97', 'docassemblekvsession>=0.6', 'docopt>=0.6.2', 'docutils>=0.17.1', 'docxcompose>=1.3.2', 'docxtpl>=0.11.5', 'email-validator>=1.1.2', 'et-xmlfile>=1.1.0', 'eventlet>=0.31.0', 'future>=0.18.2', 'gcs-oauth2-boto-plugin>=2.7', 'geographiclib>=1.50', 'geopy>=2.1.0', 'gherkin-official>=4.1.3', 'google-api-core>=1.26.3', 'google-api-python-client>=2.3.0', 'google-auth>=1.30.0', 'google-auth-httplib2>=0.1.0', 'google-auth-oauthlib>=0.4.4', 'google-cloud-core>=1.5.0', 'google-cloud-storage>=1.38.0', 'google-cloud-translate>=3.1.0', 'google-crc32c>=1.1.2', 'google-i18n-address>=2.4.0', 'google-reauth>=0.1.1', 'google-resumable-media>=1.2.0', 'googleapis-common-protos>=1.53.0', 'greenlet>=1.0.0', 'grpcio>=1.37.1', 'gspread>=3.7.0', 'guess-language-spirit>=0.5.3', 'httplib2>=0.19.1', 'humanize>=3.5.0', 'idna>=2.10', 'importlib-metadata>=4.0.1', 'importlib-resources>=5.1.2', 'iniconfig>=1.1.1', 'iso8601>=0.1.14', 'isodate>=0.6.0', 'itsdangerous>=2.0.0', 'jdcal>=1.4.1', 'jeepney>=0.6.0', 'jellyfish>=0.6.1', 'jmespath>=0.10.0', 'joblib>=1.0.1', 'josepy>=1.8.0', 'keyring>=1.2.3', 'kombu>=5.0.2', 'libcst>=0.3.18', 'links-from-link-header>=0.1.0', 'lxml>=1.0.4', 'mdx-smartypants>=1.5.1', 'minio>=7.0.3', 'mod-wsgi>=4.7.1', 'monotonic>=1.6', 'msal>=1.11.0', 'msal-extensions>=0.3.0', 'msrest>=0.6.21', 'mypy-extensions>=0.4.3', 'namedentities>=1.5.2', 'netifaces>=0.10.9', 'nltk>=2.0.5', 'nose>=1.3.7', 'num2words>=0.5.10', 'numpy>=1.0.4', 'oauth2client>=4.1.3', 'oauthlib>=3.1.0', 'openpyxl>=3.0.7', 'ordered-set>=4.0.2', 'packaging>=20.9', 'pandas>=1.2.4', 'parsedatetime>=2.6', 'passlib>=1.7.4', 'pathlib>=1.0.1', 'pdfminer.six>=20201018', 'phonenumbers>=5.9.2', 'pip>=20.1.1', 'pkginfo>=1.2.1', 'pluggy>=0.13.1', 'ply>=3.11', 'portalocker>=1.7.1', 'prompt-toolkit>=3.0.18', 'proto-plus>=1.18.1', 'protobuf>=3.16.0', 'psutil>=5.8.0', 'psycopg2-binary>=2.8.6', 'py>=1.10.0', 'pyOpenSSL>=20.0.1', 'pyPdf>=1.13', 'pyRFC3339>=1.1', 'pyasn1>=0.4.8', 'pyasn1-modules>=0.2.8', 'pycountry>=20.7.3', 'pycparser>=2.20', 'pycryptodome>=3.10.1', 'pycryptodomex>=3.10.1', 'pycurl>=7.43.0.6', 'pyotp>=2.6.0', 'pyparsing>=2.4.7', 'pypdftk>=0.5', 'pypng>=0.0.20', 'pytest>=6.2.4', 'python-augeas>=1.1.0', 'python-dateutil>=2.8.1', 'python-docx>=0.8.10', 'python-editor>=1.0.4', 'python-engineio>=4.1.0', 'python-http-client>=3.3.2', 'python-ldap>=3.3.1', 'python-socketio>=5.2.1', 'pytz>=2013.9', 'pyu2f>=0.1.5', 'pyzbar>=0.1.8', 'qrcode>=6.1', 'rauth>=0.7.3', 'readme-renderer>=29.0', 'redis>=3.5.3', 'regex>=2021.4.4', 'reportlab>=3.3.0', 'repoze.lru>=0.7', 'requests>=2.25.1', 'requests-oauthlib>=1.3.0', 'requests-toolbelt>=0.9.1', 'retry-decorator>=1.1.1', 'rfc3339>=6.2', 'rfc3986>=1.5.0', 'rsa>=4.7.2', 'ruamel.yaml>=0.17.4', 'ruamel.yaml.clib>=0.2.2', 's3transfer>=0.4.2', 's4cmd>=2.1.0', 'scikit-learn>=0.14.1', 'scipy>=1.5.4', 'selenium>=2.0-dev-9429', 'sendgrid>=6.7.0', 'setuptools>=56.0.0', 'simplekv>=0.14.1', 'six>=1.0.0', 'sklearn>=0.0', 'sortedcontainers>=2.3.0', 'soupsieve>=1.0.2', 'starkbank-ecdsa>=1.1.0', 'tailer>=0.4.1', 'telnyx>=1.4.0', 'threadpoolctl>=2.1.0', 'titlecase>=2.0.0', 'toml>=0.10.2', 'tqdm>=4.60.0', 'twilio>=5.0.0', 'twine>=3.4.1', 'typing-extensions>=3.10.0.0', 'typing-inspect>=0.6.0', 'tzlocal>=2.1', 'uWSGI>=2.0.19.1', 'ua-parser>=0.10.0', 'uritemplate>=3.0.1', 'urllib3>=1.26.5', 'us>=2.0.2', 'user-agents>=2.2.0', 'vine>=5.0.0', 'wcwidth>=0.2.5', 'webdriver-manager>=3.4.1', 'webencodings>=0.5.1', 'wheel>=0.36.2', 'xfdfgen>=0.4', 'xlrd>=2.0.1', 'xlwt>=1.3.0', 'zipp>=3.4.1', 'zope.component>=5.0.1', 'zope.event>=4.5.0', 'zope.hookable>=5.1.0', 'zope.interface>=3.3.0.1'],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/helpfullegaladviceforall/', package='docassemble.helpfullegaladviceforall'),
     )

