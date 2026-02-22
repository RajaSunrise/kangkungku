const { createRoot } = ReactDOM;
const { MemoryRouter, Routes, Route } = ReactRouterDOM;

// Wait for components to be loaded
const App = () => {
    // Access global components
    const MainLayout = window.MainLayout;
    const HomeScreen = window.HomeScreen;
    const Encyclopedia = window.Encyclopedia;
    const Calculator = window.Calculator;
    const Dashboard = window.Dashboard;
    const AdminDashboard = window.AdminDashboard;
    const Community = window.Community;
    const Blog = window.Blog;
    const DiagnosisStep1 = window.DiagnosisStep1;
    const DiagnosisResult = window.DiagnosisResult;

    return (
        <MemoryRouter>
            <MainLayout>
                <Routes>
                    <Route path="/" element={<HomeScreen />} />
                    <Route path="/diagnosis" element={<DiagnosisStep1 />} />
                    <Route path="/diagnosis/result" element={<DiagnosisResult />} />
                    <Route path="/encyclopedia" element={<Encyclopedia />} />
                    <Route path="/calculator" element={<Calculator />} />
                    <Route path="/dashboard" element={<Dashboard />} />
                    <Route path="/admin" element={<AdminDashboard />} />
                    <Route path="/community" element={<Community />} />
                    <Route path="/blog" element={<Blog />} />
                </Routes>
            </MainLayout>
        </MemoryRouter>
    );
};

const root = createRoot(document.getElementById('root'));
root.render(<App />);
