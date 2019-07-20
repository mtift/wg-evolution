import unittest
import json
import sys
from datetime import datetime
sys.path.append('..')

from code_df import utils


def read_file(path):
    """
    Given a line-by-line JSON file, this function converts it to
    a Python dictionary and returns all such lines as a list.

    :param path: the path to the JSON file

    :returns items: a list of dictionaries read from the JSON file
    """

    items = list()
    with open(path, 'r') as raw_data:
        for line in raw_data:
            line = json.loads(line)

            items.append(line)
    return items


class TestUtils(unittest.TestCase):
    """
    Tests for utility functions
    """

    def test_str_to_date_commit(self):
        """
        Test whether _str_to_date correctly converts
        a commit's date string to a datetime object.
        """

        date = "Tue Aug 18 18:08:27 2015 +0200"
        expected = datetime.strptime(
                            date,
                            "%a %b %d %H:%M:%S %Y %z") \
            .strftime("%Y-%m-%d")

        expected = datetime.strptime(expected, "%Y-%m-%d")

        datetimeobj = utils.str_to_date(date)
        self.assertEqual(expected, datetimeobj)

    def test_str_to_date_issue(self):
        """
        Test whether str_to_date correctly converts
        a commit's date string to a datetime object.
        """

        date = "2013-10-20T01:56:25Z"
        expected = datetime.strptime(
                            date,
                            "%Y-%m-%dT%H:%M:%SZ") \
            .strftime("%Y-%m-%d")

        expected = datetime.strptime(expected, "%Y-%m-%d")

        datetimeobj = utils.str_to_date(date)
        self.assertEqual(expected, datetimeobj)

    def test_read_json_file(self):
        """
        Test whether read_json_file correctly reads a file of
        Perceval data, where each line in the file is of json format.
        """

        expected = read_file('test_commits_data.json')
        items = utils.read_json_file('test_commits_data.json')

        self.assertEqual(expected, items)


if __name__ == '__main__':
    unittest.main(verbosity=2)
