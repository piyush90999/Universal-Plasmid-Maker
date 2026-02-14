# src/ori_finder.py

def calculate_gc_skew(sequence):
    """
    Identifies the ORI by finding the global minimum of the Cumulative GC Skew.
    """
    sequence = sequence.upper()
    current_skew = 0
    min_skew = 0
    min_index = 0
    
    for i, base in enumerate(sequence):
        if base == 'G':
            current_skew += 1
        elif base == 'C':
            current_skew -= 1
        
        if current_skew < min_skew:
            min_skew = current_skew
            min_index = i
            
    return min_index

def extract_ori(sequence, window_size=500):
    """Extracts a sequence block around the detected ORI index."""
    idx = calculate_gc_skew(sequence)
    start = max(0, idx - window_size)
    end = min(len(sequence), idx + window_size)
    return sequence[start:end]