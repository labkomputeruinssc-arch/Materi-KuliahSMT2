Visualisasi Blok Memori & Proses CRUD

Dokumen ini menyediakan representasi visual bagaimana Python mengelola memori untuk List, Tuple, Set, dan Dictionary.

1. Python LIST (Dynamic Array)

Karakteristik: Kontigu (berurutan), Terindeks, dan memiliki Over-allocation.

A. Create (Append) & Over-allocation

Saat kita membuat list, Python memesan ruang ekstra (loker kosong) untuk mempercepat penambahan data di masa depan.

<svg viewBox="0 0 500 120" xmlns="[http://www.w3.org/2000/svg](http://www.w3.org/2000/svg)">
  <!-- Blocks -->
  <rect x="10" y="40" width="60" height="40" fill="#e0f2fe" stroke="#0369a1" stroke-width="2" rx="4"/>
  <rect x="70" y="40" width="60" height="40" fill="#e0f2fe" stroke="#0369a1" stroke-width="2" rx="4"/>
  <rect x="130" y="40" width="60" height="40" fill="#e0f2fe" stroke="#0369a1" stroke-width="2" rx="4"/>
  <rect x="190" y="40" width="60" height="40" fill="white" stroke="#94a3b8" stroke-dasharray="4" stroke-width="2" rx="4"/>
  <rect x="250" y="40" width="60" height="40" fill="white" stroke="#94a3b8" stroke-dasharray="4" stroke-width="2" rx="4"/>
  
  <!-- Labels -->
  <text x="40" y="65" font-family="sans-serif" font-size="12" text-anchor="middle" fill="#0369a1">Data 0</text>
  <text x="100" y="65" font-family="sans-serif" font-size="12" text-anchor="middle" fill="#0369a1">Data 1</text>
  <text x="160" y="65" font-family="sans-serif" font-size="12" text-anchor="middle" fill="#0369a1">Data 2</text>
  <text x="220" y="65" font-family="sans-serif" font-size="10" text-anchor="middle" fill="#94a3b8">Kosong</text>
  
  <text x="10" y="30" font-family="sans-serif" font-size="10" fill="#64748b">Index: 0</text>
  <text x="70" y="30" font-family="sans-serif" font-size="10" fill="#64748b">1</text>
  <text x="130" y="30" font-family="sans-serif" font-size="10" fill="#64748b">2</text>
  
  <path d="M 320 60 L 350 60" stroke="#64748b" stroke-width="2" marker-end="url(#arrow)"/>
  <text x="360" y="65" font-family="sans-serif" font-size="12" fill="#0369a1">O(1) Append</text>
</svg>


B. Delete (Shifting) - $O(n)$

Jika kita menghapus elemen di tengah, elemen di belakangnya harus bergeser ke kiri.

<svg viewBox="0 0 500 150" xmlns="[http://www.w3.org/2000/svg](http://www.w3.org/2000/svg)">
  <rect x="10" y="40" width="60" height="40" fill="#e0f2fe" stroke="#0369a1" stroke-width="2" rx="4"/>
  <rect x="70" y="40" width="60" height="40" fill="#fee2e2" stroke="#dc2626" stroke-width="2" rx="4"/>
  <rect x="130" y="40" width="60" height="40" fill="#e0f2fe" stroke="#0369a1" stroke-width="2" rx="4"/>
  <rect x="190" y="40" width="60" height="40" fill="#e0f2fe" stroke="#0369a1" stroke-width="2" rx="4"/>
  
  <text x="40" y="65" font-family="sans-serif" font-size="12" text-anchor="middle">A</text>
  <text x="100" y="65" font-family="sans-serif" font-size="12" text-anchor="middle" fill="#dc2626">X</text>
  <text x="160" y="65" font-family="sans-serif" font-size="12" text-anchor="middle">C</text>
  <text x="220" y="65" font-family="sans-serif" font-size="12" text-anchor="middle">D</text>
  
  <!-- Shifting Arrows -->
  <path d="M 160 90 Q 130 110 100 90" stroke="#0369a1" fill="none" stroke-width="2" marker-end="url(#arrow)"/>
  <path d="M 220 90 Q 190 110 160 90" stroke="#0369a1" fill="none" stroke-width="2" marker-end="url(#arrow)"/>
  <text x="160" y="130" font-family="sans-serif" font-size="10" text-anchor="middle" fill="#0369a1">Shifting (Pergeseran) ke kiri</text>
  <defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#0369a1"/></marker></defs>
</svg>


2. Python TUPLE (Fixed Array)

Karakteristik: Kontigu, Ukuran Tetap, Tanpa Cadangan Memori (Lean).

<svg viewBox="0 0 500 100" xmlns="[http://www.w3.org/2000/svg](http://www.w3.org/2000/svg)">
  <rect x="10" y="40" width="60" height="40" fill="#f1f5f9" stroke="#475569" stroke-width="2" rx="4"/>
  <rect x="70" y="40" width="60" height="40" fill="#f1f5f9" stroke="#475569" stroke-width="2" rx="4"/>
  <rect x="130" y="40" width="60" height="40" fill="#f1f5f9" stroke="#475569" stroke-width="2" rx="4"/>
  
  <text x="40" y="65" font-family="sans-serif" font-size="12" text-anchor="middle">192.1</text>
  <text x="100" y="65" font-family="sans-serif" font-size="12" text-anchor="middle">8080</text>
  <text x="160" y="65" font-family="sans-serif" font-size="12" text-anchor="middle">Admin</text>
  
  <text x="210" y="65" font-family="sans-serif" font-size="12" fill="#64748b">Immutable (Gembok)</text>
</svg>


Tuple tidak mendukung Create/Delete/Update setelah inisialisasi.

3. SET (Hash Table - Unordered)

Karakteristik: Unik, Berbasis Hash, Tidak Berurutan.

<svg viewBox="0 0 500 180" xmlns="[http://www.w3.org/2000/svg](http://www.w3.org/2000/svg)">
  <!-- Hash Function -->
  <rect x="10" y="60" width="80" height="40" fill="#fef3c7" stroke="#d97706" rx="8"/>
  <text x="50" y="85" font-family="sans-serif" font-size="10" text-anchor="middle">Hash Function</text>
  
  <!-- Buckets -->
  <rect x="150" y="20" width="100" height="30" fill="white" stroke="#94a3b8" rx="4"/>
  <rect x="150" y="60" width="100" height="30" fill="#dcfce7" stroke="#16a34a" rx="4"/>
  <rect x="150" y="100" width="100" height="30" fill="white" stroke="#94a3b8" rx="4"/>
  <rect x="150" y="140" width="100" height="30" fill="#dcfce7" stroke="#16a34a" rx="4"/>
  
  <text x="30" y="45" font-family="sans-serif" font-size="10" fill="#d97706">Input: "IP_A"</text>
  <path d="M 90 80 L 140 75" stroke="#d97706" stroke-width="2" marker-end="url(#arrow_hash)"/>
  <text x="200" y="80" font-family="sans-serif" font-size="10" text-anchor="middle">Stored here</text>
  
  <text x="300" y="80" font-family="sans-serif" font-size="12" fill="#16a34a">O(1) CRUD</text>
  <text x="300" y="100" font-family="sans-serif" font-size="10" fill="#64748b">(Tanpa Shifting)</text>
  <defs><marker id="arrow_hash" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#d97706"/></marker></defs>
</svg>


4. DICTIONARY (Key-Value Mapping)

Karakteristik: Pasangan Kunci-Nilai, Akses Instan via Key.

<svg viewBox="0 0 550 200" xmlns="[http://www.w3.org/2000/svg](http://www.w3.org/2000/svg)">
  <!-- Key Column -->
  <text x="50" y="20" font-family="sans-serif" font-size="12" font-weight="bold">Key</text>
  <rect x="20" y="40" width="80" height="30" fill="#ddd6fe" stroke="#7c3aed" rx="4"/>
  <text x="60" y="60" font-family="sans-serif" font-size="10" text-anchor="middle">"user_1"</text>
  
  <!-- Hash Arrow -->
  <path d="M 105 55 L 180 80" stroke="#7c3aed" stroke-width="2" marker-end="url(#arrow_purple)"/>
  
  <!-- Hash Table Memory -->
  <text x="250" y="20" font-family="sans-serif" font-size="12" font-weight="bold">Memory (RAM)</text>
  <rect x="200" y="40" width="150" height="120" fill="#f8fafc" stroke="#94a3b8" rx="4"/>
  
  <!-- Stored Pair -->
  <rect x="210" y="70" width="130" height="40" fill="#ede9fe" stroke="#7c3aed" rx="4"/>
  <text x="275" y="85" font-family="sans-serif" font-size="9" text-anchor="middle">Key: "user_1"</text>
  <text x="275" y="100" font-family="sans-serif" font-size="9" text-anchor="middle" font-weight="bold">Value: "Budi"</text>
  
  <text x="380" y="90" font-family="sans-serif" font-size="12" fill="#7c3aed">O(1) Search</text>
  <text x="380" y="110" font-family="sans-serif" font-size="10" fill="#64748b">Direct Access via Key</text>
  
  <defs><marker id="arrow_purple" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#7c3aed"/></marker></defs>
</svg>


Kesimpulan untuk Mahasiswa:

List: Lambat di tengah karena harus memindahkan "kursi" (shifting).

Tuple: Hemat ruang karena tidak menyediakan "kursi cadangan".

Set/Dict: Cepat karena menggunakan "GPS" (Hash) untuk langsung menuju lokasi tanpa harus menelusuri dari depan.