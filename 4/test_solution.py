import unittest
import solution
from io import StringIO

class TestSolution1(unittest.TestCase):
    def setUp(self):
        self.data = StringIO("""ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in""")

    def test_single_field(self):
        result = solution.extract_passports(StringIO("iyr:2013"))
        self.assertEqual(result[0], {"iyr":"2013"})

    def test_extract_single_passport_single_line(self):
        result = solution.extract_passports(StringIO("ecl:gry pid:860033327 eyr:2020 hcl:#fffffd"))
        expected = {"ecl":"gry","pid":"860033327", "eyr":"2020","hcl":"#fffffd"}
        self.assertEqual(result[0], expected)

    def test_extract_single_passport_multi_line(self):
        input_data = StringIO("""hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm
""")
        result = solution.extract_passports(input_data)
        expected = {
            "hcl":"#ae17e1",
            "iyr":"2013",
            "eyr":"2024", 
            "ecl":"brn",
            "pid":"760753108",
            "byr":"1931",
            "hgt":"179cm",
        }
        self.assertEqual(result[0], expected)

    def test_extract_multiple_passport(self):

        results = solution.extract_passports(self.data)
        self.assertEqual(len(results), 4)

    def test_passport_with_cid_valid(self):
        input_data = {
            "ecl":"gry",
            "pid":"860033327",
            "eyr":"2020",
            "hcl":"#fffffd",
            "byr":"1937",
            "iyr":"2017",
            "cid":"147",
            "hgt":"183cm",
        }
        result = solution.validate_passport(input_data)
        self.assertEqual(result, True, f"data {input_data.keys()} must be True")

    def test_passport_without_cid_valid(self):
        input_data = {
            "ecl":"gry",
            "pid":"860033327",
            "eyr":"2020",
            "hcl":"#fffffd",
            "byr":"1937",
            "iyr":"2017",
            "hgt":"183cm",
        }
        result = solution.validate_passport(input_data)
        self.assertEqual(result, True, f"data must have {input_data.keys()} in True")

    def test_passport_invalid(self):
        input_data = {
            "ecl":"gry",
            "pid":"860033327",
            "eyr":"2020",
            "hcl":"#fffffd",
            "byr":"1937",
            "iyr":"2017",
            "cid":"147",
        }
        result = solution.validate_passport(input_data)
        self.assertEqual(result, False, f"data {input_data} must be False")

    def test_count_valid(self):
        result = solution.valid_count(self.data)
        self.assertEqual(result, 2)

    def test_validate_number_valid(self):
        result = solution.validate_number("2021", low=2020, high=2030)
        self.assertEqual(result, True)

    def test_validate_number_invalid(self):
        result = solution.validate_number("2019", low=2020, high=2030)
        self.assertEqual(result, False)

    def test_validate_hgt_cm_valid(self):
        result = solution.validate_hgt("190cm")
        self.assertEqual(result, True)

    def test_validate_hgt_cm_invalid(self):
        result = solution.validate_hgt("149cm")
        self.assertEqual(result, False)

    def test_validate_hgt_in_valid(self):
        result = solution.validate_hgt("60in")
        self.assertEqual(result, True)

    def test_validate_hgt_in_invalid(self):
        result = solution.validate_hgt("190in")
        self.assertEqual(result, False)

    def test_validate_ecl_valid(self):
        result = solution.validate_ecl("amb")
        self.assertEqual(result, True)

    def test_validate_ecl_invalid(self):
        result = solution.validate_ecl("org")
        self.assertEqual(result, False)

    def test_validate_hcl_valid(self):
        result = solution.validate_hcl("#123abc")
        self.assertEqual(result, True)

    def test_validate_hcl_invalid_hex(self):
        result = solution.validate_hcl("#123abz")
        self.assertEqual(result, False)

    def test_validate_hcl_invalid(self):
        result = solution.validate_hcl("123abc")
        self.assertEqual(result, False)

    def test_validate_pid_valid(self):
        result = solution.validate_pid("000000001")
        self.assertEqual(result, True)

    def test_validate_pid_invalid(self):
        result = solution.validate_pid("0123456789")
        self.assertEqual(result, False)

    def test_invalid_count_strict(self):
        input_data = StringIO("""eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007""")
        count = solution.valid_count(input_data, strict=True)
        self.assertEqual(count, 0)

    def test_valid_count_strict(self):
        input_data = StringIO("""pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
""")
        count = solution.valid_count(input_data, strict=True)
        self.assertEqual(count, 4)

if __name__ == "__main__":
    unittest.main()
