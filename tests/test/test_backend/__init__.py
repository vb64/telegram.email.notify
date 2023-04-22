"""GAE service backend."""
from .. import TestCase


class TestBackend(TestCase):
    """Backend service."""

    def setUp(self):  # pylint: disable=arguments-differ
        """Use backend app."""
        from back import app
        TestCase.setUp(self, app)
