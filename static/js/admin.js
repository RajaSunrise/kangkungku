document.addEventListener("DOMContentLoaded", () => {
    checkAdmin();
    loadDashboard();

    document.getElementById("nav-dashboard").addEventListener("click", (e) => {
        e.preventDefault();
        loadDashboard();
        updateActiveNav("nav-dashboard");
    });
    document.getElementById("nav-diseases").addEventListener("click", (e) => {
        e.preventDefault();
        loadDiseases();
        updateActiveNav("nav-diseases");
    });
    document.getElementById("nav-symptoms").addEventListener("click", (e) => {
        e.preventDefault();
        loadSymptoms();
        updateActiveNav("nav-symptoms");
    });
    document.getElementById("btn-logout").addEventListener("click", (e) => {
        e.preventDefault();
        logout();
    });
});

function updateActiveNav(activeId) {
    const navIds = ["nav-dashboard", "nav-diseases", "nav-symptoms"];
    navIds.forEach(id => {
        const el = document.getElementById(id);
        if (id === activeId) {
            el.classList.add("bg-gray-100", "font-medium", "text-gray-900");
            el.classList.remove("text-gray-600");
        } else {
            el.classList.remove("bg-gray-100", "font-medium", "text-gray-900");
            el.classList.add("text-gray-600");
        }
    });
}

function loadDashboard() {
    const content = document.getElementById("main-content");
    content.innerHTML = `
        <h1 class="text-2xl font-bold text-gray-900 mb-8">Tinjauan Sistem</h1>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
            <div class="bg-white p-6 rounded-xl border border-gray-200">
                <p class="text-gray-500 text-sm">Selamat Datang</p>
                <h3 class="text-2xl font-bold">Admin Panel</h3>
                <p class="mt-2 text-gray-600">Gunakan menu di samping untuk mengelola data penyakit dan gejala.</p>
            </div>
        </div>
    `;
}

// --- Diseases ---

async function loadDiseases() {
    const content = document.getElementById("main-content");
    content.innerHTML = `
        <div class="flex justify-between items-center mb-6">
            <h1 class="text-2xl font-bold text-gray-900">Kelola Penyakit</h1>
            <button onclick="showAddDiseaseModal()" class="bg-primary text-secondary px-4 py-2 rounded-lg font-bold shadow hover:bg-opacity-90">Tambah Penyakit</button>
        </div>
        <div class="bg-white rounded-xl border border-gray-200 overflow-hidden overflow-x-auto">
            <table class="w-full text-left text-sm">
                <thead class="bg-gray-50 text-gray-500">
                    <tr>
                        <th class="px-6 py-3">ID</th>
                        <th class="px-6 py-3">Nama</th>
                        <th class="px-6 py-3">Nama Ilmiah</th>
                        <th class="px-6 py-3">Aksi</th>
                    </tr>
                </thead>
                <tbody id="diseases-table-body" class="divide-y divide-gray-100">
                    <tr><td colspan="4" class="px-6 py-4 text-center">Memuat...</td></tr>
                </tbody>
            </table>
        </div>
    `;

    try {
        const response = await fetch("/api/penyakit");
        const diseases = await response.json();
        const tbody = document.getElementById("diseases-table-body");
        tbody.innerHTML = "";

        diseases.forEach(d => {
            const tr = document.createElement("tr");
            tr.innerHTML = `
                <td class="px-6 py-4">${d.id}</td>
                <td class="px-6 py-4 font-bold">${d.nama}</td>
                <td class="px-6 py-4 italic text-gray-500">${d.nama_ilmiah || '-'}</td>
                <td class="px-6 py-4">
                    <button onclick="deleteDisease(${d.id})" class="text-red-600 hover:text-red-800 font-bold">Hapus</button>
                </td>
            `;
            tbody.appendChild(tr);
        });
    } catch (error) {
        alert("Gagal memuat penyakit");
    }
}

async function createDisease(event) {
    event.preventDefault();
    const form = event.target;
    const data = {
        nama: form.nama.value,
        nama_ilmiah: form.nama_ilmiah.value,
        deskripsi: form.deskripsi.value,
        solusi: form.solusi.value,
        url_gambar: form.url_gambar.value
    };

    try {
        const response = await fetch("/admin/penyakit", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${getToken()}`
            },
            body: JSON.stringify(data)
        });

        if (!response.ok) throw new Error("Gagal menambah penyakit");

        closeModal();
        loadDiseases();
    } catch (error) {
        alert(error.message);
    }
}

async function deleteDisease(id) {
    if (!confirm("Yakin ingin menghapus penyakit ini?")) return;

    try {
        const response = await fetch(`/admin/penyakit/${id}`, {
            method: "DELETE",
            headers: {
                "Authorization": `Bearer ${getToken()}`
            }
        });

        if (!response.ok) throw new Error("Gagal menghapus penyakit");
        loadDiseases();
    } catch (error) {
        alert(error.message);
    }
}

function showAddDiseaseModal() {
    const modal = document.createElement('div');
    modal.id = 'modal';
    modal.className = 'fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50';
    modal.innerHTML = `
        <div class="bg-white p-8 rounded-xl max-w-lg w-full max-h-screen overflow-y-auto">
            <h2 class="text-xl font-bold mb-4">Tambah Penyakit Baru</h2>
            <form onsubmit="createDisease(event)" class="space-y-4">
                <div>
                    <label class="block text-sm font-medium">Nama Penyakit</label>
                    <input type="text" name="nama" required class="w-full border rounded p-2">
                </div>
                <div>
                    <label class="block text-sm font-medium">Nama Ilmiah</label>
                    <input type="text" name="nama_ilmiah" class="w-full border rounded p-2">
                </div>
                <div>
                    <label class="block text-sm font-medium">Deskripsi</label>
                    <textarea name="deskripsi" class="w-full border rounded p-2"></textarea>
                </div>
                <div>
                    <label class="block text-sm font-medium">Solusi</label>
                    <textarea name="solusi" class="w-full border rounded p-2"></textarea>
                </div>
                <div>
                    <label class="block text-sm font-medium">URL Gambar</label>
                    <input type="text" name="url_gambar" class="w-full border rounded p-2">
                </div>
                <div class="flex justify-end gap-2 mt-6">
                    <button type="button" onclick="closeModal()" class="px-4 py-2 bg-gray-200 rounded hover:bg-gray-300">Batal</button>
                    <button type="submit" class="px-4 py-2 bg-primary text-secondary font-bold rounded hover:opacity-90">Simpan</button>
                </div>
            </form>
        </div>
    `;
    document.body.appendChild(modal);
}

// --- Symptoms ---

async function loadSymptoms() {
    const content = document.getElementById("main-content");
    content.innerHTML = `
        <div class="flex justify-between items-center mb-6">
            <h1 class="text-2xl font-bold text-gray-900">Kelola Gejala</h1>
            <button onclick="showAddSymptomModal()" class="bg-primary text-secondary px-4 py-2 rounded-lg font-bold shadow hover:bg-opacity-90">Tambah Gejala</button>
        </div>
        <div class="bg-white rounded-xl border border-gray-200 overflow-hidden overflow-x-auto">
            <table class="w-full text-left text-sm">
                <thead class="bg-gray-50 text-gray-500">
                    <tr>
                        <th class="px-6 py-3">ID</th>
                        <th class="px-6 py-3">Kode</th>
                        <th class="px-6 py-3">Deskripsi</th>
                        <th class="px-6 py-3">Aksi</th>
                    </tr>
                </thead>
                <tbody id="symptoms-table-body" class="divide-y divide-gray-100">
                    <tr><td colspan="4" class="px-6 py-4 text-center">Memuat...</td></tr>
                </tbody>
            </table>
        </div>
    `;

    try {
        const response = await fetch("/api/gejala");
        const symptoms = await response.json();
        const tbody = document.getElementById("symptoms-table-body");
        tbody.innerHTML = "";

        symptoms.forEach(g => {
            const tr = document.createElement("tr");
            tr.innerHTML = `
                <td class="px-6 py-4">${g.id}</td>
                <td class="px-6 py-4 font-mono font-bold">${g.kode}</td>
                <td class="px-6 py-4">${g.deskripsi}</td>
                <td class="px-6 py-4">
                    <button onclick="deleteSymptom(${g.id})" class="text-red-600 hover:text-red-800 font-bold">Hapus</button>
                </td>
            `;
            tbody.appendChild(tr);
        });
    } catch (error) {
        alert("Gagal memuat gejala");
    }
}

async function createSymptom(event) {
    event.preventDefault();
    const form = event.target;
    const data = {
        kode: form.kode.value,
        deskripsi: form.deskripsi.value,
        url_gambar: form.url_gambar.value
    };

    try {
        const response = await fetch("/admin/gejala", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${getToken()}`
            },
            body: JSON.stringify(data)
        });

        if (!response.ok) throw new Error("Gagal menambah gejala");

        closeModal();
        loadSymptoms();
    } catch (error) {
        alert(error.message);
    }
}

async function deleteSymptom(id) {
    if (!confirm("Yakin ingin menghapus gejala ini?")) return;

    try {
        const response = await fetch(`/admin/gejala/${id}`, {
            method: "DELETE",
            headers: {
                "Authorization": `Bearer ${getToken()}`
            }
        });

        if (!response.ok) throw new Error("Gagal menghapus gejala");
        loadSymptoms();
    } catch (error) {
        alert(error.message);
    }
}

function showAddSymptomModal() {
    const modal = document.createElement('div');
    modal.id = 'modal';
    modal.className = 'fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50';
    modal.innerHTML = `
        <div class="bg-white p-8 rounded-xl max-w-lg w-full">
            <h2 class="text-xl font-bold mb-4">Tambah Gejala Baru</h2>
            <form onsubmit="createSymptom(event)" class="space-y-4">
                <div>
                    <label class="block text-sm font-medium">Kode (contoh: G01)</label>
                    <input type="text" name="kode" required class="w-full border rounded p-2">
                </div>
                <div>
                    <label class="block text-sm font-medium">Deskripsi</label>
                    <textarea name="deskripsi" required class="w-full border rounded p-2"></textarea>
                </div>
                <div>
                    <label class="block text-sm font-medium">URL Gambar</label>
                    <input type="text" name="url_gambar" class="w-full border rounded p-2">
                </div>
                <div class="flex justify-end gap-2 mt-6">
                    <button type="button" onclick="closeModal()" class="px-4 py-2 bg-gray-200 rounded hover:bg-gray-300">Batal</button>
                    <button type="submit" class="px-4 py-2 bg-primary text-secondary font-bold rounded hover:opacity-90">Simpan</button>
                </div>
            </form>
        </div>
    `;
    document.body.appendChild(modal);
}

function closeModal() {
    const modal = document.getElementById('modal');
    if (modal) modal.remove();
}
