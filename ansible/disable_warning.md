# disable warning

1. [WARNING]: ... is using the discovered Python interpreter at /usr/bin/python, but future installation of another Python
interpreter could change the meaning of that path.
   - solution 1: [change environment](https://docs.ansible.com/ansible/latest/reference_appendices/config.html#envvar-ANSIBLE_PYTHON_INTERPRETER)

Path to the Python interpreter to be used for module execution on remote targets, or an automatic discovery mode. Supported discovery modes are auto (the default), auto_silent, auto_legacy, and auto_legacy_silent. All discovery modes employ a lookup table to use the included system Python (on distributions known to include one), falling back to a fixed ordered list of well-known Python interpreter locations if a platform-specific default is not available. The fallback behavior will issue a warning that the interpreter should be set explicitly (since interpreters installed later may change which one is used). This warning behavior can be disabled by setting auto_silent or auto_legacy_silent. The value of auto_legacy provides all the same behavior, but for backwards-compatibility with older Ansible releases that always defaulted to /usr/bin/python, will use that interpreter if present.
