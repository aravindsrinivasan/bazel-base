load("@pip//:requirements.bzl", "requirement")

package(default_visibility = ["//visibility:public"])

py_binary(
    name = "say_hello",
    srcs = ["say_hello.py"],
    deps = [
        "//protos:sample_py_proto",
        requirement('glog'),
    ],
)
