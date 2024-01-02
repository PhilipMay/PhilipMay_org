# Python Programming

## Ignore an Exception

Suppresses specified exception.

```python
import contextlib

with contextlib.suppress(FileNotFoundError):
    os.remove(os.path.join(dirname, filename))
```
