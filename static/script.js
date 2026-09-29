// ==========================================
// HELPER FUNCTIONS
// ==========================================

function escapeHTML(text) {
    const div = document.createElement("div");
    div.textContent = text;
    return div.innerHTML;
}

function showError(element, message) {
    element.innerHTML = `
        <div class="error-card">
            ⚠️ ${escapeHTML(message)}
        </div>
    `;
}
async function submitData() {
    const task = document.getElementById("task").value;
    const text = document.getElementById("input").value;
    const output = document.getElementById("output");

    if (!text.trim()) {
        output.innerText = "Please enter something first.";
        return;
    }

    output.innerText = "Thinking...";

    try {
        const response = await fetch("/" + task, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                text: text
            })
        });

        const data = await response.json();

        output.innerText = JSON.stringify(data.result, null, 2);

    } catch (error) {
        output.innerText = "Error: " + error.message;
    }
}