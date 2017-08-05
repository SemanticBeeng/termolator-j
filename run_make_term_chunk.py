#!/usr/bin/env python3

from inline_terms import *
from refactoring_support import *


## @func comp_termChunker
def main(args):
    infile_list = args[1]
    outfile_list = args[2]
    make_term_chunk_file_list(infile_list, outfile_list)


if __name__ == '__main__':
    # sys.settrace(trace_args_and_return)
    sys.exit(main(sys.argv))
