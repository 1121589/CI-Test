load("@rules_cc//cc:defs.bzl", "cc_library", "cc_test")

cc_library(
    name = "test_implementation",
    srcs = ["test_implementation.c"],
    deps = [
        "//applications/app2:even_number",
        "//applications/app2/test/unity:unity",
        ],
)

cc_test(
    name = "main",
    srcs = [
        "main_test.c",
    ],
    deps = [
        ":test_implementation",
        "//applications/app2:even_number",
        "//applications/app2/test/unity:unity",
    ],
)
