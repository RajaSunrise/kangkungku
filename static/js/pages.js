const { useState, useEffect } = React;
const { Link, useNavigate } = ReactRouterDOM;

const HomeScreen = () => {
    const navigate = useNavigate();
    return (
        <section className="relative overflow-hidden pt-12 pb-16 lg:pt-20 lg:pb-24">
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
                <div className="grid lg:grid-cols-2 gap-12 items-center">
                    <div className="flex flex-col gap-6 max-w-2xl">
                        <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-primary/10 border border-primary/20 w-fit">
                            <span className="relative flex h-2 w-2">
                                <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-primary opacity-75"></span>
                                <span className="relative inline-flex rounded-full h-2 w-2 bg-green-500"></span>
                            </span>
                            <span className="text-xs font-semibold text-green-800 tracking-wide uppercase">AI-Powered Diagnosis</span>
                        </div>
                        <h1 className="text-5xl lg:text-6xl font-bold leading-[1.1] tracking-tight text-secondary">
                            Protect Your Harvest with <span className="text-green-600">Confidence</span>
                        </h1>
                        <p className="text-lg text-gray-600 leading-relaxed max-w-lg">
                            An intelligent expert system using the Certainty Factor method to accurately diagnose and treat water spinach diseases in seconds. Keep your crops healthy and productive.
                        </p>
                        <div className="flex flex-col sm:flex-row gap-4 mt-2">
                            <button onClick={() => navigate('/diagnosis')} className="flex items-center justify-center h-12 px-8 rounded-lg bg-primary text-secondary text-base font-bold hover:bg-[#25d642] transition-colors shadow-lg shadow-green-200">
                                Start Diagnosis
                                <span className="material-symbols-outlined ml-2 text-[20px]">stethoscope</span>
                            </button>
                            <button onClick={() => navigate('/encyclopedia')} className="flex items-center justify-center h-12 px-8 rounded-lg bg-white border border-border-light text-secondary text-base font-bold hover:bg-gray-50 transition-colors">
                                Browse Encyclopedia
                            </button>
                        </div>
                        <div className="flex items-center gap-4 mt-6 pt-6 border-t border-gray-100">
                            <div className="flex -space-x-3">
                                <img alt="Expert 1" className="w-10 h-10 rounded-full border-2 border-white object-cover" src="https://lh3.googleusercontent.com/aida-public/AB6AXuC_T8UAtf7a2S9hze-9G8JKHLX-XnTcP63l8UNasCEZzjbZnFCJlvw2W5pfK8bk-uc95DJmMsVeibgpeeLEcIbnK2WMJIHTpBqZdSFY5pQtLsxzfQKq51A2HtWEWPQlnSeogfUSRyldaNxBLcS4LSk6IGzeG1zKM9Vtn0kcnV3CXDQE9ojG5DCPQqea2cC5cupzwjXoZ-LMljkvEZkpjxMaWGt4iGgdQ7eQryNxB-wehqqZv1ZiXQhiNkrZGIK4nirkWpqo5SVd12I"/>
                                <img alt="Expert 2" className="w-10 h-10 rounded-full border-2 border-white object-cover" src="https://lh3.googleusercontent.com/aida-public/AB6AXuBW977hWNxyrVMBhuPKyR0J5hUi7YN5GdvyLieZjErJCtppHGJdSWAgNspXUVbMrJxE23vl8zbkyF7sc9jPqkbt4EkVK9hO2rNv1zNzh7zPHVCuLLrxqSqlNPb1vm3h11YrlZkhKqsKC4hTm-VA41AQgtWw-1fzL959s0N_Y0Y2yXSchuXzFj05IKY5vhbpGv3THA2G_6_mo_AdhhSZupAp4VzYWuR15RUCN__abENA-8oTraFPr77-B9vFWxsQkp3le32r0xdXcT8"/>
                                <img alt="Expert 3" className="w-10 h-10 rounded-full border-2 border-white object-cover" src="https://lh3.googleusercontent.com/aida-public/AB6AXuAhH17UbER_H7aZtYrQkts9TSvSdXSzKk6OoazMJcFsEEIaLQSRiOYK8gNgMiakei1qfBDJlsnn07G-xpruUWElkp6OGljzAuapsETKzSEx51v4wo10hGxf1JdP5sEqb8awmVt4XqjfpPz6tOL54r1XnL4iPFRsFz_9QeU9SBRVmFHGhdo13hNAcVOe8rMfwmpzIf8LyydXoxPbrNcWD7L2ts2xB5w9TB9Elw04PIv3vg_ZhMoLaxUXVdNhAjn4QBJorft4xqBJtkI"/>
                            </div>
                            <p className="text-sm font-medium text-gray-500">Validated by Agricultural Experts</p>
                        </div>
                    </div>
                    <div className="relative lg:h-auto">
                        <div className="absolute -z-10 top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[120%] h-[120%] bg-gradient-to-tr from-green-100/50 via-primary/10 to-transparent rounded-full blur-3xl"></div>
                        <div className="relative rounded-2xl overflow-hidden shadow-2xl border border-white/50 aspect-[4/3] group">
                            <div className="absolute inset-0 bg-gradient-to-t from-black/20 to-transparent z-10"></div>
                            <img alt="Fresh water spinach" className="w-full h-full object-cover transform group-hover:scale-105 transition-transform duration-700" src="https://lh3.googleusercontent.com/aida-public/AB6AXuBoxurf_A0WkXlownxTFbXYXgfRlMi4xxVqIgtU5fg37YNZN7INsZZWERGw71oNMa62PcJVvgkviunBaqotZkSt0OF4mc1bmD3kPY-EFe5ExXFPF9kJoLVZpUIiqWeef0PdbwyqgxPQjBm-rgrcB81O8Uoojk1rhqYqCiCTFFBi4A7ELH6khluOg99HoI-J1xMNXMaKtEWoSy1zDuZ_ageC1xSNhLv54Lr2F-_7OgP39uppOWliFyroEgYy2qmUh99JKORsfuzKjJQ"/>
                            <div className="absolute bottom-6 left-6 right-6 z-20 bg-white/95 backdrop-blur-sm p-4 rounded-xl shadow-lg border border-green-100 flex items-start gap-4">
                                <div className="bg-green-50 p-3 rounded-lg text-green-700">
                                    <span className="material-symbols-outlined">health_and_safety</span>
                                </div>
                                <div>
                                    <h3 className="font-bold text-secondary">Instant Analysis</h3>
                                    <p className="text-sm text-gray-500">Upload a photo or answer symptoms to get immediate results.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    );
};

const Encyclopedia = () => {
    const [diseases, setDiseases] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        fetch('/api/diseases')
            .then(res => res.json())
            .then(data => {
                setDiseases(data);
                setLoading(false);
            })
            .catch(err => {
                console.error(err);
                setLoading(false);
            });
    }, []);

    return (
        <div className="max-w-[1280px] mx-auto px-4 md:px-8 py-8 flex flex-col gap-8">
            <div className="text-center max-w-2xl mx-auto mb-8">
                <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-primary/10 text-emerald-700 text-xs font-bold uppercase tracking-wider mb-4">
                    <span className="material-symbols-outlined text-sm">local_florist</span>
                    Knowledge Base
                </div>
                <h1 className="text-4xl md:text-5xl font-black tracking-tight text-text-main leading-[1.1]">Disease Encyclopedia</h1>
            </div>

            {loading ? (
                <div className="flex justify-center p-10"><span className="material-symbols-outlined animate-spin text-4xl text-primary">autorenew</span></div>
            ) : (
                <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
                    {diseases.map((d, i) => (
                        <article key={i} className="group bg-white rounded-xl overflow-hidden border border-slate-100 shadow-sm hover:shadow-xl hover:border-primary/50 transition-all duration-300 flex flex-col h-full">
                            <div className="relative h-48 overflow-hidden">
                                <div className="absolute inset-0 bg-gradient-to-t from-black/60 to-transparent z-10 opacity-60"></div>
                                <img alt={d.name} className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" src={d.image_url || 'https://via.placeholder.com/400'} />
                                <div className="absolute top-3 right-3 z-20">
                                    <span className="inline-flex items-center px-2.5 py-1 rounded-md text-xs font-bold bg-amber-100 text-amber-800">
                                        Disease
                                    </span>
                                </div>
                            </div>
                            <div className="p-5 flex flex-col flex-grow">
                                <div className="mb-3">
                                    <h3 className="text-xl font-bold text-text-main group-hover:text-primary transition-colors">{d.name}</h3>
                                    <p className="text-sm text-text-muted italic font-medium">{d.scientific_name}</p>
                                </div>
                                <div className="mt-auto pt-4 border-t border-slate-100 flex items-center justify-between">
                                    <span className="inline-flex items-center gap-1 text-xs font-semibold text-text-muted uppercase tracking-wider">
                                        Info
                                    </span>
                                    <button className="inline-flex items-center text-sm font-bold text-primary hover:text-primary-dark transition-colors gap-1">
                                        Learn More <span className="material-symbols-outlined text-[16px]">arrow_forward</span>
                                    </button>
                                </div>
                            </div>
                        </article>
                    ))}
                </div>
            )}
        </div>
    );
};

const Calculator = () => {
    const [area, setArea] = useState(50);
    return (
        <div className="px-4 lg:px-40 py-8 w-full max-w-[1440px] mx-auto">
            <div className="mb-8">
                <h1 className="text-[#111812] text-4xl lg:text-5xl font-black leading-tight tracking-[-0.033em] mb-2">Nutrient Optimizer</h1>
                <p className="text-text-muted text-lg font-normal leading-normal max-w-2xl">
                    Get precise fertilizer recommendations based on your cultivation method and growth stage.
                </p>
            </div>
            <div className="flex flex-col lg:flex-row gap-8 items-start">
                <div className="flex-1 w-full flex flex-col gap-6">
                    <div className="bg-white rounded-xl p-6 shadow-sm border border-gray-100">
                        <h3 className="text-lg font-bold uppercase tracking-wide text-[#111812] mb-4">Parameters</h3>
                        <div className="mb-8 group">
                            <div className="flex justify-between items-end mb-4">
                                <label className="text-[#111812] font-medium text-base flex flex-col">
                                    <span className="text-sm text-text-muted font-normal mb-1">Cultivation Area Size</span>
                                    Land Surface Area
                                </label>
                                <div className="bg-green-50 px-3 py-1 rounded-lg text-[#111812] font-bold font-mono text-xl border border-primary/20">
                                    <span>{area}</span> <span className="text-sm font-normal text-text-muted">m²</span>
                                </div>
                            </div>
                            <input className="w-full z-20 focus:outline-none focus:ring-2 focus:ring-primary/50 rounded-full" type="range" min="10" max="500" value={area} onChange={(e) => setArea(e.target.value)} />
                        </div>
                    </div>
                </div>
                <div className="w-full lg:w-[480px] flex flex-col gap-6">
                    <div className="bg-white rounded-xl overflow-hidden shadow-lg border border-primary/30 relative">
                        <div className="h-2 w-full bg-gradient-to-r from-primary to-[#21b83a]"></div>
                        <div className="p-6 md:p-8">
                            <h2 className="text-2xl font-black text-[#111812] uppercase tracking-tight mb-6">Recommendation</h2>
                            <div className="bg-[#fcfdfc] rounded-xl border border-dashed border-gray-300 p-6 mb-6">
                                <div className="flex flex-col gap-4">
                                    <div className="flex justify-between items-center pb-4 border-b border-gray-100">
                                        <div className="flex items-center gap-3">
                                            <div className="w-10 h-10 rounded-full bg-blue-100 flex items-center justify-center text-blue-600 font-bold">N</div>
                                            <div>
                                                <p className="text-sm font-bold text-[#111812]">Urea (Nitrogen)</p>
                                            </div>
                                        </div>
                                        <div className="text-right">
                                            <p className="text-2xl font-black text-[#111812]">{area * 5}<span className="text-sm font-normal text-text-muted ml-1">g</span></p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};

const Dashboard = () => {
    return (
        <div className="flex h-screen bg-background-light">
            <aside className="w-64 bg-white border-r border-slate-200 hidden md:flex flex-col">
                <div className="p-6 flex items-center gap-3">
                    <div className="h-10 w-10 rounded-xl bg-primary flex items-center justify-center text-slate-900 shadow-lg shadow-primary/20">
                        <span className="material-symbols-outlined text-2xl font-bold">eco</span>
                    </div>
                    <h1 className="text-lg font-bold tracking-tight">KangkungKu</h1>
                </div>
                <nav className="flex-1 px-4 space-y-2 mt-4">
                    <a href="#" className="flex items-center gap-3 px-4 py-3 rounded-lg bg-primary text-slate-900 font-semibold shadow-md shadow-primary/20">
                        <span className="material-symbols-outlined">dashboard</span> Dashboard
                    </a>
                    <a href="#" className="flex items-center gap-3 px-4 py-3 rounded-lg text-slate-600 hover:bg-slate-100">
                        <span className="material-symbols-outlined">history</span> History
                    </a>
                </nav>
            </aside>
            <main className="flex-1 p-8 overflow-y-auto">
                <h1 className="text-3xl font-bold text-slate-900 mb-8">User Dashboard</h1>
                <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
                    <div className="bg-white p-6 rounded-xl border border-slate-200 shadow-sm">
                        <p className="text-sm font-medium text-slate-500">Total Diagnoses</p>
                        <h3 className="text-3xl font-bold text-slate-900">24</h3>
                    </div>
                    <div className="bg-white p-6 rounded-xl border border-slate-200 shadow-sm">
                        <p className="text-sm font-medium text-slate-500">Avg. Certainty</p>
                        <h3 className="text-3xl font-bold text-slate-900">82%</h3>
                    </div>
                </div>
                <div className="bg-white rounded-xl border border-slate-200 overflow-hidden">
                    <div className="px-6 py-4 border-b border-slate-100 bg-slate-50">
                        <h3 className="font-bold text-slate-700">Recent Activity</h3>
                    </div>
                    <table className="w-full text-left text-sm">
                        <thead className="bg-slate-50 text-slate-500">
                            <tr>
                                <th className="px-6 py-3">Date</th>
                                <th className="px-6 py-3">Result</th>
                                <th className="px-6 py-3">Confidence</th>
                            </tr>
                        </thead>
                        <tbody className="divide-y divide-slate-100">
                            <tr>
                                <td className="px-6 py-4">Oct 24, 2023</td>
                                <td className="px-6 py-4 font-bold text-red-600">White Rust</td>
                                <td className="px-6 py-4">85%</td>
                            </tr>
                            <tr>
                                <td className="px-6 py-4">Oct 22, 2023</td>
                                <td className="px-6 py-4 font-bold text-orange-600">Leaf Spot</td>
                                <td className="px-6 py-4">62%</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </main>
        </div>
    );
};

const AdminDashboard = () => {
    return (
        <div className="flex h-screen bg-gray-50">
                <aside className="w-64 bg-white border-r border-gray-200 hidden lg:flex flex-col">
                <div className="p-6">
                    <h1 className="font-bold text-lg">Admin Panel</h1>
                </div>
                <nav className="flex-1 px-4 space-y-1">
                    <a href="#" className="flex items-center gap-3 px-3 py-2 rounded-lg bg-gray-100 text-gray-900 font-medium">Dashboard</a>
                    <a href="#" className="flex items-center gap-3 px-3 py-2 rounded-lg text-gray-600 hover:bg-gray-50">Users</a>
                    <a href="#" className="flex items-center gap-3 px-3 py-2 rounded-lg text-gray-600 hover:bg-gray-50">Reports</a>
                </nav>
                </aside>
                <main className="flex-1 p-8 overflow-y-auto">
                <div className="flex justify-between items-center mb-8">
                        <h1 className="text-2xl font-bold text-gray-900">System Overview</h1>
                        <button className="bg-primary text-white px-4 py-2 rounded-lg font-bold">New Report</button>
                </div>
                <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">
                    <div className="bg-white p-6 rounded-xl border border-gray-200">
                        <p className="text-gray-500 text-sm">Total Users</p>
                        <h3 className="text-2xl font-bold">1,248</h3>
                    </div>
                    <div className="bg-white p-6 rounded-xl border border-gray-200">
                        <p className="text-gray-500 text-sm">Active Today</p>
                        <h3 className="text-2xl font-bold">342</h3>
                    </div>
                </div>
                <div className="bg-white rounded-xl border border-gray-200 p-6">
                    <h3 className="font-bold mb-4">Recent System Logs</h3>
                    <div className="space-y-4">
                        <div className="flex justify-between border-b pb-2">
                            <span>User #2942 completed diagnosis</span>
                            <span className="text-gray-500 text-sm">2 mins ago</span>
                        </div>
                        <div className="flex justify-between border-b pb-2">
                            <span>New user registration</span>
                            <span className="text-gray-500 text-sm">15 mins ago</span>
                        </div>
                    </div>
                </div>
                </main>
        </div>
    )
}

const Community = () => {
        return (
            <div className="max-w-6xl mx-auto px-4 py-8">
                <div className="flex justify-between items-end mb-8">
                    <div>
                        <h1 className="text-3xl font-bold mb-2">Community Forum</h1>
                        <p className="text-gray-500">Join the conversation with fellow farmers.</p>
                    </div>
                    <button className="bg-primary px-6 py-2 rounded-lg font-bold">Ask Question</button>
                </div>
                <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
                    <div className="lg:col-span-2 space-y-4">
                        <div className="bg-white p-5 rounded-xl border border-gray-200 shadow-sm hover:shadow-md cursor-pointer">
                            <div className="flex items-center gap-2 mb-2">
                                <span className="bg-red-50 text-red-700 text-xs px-2 py-1 rounded font-bold">Disease</span>
                                <span className="text-xs text-gray-400">• Posted 2 hours ago</span>
                            </div>
                            <h3 className="text-xl font-bold mb-2">Yellowing leaves after heavy rain?</h3>
                            <p className="text-gray-600 text-sm mb-4">My kangkung was doing great until the storm last night. Now the lower leaves are turning yellow...</p>
                            <div className="flex gap-4 text-sm text-gray-500">
                                <span>24 Likes</span>
                                <span>12 Replies</span>
                            </div>
                        </div>
                        <div className="bg-white p-5 rounded-xl border border-gray-200 shadow-sm hover:shadow-md cursor-pointer">
                            <div className="flex items-center gap-2 mb-2">
                                <span className="bg-blue-50 text-blue-700 text-xs px-2 py-1 rounded font-bold">Hydroponics</span>
                                <span className="text-xs text-gray-400">• Posted 5 hours ago</span>
                            </div>
                            <h3 className="text-xl font-bold mb-2">Best fertilizer mix for hydroponic kangkung</h3>
                            <p className="text-gray-600 text-sm mb-4">I've been experimenting with AB Mix ratios. Currently using 5ml/L but growth seems slow...</p>
                            <div className="flex gap-4 text-sm text-gray-500">
                                <span>34 Likes</span>
                                <span>8 Replies</span>
                            </div>
                        </div>
                    </div>
                    <div className="space-y-6">
                        <div className="bg-gradient-to-br from-[#102213] to-[#1a3821] p-6 rounded-xl text-white">
                            <h3 className="font-bold text-lg mb-2">Spot a problem?</h3>
                            <p className="text-sm text-gray-300 mb-4">Use our expert diagnosis tool.</p>
                            <button className="w-full bg-primary text-black font-bold py-2 rounded-lg text-sm">Start Diagnosis</button>
                        </div>
                        <div className="bg-white p-5 rounded-xl border border-gray-200">
                            <h4 className="font-bold mb-4">Trending Topics</h4>
                            <div className="flex flex-col gap-2 text-sm text-gray-600">
                                <a href="#" className="flex justify-between"><span>#LeafRot</span> <span>124 posts</span></a>
                                <a href="#" className="flex justify-between"><span>#Hydroponics</span> <span>65 posts</span></a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        )
}

const Blog = () => {
        return (
            <div className="max-w-7xl mx-auto px-4 py-12">
                <div className="flex flex-col lg:flex-row gap-8 mb-12">
                    <div className="w-full lg:w-3/5 aspect-video rounded-xl bg-gray-200 relative overflow-hidden group">
                        <img src="https://lh3.googleusercontent.com/aida-public/AB6AXuA_cd5wLfQrpkUL630iLHiz7W9b8yAW3K5eiZewInvx1gQHlnqxFg7XUfFmQpKA2-4BQwnY4-ebbgXMblwD3sEmCUadjFnmp03s1SudLFtCHiaF5Oe0XXQQWVmdc78rzNw_cb_K-5m3Tqj7c4aBeb1t4tYPmeI95mBPMGyf7v9FHY0BMDVNif7u7xKuFzxdeaPKF46yS7fKeHk-gS6iPKa-uv1kbqzCi7v_IGuxSija9Cdk3YsWrXL5yaWTmZVZgCQoGG5b5MvUnPc" className="w-full h-full object-cover"/>
                        <div className="absolute bottom-0 left-0 p-8 bg-gradient-to-t from-black/80 to-transparent w-full">
                            <span className="bg-primary text-black text-xs font-bold px-2 py-1 rounded mb-2 inline-block">Featured</span>
                            <h1 className="text-3xl text-white font-bold mb-2">Understanding White Rust: The Silent Killer</h1>
                            <p className="text-gray-200 text-sm">New research reveals how early detection using AI can save 80% of your crop.</p>
                        </div>
                    </div>
                    <div className="w-full lg:w-2/5 flex flex-col justify-center gap-6">
                    <div className="p-6 bg-white border border-gray-200 rounded-xl">
                        <h2 className="text-xl font-bold mb-2">Trending Now</h2>
                        <h3 className="text-lg font-bold mb-2">How We Calculate Disease Probability</h3>
                        <p className="text-gray-600 text-sm mb-4">A deep dive into the math behind our expert system.</p>
                        <a href="#" className="text-primary font-bold text-sm flex items-center gap-1">Read Full Analysis <span className="material-symbols-outlined text-sm">arrow_forward</span></a>
                    </div>
                    </div>
                </div>
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                    {[1, 2, 3].map((i) => (
                        <div key={i} className="group cursor-pointer">
                            <div className="aspect-video bg-gray-100 rounded-lg mb-4 overflow-hidden">
                                <img src={`https://lh3.googleusercontent.com/aida-public/AB6AXuAd9qUTRB-1fzSXFk9Nx1UB1PyNhb_BL2iNuCduMGi5h_nH1k2R8lXppj6h_-1ptF2sqKatoRn6Ey0X5A-NcRE3FsBvz8w76WpByMqhIY_1bkWvLumoN0ulo-pM7-SMHrsFQhwhwFwMtTzzRuWMEphcLgbAOdj9afpn3-VRvws7p3arduYY800qPNRBKM29VH-788p8c0-TfhZbDJp_omeDuZQAn0l7kTQa51z662KmqwBM3TCJQ9vzOlKYmZMeaZUz7PhUf0dKW8M`} className="w-full h-full object-cover group-hover:scale-105 transition-transform"/>
                            </div>
                            <div className="text-xs font-bold text-gray-500 uppercase mb-2">Farming Tips • Oct 08</div>
                            <h3 className="text-xl font-bold mb-2 group-hover:text-primary transition-colors">Optimal pH Levels for Hydroponic Kangkung</h3>
                            <p className="text-gray-600 text-sm line-clamp-2">Water spinach thrives in specific conditions. We break down the ideal nutrient solution acidity.</p>
                        </div>
                    ))}
                </div>
            </div>
        )
}

// Make global
window.HomeScreen = HomeScreen;
window.Encyclopedia = Encyclopedia;
window.Calculator = Calculator;
window.Dashboard = Dashboard;
window.AdminDashboard = AdminDashboard;
window.Community = Community;
window.Blog = Blog;
