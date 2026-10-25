from pybuilder.core import init, use_plugin

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.distutils")

name = "calculator_Majd_Aboul_Hosn"
version = "0.1"
summary = "A simple calculator for Lab 6."
default_task = "publish"


@init
def initialize(project):
    project.set_property("dir_source_main_python", "src/main/python")
    project.set_property(
        "dir_source_unittest_python",
        "tests/unittest/calculator_Majd_Aboul_Hosn",
    )
    project.set_property("unittest_module_glob", "test_*")
    # Keep generated paths short enough for Windows.
    project.set_property("dir_dist", "$dir_target/dist")
    project.set_property("distutils_commands", ["sdist", "bdist_wheel"])
