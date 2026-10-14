# ProjectEuler

My Python solutions to the first problems of [Project Euler](https://projecteuler.net). Each file explains the approach (algorithm, complexity) instead of just giving a result: the goal is to learn.

## Publication policy

Project Euler asks that solutions not be published outside the site, except for the first 100 problems and as long as the method is explained (see their [rules](https://projecteuler.net/about)). This repository only contains solutions to problems 1 to 100, and numerical answers are not written down: run the code to get them.

## Quick start

Requirements: Python 3 and Git.

```bash
git clone https://github.com/clarkhawk/ProjectEuler.git
cd ProjectEuler
python3 -m venv .venv
source .venv/bin/activate
```

Run a solution from the repository root:

```bash
python -m solutions.p000
```

## Layout

`solutions/` holds one file per problem (`p001.py`, `p002.py`, ...), each starting with a link to the official statement and a short summary of the approach. `euler/` holds helpers shared between problems.

## License

The code is released under the [MIT](LICENSE) license. Problem statements are not included: they belong to [Project Euler](https://projecteuler.net) and are published under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). Each file links to the official statement.