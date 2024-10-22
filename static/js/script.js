function toggleSidebar() {
    document.getElementById('sidebar').classList.toggle('active');
    document.getElementById('content').classList.toggle('active');
    document.body.classList.toggle('sidebar-active');
}

function toggleSubitems(element) {
    const subitems = element.querySelectorAll('.sidebar-subitem');
    subitems.forEach(subitem => {
        subitem.classList.toggle('show');
    });
}

// Fechar o sidebar ao clicar fora dele em dispositivos móveis
document.addEventListener('click', function(event) {
    const sidebar = document.getElementById('sidebar');
    const toggleBtn = document.querySelector('.btn-light');
    if (window.innerWidth <= 991 && sidebar.classList.contains('active') && !sidebar.contains(event.target) && event.target !== toggleBtn) {
        toggleSidebar();
    }
});
