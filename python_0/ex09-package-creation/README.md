
## Allowed functions:
- PyPI or any library for creation package

- Files to turn in : *.py, *.txt, *.toml,

Create your first package in python the way you want, it will appear in the list of
installed packages when you type the command "pip list" and display its characteristics
when you type "pip show -v ft_package"

Example:
$>pip show -v ft_package
Name: ft_package
Version: 0.0.1
Summary: A sample test package
Home-page: https://github.com/eagle/ft_package
Author: eagle
Author-email: eagle@42.fr
License: MIT
Location: /home/eagle/...
Requires:
Required-by:
Metadata-Version: 2.1
Installer: pip
Classifiers:
Entry-points:
$>

The package will be installed via pip using one of the following commands (both
should work):
• pip install ./dist/ft_package-0.0.1.tar.gz
• pip install ./dist/ft_package-0.0.1-py3-none-any.whl
Your package must be able to be called from a script like this one:
from ft_package import count_in_list
print(count_in_list(["toto", "tata", "toto"], "toto")) # output: 2
print(count_in_list(["toto", "tata", "toto"], "tutu")) # output: 0
