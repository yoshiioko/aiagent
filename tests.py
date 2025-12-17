import unittest
import os
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file


class FunctionTests(unittest.TestCase):
    def setUp(self):
        self.working_dir = "calculator"
        self.test_files = []

    def tearDown(self):
        for rel_path in self.test_files:
            abs_path = os.path.join(self.working_dir, rel_path)
            try:
                if os.path.exists(abs_path):
                    os.remove(abs_path)
            except Exception:
                pass

    def test_get_files_info_root(self):
        result = get_files_info(self.working_dir)
        self.assertIsInstance(result, str)
        self.assertIn("main.py", result)
        self.assertIn("tests.py", result)

    def test_get_files_info_subdirectory(self):
        # Assumes 'pkg' is a valid subdirectory in 'calculator'
        result = get_files_info(self.working_dir, "pkg")
        self.assertIsInstance(result, str)
        self.assertIn("render.py", result)
        self.assertIn("calculator.py", result)

    def test_get_files_info_invalid_directory(self):
        # Should return an error for directory outside working dir
        result = get_files_info(self.working_dir, "../")
        self.assertIsInstance(result, str)
        self.assertTrue(result.startswith('Error:'))

    def test_get_files_info_absolute_path_outside(self):
        # Should return an error for absolute path outside working dir
        result = get_files_info(self.working_dir, "/tmp")
        self.assertIsInstance(result, str)
        self.assertTrue(result.startswith('Error:'))

    def test_get_file_content_main(self):
        result = get_file_content(self.working_dir, "main.py")
        self.assertIsInstance(result, str)
        self.assertIn("# calculator/main.py", result)  # Assumes main.py contains Python code

    def test_get_file_content_subdirectory(self):
        result = get_file_content(self.working_dir, "pkg/calculator.py")
        self.assertIsInstance(result, str)
        self.assertIn("# calculator/pkg/calculator.py", result)  # Assumes calculator.py contains Python code

    def test_get_file_content_outside_working_dir(self):
        result = get_file_content(self.working_dir, "/bin/cat")
        self.assertIsInstance(result, str)
        self.assertTrue(result.startswith('Error:'))

    def test_get_file_content_nonexistent_file(self):
        result = get_file_content(self.working_dir, "does_not_exist.py")
        self.assertIsInstance(result, str)
        self.assertTrue(result.startswith('Error:'))

    def test_write_file_new_file(self):
        rel_path = "lorem_test.txt"
        self.test_files.append(rel_path)
        result = write_file(self.working_dir, rel_path, "Lorem ipsum dolor sit amet, consectetur adipiscing elit.")
        self.assertIsInstance(result, str)
        self.assertTrue(result.startswith('Successfully wrote to "lorem_test.txt"'))

    def test_write_file_subdirectory(self):
        rel_path = "pkg/more_lorem.txt"
        self.test_files.append(rel_path)
        result = write_file(self.working_dir, rel_path, "Lorem ipsum dolor sit amet, consectetur adipiscing elit.")
        self.assertIsInstance(result, str)
        self.assertTrue(result.startswith('Successfully wrote to "pkg/more_lorem.txt"'))

    def test_write_file_outside_working_dir(self):
        result = write_file(self.working_dir, "/tmp/temp.txt", "This should not be allowed.")
        self.assertIsInstance(result, str)
        self.assertTrue(result.startswith('Error:'))

    def test_write_file_invalid_parent(self):
        # Try to write to a path with invalid parent directory (simulate error)
        result = write_file(self.working_dir, "invalid_dir/../\0bad.txt", "bad")
        self.assertIsInstance(result, str)
        self.assertTrue(result.startswith('Failed to write to file:'))

    def test_run_python_file_outside_working_dir(self):
        result = run_python_file(self.working_dir, "/bin/ls")
        self.assertTrue(result.startswith('Error:'))

    def test_run_python_file_nonexistent(self):
        result = run_python_file(self.working_dir, "does_not_exist.py")
        self.assertTrue(result.startswith('Error:'))

    def test_run_python_file_tests(self):
        result = run_python_file(self.working_dir, "tests.py")
        self.assertIn("OK", result)

    def test_run_python_file_main(self):
        result = run_python_file(self.working_dir, "main.py", ["3 + 5"])
        self.assertIn("8", result)


if __name__ == "__main__":
    unittest.main()
