import unittest
from unittest.mock import patch
from documents_todo import documents, people, number_shelf, directories, save_shelf, append, delete_shelf, delete, move, append_shelf


class TestDocuments(unittest.TestCase):

    def test_people1(self):
        self.assertEqual(people(documents, '2207 876234'), 'Василий Гупкин')

    def test_people2(self):
        self.assertEqual(people(documents, '15448'), 'Данный документ не обнаружен.')

    def test_number_shelf1(self):
        self.assertEqual(number_shelf(directories, '11-2'), '1')

    def test_number_shelf2(self):
        self.assertEqual(number_shelf(directories, '11362'), 'Данный документ не обнаружен.')

    @patch('builtins.input', lambda *args: '3')
    def test_save_shelf1(self):
        self.assertTrue(save_shelf('12345', directories), 'Запись успешно добавлена!')

    @patch('builtins.input', lambda *args: '4')
    def test_save_shelf2(self):
        self.assertTrue(save_shelf('12345', directories), f'Введите полку из существующих: {directories.keys()}')

    @patch('builtins.input', lambda *args: '3')
    def test_append(self):
        self.assertIn(append(documents, directories, '12345', 'passport', 'Юлия Попова'), documents)

    def test_delete_shelf1(self):
        self.assertNotIn(delete_shelf('10006', directories), directories.values())

    def test_delete_shelf2(self):
        self.assertEqual(delete_shelf('1345', directories), 'Документ не найден!')

    def test_delete1(self):
        self.assertEqual(delete(documents, directories, '12556'), 'Документ удален')

    def test_delete2(self):
        self.assertEqual(delete(documents, directories, '88995'), 'Документ не найден')

    @patch('builtins.input', lambda *args: '3')
    def test_move1(self):
        self.assertEqual(move(directories, '22-5'), 'Документ перемещен')

    @patch('builtins.input', lambda *args: '4')
    def test_move2(self):
        self.assertEqual(move(directories, '22-5'), 'Документ перемещен')

    @patch('builtins.input', lambda *args: '1')
    def test_move(self):
        self.assertEqual(move(directories, '28569'), 'Документ в перечне отсутствует.')

    @patch('builtins.input', lambda *args: '1')
    def test_append_shelf1(self):
        self.assertEqual(append_shelf(directories), 'Данная полка уже существует.')

    @patch('builtins.input', lambda *args: '5')
    def test_append_shelf2(self):
        self.assertIn(append_shelf(directories), directories.keys())


if __name__ == '__main__':
    unittest.main()

