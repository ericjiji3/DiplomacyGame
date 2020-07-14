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
                              ["D", "Austin", "Move", "London"])

    def test_read_3(self):
        s = "A Madrid Hold\nB Barcelona Move Madrid\nC London Move Madrid\nD Paris Support B\n"
        i = diplomacy_read(s)
        self.assertEqual(i,  [[["A", "Madrid", "Hold"], ["B", "Barcelona", "Move", "Madrid"], ["C", "London", "Move", "Madrid"],\n
                              ["D", "Paris", "Support", "B"]])

    # ----
    # eval
    # ----

    def test_eval(self):
        v = diplomacy_eval(["A", "Madrid", "Hold"])
        self.assertEqual(v, ["A", "Madrid"])

    def test_eval_2(self):
        v = diplomacy_eval(["B", "Barcelona", "Move", "Madrid"])
        self.assertEqual(v, ["B", "Madrid"])

    def test_eval_3(self):
        v = diplomacy_solve(["C", "London", "Move", "Madrid"])
        self.assertEqual(v, ["C", "Madrid"])

    def test_eval_4(self):
        v = diplomacy_solve(["D", "Paris", "Support", "B"])
        self.assertEqual(v, ["D", "Paris", "Support", "B"])


    # -----
    # print
    # -----

    def test_print(self):
        w = StringIO()
        diplomacy_print(w, ["A", "Madrid", "Hold"])
        self.assertEqual(w.getvalue(), "A Madrid Hold\n")

    def test_print_2(self):
        w = StringIO()
        diplomacy_print(w, ["B", "Barcelona", "Move", "Madrid"])
        self.assertEqual(w.getvalue(), "B Barcelona Move Madrid\n")

    def test_print_3(self):
        w = StringIO()
        diplomacy_print(w, ["D", "Paris", "Support", "B"])
        self.assertEqual(w.getvalue(), "D Paris Support B\n")

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
