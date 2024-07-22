# Intro

This is for the DroneBlocks 2.0 camp!


# Modules to Install:

```bash
pip install droneblocks-python-utils
```

```bash
pip install keyboard
```
Run the following code:

```Python
import cv2
import droneblocks

print("Hello!")
```


In the case of the following error:
```text
RuntimeError: module compiled against ABI version 0x1000009 but this version of numpy is 0x2000000
```

Please run the following in the command prompt:

```Python
pip uninstall numpy
pip install numpy==2.0.0
```
