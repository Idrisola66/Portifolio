// Lightbox functionality
const lightbox = document.getElementById('lightbox');
const lightboxImg = document.getElementById('lightbox-img');
const gallery = document.getElementById('gallery');
const closeBtn = document.querySelector('.close');

gallery.addEventListener('click', (e) => {
    if (e.target.classList.contains('gallery-img')) {
        lightbox.style.display = 'block';
        lightboxImg.src = e.target.src;
    }
});

closeBtn.addEventListener('click', () => {
    lightbox.style.display = 'none';
});

lightbox.addEventListener('click', (e) => {
    if (e.target !== lightboxImg) {
        lightbox.style.display = 'none';
    }
});