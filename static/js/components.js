const { Link, useNavigate, useLocation } = ReactRouterDOM;

// Ensure these are available globally or locally
const MainLayout = ({ children }) => {
    const navigate = useNavigate();
    const location = useLocation();

    // Simple conditional rendering for nav based on path to simulate different layouts
    const isAuthOrAdmin = location.pathname.includes('/admin') || location.pathname.includes('/dashboard');

    return (
        <div className="flex flex-col min-h-screen bg-background-light text-secondary">
            {!isAuthOrAdmin && (
                <nav className="sticky top-0 z-50 w-full bg-white/80 backdrop-blur-md border-b border-border-light">
                    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                        <div className="flex justify-between items-center h-16">
                            <Link to="/" className="flex items-center gap-2">
                                <div className="p-1.5 bg-primary rounded-lg text-secondary">
                                    <span className="material-symbols-outlined text-[20px] font-bold">eco</span>
                                </div>
                                <span className="text-xl font-bold tracking-tight text-secondary">KangkungKu</span>
                            </Link>
                            <div className="hidden md:flex items-center gap-8">
                                <Link to="/" className="text-sm font-medium hover:text-primary transition-colors">Home</Link>
                                <Link to="/diagnosis" className="text-sm font-medium hover:text-primary transition-colors">Diagnosis</Link>
                                <Link to="/encyclopedia" className="text-sm font-medium hover:text-primary transition-colors">Encyclopedia</Link>
                                <Link to="/calculator" className="text-sm font-medium hover:text-primary transition-colors">Calculator</Link>
                                <Link to="/community" className="text-sm font-medium hover:text-primary transition-colors">Community</Link>
                                <Link to="/blog" className="text-sm font-medium hover:text-primary transition-colors">Blog</Link>
                            </div>
                            <div className="flex items-center gap-4">
                                    <Link to="/dashboard" className="hidden md:flex items-center justify-center h-10 px-5 rounded-lg bg-secondary text-white text-sm font-bold hover:bg-opacity-90 transition-all">
                                    User Dashboard
                                </Link>
                                <Link to="/admin" className="text-sm font-medium text-gray-500 hover:text-primary">Admin</Link>
                            </div>
                        </div>
                    </div>
                </nav>
            )}
            <main className="flex-grow">
                {children}
            </main>
        </div>
    );
};

// Make it global
window.MainLayout = MainLayout;
