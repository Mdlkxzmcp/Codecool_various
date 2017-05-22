def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3
    balls of the same color were drawn in the first 3 draws.
    '''
    from random import sample
    same_color = 0
    for trial in range(numTrials):
        bucket = ['R'] * 4 + ['G'] * 4
        draws = sample(bucket, 3)
        if draws == ['R'] * 3 or draws == ['G'] * 3:
            same_color += 1
    print(same_color)
    return same_color / numTrials
