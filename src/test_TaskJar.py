from click.testing import CliRunner
import unittest
import TaskJar


class TestTaskJar(unittest.TestCase):
    def test_draw(self):
        runner = CliRunner()
        result = runner.invoke(TaskJar.pick, ['--file', '../example_files/test_one_task'])
        assert result.exit_code == 0
        assert result.output == "Run unit tests lol\n"


if __name__ == '__main__':
    unittest.main()
