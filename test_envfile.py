import pytest
import subprocess


def test_printenv():
    output = subprocess.check_output(
        ['envfile', '--clear', 'printenv'])
    assert output.decode().strip() == 'test=printenv'


def test_printenv_upper():
    output = subprocess.check_output(
        ['envfile', '--clear', '--upper', 'printenv'])
    assert output.decode().strip() == 'TEST=printenv'


def test_section():
    output = subprocess.check_output(
        ['envfile', '--clear', '--section', 'foo', 'printenv'])
    assert output.decode().strip() == 'test=foo'


def test_missing_section():
    with pytest.raises(subprocess.CalledProcessError):
        subprocess.check_output(
            ['envfile', '--section', 'missing', 'printenv'])


def test_missing_file():
    with pytest.raises(subprocess.CalledProcessError):
        subprocess.check_output(
            ['envfile', '--config', 'missing.ini', 'printenv'])


def test_args():
    output = subprocess.check_output(
        ['envfile', '--section', 'foo', '--', 'echo', '-a', 'b'])
    assert output.decode().strip() == '-a b'
