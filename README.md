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
  - [How to use](#how-to-use)

## Installation

```console
pip install os2apwrapper@git+https://github.com/BorholmsRegionsKommuneIT/os2apwrapper@main
```

### Update
To update you'll need to add the `--force-reinstall` parameter to the pip install command. This command can also be used as the install command.
```console
pip install --force-reinstall os2apwrapper@git+https://github.com/BorholmsRegionsKommuneIT/os2apwrapper@main
```
If you don't want to also reinstall the dependencies you can add the following parameter `--no-deps`.

If your project is using older versions of the packages that this project is using, you might need to add the `--update` parameter in between `install` and `--force-reinstall`.

## License

`os2apwrapper` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.

## How to use
1) First you'll need the os2autoprocess apikey. Get it from [Digital Identity](https://www.digital-identity.dk/) 
2) Now create a file only containing the apikey as plaintext, and copy the absolute path to to this file.
3) Create a .env file at the root of this project.
4) Inside the .env file add a varible called `api_key_path` and give it the filepath as it's value:
```
api_key_path=your/file/path/totheapikey.txt
```

5) Import, create a class object and call a class method with the ID of the process you wish to update, along with the new phase and/or status like so:
   ```
   from os2apwrapper import ApiClient
   
   os2ap = ApiClient()

   os2ap.update_process(5211, "DEVELOPMENT", "INPROGRESS")
   ```

   Note that once you start typing the string for phase/status auto-complete options should show up. These are the only allowed values.
