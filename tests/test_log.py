from src.decorators import log


@log("test.txt")
def test_log_with_file() -> str:
    return "Test data"


@log("")
def test_log_without_file() -> str:
    return "Test data without file"
