"""### Task 1.) Different Integers Problem

Suppose we throw a party with exactly n guests. When they arrive at the party each guest is given a random integer 1-k. One number could be distributed to more than one guest.

What is the probability that all k integers are distributed to the n guests?

Write a Python function `sim_diff_integers(n: int, k: int, NUM_SIM: int) -> float` with the following inputs:

`n` := The number of guests that are at the party.

`k` := The number of different numbers that are distributed (1-k)

`NUM_SIM` := The number of simulations to run your program for. Recommended that the input be at least 1000

 The function will ouput an estimate to the the theoretical probability that all `k` numbers will be distributed to the `n` guests.

For example,

`sim_diff_integers(3, 4, 10000) ~= 0`

`sim_diff_integers(5, 4, 10000) ~= 0.234375`

`sim_diff_integers(20,4,10000) ~= 0.98`
"""

def sim_diff_integers(n: int, k: int, NUM_SIM: int) -> float:
    import random

    i = 0
    count = 0
    while i < NUM_SIM:
        options = []
        ints = []
        for x in range(k):
            options.append(x)
        for y in range(n):
            ints.append(random.choice(options))
        if(len(set(ints))) == k:
            count += 1
        i += 1
    return count / NUM_SIM

#print(sim_diff_integers(3, 4, 10000))
#print(sim_diff_integers(5, 4, 10000))
#print(sim_diff_integers(20, 4, 10000))

"""### Task 2.) Gambler's Ruin: Two Absorbing States

Suppose a gambler starts with  k dollars.

She gambles 1 dollar on each game. The probability she wins a game is p, and the probability she loses a game is q = 1-p. In other words, p + q = 1.

The gambler will play until she goes bankrupt (reaches 0 dollars) or she reaches some specified amount M dollars.

What is the expected amount of rounds she will play before she either goes bankrupt or she reaches her goal?

Write a Python function `gamblers_expected_time(k: int, M: int, p: float, NUM_SIM: int) -> float` that will simulate this situation and return an expected amount of trials the gambler plays before going bankrupt or reaching her goal.


For example,

`gamblers_expected_time(10, 100, 0.5, 1000) ~= 900`
"""

def gamblers_expected_time(k: int, M: int, p: float, NUM_SIM: int) -> float:
    import random

    i = 0
    results = []
    while i < NUM_SIM:
        trials = 0
        current_k = k
        while 0 < current_k < M:
            if random.random() > 1 - p:
                current_k += 1
            else:
                current_k -= 1
            trials += 1
        results.append(trials)
        i += 1
    return sum(results) / NUM_SIM

#print(gamblers_expected_time(10, 100, 0.5, 1000))

"""### Task 3.) Run of Successes vs Run of Failures

Bernoulli trials are independent trials where the probability of success on each trial is p, 0 < p < 1, and the probability of failure on each trial is 1-p.

Consider a sequence of Bernoulli trials. For example, a sequence of 5 Bernoulli trails could look like: success success success failure failure.

We would like to estimate the probability that a run of S successes happens before a run of F failures do.

Write a Python function `run_of_success(p: float, S: int, F: int, NUM_SIM: int) -> float` that will estimate the probability that we see a run of S successes before a run of F failures.
"""

#write your code for Task 3.) Run of Success vs Failures
def run_of_success(p: float, S: int, F: int, NUM_SIM: int) -> float:
    import random

    i = 0
    count = 0
    s_run = '1' * S
    f_run = '0' * F
    while i < NUM_SIM:
        sequence = ''
        for j in range(i):
            if random.random() > 1 - p:
                sequence += '1'
            else:
                sequence += '0'
        if sequence.find(s_run) != -1 and (sequence.find(s_run) < sequence.find(f_run) or sequence.find(f_run) == -1):
            count += 1
        i += 1

    #probability = (pow(p, S - 1) * (1 - pow(1 - p, F))) / (pow(p, S - 1) + pow(1 - p, F - 1) - (pow(p, S - 1) * pow(1 - p, F - 1)))
    #print(probability)

    return count / NUM_SIM

#print(run_of_success(0.2, 2, 3, 10000))

"""### Task 4.) Bus Ridership Simulation

Consider the following analysis of bus ridership, which (in more complex form) could be used by the bus company to plan the number of bues, frequency of stops, and so on.

Here is (a simplified) model:



*   At each stop, each passenger gets off from the bus, independently of the actions of the others, with probability 0.2 each.

*   Either 0, 1, or 2 new passengers get on the bus, with probabilities 0.45, 0.45, and 0.1 respectively. Passengers at each successive stop act independently.

*  Assume the bus is so large that it never becomes full, so the new passengers can always board.

*  Suppose the bus is empty when it arrives at the first stop.


Estimate the probability (using simulation) that after visiting the nth stop, the bus is empty.

Write a Python function ``bus_sim(nth_stop: int, NUM_SIM: int) -> float`` that will estimate the probability of interest stated above.

For example, ``bus_sum(10, 100000) ~= 0.038``
"""

def bus_sim(nth_stop: int, NUM_SIM: int) -> float:
    import random

    i = 0
    passengers = [0, 1, 2]
    results = []
    while i < NUM_SIM:
        bus = []
        for _ in range(nth_stop):
            bus = [passenger for passenger in bus if random.random() > 0.2]
            new_passengers = random.choices(passengers, [0.45, 0.45, 0.1])[0]
            for j in range(new_passengers):
                bus.append(1)
        results.append(len(bus))
        i += 1
    return results.count(0) / NUM_SIM

#print(bus_sim(10, 10000))