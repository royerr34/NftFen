# test_nftfen.py
"""
Tests for NftFen module.
"""

import unittest
from nftfen import NftFen

class TestNftFen(unittest.TestCase):
    """Test cases for NftFen class."""

    def test_initialization(self):
        """Test class initialization."""
        instance = NftFen()
        self.assertIsInstance(instance, NftFen)

    def test_run_method(self):
        """Test the run method."""
        instance = NftFen()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
