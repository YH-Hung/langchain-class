import argparse

from app_modes import get_mode_names, get_mode_runner


def build_parser():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("--mode", choices=get_mode_names(), default="codegen")
    arg_parser.add_argument("--task", default="return a list of numbers")
    arg_parser.add_argument("--language", default="python")
    arg_parser.add_argument("--base-url", default="http://localhost:1234/v1")
    arg_parser.add_argument(
        "--api-key",
        default="lm-studio",
        help="Any non-empty string usually works for LM Studio.",
    )
    arg_parser.add_argument("--model", default="google/gemma-4-e4b")
    return arg_parser


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    runner = get_mode_runner(args.mode)
    runner(args)


if __name__ == "__main__":
    main()
