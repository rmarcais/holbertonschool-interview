# 0x1F-pascal_triangle

<p align="center">
<img src="https://miro.medium.com/v2/resize:fit:958/1*7g4Dq4vhGVT5Prn-AYbL5A.jpeg">
</p>

## Task 0: Pascal's Triangle

Create a function `def pascal_triangle(n):` that returns a list of lists of integers representing the Pascal’s triangle of `n`:

- Returns an empty list if `n <= 0`
- You can assume `n` will be always an integer

### Main file

```
#!/usr/bin/python3
"""
0-main
"""
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))

```

### Expected output

```
remi@ubuntu:~/0x1F$ ./0-main.py
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
remi@ubuntu:~/0x1F$ 
```
