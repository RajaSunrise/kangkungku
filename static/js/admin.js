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
    document.getElementById("nav-users").addEventListener("click", (e) => {
        e.preventDefault();
        loadUsers();
        updateActiveNav("nav-users");
    });
    document.getElementById("btn-logout").addEventListener("click", (e) => {
        e.preventDefault();
        logout();
    });
});

function updateActiveNav(activeId) {
    const navIds = ["nav-dashboard", "nav-diseases", "nav-symptoms", "nav-users"];
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

async function loadDashboard() {
    const content = document.getElementById("main-content");
    content.innerHTML = `
        <h1 class="text-2xl font-bold text-gray-900 mb-8">Tinjauan Sistem</h1>
        <div id="stats-container" class="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">
            <div class="animate-pulse bg-white p-6 rounded-xl border border-gray-100 h-32"></div>
            <div class="animate-pulse bg-white p-6 rounded-xl border border-gray-100 h-32"></div>
            <div class="animate-pulse bg-white p-6 rounded-xl border border-gray-100 h-32"></div>
            <div class="animate-pulse bg-white p-6 rounded-xl border border-gray-100 h-32"></div>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
            <div class="bg-white p-8 rounded-3xl border border-slate-200 shadow-sm">
                <h3 class="text-lg font-black text-slate-900 mb-6 flex items-center gap-2">
                    <span class="material-symbols-outlined text-primary">history</span>
                    Aktivitas Diagnosa Terbaru
                </h3>
                <div id="recent-history" class="space-y-4">
                    <!-- History akan dimuat -->
                </div>
            </div>

            <div class="bg-slate-900 p-8 rounded-3xl text-white relative overflow-hidden">
                 <div class="absolute -right-4 -bottom-4 text-white/10">
                    <span class="material-symbols-outlined text-9xl">analytics</span>
                </div>
                <h3 class="text-xl font-bold mb-4 relative z-10">Status Server</h3>
                <div class="space-y-4 relative z-10">
                    <div class="flex justify-between items-center p-3 rounded-xl bg-white/5 border border-white/10">
                        <span class="text-slate-400 text-sm">Database</span>
                        <span class="flex items-center gap-2 text-primary text-xs font-bold uppercase tracking-widest">
                            <span class="size-2 rounded-full bg-primary animate-pulse"></span>
                            Connected
                        </span>
                    </div>
                    <div class="flex justify-between items-center p-3 rounded-xl bg-white/5 border border-white/10">
                        <span class="text-slate-400 text-sm">Engine</span>
                        <span class="text-white text-xs font-bold uppercase tracking-widest">Certainty Factor</span>
                    </div>
                </div>
            </div>
        </div>
    `;

    try {
        const res = await fetch('/admin/stats', {
            headers: { 'Authorization': `Bearer ${getToken()}` }
        });
        const stats = await res.json();

        // Render Stats
        document.getElementById('stats-container').innerHTML = `
            <div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm transition-all hover:shadow-lg group">
                <div class="flex items-center justify-between mb-4">
                    <div class="p-3 rounded-xl bg-blue-50 text-blue-600 group-hover:bg-blue-600 group-hover:text-white transition-colors">
                        <span class="material-symbols-outlined">group</span>
                    </div>
                </div>
                <p class="text-slate-500 text-xs font-black uppercase tracking-widest">Total Users</p>
                <h3 class="text-3xl font-black text-slate-900 mt-1">${stats.total_users}</h3>
            </div>
            <div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm transition-all hover:shadow-lg group">
                <div class="flex items-center justify-between mb-4">
                    <div class="p-3 rounded-xl bg-primary/10 text-primary group-hover:bg-primary group-hover:text-slate-900 transition-colors">
                        <span class="material-symbols-outlined">analytics</span>
                    </div>
                </div>
                <p class="text-slate-500 text-xs font-black uppercase tracking-widest">Diagnosa</p>
                <h3 class="text-3xl font-black text-slate-900 mt-1">${stats.total_diagnosa}</h3>
            </div>
            <div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm transition-all hover:shadow-lg group">
                <div class="flex items-center justify-between mb-4">
                    <div class="p-3 rounded-xl bg-red-50 text-red-600 group-hover:bg-red-600 group-hover:text-white transition-colors">
                        <span class="material-symbols-outlined">coronavirus</span>
                    </div>
                </div>
                <p class="text-slate-500 text-xs font-black uppercase tracking-widest">Penyakit</p>
                <h3 class="text-3xl font-black text-slate-900 mt-1">${stats.total_penyakit}</h3>
            </div>
            <div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm transition-all hover:shadow-lg group">
                <div class="flex items-center justify-between mb-4">
                    <div class="p-3 rounded-xl bg-amber-50 text-amber-600 group-hover:bg-amber-600 group-hover:text-white transition-colors">
                        <span class="material-symbols-outlined">healing</span>
                    </div>
                </div>
                <p class="text-slate-500 text-xs font-black uppercase tracking-widest">Gejala</p>
                <h3 class="text-3xl font-black text-slate-900 mt-1">${stats.total_gejala}</h3>
            </div>
        `;

        // Render History
        const historyContainer = document.getElementById('recent-history');
        if (stats.history_terbaru.length === 0) {
            historyContainer.innerHTML = '<p class="text-slate-500 text-center py-8">Belum ada data diagnosa.</p>';
        } else {
            historyContainer.innerHTML = stats.history_terbaru.map(h => `
                <div class="flex items-center justify-between p-4 rounded-2xl bg-slate-50 border border-slate-100 group hover:bg-white hover:shadow-md transition-all">
                    <div class="flex items-center gap-4">
                        <div class="size-10 rounded-xl bg-white border border-slate-100 flex items-center justify-center text-primary shadow-sm">
                            <span class="material-symbols-outlined text-xl">medical_services</span>
                        </div>
                        <div>
                            <p class="text-sm font-bold text-slate-900">${h.penyakit.nama}</p>
                            <p class="text-[10px] text-slate-400 font-bold uppercase tracking-widest">${h.created_at} • ${h.user_id ? 'Registered User' : 'Guest'}</p>
                        </div>
                    </div>
                    <span class="text-xs font-black text-primary bg-primary/10 px-2 py-1 rounded-lg">${h.persentase}%</span>
                </div>
            `).join('');
        }

    } catch (err) {
        console.error(err);
    }
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
                    <button onclick="editDisease(${d.id})" class="text-blue-600 hover:text-blue-800 font-bold mr-2">Edit</button>
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

async function editDisease(id) {
    try {
        const response = await fetch(`/api/penyakit/${id}`);
        if (!response.ok) throw new Error("Gagal mengambil data penyakit");
        const data = await response.json();
        showEditDiseaseModal(data);
    } catch (error) {
        alert(error.message);
    }
}

async function updateDisease(event, id) {
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
        const response = await fetch(`/admin/penyakit/${id}`, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${getToken()}`
            },
            body: JSON.stringify(data)
        });

        if (!response.ok) throw new Error("Gagal memperbarui penyakit");

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

function showEditDiseaseModal(data) {
    const modal = document.createElement('div');
    modal.id = 'modal';
    modal.className = 'fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50';
    modal.innerHTML = `
        <div class="bg-white p-8 rounded-xl max-w-lg w-full max-h-screen overflow-y-auto">
            <h2 class="text-xl font-bold mb-4">Edit Penyakit</h2>
            <form onsubmit="updateDisease(event, ${data.id})" class="space-y-4">
                <div>
                    <label class="block text-sm font-medium">Nama Penyakit</label>
                    <input type="text" name="nama" value="${data.nama}" required class="w-full border rounded p-2">
                </div>
                <div>
                    <label class="block text-sm font-medium">Nama Ilmiah</label>
                    <input type="text" name="nama_ilmiah" value="${data.nama_ilmiah || ''}" class="w-full border rounded p-2">
                </div>
                <div>
                    <label class="block text-sm font-medium">Deskripsi</label>
                    <textarea name="deskripsi" class="w-full border rounded p-2">${data.deskripsi || ''}</textarea>
                </div>
                <div>
                    <label class="block text-sm font-medium">Solusi</label>
                    <textarea name="solusi" class="w-full border rounded p-2">${data.solusi || ''}</textarea>
                </div>
                <div>
                    <label class="block text-sm font-medium">URL Gambar</label>
                    <input type="text" name="url_gambar" value="${data.url_gambar || ''}" class="w-full border rounded p-2">
                </div>
                <div class="flex justify-end gap-2 mt-6">
                    <button type="button" onclick="closeModal()" class="px-4 py-2 bg-gray-200 rounded hover:bg-gray-300">Batal</button>
                    <button type="submit" class="px-4 py-2 bg-primary text-secondary font-bold rounded hover:opacity-90">Update</button>
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
                    <button onclick="editSymptom(${g.id})" class="text-blue-600 hover:text-blue-800 font-bold mr-2">Edit</button>
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

async function editSymptom(id) {
    try {
        const response = await fetch("/api/gejala");
        if (!response.ok) throw new Error("Gagal mengambil data gejala");
        const data = await response.json();
        const symptom = data.find(s => s.id === id);
        if (!symptom) throw new Error("Gejala tidak ditemukan");
        showEditSymptomModal(symptom);
    } catch (error) {
        alert(error.message);
    }
}

async function updateSymptom(event, id) {
    event.preventDefault();
    const form = event.target;
    const data = {
        kode: form.kode.value,
        deskripsi: form.deskripsi.value,
        url_gambar: form.url_gambar.value
    };

    try {
        const response = await fetch(`/admin/gejala/${id}`, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${getToken()}`
            },
            body: JSON.stringify(data)
        });

        if (!response.ok) throw new Error("Gagal memperbarui gejala");

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

function showEditSymptomModal(data) {
    const modal = document.createElement('div');
    modal.id = 'modal';
    modal.className = 'fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50';
    modal.innerHTML = `
        <div class="bg-white p-8 rounded-xl max-w-lg w-full">
            <h2 class="text-xl font-bold mb-4">Edit Gejala</h2>
            <form onsubmit="updateSymptom(event, ${data.id})" class="space-y-4">
                <div>
                    <label class="block text-sm font-medium">Kode</label>
                    <input type="text" name="kode" value="${data.kode}" required class="w-full border rounded p-2">
                </div>
                <div>
                    <label class="block text-sm font-medium">Deskripsi</label>
                    <textarea name="deskripsi" required class="w-full border rounded p-2">${data.deskripsi}</textarea>
                </div>
                <div>
                    <label class="block text-sm font-medium">URL Gambar</label>
                    <input type="text" name="url_gambar" value="${data.url_gambar || ''}" class="w-full border rounded p-2">
                </div>
                <div class="flex justify-end gap-2 mt-6">
                    <button type="button" onclick="closeModal()" class="px-4 py-2 bg-gray-200 rounded hover:bg-gray-300">Batal</button>
                    <button type="submit" class="px-4 py-2 bg-primary text-secondary font-bold rounded hover:opacity-90">Update</button>
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

// --- Users ---

async function loadUsers() {
    const content = document.getElementById("main-content");
    content.innerHTML = `
        <div class="flex justify-between items-center mb-6">
            <h1 class="text-2xl font-bold text-gray-900">Kelola Pengguna</h1>
            <button onclick="showAddUserModal()" class="bg-primary text-secondary px-4 py-2 rounded-lg font-bold shadow hover:bg-opacity-90 flex items-center gap-2">
                <span class="material-symbols-outlined text-lg">person_add</span> Tambah User
            </button>
        </div>
        <div class="bg-white rounded-xl border border-gray-200 overflow-hidden overflow-x-auto">
            <table class="w-full text-left text-sm">
                <thead class="bg-gray-50 text-gray-500">
                    <tr>
                        <th class="px-6 py-3">ID</th>
                        <th class="px-6 py-3">Username</th>
                        <th class="px-6 py-3">Email</th>
                        <th class="px-6 py-3">Role</th>
                        <th class="px-6 py-3">Status</th>
                        <th class="px-6 py-3">Aksi</th>
                    </tr>
                </thead>
                <tbody id="users-table-body" class="divide-y divide-gray-100">
                    <tr><td colspan="6" class="px-6 py-4 text-center">Memuat...</td></tr>
                </tbody>
            </table>
        </div>
    `;

    try {
        const response = await fetch("/admin/users", {
            headers: { "Authorization": `Bearer ${getToken()}` }
        });
        if (!response.ok) throw new Error("Gagal memuat data pengguna");
        const users = await response.json();
        const tbody = document.getElementById("users-table-body");
        tbody.innerHTML = "";

        if (users.length === 0) {
            tbody.innerHTML = '<tr><td colspan="6" class="px-6 py-8 text-center text-gray-400">Belum ada pengguna.</td></tr>';
            return;
        }

        users.forEach(u => {
            const roleBadge = u.role === 'admin'
                ? '<span class="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-xs font-bold bg-purple-100 text-purple-700"><span class="material-symbols-outlined text-sm">shield</span>Admin</span>'
                : '<span class="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-xs font-bold bg-blue-100 text-blue-700"><span class="material-symbols-outlined text-sm">person</span>User</span>';
            const statusBadge = u.is_active
                ? '<span class="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-xs font-bold bg-green-100 text-green-700"><span class="size-1.5 rounded-full bg-green-500"></span>Aktif</span>'
                : '<span class="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-xs font-bold bg-red-100 text-red-700"><span class="size-1.5 rounded-full bg-red-500"></span>Nonaktif</span>';

            const tr = document.createElement("tr");
            tr.className = "hover:bg-gray-50 transition-colors";
            tr.innerHTML = `
                <td class="px-6 py-4 text-gray-400 font-mono text-xs">${u.id}</td>
                <td class="px-6 py-4 font-bold">${u.username}</td>
                <td class="px-6 py-4 text-gray-500">${u.email || '-'}</td>
                <td class="px-6 py-4">${roleBadge}</td>
                <td class="px-6 py-4">${statusBadge}</td>
                <td class="px-6 py-4">
                    <button onclick="editUser(${u.id})" class="text-blue-600 hover:text-blue-800 font-bold mr-2">Edit</button>
                    <button onclick="deleteUser(${u.id})" class="text-red-600 hover:text-red-800 font-bold">Hapus</button>
                </td>
            `;
            tbody.appendChild(tr);
        });
    } catch (error) {
        alert(error.message);
    }
}

function showAddUserModal() {
    const modal = document.createElement('div');
    modal.id = 'modal';
    modal.className = 'fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50';
    modal.innerHTML = `
        <div class="bg-white p-8 rounded-xl max-w-lg w-full max-h-screen overflow-y-auto">
            <h2 class="text-xl font-bold mb-4 flex items-center gap-2">
                <span class="material-symbols-outlined text-primary">person_add</span>
                Tambah Pengguna Baru
            </h2>
            <form onsubmit="createUser(event)" class="space-y-4">
                <div>
                    <label class="block text-sm font-medium mb-1">Username</label>
                    <input type="text" name="username" required class="w-full border rounded-lg p-2.5 focus:ring-2 focus:ring-primary focus:border-primary outline-none" placeholder="Masukkan username">
                </div>
                <div>
                    <label class="block text-sm font-medium mb-1">Email</label>
                    <input type="email" name="email" required class="w-full border rounded-lg p-2.5 focus:ring-2 focus:ring-primary focus:border-primary outline-none" placeholder="contoh@email.com">
                </div>
                <div>
                    <label class="block text-sm font-medium mb-1">Password</label>
                    <input type="password" name="password" required minlength="6" class="w-full border rounded-lg p-2.5 focus:ring-2 focus:ring-primary focus:border-primary outline-none" placeholder="Min. 6 karakter">
                </div>
                <div>
                    <label class="block text-sm font-medium mb-1">Role</label>
                    <select name="role" class="w-full border rounded-lg p-2.5 focus:ring-2 focus:ring-primary focus:border-primary outline-none bg-white">
                        <option value="user">User</option>
                        <option value="admin">Admin</option>
                    </select>
                </div>
                <div class="flex justify-end gap-2 mt-6">
                    <button type="button" onclick="closeModal()" class="px-4 py-2 bg-gray-200 rounded-lg hover:bg-gray-300 font-medium">Batal</button>
                    <button type="submit" class="px-4 py-2 bg-primary text-secondary font-bold rounded-lg hover:opacity-90">Simpan</button>
                </div>
            </form>
        </div>
    `;
    document.body.appendChild(modal);
}

async function createUser(event) {
    event.preventDefault();
    const form = event.target;
    const data = {
        username: form.username.value,
        email: form.email.value,
        password: form.password.value
    };

    try {
        const response = await fetch("/admin/users", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${getToken()}`
            },
            body: JSON.stringify(data)
        });

        if (!response.ok) {
            const err = await response.json();
            throw new Error(err.detail || "Gagal menambah user");
        }

        // If role is set, update it separately since UserCreate doesn't have role
        const newUser = await response.json();
        const selectedRole = form.role.value;
        if (selectedRole !== "user") {
            await fetch(`/admin/users/${newUser.id}`, {
                method: "PUT",
                headers: {
                    "Content-Type": "application/json",
                    "Authorization": `Bearer ${getToken()}`
                },
                body: JSON.stringify({ role: selectedRole })
            });
        }

        closeModal();
        loadUsers();
    } catch (error) {
        alert(error.message);
    }
}

async function editUser(id) {
    try {
        const response = await fetch(`/admin/users/${id}`, {
            headers: { "Authorization": `Bearer ${getToken()}` }
        });
        if (!response.ok) throw new Error("Gagal mengambil data user");
        const data = await response.json();
        showEditUserModal(data);
    } catch (error) {
        alert(error.message);
    }
}

function showEditUserModal(data) {
    const modal = document.createElement('div');
    modal.id = 'modal';
    modal.className = 'fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50';
    modal.innerHTML = `
        <div class="bg-white p-8 rounded-xl max-w-lg w-full max-h-screen overflow-y-auto">
            <h2 class="text-xl font-bold mb-4 flex items-center gap-2">
                <span class="material-symbols-outlined text-blue-600">edit</span>
                Edit Pengguna
            </h2>
            <form onsubmit="updateUser(event, ${data.id})" class="space-y-4">
                <div>
                    <label class="block text-sm font-medium mb-1">Username</label>
                    <input type="text" name="username" value="${data.username}" required class="w-full border rounded-lg p-2.5 focus:ring-2 focus:ring-primary focus:border-primary outline-none">
                </div>
                <div>
                    <label class="block text-sm font-medium mb-1">Email</label>
                    <input type="email" name="email" value="${data.email || ''}" class="w-full border rounded-lg p-2.5 focus:ring-2 focus:ring-primary focus:border-primary outline-none">
                </div>
                <div>
                    <label class="block text-sm font-medium mb-1">Password Baru <span class="text-gray-400 font-normal">(kosongkan jika tidak diubah)</span></label>
                    <input type="password" name="password" minlength="6" class="w-full border rounded-lg p-2.5 focus:ring-2 focus:ring-primary focus:border-primary outline-none" placeholder="Kosongkan jika tidak diubah">
                </div>
                <div>
                    <label class="block text-sm font-medium mb-1">Role</label>
                    <select name="role" class="w-full border rounded-lg p-2.5 focus:ring-2 focus:ring-primary focus:border-primary outline-none bg-white">
                        <option value="user" ${data.role === 'user' ? 'selected' : ''}>User</option>
                        <option value="admin" ${data.role === 'admin' ? 'selected' : ''}>Admin</option>
                    </select>
                </div>
                <div>
                    <label class="block text-sm font-medium mb-1">Status</label>
                    <select name="is_active" class="w-full border rounded-lg p-2.5 focus:ring-2 focus:ring-primary focus:border-primary outline-none bg-white">
                        <option value="true" ${data.is_active ? 'selected' : ''}>Aktif</option>
                        <option value="false" ${!data.is_active ? 'selected' : ''}>Nonaktif</option>
                    </select>
                </div>
                <div class="flex justify-end gap-2 mt-6">
                    <button type="button" onclick="closeModal()" class="px-4 py-2 bg-gray-200 rounded-lg hover:bg-gray-300 font-medium">Batal</button>
                    <button type="submit" class="px-4 py-2 bg-primary text-secondary font-bold rounded-lg hover:opacity-90">Update</button>
                </div>
            </form>
        </div>
    `;
    document.body.appendChild(modal);
}

async function updateUser(event, id) {
    event.preventDefault();
    const form = event.target;
    const data = {
        username: form.username.value,
        email: form.email.value,
        role: form.role.value,
        is_active: form.is_active.value === 'true'
    };

    // Only include password if it was filled in
    if (form.password.value) {
        data.password = form.password.value;
    }

    try {
        const response = await fetch(`/admin/users/${id}`, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${getToken()}`
            },
            body: JSON.stringify(data)
        });

        if (!response.ok) {
            const err = await response.json();
            throw new Error(err.detail || "Gagal memperbarui user");
        }

        closeModal();
        loadUsers();
    } catch (error) {
        alert(error.message);
    }
}

async function deleteUser(id) {
    if (!confirm("Yakin ingin menghapus pengguna ini? Semua data diagnosa terkait juga akan dihapus.")) return;

    try {
        const response = await fetch(`/admin/users/${id}`, {
            method: "DELETE",
            headers: {
                "Authorization": `Bearer ${getToken()}`
            }
        });

        if (!response.ok) {
            const err = await response.json();
            throw new Error(err.detail || "Gagal menghapus user");
        }
        loadUsers();
    } catch (error) {
        alert(error.message);
    }
}
