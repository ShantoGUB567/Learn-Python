# 1. Generate a random dataset of heights and weights of N people using Numpy.
# 2. Computes the BMI of each person.
# 3. Filter people with BMI greater than 25 and display them.
import numpy as np
import pandas as pd

def generate_data(N):
    return np.random.uniform(1.5, 2.0, N), np.random.uniform(50, 120, N)

def compute_bmi(heights, weights):
    return weights / (heights ** 2)

def main():
    N = int(input("Enter number of people: "))
    heights, weights = generate_data(N)
    bmi = compute_bmi(heights, weights)
    
    high_bmi = bmi > 25
    data = pd.DataFrame({'Height': heights[high_bmi], 'Weight': weights[high_bmi], 'BMI': bmi[high_bmi]})
    
    print("\nPeople with BMI > 25:")
    print(data)

main()
