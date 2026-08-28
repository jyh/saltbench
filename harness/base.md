# Working notes
- Run any project command inside its environment with `__EP__/rt <command>`,
  e.g. `__EP__/rt python -m pytest path/to/test_file.py -x -q`.
  To use shell features (pipes, cd, &&), quote the whole command as one argument:
  `__EP__/rt 'cd tests && python -m pytest test_x.py -q | tail -30'`.
  Commands run without it use a bare host and will not find the project's dependencies.
- There is no network. Do not try to install packages or fetch anything.
- Edit files in place under `__EP__/wc`. Do not create commits.
