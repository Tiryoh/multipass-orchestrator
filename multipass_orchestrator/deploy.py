import sys
from multipass_orchestrator.orchestrator import MultipassOrchestrator as mpo
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('config', default=None)
    parser.add_argument('-v', '--verbose', action='store_true')

    args = parser.parse_args()

    if args.config is None:
        print("Usage %s <config.yaml>" % sys.argv[0])
        sys.exit(1)

    env = mpo(args.config)
    env.span_environment()
    env.build_environment(args.verbose)
    env.run_environment(args.verbose)


if __name__ == '__main__':
    main()
