from src.Log import Log
import pytest
import logging


@pytest.fixture
def log_obj():
    return Log()


def test_log_should_be_a_singleton(log_obj: Log):
    assert log_obj == Log()


def test_log_can_change_name():
    default_logger_name = Log.log_name()
    new_logger_name = "my_logger_test"
    Log.root_logger.name = new_logger_name
    assert Log.log_name() == new_logger_name and Log.log_name() != default_logger_name


def test_log_can_add_drivers():
    number_of_default_drivers = len(Log.root_logger.handlers)
    Log.add_driver("stdout")
    number_of_current_drivers = len(Log.root_logger.handlers)
    Log.clear_drivers()
    assert number_of_current_drivers == 1 and number_of_default_drivers == 0


def test_log_cannot_add_same_driver_twice():
    number_of_default_drivers = len(Log.root_logger.handlers)
    Log.add_driver("stdout")
    Log.add_driver("stdout")
    number_of_current_drivers = len(Log.root_logger.handlers)
    Log.clear_drivers()
    assert number_of_current_drivers == 1 and number_of_default_drivers == 0


def test_log_can_right_info(mocker):
    mocker.patch("logging.Logger.info")
    Log.info("message")
    assert logging.Logger.info.assert_called_with("message", extra=None) is None

    custom_extra = {"custom": "value"}
    Log.info("another message", extra=custom_extra)
    assert (
        logging.Logger.info.assert_called_with("another message", extra=custom_extra)
        is None
    )


def test_log_can_right_warning(mocker):
    mocker.patch("logging.Logger.warning")
    Log.warn("message")
    assert logging.Logger.warning.assert_called_with("message", extra=None) is None

    custom_extra = {"custom": "value"}
    Log.warn("another message", extra=custom_extra)
    assert (
        logging.Logger.warning.assert_called_with("another message", extra=custom_extra)
        is None
    )


def test_log_can_right_error(mocker):
    mocker.patch("logging.Logger.error")
    Log.error("message")
    assert logging.Logger.error.assert_called_with("message", extra=None) is None

    custom_extra = {"custom": "value"}
    Log.error("another message", extra=custom_extra)
    assert (
        logging.Logger.error.assert_called_with("another message", extra=custom_extra)
        is None
    )


def test_log_can_right_critical(mocker):
    mocker.patch("logging.Logger.critical")
    Log.critical("message")
    assert logging.Logger.critical.assert_called_with("message", extra=None) is None

    custom_extra = {"custom": "value"}
    Log.critical("another message", extra=custom_extra)
    assert (
        logging.Logger.critical.assert_called_with(
            "another message", extra=custom_extra
        )
        is None
    )
