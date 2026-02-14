# src/assembler.py
from src.database import get_enzyme_sequence, get_marker_sequence

def parse_design_file(filepath):
    """Parses comma-separated design components."""
    design_list = []
    with open(filepath, 'r') as f:
        for line in f:
            if line.strip() and not line.startswith('*'):
                parts = line.strip().split(',')
                if len(parts) == 2:
                    design_list.append((parts[0].strip(), parts[1].strip()))
    return design_list

def build_plasmid(ori_seq, design_components):
    """Assembles the final sequence string."""
    final_seq = ori_seq
    for label, part_name in design_components:
        # Check enzymes first
        seq = get_enzyme_sequence(part_name)
        if not seq:
            # Check markers second
            seq = get_marker_sequence(part_name)
        
        if seq:
            final_seq += seq
        else:
            print(f"Warning: Component {part_name} not found in database.")
            
    return final_seq