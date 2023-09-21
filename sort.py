def sort_array(arr):
    """
    This function takes an array of numbers as input and returns the sorted array in ascending order.
    """
    return sorted(arr)

    
def test_sort_array():
    assert sort_array([3, 1, 4, 2]) == [1, 2, 3, 4]
    assert sort_array([5, 5, 5, 5]) == [5, 5, 5, 5]
    assert sort_array([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert sort_array([4, 3, 2, 1]) == [1, 2, 3, 4]
    assert sort_array([]) == []

test_sort_array()function validateIPAddress(ipAddress) {
    const ipArr = ipAddress.split('.');
    if (ipArr.length !== 4) {
        return false;
    }
    for (let i = 0; i < 4; i++) {
        const num = parseInt(ipArr[i]);
        if (isNaN(num) || num < 0 || num > 255 || (num.toString() !== ipArr[i])) {
            return false;
        }
    }
    return true;
}

// Test case 1: Valid IP address
console.assert(validateIPAddress('192.168.0.1') === true, 'Test case 1 failed');

// Test case 2: Invalid IP address (too many parts)
console.assert(validateIPAddress('192.168.0.1.1') === false, 'Test case 2 failed');

// Test case 3: Invalid IP address (part out of range)
console.assert(validateIPAddress('192.168.0.256') === false, 'Test case 3 failed');

// Test case 4: Invalid IP address (part not a number)
console.assert(validateIPAddress('192.168.0.a') === false, 'Test case 4 failed');

// Test case 5: Invalid IP address (part has leading zeros)
console.assert(validateIPAddress('192.168.01.1') === false, 'Test case 5 failed');