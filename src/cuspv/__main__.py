import argparse

def main():
    parser = argparse.ArgumentParser(
        prog='cuspv',
        description='cuspv: A CUDA to SPIR-V compiler.'
    )

    parser.add_argument(
        "input_file", 
        type=argparse.FileType('r'), 
        help="Path to the CUDA input file."
    )

    parser.add_argument(
        "-o", "--output", 
        type=str, 
        default="output.spv",
        help="Path to the output SPIR-V file. Defaults to 'output.spv'."
    )

    args = parser.parse_args()

    with args.input_file as f:
        cuda_code = f.read()
        # Process the CUDA code and compile to SPIR-V
        # For the sake of this example, just printing it:
        print(cuda_code)


if __name__ == "__main__":
    main()