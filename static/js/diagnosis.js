const { useState, useEffect } = React;
const { Link, useNavigate, useLocation } = ReactRouterDOM;

const DiagnosisStep1 = () => {
    const navigate = useNavigate();
    const [symptoms, setSymptoms] = useState([]);
    const [selectedSymptoms, setSelectedSymptoms] = useState({}); // {id: confidence}
    const [loading, setLoading] = useState(true);
    const [submitting, setSubmitting] = useState(false);

    useEffect(() => {
        fetch('/api/symptoms')
            .then(res => res.json())
            .then(data => {
                setSymptoms(data);
                setLoading(false);
            })
            .catch(err => console.error(err));
    }, []);

    const toggleSymptom = (symptom) => {
        const newSelected = { ...selectedSymptoms };
        if (newSelected[symptom.id]) {
            delete newSelected[symptom.id];
        } else {
            newSelected[symptom.id] = 0.8; // Default high confidence
        }
        setSelectedSymptoms(newSelected);
    };

    const updateConfidence = (id, val) => {
        const newSelected = { ...selectedSymptoms };
        newSelected[id] = parseFloat(val);
        setSelectedSymptoms(newSelected);
    };

    const handleSubmit = () => {
        if (Object.keys(selectedSymptoms).length === 0) {
            alert("Please select at least one symptom.");
            return;
        }

        setSubmitting(true);
        const payload = {
            symptoms: Object.entries(selectedSymptoms).map(([id, conf]) => ({
                symptom_id: parseInt(id),
                confidence: conf
            }))
        };

        fetch('/api/diagnose', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        })
        .then(res => res.json())
        .then(results => {
            setSubmitting(false);
            navigate('/diagnosis/result', { state: { results } });
        })
        .catch(err => {
            console.error(err);
            setSubmitting(false);
            alert("Error submitting diagnosis.");
        });
    };

    if (loading) return <div className="flex justify-center p-20"><span className="material-symbols-outlined animate-spin text-4xl text-primary">autorenew</span></div>;

    return (
        <div className="container mx-auto px-4 py-8 lg:px-8 max-w-7xl">
            <div className="flex flex-col lg:flex-row gap-8">
                <div className="flex-1 min-w-0">
                    <div className="mb-8">
                        <h1 className="text-3xl lg:text-4xl font-bold tracking-tight mb-3">Diagnose Water Spinach Health</h1>
                        <p className="text-slate-600 text-lg max-w-2xl">
                            Select observed symptoms to identify potential diseases using our Expert System.
                            Adjust confidence levels for more accurate results.
                        </p>
                    </div>

                    <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-8">
                        {symptoms.map(symptom => {
                            const isSelected = !!selectedSymptoms[symptom.id];
                            return (
                                <div key={symptom.id}
                                     className={`group relative flex flex-col gap-4 rounded-xl border-2 bg-surface-light p-5 shadow-sm transition-all cursor-pointer ${isSelected ? 'border-primary' : 'border-transparent hover:border-primary/50'}`}
                                     onClick={() => toggleSymptom(symptom)}>

                                    {isSelected && (
                                        <div className="absolute top-4 right-4">
                                            <div className="size-6 rounded-full bg-primary flex items-center justify-center text-black">
                                                <span className="material-symbols-outlined text-sm font-bold">check</span>
                                            </div>
                                        </div>
                                    )}

                                    <div className="flex items-start gap-4">
                                        <div className={`p-3 rounded-lg ${isSelected ? 'bg-yellow-100 text-yellow-600' : 'bg-slate-100 text-slate-600'}`}>
                                            <span className="material-symbols-outlined text-3xl">coronavirus</span>
                                        </div>
                                        <div>
                                            <h3 className="text-lg font-bold mb-1">{symptom.code}</h3>
                                            <p className="text-sm text-slate-500 leading-relaxed">
                                                {symptom.description}
                                            </p>
                                        </div>
                                    </div>

                                    {isSelected && (
                                        <div className="mt-2 pt-4 border-t border-border-light" onClick={(e) => e.stopPropagation()}>
                                            <div className="flex justify-between items-center mb-2">
                                                <label className="text-xs font-bold uppercase tracking-wider text-slate-500">Confidence Level</label>
                                                <span className="text-sm font-bold text-primary">{(selectedSymptoms[symptom.id]).toFixed(1)}</span>
                                            </div>
                                            <input
                                                className="w-full h-2 bg-slate-200 rounded-lg appearance-none cursor-pointer accent-primary"
                                                type="range" min="0.1" max="1" step="0.1"
                                                value={selectedSymptoms[symptom.id]}
                                                onChange={(e) => updateConfidence(symptom.id, e.target.value)}
                                            />
                                        </div>
                                    )}
                                </div>
                            );
                        })}
                    </div>

                    <div className="flex flex-col sm:flex-row justify-between items-center gap-4 py-6 border-t border-border-light">
                        <button onClick={() => navigate('/')} className="w-full sm:w-auto px-6 py-3 rounded-lg border border-border-light text-slate-600 font-bold hover:bg-slate-100 transition-colors flex items-center justify-center gap-2">
                            <span className="material-symbols-outlined">arrow_back</span>
                            Back
                        </button>
                        <button onClick={handleSubmit} disabled={submitting} className="w-full sm:w-auto px-8 py-3 rounded-lg bg-primary hover:bg-primary-dark text-slate-900 font-bold shadow-md hover:shadow-lg transition-all flex items-center justify-center gap-2 disabled:opacity-50">
                            {submitting ? 'Analyzing...' : 'Get Results'}
                            <span className="material-symbols-outlined">arrow_forward</span>
                        </button>
                    </div>
                </div>
            </div>
        </div>
    );
};

const DiagnosisResult = () => {
    const navigate = useNavigate();
    const location = useLocation();
    const results = location.state?.results;

    if (!results) {
        return (
            <div className="p-10 text-center">
                <h2 className="text-2xl font-bold mb-4">No results found.</h2>
                <button onClick={() => navigate('/diagnosis')} className="px-4 py-2 bg-primary rounded">Start Diagnosis</button>
            </div>
        );
    }

    const topResult = results.length > 0 ? results[0] : null;

    return (
        <div className="w-full max-w-[1440px] mx-auto p-4 md:px-10 py-8">
            <div className="flex flex-col md:flex-row justify-between items-start md:items-center mb-8 gap-4">
                <div>
                    <p className="text-sm text-slate-500 mb-1">Diagnosis Session • {new Date().toLocaleDateString()}</p>
                    <h2 className="text-3xl md:text-4xl font-black tracking-tight">Diagnosis Results</h2>
                </div>
                <div className="flex gap-3">
                    <button onClick={() => window.print()} className="flex items-center gap-2 px-4 py-2 bg-white border border-slate-200 rounded-lg text-sm font-medium hover:bg-slate-50 transition-colors">
                        <span className="material-symbols-outlined text-[20px]">print</span>
                        Print Report
                    </button>
                    <button onClick={() => navigate('/diagnosis')} className="flex items-center gap-2 px-4 py-2 bg-slate-900 text-white rounded-lg text-sm font-medium hover:bg-slate-800 transition-colors shadow-lg shadow-primary/20">
                        <span className="material-symbols-outlined text-[20px]">add</span>
                        New Diagnosis
                    </button>
                </div>
            </div>

            {results.length === 0 ? (
                 <div className="p-10 bg-white rounded-xl text-center border border-slate-200">
                    <h3 className="text-xl font-bold">No diseases identified.</h3>
                    <p className="text-slate-500">The symptoms provided do not match any known diseases strongly.</p>
                 </div>
            ) : (
                <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
                    <div className="lg:col-span-8 flex flex-col gap-6">
                        <div className="bg-surface-light rounded-xl border border-slate-200 overflow-hidden shadow-sm">
                            <div className="p-6 md:p-8 border-b border-slate-100 bg-gradient-to-r from-primary/10 via-transparent to-transparent">
                                <div className="flex flex-col md:flex-row gap-6 justify-between items-start">
                                    <div>
                                        <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-red-100 text-red-700 text-xs font-bold uppercase tracking-wider mb-3">
                                            <span className="size-2 rounded-full bg-red-600 animate-pulse"></span>
                                            Primary Diagnosis
                                        </div>
                                        <h3 className="text-3xl font-bold text-slate-900 mb-2">{topResult.disease.name}</h3>
                                        <p className="text-slate-600 text-lg"><em className="italic">{topResult.disease.scientific_name}</em></p>
                                    </div>
                                    <div className="flex items-center gap-4 bg-white p-4 rounded-xl border border-slate-100">
                                        <div className="relative size-20 flex items-center justify-center">
                                            <svg className="size-full -rotate-90 transform" viewBox="0 0 36 36">
                                                <path className="text-slate-200" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" fill="none" stroke="currentColor" strokeWidth="3"></path>
                                                <path className="text-primary" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" fill="none" stroke="currentColor" strokeDasharray={`${topResult.percentage}, 100`} strokeLinecap="round" strokeWidth="3"></path>
                                            </svg>
                                            <div className="absolute flex flex-col items-center">
                                                <span className="text-lg font-bold text-slate-900">{topResult.percentage}%</span>
                                            </div>
                                        </div>
                                        <div className="flex flex-col">
                                            <span className="text-xs uppercase tracking-wider text-slate-500 font-semibold">Certainty Factor</span>
                                            <span className="text-sm font-medium text-primary">
                                                {topResult.certainty_factor > 0.8 ? 'High Confidence' : topResult.certainty_factor > 0.5 ? 'Moderate' : 'Low'}
                                            </span>
                                        </div>
                                    </div>
                                </div>
                                <div className="mt-6 text-slate-700">
                                    <h4 className="font-bold mb-2">Description</h4>
                                    <p>{topResult.disease.description}</p>
                                </div>
                            </div>
                            <div className="p-6 md:p-8">
                                <h4 className="text-lg font-bold mb-4 flex items-center gap-2">
                                    <span className="material-symbols-outlined text-primary">medication</span>
                                    Recommended Treatment Plan
                                </h4>
                                <div className="bg-slate-50 p-6 rounded-xl text-slate-700 whitespace-pre-line">
                                    {topResult.disease.solution}
                                </div>
                            </div>
                        </div>
                    </div>
                    <div className="lg:col-span-4 flex flex-col gap-6">
                        <div className="bg-white rounded-xl border border-slate-200 p-6 shadow-sm">
                            <h3 className="text-base font-bold mb-4 flex items-center justify-between">
                                Other Possibilities
                                <span className="text-xs font-normal text-slate-500 bg-slate-100 px-2 py-1 rounded">Based on symptoms</span>
                            </h3>
                            <div className="flex flex-col gap-3">
                                {results.slice(1).map((res, i) => (
                                    <div key={i} className="relative group p-3 rounded-lg border border-slate-100 hover:border-primary/50 transition-colors cursor-pointer">
                                        <div className="flex justify-between items-center mb-1">
                                            <span className="font-bold text-sm">{res.disease.name}</span>
                                            <span className="text-xs font-bold text-slate-500">{res.percentage}%</span>
                                        </div>
                                        <div className="w-full bg-slate-100 rounded-full h-1.5 mb-2">
                                            <div className="bg-slate-400 h-1.5 rounded-full" style={{width: `${res.percentage}%`}}></div>
                                        </div>
                                    </div>
                                ))}
                            </div>
                        </div>
                    </div>
                </div>
            )}
        </div>
    );
};

window.DiagnosisStep1 = DiagnosisStep1;
window.DiagnosisResult = DiagnosisResult;
