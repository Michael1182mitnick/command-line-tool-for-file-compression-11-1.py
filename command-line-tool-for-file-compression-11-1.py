# Command-Line_Tool_for_File_Compression
# Develop a command-line tool that can compress and decompress files using various algorithms like Huffman Coding or LZW.
# Command Line Interface

import argparse


def main():
    parser = argparse.ArgumentParser(
        description="File compression and decompression tool")

    parser.add_argument("action", choices=[
                        "compress", "decompress"], help="Action to perform")
    parser.add_argument("algorithm", choices=[
                        "huffman", "lzw"], help="Compression algorithm")
    parser.add_argument("file", help="File to compress or decompress")

    args = parser.parse_args()

    if args.algorithm == "huffman":
        if args.action == "compress":
            huffman_compress(args.file)
        elif args.action == "decompress":
            huffman_decompress(args.file)
    elif args.algorithm == "lzw":
        if args.action == "compress":
            lzw_compress(args.file)
        elif args.action == "decompress":
            lzw_decompress(args.file)


if __name__ == "__main__":
    main()
