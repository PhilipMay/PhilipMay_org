# pytest

## Fixtures

## Parametrize

## Flaky Tests

- rerun flaky tests
- see [pytest-rerunfailures](https://github.com/pytest-dev/pytest-rerunfailures)

```python
import pytest

# reruns_delay is in seconds and optional
@pytest.mark.flaky(reruns=5, reruns_delay=2)
def test_example():
    assert random.choice([True, False])
```
