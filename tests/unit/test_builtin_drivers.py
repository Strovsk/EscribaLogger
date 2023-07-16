from src.drivers import driver_stdout, driver_file, DriverOption
from rich.logging import RichHandler
from logging import FileHandler
import pytest


@pytest.fixture
def stdout_stream():
    return driver_stdout()


@pytest.fixture
def file_stream():
    options: DriverOption = {"file_location": "logs"}
    return driver_file(options)


def test_driver_stdout_should_be_a_stream(stdout_stream: RichHandler):
    assert isinstance(stdout_stream, RichHandler)


def test_driver_stdout_should_init_in_debug_mode(stdout_stream: RichHandler):
    stream_level = stdout_stream.level
    debug_code = 10
    assert stream_level == debug_code


def test_driver_file_should_be_a_stream(file_stream: FileHandler):
    assert isinstance(file_stream, FileHandler)


def test_driver_file_should_init_in_debug_mode(file_stream: FileHandler):
    stream_level = file_stream.level
    debug_code = 0
    assert stream_level == debug_code