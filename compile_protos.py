import os
import subprocess

def compile_protos(proto_dir: str, out_dir: str):
    # Ensure the output directory exists
    os.makedirs(out_dir, exist_ok=True)

    # Collect all .proto files
    proto_files = []
    for root, _, files in os.walk(proto_dir):
        for file in files:
            if file.endswith(".proto"):
                proto_files.append(os.path.join(root, file))

    # Check if there are any .proto files to compile
    if not proto_files:
        print(f"No .proto files found in {proto_dir}")
        return

    # Generate the command to compile all .proto files together
    command = [
        "protoc",
        f"--proto_path={proto_dir}",  # Set proto directory for imports
        f"--python_out={out_dir}",    # Set output directory for Python files
        *proto_files                  # Compile all collected .proto files
    ]

    # Run the protoc command
    result = subprocess.run(command, capture_output=True, text=True)

    # Check for errors during compilation
    if result.returncode != 0:
        print(f"Failed to compile protos: {result.stderr}")
    else:
        print(f"Compiled {len(proto_files)} proto files successfully!")

if __name__ == "__main__":
    # Path to the directory containing .proto files
    proto_directory = "./protos"

    # Path to the directory where the compiled Python files should go
    output_directory = "./generated"

    compile_protos(proto_directory, output_directory)
