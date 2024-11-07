import unittest

class TestCyberSecurityScore(unittest.TestCase):

    def test_calculate_aggregated_score_basic(self):
        department_scores = [
            [10, 20, 30],  # Department 1
            [15, 25, 35],  # Department 2
            [20, 30, 40],  # Department 3
        ]
        importance_tags = [1, 1, 1]  # Equal importance for all departments
        result = calculate_aggregated_score(department_scores, importance_tags)
        self.assertGreaterEqual(result, 0)
        self.assertLessEqual(result, 90)

    def test_aggregated_score_weighted_importance(self):
        department_scores = [
            [10, 20, 30],  # Department 1
            [50, 60, 70],  # Department 2 with high threat scores
            [20, 30, 40],  # Department 3
        ]
        importance_tags = [1, 5, 1]  # High importance for department 2
        result = calculate_aggregated_score(department_scores, importance_tags)
        self.assertGreater(result, 30)  # Expected higher score due to high threats in department 2

    def test_aggregated_score_large_department(self):
        department_scores = [
            generate_random_data(30, 10, 150),  # Large department
            generate_random_data(20, 5, 30),    # Smaller department
        ]
        importance_tags = [3, 2]
        result = calculate_aggregated_score(department_scores, importance_tags)
        self.assertGreaterEqual(result, 0)
        self.assertLessEqual(result, 90)

    def test_no_threat_scenario(self):
        department_scores = [
            [0, 0, 0],  # All users have no threat scores
            [0, 0, 0],
        ]
        importance_tags = [1, 1]
        result = calculate_aggregated_score(department_scores, importance_tags)
        self.assertEqual(result, 0)

    def test_max_threat_scenario(self):
        department_scores = [
            [90, 90, 90],  # All users have max threat scores
            [90, 90, 90],
        ]
        importance_tags = [1, 1]
        result = calculate_aggregated_score(department_scores, importance_tags)
        self.assertEqual(result, 90)

    def test_varying_user_counts(self):
        department_scores = [
            generate_random_data(40, 20, 10),  # Small department
            generate_random_data(50, 10, 200)  # Large department
        ]
        importance_tags = [2, 3]
        result = calculate_aggregated_score(department_scores, importance_tags)
        self.assertGreaterEqual(result, 0)
        self.assertLessEqual(result, 90)

if __name__ == "__main__":
    unittest.main()
