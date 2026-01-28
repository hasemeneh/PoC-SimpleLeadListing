import { useState, useEffect } from 'react'
import './App.css'
import { type Lead, type NewLead } from "./types"
const API_BASE_URL = "https://poc-simpleleadlisting.onrender.com/api";

function App() {
  const [leads, setLeads] = useState<Lead[]>([]);
  const [loading, setLoading] = useState(true);

  const [newLead, setNewLead] = useState<NewLead>({
    job_title: "",
    phone_number: "",
    company: "",
    headcount: "",
    email: "",
    industry: "",
    name: "",
  });

  const fetchLeads = async () => {
    setLoading(true);
    console.log(`${API_BASE_URL}/leads`)
    const res = await fetch(`${API_BASE_URL}/leads`);
    const data = await res.json();
    console.log(data)
    setLeads(data);
    setLoading(false);
  };

  const handleChange = (
    e: React.ChangeEvent<HTMLInputElement>
  ) => {
    const { name, value } = e.target;
    setNewLead((prev) => ({
      ...prev,
      [name]: value,
    }));
  };

  useEffect(() => {
    fetchLeads();
  }, []);

  const enrichLead = async (id: string) => {
    const res = await fetch(
      `${API_BASE_URL}/leads/${id}/enrich`,
      { method: "POST" }
    );

    if (res.status === 200) {
      await fetchLeads(); // reload table
    } else {
      alert("Failed to enrich lead");
    }
  };

  const addLead = async (lead: NewLead) => {
    const res = await fetch(`${API_BASE_URL}/leads`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(lead),
    });

    if (res.status === 201 || res.status === 204) {
      await fetchLeads();

      // reset form
      setNewLead({
        job_title: "",
        phone_number: "",
        company: "",
        headcount: "",
        email: "",
        industry: "",
        name: "",
      });
    }
  };

  if (loading) return <p>Loading...</p>;

  return (
    <div style={{ padding: "2rem" }}>
      <h1>Leads</h1>


      {/* Table */}
      <table
        border={1}
        cellPadding={8}
        cellSpacing={0}
        width="100%"
      >
        <thead>
          <tr>
            <th>ID</th>
            <td>Job Title</td>
            <td>Phone Number</td>
            <td>Company</td>
            <td>HeadCount</td>
            <td>Email</td>
            <td>Industry</td>
            <td>Name</td>
            <td>Enrichment</td>
            <th>Action</th>
          </tr>
        </thead>

        <tbody>
          {leads.length === 0 ? (
            <tr>
              <td colSpan={10} align="center">
                No leads found
              </td>
            </tr>
          ) : (
            leads.map((lead) => (
              <tr key={lead.id}>
                <td>{lead.id}</td>
                <td>{lead.job_title}</td>
                <td>{lead.phone_number}</td>
                <td>{lead.company}</td>
                <td>{lead.headcount}</td>
                <td>{lead.email}</td>
                <td>{lead.industry}</td>
                <td>{lead.name}</td>
                <td>{lead.enrichment}</td>
                <td>
                  <button
                    disabled={lead.enrichment === "enriched"}
                    onClick={() => enrichLead(lead.id)}
                  >
                    Enrich
                  </button>
                </td>
              </tr>
            ))
          )}
        </tbody>
      </table>
      <center>

        <div style={{ marginTop: "0.5rem" }}>

          <form
            onSubmit={(e) => {
              e.preventDefault();
              addLead(newLead);
            }}
            style={{ marginBottom: "1.5rem" }}
          >
            <h3>Add Lead</h3>
            <table
            >
              <tr>
                <input name="name" placeholder="Name" value={newLead.name} onChange={handleChange} />
              </tr>
              <tr>
                <input name="email" placeholder="Email" value={newLead.email} onChange={handleChange} />
              </tr>
              <tr>
                <input name="job_title" placeholder="Job Title" value={newLead.job_title} onChange={handleChange} />
              </tr>
              <tr>
                <input name="phone_number" placeholder="Phone Number" value={newLead.phone_number} onChange={handleChange} />
              </tr>
              <tr>
                <input name="company" placeholder="Company" value={newLead.company} onChange={handleChange} />
              </tr>
              <tr>
                <input name="industry" placeholder="Industry" value={newLead.industry} onChange={handleChange} />
              </tr>
              <tr>
                <input name="headcount" placeholder="Headcount" value={newLead.headcount} onChange={handleChange} />
              </tr>

            </table>

            <button type="submit">➕ Add Lead</button>
          </form>
        </div>
      </center>

    </div>
  );
}

export default App;