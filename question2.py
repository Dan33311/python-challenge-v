################################################################################
#     ____                          __     _                          ___
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          |__ \
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \         __/ /
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /        / __/
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/        /____/
#
#  Question 2
################################################################################
#
# Instructions:
# Write a function that will swap a tuple of two items. For example, the function
# should change (x, y) into (y, x).
# Assign the function to `swapper` so that the function `run_swapper(..)` can use
# it. As always, there is a test suite that checks the result. It is in
# `question2_test.py.`


# My function
def swapper(tuple_to_swap):
    a, b = tuple_to_swap
    a, b = b, a
    print('✅ swapper function is running')
    return a, b


def run_swapper(list_of_tuples):
    print('✅ run_swapper function is running')
    # EXPECTED RESULT:
    return print('swapper_list:', list(map(swapper, list_of_tuples)))


# TEST
def test_run_swapper():
    run_swapper(
        [("a", "b"), ("c", "d"), ("e", "f")]
    )


test_run_swapper()

# TEST FILE
# def test_run_swapper():
#   assert run_swapper(
#     [ ("a", "b"), ("c", "d"), ("e", "f") ]
#   ) == [ ("b", "a"), ("d", "c"), ("f", "e")]
#
#   assert run_swapper(
#     [ (1, 1), ("foo", "bar"), (13, "cows"), (None, "Some") ]
#   ) == [ (1, 1), ("bar", "foo"), ("cows", 13), ("Some", None) ]
