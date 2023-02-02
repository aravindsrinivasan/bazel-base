```s
# TODO: Need to use this flag explicitly when using compiled protos. Otherwise
# the proto will overwrite the py_library deps and no imports will be available.
# Docs: https://rules-proto-grpc.com/en/latest/lang/python.html#python
legacy_create_init = False,
```

## Common Issues

## cannot import name 'builder'
```
Traceback (most recent call last):
  File "/private/var/tmp/_bazel_kevinhou/cb03b3e13816f52cee1882bf21f0ab52/execroot/__main__/bazel-out/darwin_arm64-fastbuild/bin/server/server.runfiles/__main__/server/server.py", line 17, in <module>
    from gps_analysis.gps_analysis import GpxAnalysis
  File "/private/var/tmp/_bazel_kevinhou/cb03b3e13816f52cee1882bf21f0ab52/execroot/__main__/bazel-out/darwin_arm64-fastbuild/bin/server/server.runfiles/__main__/gps_analysis/gps_analysis.py", line 6, in <module>
    from gps_analysis.utils import calculations, watts
  File "/private/var/tmp/_bazel_kevinhou/cb03b3e13816f52cee1882bf21f0ab52/execroot/__main__/bazel-out/darwin_arm64-fastbuild/bin/server/server.runfiles/__main__/gps_analysis/utils/calculations.py", line 4, in <module>
    from protos.gps_pb2 import EarthLocation
  File "/private/var/tmp/_bazel_kevinhou/cb03b3e13816f52cee1882bf21f0ab52/execroot/__main__/bazel-out/darwin_arm64-fastbuild/bin/server/server.runfiles/__main__/protos/gps_py_proto_pb/protos/gps_pb2.py", line 5, in <module>
    from google.protobuf.internal import builder as _builder
ImportError: cannot import name 'builder' from 'google.protobuf.internal' (/opt/anaconda3/lib/python3.9/site-packages/google/protobuf/internal/__init__.py)
```

### Solution
Must upgrade to latest package: `pip install --upgrade protobuf`