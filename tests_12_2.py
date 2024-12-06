from runner_and_tournament import Runner, Tournament
import unittest


class TournamentTest(unittest.TestCase):


    @classmethod
    def setUpClass(cls) -> None:
        cls.all_results = {}

    def setUp(self) -> None:
        self.usain = Runner('Усэйн', 10)
        self.andrei = Runner('Андрей', 9)  # быстрый, однако, парень
        self.nick = Runner('Ник', 3)


    def test_start1(self):
        tour1 = Tournament(90, self.usain, self.nick)
        # для более понятной структуры из объектов (Runner) вытаскиваю позицию и участника
        TournamentTest.all_results['tour1'] = {
            place: participant.name for place, participant in tour1.start().items()
        }
        self.assertTrue(TournamentTest.all_results['tour1'][2] == 'Ник')


    def test_start2(self):
        tour2 = Tournament(90, self.andrei, self.nick)
        TournamentTest.all_results['tour2'] = {
            place: participant.name for place, participant in tour2.start().items()
        }
        self.assertTrue(TournamentTest.all_results['tour2'][2] == 'Ник')


    def test_start3(self):
        tour3 = Tournament(90, self.usain, self.andrei, self.nick)
        TournamentTest.all_results['tour3'] = {
            place: participant.name for place, participant in tour3.start().items()
        }
        self.assertTrue(TournamentTest.all_results['tour3'][3] == 'Ник')

    @classmethod
    def tearDownClass(cls) -> None:
        for tour, value in cls.all_results.items():
            print(value)


if __name__ == '__main__':
    unittest.main()