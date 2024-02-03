import unittest
from unittest.mock import patch
import sys

sys.path.append('../src/team_malthus/')

from pop import validate, get_indicator_id, population


class TestPopulationFunctions(unittest.TestCase):

#Test 1: Validate Function, to ensure validate function correctly verifies input parameters' validity
    
    def test_validate(self):
        # Test valid input
        self.assertIsNone(validate(2010, 'm', 10, 50, 'NAM'))
        
        # Test invalid year
        with self.assertRaises(ValueError) as context:
            validate(1990, 'm', 10, 50, 'NAM')
        self.assertTrue("year must be between 2000 and 2020" in str(context.exception))
        
        # Test invalid sex
        with self.assertRaises(ValueError) as context:
            validate(2010, 'x', 10, 50, 'NAM')
        self.assertTrue("sex must be m, f, or p (for total)" in str(context.exception))
        
        # Test invalid age range
        with self.assertRaises(ValueError) as context:
            validate(2010, 'm', 80, 79, 'NAM')
        self.assertTrue("age values invalid" in str(context.exception))

#Test 2: 'get_indicator_id' function (known inputs, edge cases)

    def test_get_indicator_id(self):
        # Known input
        indicator, label = get_indicator_id(25, 'm')
        self.assertEqual(indicator, "SP.POP.2529.MA")
        self.assertEqual(label, "male_25_29")
        
        # Edge case input
        indicator, label = get_indicator_id(0, 'f')
        self.assertEqual(indicator, "SP.POP.0004.FE")
        self.assertEqual(label, "female_0_4")


#Test 'population' function with mocked 'wbdata' calls

    @patch('pop.wbdata.get_data')
    def test_population(self, mock_get_data):
        # Mocking wbdata.get_data to return a specific value
        mock_get_data.return_value = [{"value": 100000}]
        
        # Assuming the mock value applies for all age ranges and indicators
        pop_count = population(2020, 'p', "13-24", "USA")
        # Since the logic and return values might vary based on your implementation,
        # adjust the expected population count accordingly
        self.assertTrue(pop_count > 0)
        
import unittest
from test_pop import TestPopulationFunctions

# Create a test suite
suite = unittest.TestLoader().loadTestsFromTestCase(TestPopulationFunctions)

# Run the test suite
unittest.TextTestRunner().run(suite)
