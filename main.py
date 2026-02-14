# main.py
import argparse
import os
from src.ori_finder import extract_ori
from src.assembler import parse_design_file, build_plasmid

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", required=True, help="Path to pUC19.fa")
    parser.add_argument("-d", "--design", required=True, help="Path to Design_pUC19.txt")
    args = parser.parse_args()

    # Dynamic naming: input 'data/pUC19.fa' -> 'pUC19_Output.Fa'
    base_name = os.path.splitext(os.path.basename(args.input))[0]
    output_name = f"{base_name}_Output.Fa"

    # Read input sequence
    with open(args.input, 'r') as f:
        # Skips the header and joins the lines 
        sequence = "".join([line.strip() for line in f if not line.startswith(">")])

    # Mining ORI from the unknown organism sequence 
    print(f"Mining ORI from {base_name}...")
    mined_ori = extract_ori(sequence)
    
    # Parsing the Design file provided (e.g., Design_pUC19.txt) 
    design = parse_design_file(args.design)
    print(f"Assembling plasmid according to {args.design}...")
    final_plasmid = build_plasmid(mined_ori, design)

    # Output to file with line wrapping
    with open(output_name, 'w') as f:
        f.write(f">{base_name}_Constructed_Plasmid\n")
        # Fix: Write in 80-character blocks for standard FASTA format
        for i in range(0, len(final_plasmid), 80):
            f.write(final_plasmid[i:i+80] + "\n")

    print(f"Successfully generated {output_name}")
    print("Verification: Sequence wrapped to 80 characters per line.")

if __name__ == "__main__":
    main()