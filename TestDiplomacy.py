# TestDiplomacy.py
# unit tests that test corner and failure cases for diplomacy_solve()

from unittest import main, TestCase

from Diplomacy import diplomacy_read, diplomacy_solve

# -------------
# TestDiplomacy
# -------------


class TestCollatz (TestCase):

    # ----
    # read
    # ----

    def test_read(self):
        s = "A Madrid Hold\nB Barcelona Move Madrid\nC London Move Madrid\nD Paris Support B\nE Austin Support A\n"
        i = diplomacy_read(s)
        self.assertEqual(i,  [["A", "Madrid", "Hold"], ["B", "Barcelona", "Move", "Madrid"], ["C", "London", "Move", "Madrid"],\n
                              ["D", "Paris", "Support", "B"], ["E", "Austin", "Support", "A"]])

    def test_read_2(self):
        s = "A Madrid Hold\nB Barcelona Move Madrid\nC London Support B\nD Austin Move London\n"
        i = diplomacy_read(s)
        self.assertEqual(i,  [["A", "Madrid", "Hold"], ["B", "Barcelona", "Move", "Madrid"], ["C", "London", "Support", "B"],\n
                              ["D", "Austin", "Move", "London"]])

    def test_read_3(self):
        s = "A Madrid Hold\nB Barcelona Move Madrid\nC London Move Madrid\nD Paris Support B\n"
        i = diplomacy_read(s)
        self.assertEqual(i,  [["A", "Madrid", "Hold"], ["B", "Barcelona", "Move", "Madrid"], ["C", "London", "Move", "Madrid"],\n
                              ["D", "Paris", "Support", "B"]])

    # ----
    # eval
    # ----

    def test_eval(self):
        v = diplomacy_eval([["A", "Madrid", "Hold"], ["B", "Barcelona", "Move", "Madrid"], ["C", "London", "Move", "Madrid"],\n
                              ["D", "Paris", "Support", "B"], ["E", "Austin", "Support", "A"]])
        self.assertEqual(v, [["A", "[dead]"], ["B", "[dead]"], ["C", "[dead]"], ["D", "Paris"], ["E", "Austin"]])

    def test_eval_2(self):
        v = diplomacy_eval([["A", "Madrid", "Hold"], ["B", "Barcelona", "Move", "Madrid"], ["C", "London", "Support", "B"],\n
                              ["D", "Austin", "Move", "London"]])
        self.assertEqual(v, [["A", "[dead]"], ["B", "[dead]"], ["C", "[dead]"], ["D", "[dead]"]])

    def test_eval_3(self):
        v = diplomacy_solve([["A", "Madrid", "Hold"], ["B", "Barcelona", "Move", "Madrid"], ["C", "London", "Move", "Madrid"],\n
                              ["D", "Paris", "Support", "B"]])
        self.assertEqual(v, [["A", "[dead]"], ["B", "Madrid"], ["C", "[dead]"], ["D", "Paris"]])

    # -----
    # print
    # -----

    def test_print(self):
        w = StringIO()
        diplomacy_print(w, ["A", "Madrid"])
        self.assertEqual(w.getvalue(), "A Madrid\n")

    def test_print_2(self):
        w = StringIO()
        diplomacy_print(w, ["B", "[dead]"])
        self.assertEqual(w.getvalue(), "B [dead]\n")

    def test_print_3(self):
        w = StringIO()
        diplomacy_print(w, ["D", "Paris"])
        self.assertEqual(w.getvalue(), "D Paris\n")

    # -----
    # solve
    # -----

    def test_solve(self):
        r = StringIO("A Madrid Hold\nB Barcelona Move Madrid\nC London Move Madrid\nD Paris Support B\nE Austin Support A\n")
        w = StringIO()
        diplomacy_solve(r, w)
        self.assertEqual(
            w.getvalue(), "A [dead]\nB [dead]\nC [dead]\nD Paris\nE Austin\n")

    def test_solve_2(self):
        r = StringIO("A Madrid Hold\nB Barcelona Move Madrid\nC London Support B\nD Austin Move London\n")
        w = StringIO()
        diplomacy_solve(r, w)
        self.assertEqual(
            w.getvalue(), "A [dead]\nB [dead]\nC [dead]\nD [dead]\n")

    def test_solve_3(self):
        r = StringIO("A Madrid Hold\nB Barcelona Move Madrid\nC London Move Madrid\nD Paris Support B\n")
        w = StringIO()
        diplomacy_solve(r, w)
        self.assertEqual(
            w.getvalue(), "A [dead]\nB Madrid\nC [dead]\nD Paris\n")
