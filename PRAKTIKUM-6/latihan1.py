from typing import List, Tuple
import sys
import math

# ---------- DES Tables ----------

# Permuted Choice 1 (PC-1) – 64 → 56 bit (menghapus bit paritas)
PC1 = [
    57,49,41,33,25,17,9,
    1,58,50,42,34,26,18,
    10,2,59,51,43,35,27,
    19,11,3,60,52,44,36,
    63,55,47,39,31,23,15,
    7,62,54,46,38,30,22,
    14,6,61,53,45,37,29,
    21,13,5,28,20,12,4
]

# Permuted Choice 2 (PC-2) - 56 -> 48 bits
PC2 = [
    14,17,11,24,1,5,
    3,28,15,6,21,10,
    23,19,12,4,26,8,
    16,7,27,20,13,2,
    41,52,31,37,47,55,
    30,40,51,45,33,48,
    44,49,39,56,34,53,
    46,42,50,36,29,32
]

# Number of left shifts per round
SHIFT_SCHEDULE = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]

# Initial Permutation (IP)
IP = [
    58,50,42,34,26,18,10,2,
    60,52,44,36,28,20,12,4,
    62,54,46,38,30,22,14,6,
    64,56,48,40,32,24,16,8,
    57,49,41,33,25,17,9,1,
    59,51,43,35,27,19,11,3,
    61,53,45,37,29,21,13,5,
    63,55,47,39,31,23,15,7
]

# Inverse Initial Permutation (IP^-1)
IP_INV = [
    40,8,48,16,56,24,64,32,
    39,7,47,15,55,23,63,31,
    38,6,46,14,54,22,62,30,
    37,5,45,13,53,21,61,29,
    36,4,44,12,52,20,60,28,
    35,3,43,11,51,19,59,27,
    34,2,42,10,50,18,58,26,
    33,1,41,9,49,17,57,25
]

# Expansion (E) - expands 32 -> 48
E = [
    32,1,2,3,4,5,
    4,5,6,7,8,9,
    8,9,10,11,12,13,
    12,13,14,15,16,17,
    16,17,18,19,20,21,
    20,21,22,23,24,25,
    24,25,26,27,28,29,
    28,29,30,31,32,1
]

# S-boxes: 8 boxes, each 4x16
S_BOXES = [
    # S1
    [
        [14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],
        [0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],
        [4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],
        [15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]
    ],
    # S2
    [
        [15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],
        [3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],
        [0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],
        [13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]
    ],
    # S3
    [
        [10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],
        [13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],
        [13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],
        [1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]
    ],
    # S4
    [
        [7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],
        [13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],
        [10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],
        [3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]
    ],
    # S5
    [
        [2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],
        [14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],
        [4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],
        [11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]
    ],
    # S6
    [
        [12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],
        [10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],
        [9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],
        [4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]
    ],
    # S7
    [
        [4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],
        [13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],
        [1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],
        [6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]
    ],
    # S8
    [
        [13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],
        [1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],
        [7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],
        [2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]
    ]
]

# P-permutation (32 bits)
P = [
    16,7,20,21,
    29,12,28,17,
    1,15,23,26,
    5,18,31,10,
    2,8,24,14,
    32,27,3,9,
    19,13,30,6,
    22,11,4,25
]

# ---------- Utilities ----------

def bytes_to_bits(b: bytes) -> List[int]:
    bits = []
    for byte in b:
        for i in range(8):
            bits.append((byte >> (7 - i)) & 1)
    return bits

def bits_to_bytes(bits: List[int]) -> bytes:
    if len(bits) % 8 != 0:
        raise ValueError("bits length must be multiple of 8")
    out = bytearray()
    for i in range(0, len(bits), 8):
        val = 0
        for j in range(8):
            val = (val << 1) | bits[i+j]
        out.append(val)
    return bytes(out)

def bits_to_hex(bits: List[int]) -> str:
    return bits_to_bytes(bits).hex().upper()

def permute(bits: List[int], table: List[int]) -> List[int]:
    # table uses 1-based indexing
    return [bits[i-1] for i in table]

def left_rotate(lst: List[int], n: int) -> List[int]:
    n = n % len(lst)
    return lst[n:] + lst[:n]

def xor_bits(a: List[int], b: List[int]) -> List[int]:
    return [x ^ y for x,y in zip(a,b)]

def int_from_bits(bits: List[int]) -> int:
    v = 0
    for b in bits:
        v = (v << 1) | b
    return v

def bits_from_int(value: int, size: int) -> List[int]:
    return [(value >> (size-1-i)) & 1 for i in range(size)]

# ---------- Key schedule ----------

def generate_subkeys(key_bits_64: List[int]) -> Tuple[List[List[int]], List[List[int]]]:
    # PC-1: 64 -> 56
    key56 = permute(key_bits_64, PC1)
    # Split into C0, D0 (28 bits each)
    C = key56[:28]
    D = key56[28:]
    Cs = [C.copy()]
    Ds = [D.copy()]
    subkeys = []
    for round_idx, shift in enumerate(SHIFT_SCHEDULE, start=1):
        C = left_rotate(C, shift)
        D = left_rotate(D, shift)
        Cs.append(C.copy())
        Ds.append(D.copy())
        combined = C + D  # 56 bits
        Ki = permute(combined, PC2)  # 48 bits
        subkeys.append(Ki)
    return subkeys, (Cs, Ds)

# ---------- Feistel (F) function ----------

def sbox_substitute(bits48: List[int]) -> List[int]:
    # split into 8 groups of 6
    out_bits = []
    for i in range(8):
        block = bits48[i*6:(i+1)*6]
        row = (block[0] << 1) | block[5]
        col = int_from_bits(block[1:5])
        s_val = S_BOXES[i][row][col]
        out_bits.extend(bits_from_int(s_val, 4))
    return out_bits  # 32 bits

def feistel(R: List[int], K: List[int]) -> List[int]:
    # Expansion 32 -> 48
    expanded = permute(R, E)
    # XOR with subkey
    x = xor_bits(expanded, K)
    # S-box substitution 48 -> 32
    s_out = sbox_substitute(x)
    # P permutation 32 -> 32
    p_out = permute(s_out, P)
    return p_out

# ---------- DES encrypt 64-bit block ----------

def des_encrypt_block(block_bits: List[int], subkeys: List[List[int]]) -> List[int]:
    # Initial Permutation
    ip = permute(block_bits, IP)
    L = ip[:32]
    R = ip[32:]
    # 16 rounds
    for i in range(16):
        Ki = subkeys[i]
        f_out = feistel(R, Ki)
        newR = xor_bits(L, f_out)
        L = R
        R = newR
    # Preoutput (R16,L16)
    preoutput = R + L
    # Final Permutation (IP^-1)
    cipher_bits = permute(preoutput, IP_INV)
    return cipher_bits

# ---------- Padding ----------

def pkcs7_pad(data: bytes, block_size: int = 8) -> bytes:
    pad_len = block_size - (len(data) % block_size)
    if pad_len == 0:
        pad_len = block_size
    return data + bytes([pad_len]) * pad_len

# ---------- Main flow ----------

def validate_key(key_str: str) -> bytes:
    if len(key_str) == 0:
        raise ValueError("Key must not be empty")
    if len(key_str) > 8:
        # user requested max 8 chars; we'll truncate and warn
        print("Warning: key longer than 8 chars - truncating to first 8 characters.")
        key_str = key_str[:8]
    # pad key to 8 bytes if shorter (DES keys are 8 bytes; parity bits ignored)
    key_bytes = key_str.encode('utf-8')
    if len(key_bytes) < 8:
        key_bytes = key_bytes + b'\x00' * (8 - len(key_bytes))
    return key_bytes

def process(plaintext: str, key_str: str, show_details: bool = True):
    # Key processing
    key_bytes = validate_key(key_str)
    key_bits = bytes_to_bits(key_bytes)  # 64 bits

    print("\n=====================")
    print("🔐 INFORMASI KUNCI")
    print("=====================")
    print(f"Kunci (byte): {key_bytes}")
    print("Kunci (64-bit binary):")
    print(''.join(str(b) for b in key_bits))

    # Generate subkeys
    subkeys, (Cs, Ds) = generate_subkeys(key_bits)

    # Show C0 and D0
    print("\n=====================")
    print("🔑 PEMBENTUKAN SUBKEY")
    print("=====================")
    print("C0:", ''.join(str(b) for b in Cs[0]))
    print("D0:", ''.join(str(b) for b in Ds[0]))

    for i in range(1, len(Cs)):
        print(f"Round {i:2d} | C{i}: {''.join(str(b) for b in Cs[i])} | D{i}: {''.join(str(b) for b in Ds[i])}")

    # Print subkeys
    print("\n=====================")
    print("🔑 16 SUBKEY (K1 - K16)")
    print("=====================")
    for i, k in enumerate(subkeys, start=1):
        binstr = ''.join(str(b) for b in k)
        hexstr = bits_to_hex(k)
        print(f"K{i:2d}: {binstr}   | hex: {hexstr}")

    # Plaintext processing and padding
    plaintext_bytes = plaintext.encode('utf-8')
    padded = pkcs7_pad(plaintext_bytes)

    print("\n=====================")
    print("📄 PLAINtext")
    print("=====================")
    print(f"Plaintext bytes: {plaintext_bytes}")
    print(f"Padded (len={len(padded)}): {padded}")

    # Encrypt block-by-block
    cipher_bits_all = []
    for block_idx in range(0, len(padded), 8):
        block = padded[block_idx:block_idx+8]
        block_bits = bytes_to_bits(block)

        print("\n----------------------------")
        print(f"🔷 BLOCK {block_idx//8 + 1}")
        print("----------------------------")
        print("Block bytes:", block)
        print("Block bits :", ''.join(str(b) for b in block_bits))

        cipher_bits = des_encrypt_block(block_bits, subkeys)
        cipher_bits_all.extend(cipher_bits)

        print("Cipher block bits:", ''.join(str(b) for b in cipher_bits))
        print("Cipher block hex :", bits_to_hex(cipher_bits))

    cipher_hex = bits_to_hex(cipher_bits_all)
    cipher_bin = ''.join(str(b) for b in cipher_bits_all)

    print("\n=====================")
    print("🔒 HASIL AKHIR ENKRIPSI DES")
    print("=====================")
    print("Ciphertext (binary):")
    print(cipher_bin)
    print("\nCiphertext (hex):")
    print(cipher_hex)

    return {
        "subkeys": subkeys,
        "cipher_bits": cipher_bits_all,
        "cipher_hex": cipher_hex,
        "padded_plaintext": padded
    }


# ---------- CLI ----------

def main():
    print("DES Encryption - Implementasi lengkap (enkripsi saja)")
    try:
        plaintext = input("Masukkan plaintext: ")
        key_input = input("Masukkan kunci (max 8 karakter): ")
        result = process(plaintext, key_input, show_details=True)
    except Exception as e:
        print("Error:", e)
        sys.exit(1)

if __name__ == "__main__":
    main()
