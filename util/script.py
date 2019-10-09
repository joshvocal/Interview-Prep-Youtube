import sys

# Convert LeetCode title to markdown link
a = b = sys.argv[1]

one = "[" + a + "]"
two = '(#' + b.replace(' ', '-') + ')'

print(one + two)
