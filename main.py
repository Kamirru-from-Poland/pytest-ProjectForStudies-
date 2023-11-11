import pytest
import random

element_in_list = lambda list, element : list.count(element) if len(list) > 0 else 0

if __name__ == "__main__":
    pytest.main()
    random_numbers = [random.choice([i for i in range(1, 10) if i != 6]) for _ in range(20)]
    print(random_numbers)

    print(element_in_list(random_numbers, 9))
    print(bool(element_in_list(random_numbers, 9)))

    print(element_in_list(random_numbers, 6))
    print(bool(element_in_list(random_numbers, 6)))