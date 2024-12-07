import unittest
import tests_12_1, tests_12_2


tournamentsST = unittest.TestSuite()
tournamentsST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_1.RunnerTest))
tournamentsST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(tournamentsST)