document.addEventListener('DOMContentLoaded', () => {
  const tabLinks = document.querySelectorAll('[data-te-toggle="pill"]');
  const tabContents = document.querySelectorAll('[role="tabpanel"]');

  function deactivateTabs() {
    tabLinks.forEach((tabLink) => {
      tabLink.classList.remove('border-b-0', 'bg-red-400');
      tabLink.classList.add('bg-red-300');
      tabLink.setAttribute('aria-selected', 'false');
    });
  
    tabContents.forEach((tabContent) => {
      tabContent.style.display = 'none';
      tabContent.classList.remove('opacity-100');
      tabContent.classList.add('opacity-0');
    });
  }

  function activateTab(tabLink) {
    const targetId = tabLink.getAttribute('href');
    const targetContent = document.querySelector(targetId);
  
    tabLink.classList.add('border-b-2', 'bg-red-400');
    tabLink.classList.remove('bg-red-300');
    tabLink.setAttribute('aria-selected', 'true');
  
    targetContent.style.display = 'block';
    targetContent.classList.remove('opacity-0');
    targetContent.classList.add('opacity-100');
  }

  tabLinks.forEach((tabLink) => {
    tabLink.addEventListener('click', (event) => {
      event.preventDefault();

      deactivateTabs();
      activateTab(tabLink);
    });
  });
});