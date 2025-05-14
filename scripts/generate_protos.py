#!/usr/bin/env python3
import os
import subprocess
import sys
from pathlib import Path
import shutil

PROTO_DIR = Path("../protos").resolve()
GENERATED_ROOT = Path("../src/generated").resolve()

def clean():
    """Clean generated directory"""
    if GENERATED_ROOT.exists():
        shutil.rmtree(GENERATED_ROOT)
    GENERATED_ROOT.mkdir(parents=True)
    (GENERATED_ROOT / "__init__.py").touch()

def generate():
    """Generate gRPC/protobuf files"""
    for proto_file in PROTO_DIR.glob("*.proto"):
        module = proto_file.stem
        output_dir = GENERATED_ROOT / module

        output_dir.mkdir()

        cmd = [
            sys.executable, "-m", "grpc_tools.protoc",
            f"-I{PROTO_DIR}",
            f"--python_out={output_dir}",
            f"--grpc_python_out={output_dir}",
            str(proto_file.name)
        ]

        result = subprocess.run(cmd, cwd=PROTO_DIR, capture_output=True)
        if result.returncode != 0:
            print(f"Error generating {module}:")
            print(result.stderr.decode())
            continue

        # Create package marker
        (output_dir / "__init__.py").touch()
        print(f"Generated {module} in {output_dir.relative_to(Path.cwd())}")

if __name__ == "__main__":
    clean()
    generate()