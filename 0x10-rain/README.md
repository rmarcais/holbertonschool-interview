# 0x10. Rain

<p align="center">
<img src="https://www.digitalmomblog.com/wp-content/uploads/2022/03/you-cant-stop-the-rain-meme.jpg" alt="meme">
</p>

## Requirements
### General
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 14.04 LTS using `python3` (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `PEP 8` style (version 1.7.x)
- You are not allowed to import any module
- All modules and functions must be documented
- All your files must be executable

## Task 0: Rain

Given a list of non-negative integers representing the heights of walls with unit width 1, as if viewing the cross-section of a relief map, calculate how many square units of water will be retained after it rains.

- Prototype: `def rain(walls)`
- `walls` is a list of non-negative integers.
- Return: Integer indicating total amount of rainwater retained.
- Assume that the ends of the list (before index 0 and after index walls[-1]) are not walls, meaning they will not retain water.
- If the list is empty return `0`.

## Main file

```
#!/usr/bin/python3
"""
0_main
"""
rain = __import__('0-rain').rain

if __name__ == "__main__":
    walls = [0, 1, 0, 2, 0, 3, 0, 4]
    print(rain(walls))
    walls = [2, 0, 0, 4, 0, 0, 1, 0]
    print(rain(walls))
```

## Expected output

```
remi@ubuntu:~/0x10$ ./0_main.py
6
6
remi@ubuntu:~/0x10$ 
```

Visual representation of the walls `[0, 1, 0, 2, 0, 3, 0, 4]`

<p align="center">
<img src="./rain_1.png" alt="meme">
</p>

Visual representation of the walls `[2, 0, 0, 4, 0, 0, 1, 0]`

<p align="center">
<img src="./rain_2.png" alt="meme">
</p>
