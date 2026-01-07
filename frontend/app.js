const API_BASE = "http://localhost:8000/api";

const select = document.getElementById("provinceSelect");
const results = document.getElementById("results");

fetch(`${API_BASE}/provinces`)
  .then(res => res.json())
  .then(provinces => {
    provinces.forEach(p => {
      const option = document.createElement("option");
      option.value = p;
      option.textContent = p;
      select.appendChild(option);
    });
  });

select.addEventListener("change", () => {
  results.innerHTML = "";
  if (!select.value) return;

  fetch(`${API_BASE}/constituencies/${select.value}`)
    .then(res => res.json())
    .then(data => {
      data.constituencies.forEach(c => {
        const li = document.createElement("li");
        li.textContent = c;
        results.appendChild(li);
      });
    });
});
