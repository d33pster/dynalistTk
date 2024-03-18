# <p align='center'> dynaListTk </p>

![Static Badge](https://img.shields.io/badge/pypi-available-brightgreen?style=flat&logo=Pypi&logoColor=red)
![Static Badge](https://img.shields.io/badge/Linux-supported-blue?style=flat&logo=Linux&logoColor=red)
![Static Badge](https://img.shields.io/badge/Windows-supported-blue?style=flat&logo=Windows&logoColor=red)
![Static Badge](https://img.shields.io/badge/MacOS-supported-blue?style=flat&logo=Macintosh&logoColor=red)
![Static Badge](https://img.shields.io/badge/Tkinter-dependent-yellow?style=flat&logo=tkinter&logoColor=red)
![Static Badge](https://img.shields.io/badge/python-only-green?style=flat&logo=python&logoColor=red)
<br><br><br>

<p align='center'>
    <a href='#Installation'>Installation</a>
    &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
    <a href='#Usage'>Usage</a>
    &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
    <a href='#Screenshots'>Screenshots</a>
</p><br>

## About
dynalistTK extends Tkinter and helps in making Dynamic Lists with multiple columns. It also allows sorting of the columns when you click the column name and has two scrollbars.

## Installation
```console
## requires python3.9 or above with pip installed
## run
$ pip install dynalistTk
```

## Usage

###### dynalistTk class docstring:
```console
"""_summary_
class dynaList: initiate class object

Args:
    master (Tk.Frame | ttk.Frame | Tk | Toplevel): parent frame or Tk window (root window) or Toplevel window (Tk popup)
    headers (list): Column names
    data (list): data to be put
Data Format:
data = [
    (value1_row1, value2_row1, ...),
    (value1_row2, value2_row2, ...),
    ...
]
 """
```

###### usage code example:

```console
###  python code:

# import the packaged
from tkinter import Tk, Toplevel
from dynalistTk import dynalistTk

# define column headers
headers = ['column1', 'column2']

# define column data
data = [
    (1, 2),
    (3, 4),
    (90, 100)
]

# create a main root window using tkinter
root = Tk()

# create a list for the whole screen
list_control = dynalistTk(root, headers, data)


# start mainloop
root.mainloop()

```

->-> The above code will generate:

| column1 | column2 |
| ------- | ------- |
|    1    |    2    |
|    3    |    4    |
|    90   |   100   |

## Screenshots
<img src='images/test.png'>