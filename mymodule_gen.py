
import sys

from pybindgen import FileCodeSink
from pybindgen.gccxmlparser import ModuleParser

def generate():
    module_parser = ModuleParser('opennurbs', '::')
    module_parser.parse(["opennurbs.h"], includes=['"opennurbs.h"'], pygen_sink=FileCodeSink(sys.stdout))



if __name__ == '__main__':
    generate()

