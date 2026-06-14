import unittest

import main


class CliParserTest(unittest.TestCase):
    def test_defaults_to_codegen_mode(self):
        parser = main.build_parser()

        args = parser.parse_args([])

        self.assertEqual(args.mode, "codegen")

    def test_accepts_chatbot_mode(self):
        parser = main.build_parser()

        args = parser.parse_args(["--mode", "chatbot"])

        self.assertEqual(args.mode, "chatbot")

    def test_rejects_unknown_mode(self):
        parser = main.build_parser()

        with self.assertRaises(SystemExit):
            parser.parse_args(["--mode", "unknown"])


if __name__ == "__main__":
    unittest.main()
