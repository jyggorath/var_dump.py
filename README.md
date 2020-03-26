# var_dump.py
I know PHP can be a controversial subject, but one of the things that are really useful in PHP, is the [var_dump()](https://www.php.net/manual/en/function.var-dump.php) function. This is something I have been genuinly missing in Python, so I decided to make a module implementation of it myself.

## How to use
After installing the module, just import it and use it:
```python
import var_dump
var_dump.var_dump('I am a string')
```
```python
from var_dump import var_dump
var_dump('I am a string')
```

## Todo
I might look into a fix for the indentation when dumping dicts. There is currently an issue with lists and dicts within a dict.