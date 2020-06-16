from click.testing import CliRunner
import TaskJar
import unittest


class TestTaskJar(unittest.TestCase):
    def test_draw(self):
        runner = CliRunner()
        result = runner.invoke(TaskJar.pick)
        assert result.exit_code == 0
        assert result.output == "Run unit tests lol\n"
