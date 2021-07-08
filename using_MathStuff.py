import MathStuff

# Example of how to use get_factors_
factor_test = MathStuff.get_factors_(4096)
print(f"get_factors test: {factor_test}")

# Example of how to use common_factors_
common_factors_test = MathStuff.common_factors_([10, 20, 30])
print(f"\ncommon_factors test: {common_factors_test}")

# Example of how to use gcf_
gcf_test = MathStuff.gcf_([10, 20, 30])
print(f"\ngcf test: {gcf_test}")

# Example of how to use lcf_
lcf_test = MathStuff.lcf_([10, 20, 30])
print(f"\nlcf test: {lcf_test}")

# Example of how to use root_
root_test = MathStuff.root_(16, 2)
print(f"\nroot test: {root_test}")

# Example of how to use temperature_convert_
temp_test = MathStuff.temperature_convert_(32, 'F', 'C')
print(f"\ntemperature_convert test: {temp_test}")

# Example of how to use maintain_aspect_ratio_
mar_test = MathStuff.maintain_aspect_ratio_([20, 20], [100, 70])
print(f"\nmaintain_aspect_ratio test: {mar_test}")

# Example of how to use average_
average_test = MathStuff.average_([8, 16, 32, 64, 128, 256])
print(f"\naverage test: {average_test}")

# Example of how to use median_
median_test = MathStuff.median_([2, 4, 6, 8])
print(f"\nmedian test: {median_test}")

# Example of how to use mode_
mode_test = MathStuff.mode_([1, 2, 1])
print(f"\nmode test: {mode_test}")

# Example of how to use range_
range_test = MathStuff.range_([1, 1, 2, 3, 4, 4, 5, 6, 7])
print(f"\nrange test: {range_test}")

# Example of how to use solid_polygon_info_
solid_polygon_info_test = MathStuff.solid_polygon_info_(4)
print(f"\nsolid_polygon_info test: {solid_polygon_info_test}")

# Example of how to use extrapolate_
extrapolate_test = MathStuff.extrapolate_(1, 2, 'multiply', 13)
print(f"\nextrapolate test: {extrapolate_test}")

# Example of how to use byte_convert_
byte_convert_test = MathStuff.byte_convert_(1000, '', 'kb')
print(f"\nbyte_convert test: {byte_convert_test}")

# Example of how to use even_or_odd_
even_or_odd_test = MathStuff.even_or_odd_(64)
print(f"\neven_or_odd test: {even_or_odd_test}")

# Example of how to use even_or_odd_
prime_or_composite_test = MathStuff.prime_or_composite_(7)
print(f"\nprime_or_composite test: {prime_or_composite_test}")
