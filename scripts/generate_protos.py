#!/usr/bin/env python3
import os
import re
import subprocess
import sys
from pathlib import Path
import shutil

# Calculate paths relative to the project root
PROJECT_ROOT = Path(__file__).parent.parent
PROTO_DIR = PROJECT_ROOT / "protos"
GENERATED_ROOT = PROJECT_ROOT / "src" / "generated"

def clean():
    """Clean generated directory"""
    if GENERATED_ROOT.exists():
        shutil.rmtree(GENERATED_ROOT)
    GENERATED_ROOT.mkdir(parents=True, exist_ok=True)
    (GENERATED_ROOT / "__init__.py").touch()

def generate():
    """Generate gRPC/protobuf files"""
    # Check if proto directory exists
    if not PROTO_DIR.exists():
        print(f"Error: Proto directory not found at {PROTO_DIR}")
        return

    # Get all proto files
    proto_files = list(PROTO_DIR.glob("*.proto"))
    if not proto_files:
        print(f"Warning: No .proto files found in {PROTO_DIR}")
        return

    for proto_file in proto_files:
        module = proto_file.stem
        output_dir = GENERATED_ROOT / module

        output_dir.mkdir(exist_ok=True)

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
        
        # Fix imports in generated files
        fix_imports(output_dir, module)
        
        print(f"Generated {module} in {output_dir}")

def fix_imports(generated_dir, module_name):
    """Fix imports in generated files to use correct package paths"""
    pb2_file = generated_dir / f"{module_name}_pb2.py"
    grpc_file = generated_dir / f"{module_name}_pb2_grpc.py"

    # Fix imports in the grpc file
    if grpc_file.exists():
        with open(grpc_file, "r") as f:
            content = f.read()

        # Replace direct imports with relative imports
        content = re.sub(
            fr"import {module_name}_pb2",
            fr"from . import {module_name}_pb2",
            content
        )

        with open(grpc_file, "w") as f:
            f.write(content)

def main():
    """Main entry point"""
    print(f"Generating gRPC code from proto files in {PROTO_DIR}")
    print(f"Output directory: {GENERATED_ROOT}")
    clean()
    generate()
    print("gRPC code generation complete")
    return 0

if __name__ == "__main__":
    sys.exit(main())
