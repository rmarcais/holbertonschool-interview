![Holberton France Logo](https://images.squarespace-cdn.com/content/v1/60bf70d860f31b4f60455443/1625061110826-904UGWRZ9PX81YWARXMT/HolbertonFRANCEFichier+16.png?format=1500w)

# 0x00. Lockboxes

![meme](https://cdn.memegenerator.es/imagenes/memes/full/27/76/27763391.jpg)

## Requirements
### General
- Allowed editors: ```vi```, ```vim```, ```emacs```
- All your files will be interpreted/compiled on Ubuntu 14.04 LTS using ```python3``` (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly ```#!/usr/bin/python3```
- A ```README.md``` file, at the root of the folder of the project, is mandatory
- Your code should be documented
- Your code should use the ```PEP 8``` style (version 1.7.x)
- All your files must be executable

## Context
You have n number of locked boxes in front of you. Each box is numbered sequentially from 0 to n - 1 and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.

- Prototype: ```def canUnlockAll(boxes)```
- ```boxes``` is a list of lists
- A key with the same number as a box opens that box
- You can assume all keys will be positive integers
   - There can be keys that do not have boxes
- The first box ```boxes[0]``` is unlocked
- Return ```True``` if all boxes can be opened, else return ```False```

### Main file
```
remi@ubuntu:~/0x00-lockboxes$ cat main_0.py
#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))

remi@ubuntu:~/0x00-lockboxes$
```

### Expected output

```
remi@ubuntu:~/0x00-lockboxes$ ./main_0.py
True
True
False
remi@ubuntu:~/0x00-lockboxes$
```