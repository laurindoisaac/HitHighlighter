# test_hithighlighter.py
"""
Tests for HitHighlighter module.
"""

import unittest
from hithighlighter import HitHighlighter

class TestHitHighlighter(unittest.TestCase):
    """Test cases for HitHighlighter class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = HitHighlighter()
        self.assertIsInstance(instance, HitHighlighter)
        
    def test_run_method(self):
        """Test the run method."""
        instance = HitHighlighter()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
