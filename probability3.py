# Fraction of defective pipes produced by each plant
p_defective_plant1 = 0.1
p_defective_plant2 = 0.15
p_defective_plant3 = 0.2

# Total production from each plant
production_plant1 = 1000
production_plant2 = 800
production_plant3 = 1200

# Total production across all plants
total_production = production_plant1 + production_plant2 + production_plant3

# Probability that a randomly selected pipe is defective
p_defective = (production_plant1 * p_defective_plant1 + production_plant2 * p_defective_plant2 + production_plant3 * p_defective_plant3) / total_production

# Probability that a defective pipe came from plant 1 using Bayes' theorem
p_plant1_given_defective = (p_defective_plant1 * production_plant1) / (p_defective * total_production)

# Simplify the fraction to get the answer in the required format
def simplify_fraction(numerator, denominator):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    common_divisor = gcd(numerator, denominator)
    return numerator // common_divisor, denominator // common_divisor

# Simplify the fraction
simplified_fraction = simplify_fraction(p_plant1_given_defective, 1)

# Print the answer in the required format
print(f"{simplified_fraction[0]}/{simplified_fraction[1]}")
