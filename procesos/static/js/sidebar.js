function toggleSidebar() {
    const sidebar = document.getElementById("sidebar");
    const toggleBtn = document.querySelector('.bottom button[onclick="toggleSidebar()"]');
    sidebar.classList.toggle("collapsed");
    if (sidebar.classList.contains("collapsed")) {
        toggleBtn.innerHTML = "➡";
    } else {
        toggleBtn.innerHTML = "⬅";
    }
}

function toggleTheme() {
    document.body.classList.toggle("light");
}