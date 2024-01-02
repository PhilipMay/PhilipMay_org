# pytest

## Fixtures

```python
import pytest

@pytest.fixture
def my_value():
    return 5

def test_my_fruit_in_basket(my_value):
    result = my_value + 5
    assert result == 10
```

- also see <https://docs.pytest.org/en/6.2.x/fixture.html#back-to-fixtures>

## Parametrize

## Skip Tests

## Expect Test to fail

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
