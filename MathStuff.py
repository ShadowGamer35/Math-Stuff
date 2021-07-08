def get_factors_(number, printed=False):
    """Get the factors of a number."""
    factors = []
    for x in range(1, number+1): # For each number from 1 to the given number.
        if number % x == 0: # If number divided by x has a remainder of 0.
            factors.append(x) # Then it is a factor of the given number.
    if printed:
        print(factors)
    else:
        return factors

def common_factors_(numList, printed=False):
    """Get the common factors of a set of numbers."""
    common_factors, all_factors, unique_numbers, unique_factors = [], [], [], []
    # Create a list of the factors of each unique number in the numList.
    for number in numList:
        if number not in unique_numbers:
            unique_numbers.append(number)
            factors = get_factors_(number)
            for factor in factors:
                all_factors.append(factor)
    # Create a list of the common factors.
    for number in all_factors:
        if number not in unique_factors:
            unique_factors.append(number)
            if all_factors.count(number) == len(unique_numbers):
                common_factors.append(number)

    if printed:
        print(common_factors)
    else:
        return common_factors

def gcf_(numList, printed=False):
    """Get the greatest common factor of a set of numbers."""
    # The last number in the list of common factors is the GCF.
    factors = common_factors_(numList)
    try:
        gcf = factors[-1]
    except IndexError:
        gcf = factors

    if printed:
        print(gcf)
    else:
        return gcf

def lcf_(numList, printed=False):
    """Get the least common factor of a set of numbers."""
    # The first number in the list of common factors is the LCF.
    factors = common_factors_(numList)
    try:
        lcf = factors[0]
    except IndexError:
        lcf = factors

    if printed:
        print(lcf)
    else:
        return lcf

def root_(radicand, index, printed=False):
    """Get the nth root of a number."""
    # Example: The square root of a number can be gotten by raising that
    # number to the power of 1/2.
    if radicand < 0:
        root = f'{(radicand*-1)**(1/index)}i'
    else:
        root = radicand**(1/index)
    if printed:
        print(root)
    else:
        return root

def temperature_convert_(temperature, original, new, printed=False):
    """Convert from a given temperature to a different one."""
    if original =='F':
        if new == 'C':
           new_temp = (temperature - 32) / 1.8
        elif new == 'K':
            new_temp = (temperature + 459.67) / 1.8
        elif new == 'F':
            new_temp = temperature

    elif original == 'C':
        if new == 'F':
            new_temp = temperature * 1.8 + 32
        elif new == 'K':
            new_temp = temperature + 273.15
        elif new == 'C':
            new_temp = temperature

    elif original == 'K':
        if new == 'F':
            new_temp = (temperature + 459.67) * (5/9)
        elif new == 'C':
            new_temp = temperature - 273.15
        elif new == 'K':
            new_temp = temperature

    if printed:
        print(new_temp)
    else:
        return new_temp

def maintain_aspect_ratio_(object_size, surface_size, printed=False):
    """Scale an object to fit a surface and maintain its aspect ratio."""
    # Get the aspect ratio of the object.
    ogj_w, obj_h = object_size[0], object_size[1]
    obj_ratio = ogj_w/obj_h
    # Get the aspect ratio of the surface.
    surf_w, surf_h = surface_size[0], surface_size[1]
    surf_ratio = surf_w/surf_h

    # If the ratios are equal then make the object size equal the surface size.
    if obj_ratio == surf_ratio:
        obj_size = (surf_w, surf_h)
    # If the object ratio is greater then the surface ratio
    # then fill the surface height and make the object as wide as it needs
    # to be to keep its ratio
    elif obj_ratio > surf_ratio:
        obj_size = (surf_w, int(surf_w / obj_ratio))
    # If the object ratio is less then the surface ratio
    # then fill the surface width and make the object as tall as it needs
    # to be to keep its ratio
    elif obj_ratio < surf_ratio:
        obj_size = (int(surf_h * obj_ratio), surf_h)

    if printed:
        print(obj_size)
    else:
        return obj_size

def average_(numList, printed=False):
    """Find the average/mean of a set of numbers."""
    # The sum of the numbers in the numList divided by the length of the list.
    if printed:
        print(sum(numList)/len(numList))
    else:
        return sum(numList)/len(numList)

def median_(numList, printed=False):
    """Find the median of a set of numbers."""
    sort_list, list_len = sorted(numList), len(numList)
    if list_len%2 == 0:
        # The median equals the two middle indexes added then divided by 2.
        median = (sort_list[int((list_len/2) + 0.5)] + 
                                        sort_list[int((list_len/2) - 0.5)])/2
    else:
        # The median equals the middle index.
        median = sort_list[int(list_len/2)]

    if printed:
        print(median)
    else:
        return median

def mode_(numList, printed=False):
    """Find the mode of a set of numbers."""
    unique_numbers, occurrence_count, mode = [], [], []
    for number in numList:
        if number not in unique_numbers:
            unique_numbers.append(number)
            occurrence_count.append(numList.count(number))
    # If the number of times a number appears in the numList is equal to the
    # highest recorded occurrence count, then it's in the mode.
    for number in unique_numbers:
        if numList.count(number) == sorted(occurrence_count)[-1]:
            mode.append(number)
    if printed:
        print(mode)
    else:
        return mode

def range_(numList, printed=False):
    """Find the range of a set of numbers."""
    numList = sorted(numList)
    # The range equals the biggest number minus the smallest number.
    try:
        range_ = numList[-1] - numList[0]
    except IndexError:
        range_ = 0
        
    if printed:
        print(range_)
    else:
        return range_

def solid_polygon_info_(base_sides, printed=False):
    """Get information about a solid polygon from its side count."""
    # Example: A rectangular solid (Each base has four sides) is made up of
    # 12 edges, 8 vertices, 6 faces, and 12 triangles.
    edges = base_sides * 3
    vertices = base_sides * 2
    faces = base_sides + 2
    triangles = (base_sides - 2) * 2 + vertices
    if printed:
        print(f"Edges: {edges}\nVertices: {vertices}\nFaces: {faces}\nTriangles: {triangles}")
    else:
        return {"edges": edges,
                "vertices": vertices,
                "faces": faces,
                "triangles": triangles}

def extrapolate_(number, modifier, method, returnValues, printed=False):
    return_values, current_number = [number], number

    # Add the modifier to the current number.
    if method == 'add':
        for value in range(returnValues):
            current_number = current_number + modifier
            return_values.append(current_number)

    # Subtract the modifier to the current number.
    elif method == 'subtract':
        for value in range(returnValues):
            current_number = current_number - modifier
            return_values.append(current_number)

    # Multiply the modifier to the current number.
    elif method == 'multiply':
        for value in range(returnValues):
            current_number = current_number * modifier
            return_values.append(current_number)

    # Divide the modifier to the current number.
    elif method == 'divide':
        for value in range(returnValues):
            current_number = current_number / modifier
            return_values.append(current_number)

    # Raise the current number to the power of the modifier.
    elif method == 'exponent':
        for value in range(returnValues):
            current_number = current_number ** modifier
            return_values.append(current_number)

    # Get the modifier root of the current number.
    elif method == 'root':
        for value in range(returnValues):
            current_number = current_number ** (1/modifier)
            return_values.append(current_number)

    if printed:
        print(return_values)
    else:
        return return_values

def byte_convert_(number, original, new, printed=False):
    """Convert from one suffix to another suffix."""
    if original == '':
        if new == '':
            None
        elif new == 'kb':
            number = number/1_000
        elif new == 'mb':
            number = number/1_000_000
        elif new == 'gb':
            number = number/1_000_000_000
        elif new == 'tb':
            number = number/1_000_000_000_000
        elif new == 'pb':
            number = number/1_000_000_000_000_000
        elif new == 'eb':
            number = number/1_000_000_000_000_000_000
        elif new == 'zb':
            number = number/1_000_000_000_000_000_000_000
        elif new == 'yb':
            number = number/1_000_000_000_000_000_000_000_000
    
    elif original == 'kb':
        if new == '':
            number = number*1_000
        elif new == 'kb':
            None
        elif new == 'mb':
            number = number/1_000
        elif new == 'gb':
            number = number/1_000_000
        elif new == 'tb':
            number = number/1_000_000_000
        elif new == 'pb':
            number = number/1_000_000_000_000
        elif new == 'eb':
            number = number/1_000_000_000_000_000
        elif new == 'zb':
            number = number/1_000_000_000_000_000_000
        elif new == 'yb':
            number = number/1_000_000_000_000_000_000_000
    
    elif original == 'gb':
        if new == '':
            number = number*1_000_000_000
        elif new == 'kb':
            number = number*1_000_000
        elif new == 'mb':
            number = number*1_000
        elif new == 'gb':
            None
        elif new == 'tb':
            number = number/1_000
        elif new == 'pb':
            number = number/1_000_000
        elif new == 'eb':
            number = number/1_000_000_000
        elif new == 'zb':
            number = number/1_000_000_000_000
        elif new == 'yb':
            number = number/1_000_000_000_000_000
    
    elif original == 'tb':
        if new == '':
            number = number*1_000_000_000_000
        elif new == 'kb':
            number = number*1_000_000_000
        elif new == 'mb':
            number = number*1_000_000
        elif new == 'gb':
            number = number*1_000
        elif new == 'tb':
            None
        elif new == 'pb':
            number = number/1_000
        elif new == 'eb':
            number = number/1_000_000
        elif new == 'zb':
            number = number/1_000_000_000
        elif new == 'yb':
            number = number/1_000_000_000_000

    elif original == 'pb':
        if new == '':
            number = number*1_000_000_000_000_000
        elif new == 'kb':
            number = number*1_000_000_000_000
        elif new == 'mb':
            number = number*1_000_000_000
        elif new == 'gb':
            number = number*1_000_000
        elif new == 'tb':
            number = number*1_000
        elif new == 'pb':
            None
        elif new == 'eb':
            number = number/1_000
        elif new == 'zb':
            number = number/1_000_000
        elif new == 'yb':
            number = number/1_000_000_000

    elif original == 'eb':
        if new == '':
            number = number*1_000_000_000_000_000_000
        elif new == 'kb':
            number = number*1_000_000_000_000_000
        elif new == 'mb':
            number = number*1_000_000_000_000
        elif new == 'gb':
            number = number*1_000_000_000
        elif new == 'tb':
            number = number*1_000_000
        elif new == 'pb':
            number = number*1_000
        elif new == 'eb':
            None
        elif new == 'zb':
            number = number/1_000
        elif new == 'yb':
            number = number/1_000_000
    
    elif original == 'zb':
        if new == '':
            number = number*1_000_000_000_000_000_000_000
        elif new == 'kb':
            number = number*1_000_000_000_000_000_000
        elif new == 'mb':
            number = number*1_000_000_000_000_000
        elif new == 'gb':
            number = number*1_000_000_000_000
        elif new == 'tb':
            number = number*1_000_000_000
        elif new == 'pb':
            number = number*1_000_000
        elif new == 'eb':
            number = number*1_000
        elif new == 'zb':
            None
        elif new == 'yb':
            number = number/1_000
    
    elif original == 'yb':
        if new == '':
            number = number*1_000_000_000_000_000_000_000_000
        elif new == 'kb':
            number = number*1_000_000_000_000_000_000_000
        elif new == 'mb':
            number = number*1_000_000_000_000_000_000
        elif new == 'gb':
            number = number*1_000_000_000_000_000
        elif new == 'tb':
            number = number*1_000_000_000_000
        elif new == 'pb':
            number = number*1_000_000_000
        elif new == 'eb':
            number = number*1_000_000
        elif new == 'zb':
            number = number*1_000
        elif new == 'yb':
            None

    if printed == True:
        print(number)
    else:
        return number

def even_or_odd_(number, printed=False):
    """Return whether a number is even or odd."""
    if number%2 == 0: # If the number divided by 2 has a remainder of zero.
        number = 'even' # Then the number is an even number.
    else:
        number = 'odd' # If not then it's an odd number.

    if printed:
        print(number)
    else:
        return number

def prime_or_composite_(number, printed=False):
    """Return whether a number is prime or composite."""
    # If the number's factors are 1 and itself.
    if get_factors_(number) == [1, number]:
        number = 'prime' # Then the number is a prime number.
    else:
        number = 'composite' # If not then it's a composite number.

    if printed:
        print(number)
    else:
        return number
