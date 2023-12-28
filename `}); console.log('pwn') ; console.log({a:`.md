[![PyPi](https://img.shields.io/pypi/v/markdown-checker)](https://example.com/some%29page)
[![Downloads](https://img.shields.io/pypi/dm/markdown-checker)](https://pypi.org/project/markdown-checker/)
[![GitHub issues](https://img.shields.io/badge/issue_tracking-github-blue.svg)](https://github.com/john0isaac/markd
own-checker/issues}\\))aaaaa
[Link with parentheses](https://example.com/some%29page)
[Link with parentheses](https://example.com/some%29page)
[![Contributing](https://img.shields.io/badge/PR-Welcome-%23FF8300.svg?)](https://github.com/john0isaac/markdown-ch
ecker/pulls)
[aa](./aaaaa
markdown-checker is a markdown validation reporting tool.
# How To
1. Run `pip install markdown-checker`.
2. Run `markdown-checker -d {src} -f {func}`. Replace `{src}` with the directory you want to analyse and {func} wit
h the available functions like check_broken_paths.
3. The output will be displayed in the terminal.
# Using markdown-checker in GitHub Actions
The tool has been designed to be run within a GitHub workflow using the [action-check-markdown](https://github.com/
marketplace/actions/check-markdown) GitHub action. The action will automatically post the output of the tool to you
r GitHub pull request as a comment
