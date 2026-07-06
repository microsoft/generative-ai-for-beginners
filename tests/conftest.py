"""Pytest configuration for the shared utilities test suite.

Ensures the repository root is importable so that the ``shared.python``
package resolves when the tests are run from any working directory.
"""

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
