const API_BASE = '/api';

// Format angka ke persen
const formatPersen = (val) => `${Math.round(val)}%`;

// Fungsi helper untuk mengambil data
async function ambilData(endpoint) {
    try {
        const res = await fetch(`${API_BASE}${endpoint}`);
        if (!res.ok) throw new Error('Gagal mengambil data');
        return await res.json();
    } catch (err) {
        console.error(err);
        return null;
    }
}

// Fungsi untuk navigasi mobile
function setupMobileMenu() {
    // Implementasi sederhana jika diperlukan
}

document.addEventListener('DOMContentLoaded', setupMobileMenu);
