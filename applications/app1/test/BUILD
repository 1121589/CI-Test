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
        "--file=water_level.elf", 
        "--commands=commands.gdb",
    ],
    data = glob(["applications/app1/**"]),
    deps = [
        ":testing_sim",
    ],
)
