import streamlit as st
import random
import math
from sympy import isprime

st.title("Alan Ibo jr Pogi")
st.write(
    """[Verse 1: Daniel Caesar] You don't know babe, when you hold me and kiss me slowly it's the sweetest thing, And it don't change if I had it my way, You would know that you are 
    [Pre-Chorus: Daniel Caesar] You're the coffee that I need in the morning, You're my sunshine in the rain when it's pouring, Won't you give yourself to me, Give it all, oh 
    [Chorus: Daniel Caesar & H.E.R.] I just wanna see, I just wanna see how beautiful you are, You know that I see it, I know you're a star, Where you go I'll follow, No matter how far, If life is a movie, oh you're the best part, oh oh oh, You're the best part, oh oh oh, Best part 
    [Verse 2: H.E.R.] It's this sunrise and those brown eyes, yes, You're the one that I desire when we wake up, And then we head out, ooh yeah I just wanna be, just wanna be here with you, oh 
    [Pre-Chorus: H.E.R.] You're my water when I'm stuck in the desert, You're the Tylenol I take when my head hurts, You're the sunshine on my life, Oh, I just wanna see how beautiful you are, You know that I see it, I know you're a star, Where you go I'll follow, No matter how far, If life is a movie, then you're the best part, oh oh oh, You're the best part, oh oh oh, Best part"""
)

def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = extended_gcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        return None  # modular inverse doesn't exist
    else:
        return x % m

def generate_prime(bits=8):
    while True:
        p = random.getrandbits(bits)
        if isprime(p):
            return p

def generate_keypair(bits=8):
    p = generate_prime(bits)
    q = generate_prime(bits)
    
    while p == q:
        q = generate_prime(bits)
    
    n = p * q
    phi = (p-1) * (q-1)
    
    # Choose e such that 1 < e < phi and gcd(e, phi) = 1
    e = random.randrange(1, phi)
    while math.gcd(e, phi) != 1:
        e = random.randrange(1, phi)
    
    # Compute d, the modular inverse of e
    d = modinv(e, phi)
    
    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    e, n = pk
    cipher = [pow(ord(char), e, n) for char in plaintext]
    return cipher

def decrypt(pk, ciphertext):
    d, n = pk
    plain = [chr(pow(char, d, n)) for char in ciphertext]
    return ''.join(plain)

# Streamlit UI
st.title("🔐 RSA Encryption/Decryption Tool")
st.write("""
This app demonstrates the RSA algorithm for public-key cryptography.
You can generate keys, encrypt messages, and decrypt ciphertext.
""")

st.sidebar.header("Key Generation")
key_size = st.sidebar.selectbox("Key Size (bits)", [8, 16, 32, 64], index=0)

if st.sidebar.button("Generate New Key Pair"):
    public_key, private_key = generate_keypair(key_size)
    st.session_state.public_key = public_key
    st.session_state.private_key = private_key

if 'public_key' in st.session_state:
    st.sidebar.write("Public Key (e, n):", st.session_state.public_key)
    st.sidebar.write("Private Key (d, n):", st.session_state.private_key)

tab1, tab2 = st.tabs(["Encrypt", "Decrypt"])

with tab1:
    st.header("Encrypt Message")
    plaintext = st.text_area("Enter message to encrypt:")
    
    if st.button("Encrypt") and 'public_key' in st.session_state:
        ciphertext = encrypt(st.session_state.public_key, plaintext)
        st.session_state.ciphertext = ciphertext
        st.write("Ciphertext (as numbers):")
        st.code(ciphertext)
        
        # Save to session state for decryption
        st.session_state.last_encrypted = ciphertext

with tab2:
    st.header("Decrypt Message")
    
    if 'last_encrypted' in st.session_state:
        cipher_input = st.text_area("Enter ciphertext (comma-separated numbers):", 
                                   value=",".join(map(str, st.session_state.last_encrypted)))
    else:
        cipher_input = st.text_area("Enter ciphertext (comma-separated numbers):")
    
    if st.button("Decrypt") and 'private_key' in st.session_state:
        try:
            cipher_numbers = [int(x.strip()) for x in cipher_input.split(",")]
            plaintext = decrypt(st.session_state.private_key, cipher_numbers)
            st.write("Decrypted Message:")
            st.success(plaintext)
        except Exception as e:
            st.error(f"Error in decryption: {e}")

st.write("---")
st.write("""
### How RSA Works:
1. **Key Generation**:
   - Choose two distinct primes p and q
   - Compute n = p × q and φ(n) = (p-1)(q-1)
   - Choose e where 1 < e < φ(n) and gcd(e, φ(n)) = 1
   - Compute d ≡ e⁻¹ mod φ(n)

2. **Encryption**: c ≡ mᵉ mod n  
3. **Decryption**: m ≡ cᵈ mod n
""")