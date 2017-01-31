
def get_mean(dataset):
    '''return the mean of the given data set'''
    mean = 0
    for i in dataset:
        mean = mean + i
    return float(mean)/len(dataset)


def get_median(dataset):
    '''return the median of the given data set'''
    sorted_dataset = sorted(dataset)
    mid_length = len(sorted_dataset)/2
    if len(sorted_dataset) % 2 == 1:
        return sorted_dataset[mid_length]
    else:
        return (sorted_dataset[mid_length-1]+sorted_dataset[mid_length])/2

def get_mode(dataset):
    '''return the mode of the given data set'''
    

print 'Mean = ', get_mean([4, 6, 6, 7, 7, 7, 8, 10])

print 'Median =', get_median([2, 1, 9, 6, 7, 14, 11, 11, 12])
print 'Median =', get_median([24, 12, 16, 22, 10, 25])
