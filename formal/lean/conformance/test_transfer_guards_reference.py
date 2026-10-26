import importlib.util
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("transfer_guards_reference", ROOT / "transfer_guards_reference.py")
module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(module)


class TransferGuardConformanceTest(unittest.TestCase):
    def test_exhaustive_truth_table_has_64_cases_and_one_positive(self):
        cases = list(module.exhaustive_cases())
        self.assertEqual(len(cases), 64)
        self.assertEqual(sum(int(result) for _, result in cases), 1)
        for facts, result in cases:
            self.assertEqual(result, all(facts[k] for k in module.FIELDS[:5]) and not facts["effect_unknown"])

    def test_each_individual_negative_condition_blocks_transfer(self):
        good = {key: True for key in module.FIELDS[:5]}
        good["effect_unknown"] = False
        self.assertTrue(module.transfer_permitted(good))
        for key in module.FIELDS[:5]:
            broken = dict(good)
            broken[key] = False
            self.assertFalse(module.transfer_permitted(broken), key)
        broken = dict(good)
        broken["effect_unknown"] = True
        self.assertFalse(module.transfer_permitted(broken))

    def test_missing_or_non_boolean_host_facts_fail_closed(self):
        good = {key: True for key in module.FIELDS[:5]}
        good["effect_unknown"] = False
        for key in module.FIELDS:
            broken = dict(good)
            del broken[key]
            with self.assertRaises(ValueError):
                module.transfer_permitted(broken)
        broken = dict(good)
        broken["authority_verified"] = 1
        with self.assertRaises(ValueError):
            module.transfer_permitted(broken)


if __name__ == "__main__":
    unittest.main()
