import logging
from datetime import datetime as dt
from rt_with_exceptions import Runner
import unittest

logging.basicConfig(level=logging.INFO, filemode='w', filename=f'../logs/{dt.now().strftime("%Y-%m-%d %H-%M")}.log',
                    encoding='utf-8', format='\n%(asctime)s | %(levelname)s | %(message)s')


class RunnerTest(unittest.TestCase):
    is_frozen = False


    def test_walk(self):
        try:
            walker = Runner('Default', -7)
            for _ in range(10):
                walker.walk()
            self.assertEqual(walker.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)
        except ValueError:
            logging.warning('Неверная скорость для объекта Runner', exc_info=True)
        except Exception as e:
            logging.error(f'Непредвиденная ошибка: {e}')


    def test_run(self):
        try:
            default_2 = Runner(3.14, 10)
            for _ in range(10):
                default_2.run()
            self.assertEqual(default_2.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)
        except ValueError:
            logging.warning('Неверная скорость для объекта Runner', exc_info=True)
        except Exception as e:
            logging.error(f'Непредвиденная ошибка: {e}')


    def test_challenge(self):
        try:
            default_3 = Runner('Default_3', 10)
            default_4 = Runner('Default_4', 15)
            for _ in range(10):
                default_3.walk()
                default_4.run()
            self.assertNotEqual(default_3.distance, default_4.distance)
            logging.info('"test_challenge" выполнен успешно')
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)
        except ValueError:
            logging.warning('Неверная скорость для объекта Runner', exc_info=True)
        except Exception as e:
            logging.error(f'Непредвиденная ошибка: {e}')


if __name__ == '__main__':
    unittest.main()