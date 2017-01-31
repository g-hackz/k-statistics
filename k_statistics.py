
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

# Usage

print 'Mean = ', get_mean([4, 6, 6, 7, 7, 7, 8, 10])

print 'Median = ', get_median([2, 1, 9, 6, 7, 14, 11, 11, 12])
print 'Median = ', get_median([24, 12, 16, 22, 10, 25])

print 'Mode = ', get_mode([1, 1, 4, 4, 5, 6, 8, 8, 8, 9])
