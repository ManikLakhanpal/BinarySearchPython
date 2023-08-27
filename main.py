def binarySearch(array, n):
    mid = len(array) // 2 # it's basically the value before the decimal, like eg if ans is 3.14, mid will be 3 
    
    if len(array) == 0: # checks weather the length is equal to 0
        return 'Not in array'
        
    elif len(array) == 1:
        if array[0] != n:
            return f'Not in array'
        else: 
            return f'Yes {n} is in {array}'

    elif array[mid] == n: # checks if element in mid is equal to n, if so prints yes, followed by the list 
        return f'Yes, {n} is in {array}'

    elif array[mid] > n: # checks if element just before mid value < n, array[mid] < n, slices the list before mid val and the binarySearch called again
        return binarySearch(array[0: mid], n)

    else: # if none true function is called again.
        return binarySearch(array[mid+1:], n) # returns if none of above true :)


array = [int(a) for a in input('Enter array: ').split()] # it basically 1st takes input, then splits each and every character then conversts all elements from str to int.
n = int(input('Enter number: '))

print(binarySearch(array, n))
