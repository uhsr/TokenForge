# test_tokenforge.py
"""
Tests for TokenForge module.
"""

import unittest
from tokenforge import TokenForge

class TestTokenForge(unittest.TestCase):
    """Test cases for TokenForge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = TokenForge()
        self.assertIsInstance(instance, TokenForge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = TokenForge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
