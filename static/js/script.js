function toggleSidebar() {
    const sidebar = document.getElementById('sidebar');
    const content = document.getElementById('content');
    
    sidebar.classList.toggle('active');
    
    // Apenas adicione a classe 'active' ao content em telas maiores
    if (window.innerWidth > 991) {
        content.classList.toggle('active');
    }
    
    document.body.classList.toggle('sidebar-active');
}

function toggleSubitems(element) {
    const subitems = element.querySelectorAll('.sidebar-subitem');
    subitems.forEach(subitem => {
        subitem.classList.toggle('show');
    });
}

// Fechar o sidebar ao clicar fora dele
document.addEventListener('click', function(event) {
    const sidebar = document.getElementById('sidebar');
    const toggleBtn = document.querySelector('.btn-light');
    if (sidebar.classList.contains('active') && !sidebar.contains(event.target) && event.target !== toggleBtn) {
        toggleSidebar();
    }
});

// Ajustar o layout quando a janela for redimensionada
window.addEventListener('resize', function() {
    const sidebar = document.getElementById('sidebar');
    const content = document.getElementById('content');
    
    if (window.innerWidth > 991) {
        if (sidebar.classList.contains('active')) {
            content.classList.add('active');
        }
    } else {
        content.classList.remove('active');
    }
});
