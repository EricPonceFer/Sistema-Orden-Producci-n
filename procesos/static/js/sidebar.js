const sidebar = document.querySelector('.sidebar');
const sidebartoggleBtn = document.querySelectorAll('.sidebar-toggle');
const themeToggleBtn = document.querySelector('.theme-toggle');
const themeIcon = themeToggleBtn.querySelector('.theme-icon');

// Uptade the them icon based on the current theme and sidebar state
const updateThemeIcon = () => {
    const isDark = document.body.classList.contains('dark-theme');
    themeIcon.textContent = sidebar.classList.contains('collapsed') ?
    (isDark ? 'light_mode' : 'dark_mode') : "dark_mode";
}

// Apply dark theme if saved or system prefers
const savedTheme = localStorage.getItem('theme');
const systemPrefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
const shouldUseDarkTheme = savedTheme === 'dark' || (!savedTheme && systemPrefersDark);

document.body.classList.toggle('dark-theme', shouldUseDarkTheme);
updateThemeIcon();

sidebartoggleBtn.forEach(btn => {
    btn.addEventListener('click', () => {
        sidebar.classList.toggle('collapsed');
        updateThemeIcon();
    });
});

themeToggleBtn.addEventListener('click', () => {
    const isDark = document.body.classList.toggle('dark-theme');
    localStorage.setItem('theme', isDark ? 'dark' : 'light');
    updateThemeIcon();
});

if (window.innerWidth > 768) {
    sidebar.classList.add('collapsed');
}