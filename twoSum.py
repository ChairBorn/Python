def two_sum(nums, target):
    """
    Find two numbers in the list that add up to the target.
    
    Because sometimes, even numbers need a partner in crime.
    
    :param nums: List of integers, because who doesn't love a good list?
    :param target: The sum we're aiming for, like a numerical bullseye.
    :return: Indices of the two numbers, or a witty comeback if it fails.
    """
    # Dictionary to keep track of numbers we've seen
    num_dict = {}
    
    for i, num in enumerate(nums):
        # Calculate the complement
        complement = target - num
        
        # If the complement exists in our dictionary, we've found our pair!
        if complement in num_dict:
            return [num_dict[complement], i]
        
        # If not, add this number to our dictionary
        num_dict[num] = i
    
    # If we've gone through the list and found nothing, time for humor
    return "Sorry, no love connection found. Maybe they're just not that into each other."

# Test it out
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(f"Found at indices: {result}")