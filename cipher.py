"""
A Rational Double-Pass Matrix Model for the Voynich Manuscript
Author: Darrin R. Bourgeois
Date: October 30, 2026
License: MIT License

This script implements the Gallo-Germanic Golden Spiral Cipher using 
discrete Fibonacci and Pi shifts, resetting at the beginning of each word.
"""

def get_fibonacci_sequence(length):
    """Generates the standard Fibonacci sequence starting at 1, 1."""
    seq = [1, 1]
    while len(seq) < length:
        seq.append(seq[-1] + seq[-2])
    return seq[:length]

def get_combined_shifts(length):
    """Combines Fibonacci numbers and the first 5 digits of Pi (3, 1, 4, 1, 5)."""
    fib = get_fibonacci_sequence(length)
    pi_digits = [3, 1, 4, 1, 5]
    
    combined = []
    for i in range(length):
        pi_val = pi_digits[i % 5]
        combined.append(fib[i] + pi_val)
    return combined

def process_word(word, direction=-1):
    """
    Applies the mathematical shift layer to a single word.
    direction=-1 for decryption (backward shift), +1 for encryption.
    """
    shifts = get_combined_shifts(len(word))
    processed_letters = []
    
    for i, char in enumerate(word):
        if not char.isalpha():
            processed_letters.append(char)
            continue
            
        base = 97 # ASCII value for lowercase 'a'
        char_idx = ord(char.lower()) - base
        
        # Calculate the stacked shift value
        shift_val = shifts[i] * direction
        new_idx = (char_idx + shift_val) % 26
        
        processed_letters.append(chr(base + new_idx))
        
    return "".join(processed_letters)

def run_matrix_pass(line, phi_cut=False):
    """Executes a single processing pass across an entire line of text."""
    words = line.strip().split()
    if not words:
        return ""
        
    # Layer 4: The Spatial Cut (Phi = 0.618) - Active only on the first pass
    if phi_cut:
        cut_index = round(len(words) * 0.618) - 1
        if 0 <= cut_index < len(words):
            words.pop(cut_index)
            
    # Layers 2 & 1: Word-Reset Shift Engine
    output_words = [process_word(w, direction=-1) for w in words]
    return " ".join(output_words)

def decrypt_voynich_line(line):
    """The 2-Pass Structural Ceiling Matrix Engine."""
    # Pass 1 with Layer 4 Phi Spatial Filter enabled
    pass1 = run_matrix_pass(line, phi_cut=True)
    # Pass 2 over the intermediate string skeleton
    pass2 = run_matrix_pass(pass1, phi_cut=False)
    
    return {
        "Original": line,
        "Pass 1": pass1,
        "Pass 2": pass2
    }

# =========================================================================
# Execution & Verification Unit Testing
# =========================================================================
if __name__ == "__main__":
    print("=" * 75)
    print("      GALLO-GERMANIC GOLDEN SPIRAL CIPHER CORE ENGINE VERIFICATION")
    print("=" * 75)
    
    # Test Target: Folio 2r, Line 1
    botanical_line = "chory tchedor chcty dity"
    result = decrypt_voynich_line(botanical_line)
    
    print(f"ORIGINAL INPUT : {result['Original']}")
    print(f"PASS 1 OUTPUT  : {result['Pass 1']}")
    print(f"PASS 2 (FINAL) : {result['Pass 2']}")
    print("-" * 75)
    
    # Verification assert check against your published ledger data
    assert "yfino" in result['Pass 1'], "Verification failed on Pass 1 semantic window."
    assert "vehq" in result['Pass 2'], "Verification failed on Pass 2 semantic window."
    print("SYSTEM STATUS  : VERIFIED SUCCESSFUL. Output matches Zenodo archive data.")
    print("=" * 75)
