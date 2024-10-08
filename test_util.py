import unittest

from util import filterFirstOccurrences


class TestUtil(unittest.TestCase):
    def test_filterFirstOccurrences(self):
        self.assertEqual(
            filterFirstOccurrences([[1, 2], [1, 3], [2, 4], [3, 4]]), [[1, 2], [2, 4]]
        )
        self.assertNotEqual(
            filterFirstOccurrences([[1, 2], [1, 3], [2, 4], [3, 4]]),
            [[1, 2], [1, 3], [2, 4], [3, 4]],
        )
        self.assertEqual(
            filterFirstOccurrences(
                [
                    [
                        'neuropathy-ccu000-diabetes---secondary.cwl',
                        'polyneuropathy-ccu002_01-diabetes-and-diabates-medication---primary.cwl',
                    ],
                    [
                        'neuropathy-ccu000-diabetes---secondary.cwl',
                        'nephropathy-ccu002_01-diabetes-and-diabates-medication---primary.cwl',
                    ],
                    [
                        'ccu000-diabetes-warning---secondary.cwl',
                        'ccu002_01-diabetes-and-diabates-medication-warning---primary.cwl',
                    ],
                    [
                        'neuropathic-ccu000-diabetes---secondary.cwl',
                        'neuropathy-ccu002_01-diabetes-and-diabates-medication---primary.cwl',
                    ],
                    [
                        'neuropathy-ccu000-diabetes---secondary.cwl',
                        'neuropathy-ccu002_01-diabetes-and-diabates-medication---primary.cwl',
                    ],
                    [
                        'macular-ccu000-diabetes---secondary.cwl',
                        'macular-ccu002_01-diabetes-and-diabates-medication---primary.cwl',
                    ],
                ],
            ),
            [
                [
                    'neuropathy-ccu000-diabetes---secondary.cwl',
                    'polyneuropathy-ccu002_01-diabetes-and-diabates-medication---primary.cwl',
                ],
                [
                    'ccu000-diabetes-warning---secondary.cwl',
                    'ccu002_01-diabetes-and-diabates-medication-warning---primary.cwl',
                ],
                [
                    'neuropathic-ccu000-diabetes---secondary.cwl',
                    'neuropathy-ccu002_01-diabetes-and-diabates-medication---primary.cwl',
                ],
                [
                    'macular-ccu000-diabetes---secondary.cwl',
                    'macular-ccu002_01-diabetes-and-diabates-medication---primary.cwl',
                ],
            ],
        ),


unittest.main(argv=[''], verbosity=2, exit=False)
