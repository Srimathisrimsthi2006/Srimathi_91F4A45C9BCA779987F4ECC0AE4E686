'''Write a function called linear_search_product that takes the list of products and a target product name as 
input. The function should perform a linear search to find the target product 
in the list and return a list of indices of all occurrences of the product if found, or an empty list if the product is 
not found'''

def linear_search_product(products, target_product):
  indices = []
  for i, product in enumerate(products):
    if product == target_product:
      indices.append(i)
  return indices


#eg input values
products = ["apple", "orange", "grapes", "apple", "banana", "papaya", "apple"]
target_product = "apple"
result = linear_search_product(products, target_product)
print(result)