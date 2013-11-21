import unittest
import math

from ulib import typetools


##### Public classes #####
class TestTypeTools(unittest.TestCase) :
    def __init__(self, *args_tuple, **kwargs_dict) :
        self.__from_dict = {
            "a" : {
                "b" : {
                    "c" : (),
                    "d" : None,
                    "e" : (1, 2, 3),
                },
                "f" : {
                    "c" : 10,
                },
            },
        }
        self.__to_tuple = (
            (("a", "b", "c"), ()),
            (("a", "b", "d"), None),
            (("a", "b", "e"), (1, 2, 3)),
            (("a", "f", "c"), 10),
        )
        self.__to_plain_list = [
            ("a", [
                ('b', [
                    ('c', ()),
                    ('d', None),
                    ('e', (1, 2, 3)),
                ]),
                ('f', [('c', 10)]),
            ]),
        ]
        unittest.TestCase.__init__(self, *args_tuple, **kwargs_dict)

    def test_riter(self) :
        self.assertEqual(set(typetools.riter(self.__from_dict, 2)), set(self.__to_tuple))

    def test_has_keys_chain_true(self) :
        self.assertTrue(typetools.hasKeysChain(self.__from_dict, ("a", "b", "c")))

    def test_has_keys_chain_false(self) :
        self.assertFalse(typetools.hasKeysChain(self.__from_dict, ("a", "x")))

    ###

    def test_dict_to_list(self) :
        self.assertEqual(typetools.dictToList(self.__from_dict), self.__to_plain_list)

    def test_object_hash(self) :
        self.assertEqual(typetools.objectHash(self.__from_dict), "978aaff92cac6157a5651f48febbb43782a600aa")

    ###

    def test_extend_replace(self) :
        self.assertEqual(
            typetools.extendReplace(
                [1, 2, 3, 4, 5],
                3,
                [30, 40, 50],
            ),
            [1, 2, 30, 40, 50, 4, 5],
        )

    def test_chunks(self) :
        self.assertEqual(
            typetools.chunks([1, 2, 3, 4, 5, 6, 7], 2),
            [[1, 2], [3, 4], [5, 6], [7]],
        )

    ###

    def test_pmap_one_process(self) :
        self.assertEqual(
            typetools.pmap(math.sqrt, range(1000)),
            list(map(math.sqrt, range(1000))),
        )

    def test_pmap_multiprocessing(self) :
        self.assertEqual(
            typetools.pmap(math.sqrt, range(1000), 10),
            list(map(math.sqrt, range(1000))),
        )

    ###

    def test_median(self) :
        self.assertEqual(typetools.median((5, 2, 4, 3, 1, 6)), 3.5)
        self.assertEqual(typetools.median((5, 2, 3, 1, 6)), 3)
        self.assertEqual(typetools.median((1,)), 1)
        self.assertEqual(typetools.median((1,2)), 1.5)
        self.assertEqual(typetools.median((1,2,7)), 2)

    def test_average(self) :
        self.assertEqual(typetools.average((9, 1, 4, 0, 3, 4)), 3.5)

    def test_average_one(self) :
        self.assertEqual(typetools.average((1,)), 1)

