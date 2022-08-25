[![Gate](https://github.com/szitasg/szitas-logger/actions/workflows/gate.yml/badge.svg?branch=master)](https://github.com/szitasg/szitas-logger/actions/workflows/gate.yml)
[![Tag](https://img.shields.io/github/tag/szitasg/szitas-logger?include_prereleases=&sort=semver)](https://github.com/szitasg/szitas-logger/releases)
[![License](https://img.shields.io/github/license/szitasg/szitas-logger)](https://github.com/szitasg/szitas-logger/blob/master/LICENSE.md)
[![Issues](https://img.shields.io/github/issues/szitasg/szitas-logger)](https://github.com/szitasg/szitas-logger/issues)
[![PyPI - Downloads](https://img.shields.io/pypi/dd/szitas-logger)](https://pypi.org/project/szitas-logger/)

# szitas-logger

## Overview

This project is my japl (just another python logger) project which I'm using for
years but newer goes to public.

## Usage

```python
from szitas_logger.logger import Logger

Logger(log_file='./debug.log')

log = Logger.get_logger()
```

## Features

### Multiline message

```python
log.info('This is a\nmultiline message')
```

```bash
<asctime> [<module>] [INFO   ] This is a
<asctime> [<module>] [INFO   ]    multiline message
```

### Elapsed time

Measure time duration between `timer_start()` and `timer_end()`

Code snippet
```python
log.timer_start()
...
log.timer_end()
```

Console example
```bash
[INFO   ] Elapsed time <duration>
```

Logfile example
```bash
<asctime> [<module>] [DEBUG  ] Timer start
<asctime> [<module>] [DEBUG  ] Timer end
<asctime> [<module>] [INFO   ] Elapsed time <duration>
```

### KeyboardInterrupt


## License

Apache License, Version 2.0
