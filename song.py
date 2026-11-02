import time

def compile_code():
    print("Mulai mengompilasi kode...")
    for i in range(5, 0, -1):
        print(f"Menghitung mundur: {i}...")
        time.sleep(1)
    
    print("\n[SUKSES] Kompilasi berhasil! Program berjalan dengan sempurna.")

if __name__ == "__main__":
    compile_code()