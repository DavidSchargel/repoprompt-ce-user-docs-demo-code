# RepoPrompt Community Edition Demo Repo

[RepoPrompt CE](https://repoprompt.com) is an open-source macOS app for curating codebase context, connecting coding agents, and coordinating AI-assisted development.

## Purpose and related repositories

This repository contains sample code used primarily for screenshots. It is paired with the [marketing and end-user documentation site](https://github.com/repoprompt/repoprompt-ce-user-docs) and the [RepoPrompt CE project source code](https://github.com/repoprompt/repoprompt-ce).

## It's a Hello World CLI!

Requires Python 3; no additional dependencies are needed. Run these commands from the repository root.

Print `hello world`:

```sh
python3 hello.py
```

Show usage information (`--help` is the only supported option):

```sh
python3 hello.py --help
```

Run the tests, which check the greeting and help output:

```sh
python3 -B -m unittest -v
```

The `-B` flag prevents Python from creating bytecode cache files, and `-v` shows each test result.
