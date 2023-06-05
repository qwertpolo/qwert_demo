def filter_lines_starting_with_pipe_space(lst):
    return [s for s in lst if s.startswith("| ")]

# def filter_lines_starting_with_pipe_space(lst):
#     lst.pop()
#     return lst