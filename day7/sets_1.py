# Data
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

# 1. Find the length of the set it_companies
print("Length of it_companies:", len(it_companies))

# 2. Add 'Twitter' to it_companies
it_companies.add('Twitter')
print("After adding Twitter:", it_companies)

# 3. Insert multiple IT companies at once
it_companies.update(['Spotify', 'Adobe', 'Intel'])
print("After adding multiple companies:", it_companies)

# 4. Remove one company (e.g., 'Oracle')
it_companies.remove('Oracle')
print("After removing Oracle:", it_companies)

# 5. Difference between remove and discard
# remove() raises an error if item not found
# discard() does not raise an error

# Example:
try:
    it_companies.remove('NonExistentCompany')  # Will raise an error
except KeyError:
    print("remove(): Tried to remove a company that doesn't exist!")

it_companies.discard('NonExistentCompany')  # No error raised
print("discard(): Safe to use even if the item doesn't exist")
