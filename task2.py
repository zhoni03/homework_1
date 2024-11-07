import numpy as np

def generate_random_data(mean, variance, num_samples):
    return np.random.randint(max(mean - variance, 0), min(mean + variance + 1, 90), num_samples)

def calculate_aggregated_score(department_scores, importance_tags):
    total_weighted_score = 0
    total_importance = sum(importance_tags)
    total_users = 0

    for scores, importance in zip(department_scores, importance_tags):
        total_weighted_score += sum(scores) * importance
        total_users += len(scores)

    aggregated_score = total_weighted_score / (total_users * total_importance)
    return max(0, min(90, aggregated_score))  # Ensures the score is within 0 - 90 range
