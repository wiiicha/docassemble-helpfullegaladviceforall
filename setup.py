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
      version='1.0.3',
      description=('A docassemble extension, based on providing helpful legal access for all people'),
      long_description='Made for SMU Lit Hackathon 2021 <br />\r\nTeam idk why <br />\r\n\r\n<br />\r\n\r\nHow to access the project files (.yml) <br />\r\n 1. Please feel free to download the repository and proceed to: <br />\r\ndocassemble-helpfullegaladviceforall/docassemble/helpfullegaladviceforall/data/questions \r\n\r\n<br />\r\n \r\nAlternatively, to access the completed project, \r\n 1. Head to idkwhy.ddns.net\r\n 2. Complete the online interview\r\n 3. Download the generated PDF file.\r\n \r\n ',
      long_description_content_type='text/markdown',
      author='Prakhunwicha Sararaksh',
      author_email='prakhunwich.2020@law.smu.edu.sg',
      license='',
      url='idkwhy.ddns.net',
      packages=find_packages(),
      namespace_packages=['docassemble'],
      install_requires=['py>=1.10.0'],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/helpfullegaladviceforall/', package='docassemble.helpfullegaladviceforall'),
     )

