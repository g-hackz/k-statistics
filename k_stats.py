from math import sqrt

def square(number):
    '''return the square of a number'''
    return number * number

def get_mean(dataset):
    '''returns the mean of the given data set'''
    return sum(dataset)/float(len(dataset))


def get_median(dataset):
    '''returns the median of the given data set'''
    sorted_dataset = sorted(dataset)
    mid_length = len(sorted_dataset)/2
    if len(sorted_dataset) % 2 == 1:
        return sorted_dataset[mid_length]
    else:
        return (sorted_dataset[mid_length-1]+sorted_dataset[mid_length])/2

def get_mode(dataset):
    '''returns the mode of the given data set'''
    frequencies = dict()
    count = 0
    mode = 0
    x = 0
    for i in dataset:
        for j in xrange(len(dataset)):
            if i == dataset[j]:
                count = count + 1
        frequencies.update({i: count})
        count = 0

    for keys in frequencies:
        if x < frequencies[keys]:
            x = frequencies[keys]
            mode = keys

    return mode

def freq_dist_mean(dataset, freqset):
    '''calculate the mean of a frequency distribution given the data set and frequencies'''
    fx = [dataset[i] * freqset[i] for i in xrange(len(dataset))]
    efx = sum(fx)
    ef = sum(freqset)
    return float(efx)/ef

def get_var_and_sd(dataset):
    '''calculate the variance and standard deviation of a frequency distribution given the data set and frequencies'''
    mean = get_mean(dataset)
    smx = [i-mean for i in dataset]
    smx_square = [square(i) for i in smx]
    sum_of_squares = sum(smx_square)
    variance = float(sum_of_squares)/len(dataset)
    return variance, sqrt(variance)




# Usage

print 'Mean: ', get_mean([4, 6, 6, 7, 7, 7, 8, 10])

print 'Median: ', get_median([2, 1, 9, 6, 7, 14, 11, 11, 12])
print 'Median: ', get_median([24, 12, 16, 22, 10, 25])

print 'Mode: ', get_mode([1, 1, 4, 4, 5, 6, 8, 8, 8, 9])

FREQ_DISTRIBUTION = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
FREQUENCIES = [0, 0, 1, 0, 1, 7, 16, 8, 3, 1, 1]
print 'Mean of the frequency distribution is: %.2f' % freq_dist_mean(FREQ_DISTRIBUTION, FREQUENCIES)

var, std_dev = get_var_and_sd([4, 7, 10])
print 'Variance: %.2f' % var
print 'Standard deviation: %.3f' % std_dev
