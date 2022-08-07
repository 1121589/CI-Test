py_library(
    name = "testing_sim",
    srcs = ["testing_sim.py"],
    imports = ["."],
    visibility = ["//applications/app1:__subpackages__"],
)


py_test(
    name = "main",
    srcs = ["main.py"],
    args = [
        "--file=bazel-bin/applications/app1/water_level.elf", 
        "--commands=applications/app1/testing/commands.gdb",
    ],
    data = glob(["applications/**/*.gdb"]),
    deps = [
        ":testing_sim",
    ],
)
