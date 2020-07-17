# TestDiplomacy.py
# unit tests that test corner and failure cases for diplomacy_solve()

from io import StringIO
from unittest import main, TestCase

from Diplomacy import diplomacy_solve, diplomacy_eval, diplomacy_print

# -------------
# TestDiplomacy
# -------------


class TestDiplomacy (TestCase):

    # ----
    # eval
    # ----

    def test_eval(self):
        v = diplomacy_eval([["A", "Madrid", "Hold"], ["B", "Barcelona", "Move", "Madrid"], ["C", "London", "Move", "Madrid"], ["D", "Paris", "Support", "B"], ["E", "Austin", "Support", "A"]])
        self.assertEqual(v, {"Madrid":[["A",1], ["B",1], ["C",0]], "Paris":[["D",0]], "Austin":[["E",0]]})

    def test_eval_2(self):
        v = diplomacy_eval([["A", "Madrid", "Hold"], ["B", "Barcelona", "Move", "Madrid"], ["C", "London", "Support", "B"], ["D", "Austin", "Move", "London"]])
        self.assertEqual(v, {"Madrid":[["A",0],["B",0]], "London":[["C",0], ["D",0]]})

    def test_eval_3(self):
        v = diplomacy_eval([["A", "Madrid", "Hold"], ["B", "Barcelona", "Move", "Madrid"], ["C", "London", "Move", "Madrid"], ["D", "Paris", "Support", "B"]])
        self.assertEqual(v, {"Madrid":[["A",0],["B",1],["C",0]],"Paris":[["D",0]]})

    # -----
    # print
    # -----

    def test_print(self):
        w = StringIO()
        diplomacy_print(w, {"Madrid":[["A",1], ["B",1], ["C",0]], "Paris":[["D",0]], "Austin":[["E",0]]})
        self.assertEqual(w.getvalue(), "A [dead]\nB [dead]\nC [dead]\nD Paris\nE Austin\n")

    def test_print_2(self):
        w = StringIO()
        diplomacy_print(w, {"Madrid":[["A",0],["B",0]], "London":[["C",0], ["D",0]]})
        self.assertEqual(w.getvalue(), "A [dead]\nB [dead]\nC [dead]\nD [dead]\n")

    def test_print_3(self):
        w = StringIO()
        diplomacy_print(w, {"Madrid":[["A",0],["B",1],["C",0]],"Paris":[["D",0]]})
        self.assertEqual(w.getvalue(), "A [dead]\nB Madrid\nC [dead]\nD Paris\n")

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
