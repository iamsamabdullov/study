#From a box containing n tickets with numbers 1, 2,...,n, all tickets are taken out one at a time.
# This program calculates the percentage probability that at least one ticket has a serial number that matches its own.
import random
n = int(input())
def calculate_probability(n):
    total_trials = 300000  # Count of simulated iterations
    successful_trials = 0  # Count of succesfull iterations, where at least one ticket matched

    for _ in range(total_trials):
        tickets = list(range(1, n + 1))
        random.shuffle(tickets)

        if any(tickets[i] == i + 1 for i in range(n)):
            successful_trials += 1

    probability = (successful_trials / total_trials) * 100
    return round(probability, 1)



# Call the function to calculate the probability
probability = calculate_probability(n)

# We display the probability as a percentage, rounded to 1 decimal place
print(f'{probability:.1f}%')
