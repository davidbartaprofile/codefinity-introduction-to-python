# You are managing data for a new product that has just been added to a grocery store system. Your task is to analyze the product information using membership operators and type comparisons.
#   Check if the substring 'raw' exists in description. Store the result in contains_raw.
#   Check if the substring 'Imported' exists in description. Store the result in contains_Imported.
#   Check if price is of type float. Store the result in price_is_float.
#   Check if count is of type int. Store the result in count_is_int.
#   Print the results exactly in the format provided in the code.
#   Remember that python is case sensitive, so 'imported' and 'Imported' are considered different strings.


# Product details
description = "Imported honey, raw and unfiltered"
price = "5.99"
count = 120

contains_raw = "raw" in description
contains_Imported = "Imported" in description
price_is_float = type(price) == float
count_is_int = type(count) == int

print("Contains 'raw':", contains_raw)
print("Contains 'Imported':", contains_Imported)
print("Is price a float?:", price_is_float)
print("Is count an integer?:", count_is_int)
