# Application Logging in Python

## Table Of Contents

- Once your **Python application** is running in production, it becomes a black box. You can no longer attach a **debugger** or **inspect variables** in real time. Your only insight into what it’s doing comes from the signals it emits: **logs**, **metrics**, **traces**, and other forms of telemetry.

# Logging Module

- Python’s built-in `logging` module
- Every call to a logging method (like `logger.info()`) creates a **LogRecord** object, which flows through a processing pipeline composed of four core components: the `Logger`, `Handler`, `Formatter`, and `Filter`. Your entry point into this system is the Logger object, and there is a golden rule for acquiring one: **always use** `logging.getLogger(<name>)`
- Ignore examples that call level methods on the logging module (like `logging.warning(...)`) or call `getLogger()` with no arguments. Both invoke the **root logger**, which should be avoided in anything beyond simple scripts.
- The root logger has no namespace, so its output gets mixed with logs from third-party libraries. This makes it difficult to control log levels for specific parts of your code or trace a log message’s origin.
- The correct pattern is to always create a module-specific logger, and the documentation specifically recommends using the special `__name__` variable:

  ```py
    import logging

    # In my_app/services/billing.py, __name__ == "my_app.services.billing"
    logger = logging.getLogger(__name__)
  ```

# Resources and Further Reading

1. [Application Logging in Python: Recipes for Observability](https://www.dash0.com/guides/logging-in-python)
