#!/usr/bin/env python
import os
import sys


if __name__ == "__main__":
    os.environ['DJANGAE_APP_YAML_LOCATION'] = os.path.abspath(
        os.path.dirname(__file__)
    )
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    sys.path.insert(1, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sitepackages'))
    from djangae.core.management import execute_from_command_line, test_execute_from_command_line
    if 'test' in sys.argv:
        test_execute_from_command_line(sys.argv)
    else:
        execute_from_command_line(sys.argv)
