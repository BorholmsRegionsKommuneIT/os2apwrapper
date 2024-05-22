# os2apwrapper

[![PyPI - Version](https://img.shields.io/pypi/v/os2apwrapper.svg)](https://pypi.org/project/os2apwrapper)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/os2apwrapper.svg)](https://pypi.org/project/os2apwrapper)

-----

## Table of Contents

- [os2apwrapper](#os2apwrapper)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
    - [Update](#update)
  - [License](#license)
  - [How to](#how-to)
    - [Setup](#setup)
    - [Use](#use)

## Installation

```console
pip install os2apwrapper@git+https://github.com/BorholmsRegionsKommuneIT/os2apwrapper@main
```

### Update
To update you'll need to add the `--force-reinstall` parameter to the pip install command. This command can also be used as the install command.
```console
pip install --force-reinstall os2apwrapper@git+https://github.com/BorholmsRegionsKommuneIT/os2apwrapper@main
```
If your project is using older versions of the modules that this project is using, you might need to add the `--update` parameter in between `install` and `--force-reinstall`.

## License

`os2apwrapper` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.

## How to
### Setup
1) First you'll need the os2autoprocess apikey, without it this module won't work.
2) Now create a file only containing the apikey as plaintext, and copy the absolute path to to this file.
3) Create a .env file to the root of this project.
4) Inside the .env file add a varible called `api_key_path` and give it the filepath as it's value:
```
api_key_path=yourfilepathtotheapikey.txt
```
### Use
1) Add to your python project: `from os2apwrapper import os2apwrapper`
2) Create a class object like so: 
   ```
   client = os2apwrapper.ApiClass()
   ```
3) Now simply call it using the ID of the process you wish to update, along with the new phase and/or status like so:
   ```
   client.update_process(5211, "DEVELOPMENT", "INPROGRESS")
   ```
   Note that once you start typing the string for phase/status auto-complete options should show up. These are the only allowed values.
```
# Import module
from os2apwrapper import os2apwrapper

# Instantiate the ApiClient as client
client = os2apwrapper.ApiClient()

# Change process 5211's phase to 'operation', and status to 'inprogress'
client.update_process(5211, "OPERATION", "INPROGRESS")
```