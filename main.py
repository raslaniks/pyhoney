import os
import sys
import pprint
import detect_c_compiler as comp_detector
import hisp
import hnyir
import argparse
import random


# NDRAEY: arguments parsing

argparser = argparse.ArgumentParser("hny")

argparser.add_argument("--no-stdlib", action="store_true")
argparser.add_argument("-c", dest="compiler")
argparser.add_argument("-cf", dest="compiler_flags")
argparser.add_argument("-o", dest="output")
argparser.add_argument("FILE")

args = argparser.parse_args()

# vivavy: compile time
# NDRAEY: refactored
# vivavy: added temp file names mangling

module_name = os.path.splitext(args.FILE)[0]

name_hash = hex(hash(module_name) + random.randint(-abs(hash(module_name)), \
	abs(hash(module_name))))[2:]

module_name += "." + name_hash  # vivavy: we need it for security: 
                                # if there was not mangling, file names could conflict,
                                # and it can cause a lot of problems.

hnyir.gen_write_hisp(args.FILE, module_name+".hsp")
hisp.hisp_to_c(module_name + ".hsp", args.no_stdlib)

inf = module_name + ".c"
outf = args.output if args.output else os.path.splitext(args.FILE)[0] + ".out"

comp = args.compiler
comp_opts = args.compiler_flags or ""

# If user don't provide compiler manually, then detect it automatically
if comp is None:
    comp = comp_detector.detect_compiler()

command = comp + " " + comp_opts + " " + inf + " -o " + outf

# print("Executing:", command)  # vivavy: please erstrict output better.
                                # It can break some building systems.

os.system(command)

# vivavy: we need to clear temp files after execution
os.system("rm -f " + module_name + ".hsp")
os.system("rm -f " + module_name + ".c")
