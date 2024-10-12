# FastAPI PrettyErrors Middleware

A FastAPI middleware to prettify exceptions using [PrettyErrors](https://github.com/onelivesleft/PrettyErrors).

## Installation

Install the package via pip:

```
pip install fastapi-pretty-errors
```

Or, if you’re using Poetry:

```
poetry add fastapi-pretty-errors
```

## Usage

Add the middleware to your FastAPI application:

```python
from fastapi import FastAPI
from fastapi_pretty_errors import PrettyErrorsMiddleware

app = FastAPI()
app.add_middleware(PrettyErrorsMiddleware)
```

### Custom Configuration

You can specify custom configuration options for PrettyErrors when adding the middleware. Any keyword arguments passed to PrettyErrorsMiddleware will be forwarded to `pretty_errors.configure()` .

```python
from fastapi import FastAPI
from fastapi_pretty_errors import PrettyErrorsMiddleware

app = FastAPI()

app.add_middleware(
    PrettyErrorsMiddleware,
    # PrettyErrors configuration options
    display_locals=True,
    line_number_first=True,
    lines_before=5,
    lines_after=2,
)
```

For a full list of configuration options, refer to the PrettyErrors [documentation](https://github.com/onelivesleft/PrettyErrors?tab=readme-ov-file#configuration-settings).
