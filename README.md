# os2apwrapper
Thin wrapper for connecting to the OS2AutoProcess API, only allows updating of a processes "phase" & "status" by ID.

## Setup
1) A file containing the os2autoprocess apikey.
2) If you don't already have a .evn file, you'll need to create one. Add a varible api_key_path, and give it the path to the file containing the os2autoprocess apikey. It should look something like this:

```
api_key_path=insert/your/path/to/apikey/file.txt
```

### Todo
- Change print statements to a logging system