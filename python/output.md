# output

1. unbuffered stdout

   ```python
   print("output message", flush=True)
   ```

   ```python
   import sys
   sys.stdout.write("this is output message")
   sys.stdout.flush()
   ```

   ```shell
   python -u xxx.py
   ```

   ```python
   import os
   os.environ["PYTHONUNBUFFERED"]= "1"
   ```
