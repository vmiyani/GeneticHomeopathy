/* ============================================
   GeneticHomeopathy — Main JavaScript
   Shared interactions for all pages
   ============================================ */

document.addEventListener('DOMContentLoaded', () => {
  initNavigation();
  initNavDropdowns();
  initScrollAnimations();
  initNavScroll();
  initFAQ();
  initFilters();
  initContactForm();
  initStatsCounter();
  initTreatGrid();
  initTreatPageFilters();
  initGalleryLightbox();
  initBlogFilters();
  initReviewFilters();
  initHeroSlider();
});


/* ---------- Navigation ---------- */
function initNavigation() {
  const toggle = document.getElementById('nav-toggle');
  const links = document.getElementById('nav-links');
  const overlay = document.getElementById('nav-overlay');

  if (!toggle || !links) return;

  function openNav() {
    toggle.classList.add('active');
    links.classList.add('open');
    if (overlay) overlay.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  function closeNav() {
    toggle.classList.remove('active');
    links.classList.remove('open');
    if (overlay) overlay.classList.remove('active');
    document.body.style.overflow = '';
  }

  toggle.addEventListener('click', () => {
    if (links.classList.contains('open')) {
      closeNav();
    } else {
      openNav();
    }
  });

  if (overlay) {
    overlay.addEventListener('click', closeNav);
  }

  // Close on link click (mobile) — but NOT for dropdown triggers
  links.querySelectorAll('.nav__link').forEach(link => {
    link.addEventListener('click', (e) => {
      // Skip dropdown triggers on mobile — let them toggle instead
      if (window.innerWidth <= 768 && link.classList.contains('nav__dropdown-trigger')) {
        return;
      }
      closeNav();
    });
  });

  // Close nav when clicking a dropdown sub-link on mobile
  links.querySelectorAll('.nav__dropdown-link').forEach(link => {
    link.addEventListener('click', closeNav);
  });

  // Close on escape key
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && links.classList.contains('open')) {
      closeNav();
    }
  });

  // Set active nav link
  const currentPage = window.location.pathname.split('/').pop() || 'index.html';
  links.querySelectorAll('.nav__link').forEach(link => {
    const href = link.getAttribute('href');
    if (href === currentPage || (currentPage === '' && href === 'index.html')) {
      link.classList.add('nav__link--active');
    }
  });
}


/* ---------- Nav Scroll Effect ---------- */
function initNavScroll() {
  const nav = document.querySelector('.nav');
  if (!nav) return;

  let lastScroll = 0;

  window.addEventListener('scroll', () => {
    const currentScroll = window.scrollY;

    if (currentScroll > 50) {
      nav.classList.add('nav--scrolled');
    } else {
      nav.classList.remove('nav--scrolled');
    }

    lastScroll = currentScroll;
  }, { passive: true });
}


/* ---------- Scroll Animations (IntersectionObserver) ---------- */
function initScrollAnimations() {
  const animatedElements = document.querySelectorAll('.fade-in, .fade-in-left, .fade-in-right');

  if (animatedElements.length === 0) return;

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
  });

  animatedElements.forEach(el => observer.observe(el));
}


/* ---------- Stats Counter Animation ---------- */
function initStatsCounter() {
  const counters = document.querySelectorAll('.counter');
  if (counters.length === 0) return;

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const counter = entry.target;
        const target = parseInt(counter.getAttribute('data-target'));
        animateCounter(counter, target);
        observer.unobserve(counter);
      }
    });
  }, {
    threshold: 0.3
  });

  counters.forEach(counter => observer.observe(counter));
}

function animateCounter(element, target) {
  const duration = 2000;
  const start = 0;
  const startTime = performance.now();

  function update(currentTime) {
    const elapsed = currentTime - startTime;
    const progress = Math.min(elapsed / duration, 1);

    // Ease-out cubic
    const eased = 1 - Math.pow(1 - progress, 3);
    const current = Math.round(start + (target - start) * eased);

    element.textContent = current.toLocaleString();

    if (progress < 1) {
      requestAnimationFrame(update);
    }
  }

  requestAnimationFrame(update);
}


/* ---------- Interactive "We Treat" Grid ---------- */
function initTreatGrid() {
  const treatCards = document.querySelectorAll('.treat-card');
  const expandPanel = document.getElementById('treat-expand');
  const expandTitle = document.getElementById('treat-expand-title');
  const expandList = document.getElementById('treat-expand-list');
  const expandClose = document.getElementById('treat-expand-close');

  if (treatCards.length === 0 || !expandPanel) return;

  const conditionsData = {
    skin: {
      title: 'Skin Diseases',
      url: 'treatment-skin.html',
      conditions: ['Eczema (Atopic Dermatitis)', 'Psoriasis', 'Acne Vulgaris', 'Urticaria (Hives)', 'Fungal Infections', 'Vitiligo', 'Warts & Molluscum', 'Lichen Planus', 'Dermatitis', 'Rosacea', 'Alopecia', 'Seborrheic Dermatitis']
    },
    respiratory: {
      title: 'Respiratory Conditions',
      url: 'treatment-respiratory.html',
      conditions: ['Asthma', 'Allergic Rhinitis (Hay Fever)', 'Chronic Sinusitis', 'Bronchitis', 'Recurrent Colds & Flu', 'Adenoid Hypertrophy', 'Nasal Polyps', 'Chronic Cough', 'Tonsillitis']
    },
    digestive: {
      title: 'Digestive Disorders',
      url: 'treatment-digestive.html',
      conditions: ['Irritable Bowel Syndrome (IBS)', 'Acid Reflux / GERD', 'Chronic Constipation', 'Ulcerative Colitis', 'Bloating & Gas', 'Crohn\'s Disease', 'Gastritis', 'Food Allergies & Intolerances', 'Liver Disorders']
    },
    mental: {
      title: 'Mental & Emotional Health',
      url: 'treatment-mental.html',
      conditions: ['Generalized Anxiety', 'Depression', 'Insomnia & Sleep Disorders', 'Panic Attacks', 'OCD', 'Chronic Stress & Burnout', 'PTSD', 'Grief & Emotional Trauma', 'Chronic Fatigue Syndrome']
    },
    joint: {
      title: 'Joint & Musculoskeletal',
      url: 'treatment-joint.html',
      conditions: ['Rheumatoid Arthritis', 'Osteoarthritis', 'Gout', 'Cervical Spondylosis', 'Fibromyalgia', 'Sciatica', 'Osteoporosis', 'Frozen Shoulder', 'Carpal Tunnel Syndrome']
    },
    women: {
      title: 'Women\'s Health',
      url: 'treatment-women.html',
      conditions: ['PCOS', 'Endometriosis', 'PMS & Dysmenorrhea', 'Menopause Symptoms', 'Infertility Support', 'Uterine Fibroids', 'Leucorrhea', 'Pregnancy-Related Complaints', 'Thyroid Disorders']
    },
    children: {
      title: 'Pediatric Care',
      url: 'treatment-pediatric.html',
      conditions: ['Colic & Infantile Reflux', 'Teething Problems', 'ADHD & Behavioral Issues', 'Recurrent Ear Infections', 'Bedwetting (Enuresis)', 'Growth & Development Delays', 'Childhood Asthma', 'Autism Spectrum Support', 'Frequent Tonsillitis']
    }
  };

  treatCards.forEach(card => {
    card.addEventListener('click', () => {
      const category = card.dataset.treat;
      const data = conditionsData[category];

      if (!data) return;

      // Remove active state from all cards
      treatCards.forEach(c => c.style.outline = '');
      card.style.outline = '2px solid var(--sage-600)';

      expandTitle.textContent = data.title;

      const checkSVG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><polyline points="20 6 9 17 4 12"/></svg>';

      expandList.innerHTML = data.conditions.map(condition =>
        `<div class="treat-expand__item">${checkSVG}${condition}</div>`
      ).join('');

      const treatBookBtn = document.getElementById('treat-book-btn');
      if (treatBookBtn) {
        treatBookBtn.href = data.url;
        treatBookBtn.textContent = `View Details for ${data.title}`;
      }

      expandPanel.classList.add('active');
      expandPanel.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    });
  });

  if (expandClose) {
    expandClose.addEventListener('click', () => {
      expandPanel.classList.remove('active');
      treatCards.forEach(c => c.style.outline = '');
    });
  }
}


/* ---------- We Treat Page Filters ---------- */
function initTreatPageFilters() {
  const filterPills = document.querySelectorAll('.filter-pill');
  const categorySections = document.querySelectorAll('.treat-category-section');

  if (filterPills.length === 0 || categorySections.length === 0) return;

  // Also get the hr separators
  const hrSeparators = document.querySelectorAll('#treatment-directory hr');

  filterPills.forEach(pill => {
    pill.addEventListener('click', () => {
      filterPills.forEach(p => p.classList.remove('filter-pill--active'));
      pill.classList.add('filter-pill--active');

      const filter = pill.dataset.filter;

      categorySections.forEach(section => {
        if (filter === 'all' || section.dataset.category === filter) {
          section.style.display = '';
          // Re-animate
          section.classList.remove('visible');
          requestAnimationFrame(() => {
            section.classList.add('fade-in');
            requestAnimationFrame(() => {
              section.classList.add('visible');
            });
          });
        } else {
          section.style.display = 'none';
        }
      });

      // Show/hide separators
      hrSeparators.forEach(hr => {
        hr.style.display = filter === 'all' ? '' : 'none';
      });
    });
  });
}


/* ---------- FAQ Accordion ---------- */
function initFAQ() {
  const faqItems = document.querySelectorAll('.faq-item');
  const categoryBtns = document.querySelectorAll('.faq-category');

  if (faqItems.length === 0) return;

  // Accordion toggle
  faqItems.forEach(item => {
    const question = item.querySelector('.faq-question');
    if (!question) return;

    question.addEventListener('click', () => {
      const isOpen = item.classList.contains('faq-item--open');

      // Close all other items
      faqItems.forEach(other => {
        if (other !== item) {
          other.classList.remove('faq-item--open');
        }
      });

      // Toggle current
      item.classList.toggle('faq-item--open', !isOpen);
    });
  });

  // Category filter
  categoryBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      // Update active state
      categoryBtns.forEach(b => b.classList.remove('faq-category--active'));
      btn.classList.add('faq-category--active');

      const category = btn.dataset.category;

      // Filter FAQ items
      faqItems.forEach(item => {
        if (category === 'all' || item.dataset.category === category) {
          item.style.display = '';
          // Trigger re-animation
          item.classList.remove('visible');
          requestAnimationFrame(() => {
            item.classList.add('fade-in');
            requestAnimationFrame(() => {
              item.classList.add('visible');
            });
          });
        } else {
          item.style.display = 'none';
        }
      });
    });
  });
}


/* ---------- Product Filters ---------- */
function initFilters() {
  const filterPills = document.querySelectorAll('.filter-pill');
  const productCards = document.querySelectorAll('.product-card');

  // Only run on pages with product cards (not the we-treat page)
  if (filterPills.length === 0 || productCards.length === 0) return;

  filterPills.forEach(pill => {
    pill.addEventListener('click', () => {
      // Update active state
      filterPills.forEach(p => p.classList.remove('filter-pill--active'));
      pill.classList.add('filter-pill--active');

      const filter = pill.dataset.filter;

      productCards.forEach(card => {
        if (filter === 'all' || card.dataset.category === filter) {
          card.style.display = '';
          card.style.animation = 'fadeInUp 0.4s ease-out forwards';
        } else {
          card.style.display = 'none';
        }
      });
    });
  });
}


/* ---------- Contact Form ---------- */
function initContactForm() {
  const form = document.getElementById('contact-form');
  if (!form) return;

  form.addEventListener('submit', (e) => {
    e.preventDefault();

    // Basic validation
    const name = form.querySelector('#contact-name');
    const email = form.querySelector('#contact-email');
    const message = form.querySelector('#contact-message');

    let isValid = true;

    [name, email, message].forEach(field => {
      if (!field) return;
      if (!field.value.trim()) {
        field.style.borderColor = '#e74c3c';
        isValid = false;
      } else {
        field.style.borderColor = '';
      }
    });

    // Email format check
    if (email && email.value && !isValidEmail(email.value)) {
      email.style.borderColor = '#e74c3c';
      isValid = false;
    }

    if (isValid) {
      // Show success message
      const successMsg = document.getElementById('form-success');
      if (successMsg) {
        successMsg.classList.add('show');
        form.reset();
        setTimeout(() => {
          successMsg.classList.remove('show');
        }, 5000);
      }
    }
  });

  // Clear error on focus
  form.querySelectorAll('.form-input').forEach(input => {
    input.addEventListener('focus', () => {
      input.style.borderColor = '';
    });
  });
}

function isValidEmail(email) {
  const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return re.test(email);
}


/* ---------- Smooth Scroll for Anchor Links ---------- */
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', (e) => {
    const targetId = anchor.getAttribute('href');
    if (targetId === '#') return;

    const target = document.querySelector(targetId);
    if (target) {
      e.preventDefault();
      const navHeight = document.querySelector('.nav')?.offsetHeight || 80;
      const topBarHeight = document.querySelector('.top-bar')?.offsetHeight || 0;
      const targetPosition = target.getBoundingClientRect().top + window.scrollY - navHeight - topBarHeight;
      window.scrollTo({ top: targetPosition, behavior: 'smooth' });
    }
  });
});


/* ---------- Nav Dropdowns (Mobile) ---------- */
function initNavDropdowns() {
  const dropdowns = document.querySelectorAll('.nav__dropdown');
  if (!dropdowns.length) return;

  dropdowns.forEach(dropdown => {
    const trigger = dropdown.querySelector('.nav__dropdown-trigger');
    if (!trigger) return;

    trigger.addEventListener('click', (e) => {
      // Only toggle on mobile
      if (window.innerWidth <= 768) {
        e.preventDefault();
        // Close other dropdowns
        dropdowns.forEach(other => {
          if (other !== dropdown) other.classList.remove('open');
        });
        dropdown.classList.toggle('open');
      }
    });
  });

  // Close dropdowns when clicking outside
  document.addEventListener('click', (e) => {
    if (!e.target.closest('.nav__dropdown')) {
      dropdowns.forEach(d => d.classList.remove('open'));
    }
  });
}


/* ---------- Gallery Lightbox ---------- */
function initGalleryLightbox() {
  const lightbox = document.getElementById('gallery-lightbox');
  const lightboxImage = document.getElementById('lightbox-image');
  const lightboxCaption = document.getElementById('lightbox-caption');
  const closeBtn = document.getElementById('lightbox-close');
  const prevBtn = document.getElementById('lightbox-prev');
  const nextBtn = document.getElementById('lightbox-next');
  const galleryItems = document.querySelectorAll('.gallery-item');

  if (!lightbox || !galleryItems.length) return;

  let currentIndex = 0;
  const visibleItems = () => Array.from(galleryItems).filter(item => item.style.display !== 'none');

  function openLightbox(index) {
    const items = visibleItems();
    if (index < 0 || index >= items.length) return;
    currentIndex = index;
    const item = items[index];
    const img = item.querySelector('img');
    const caption = item.dataset.caption || '';
    lightboxImage.src = img.src;
    lightboxImage.alt = img.alt;
    lightboxCaption.textContent = caption;
    lightbox.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  function closeLightbox() {
    lightbox.classList.remove('active');
    document.body.style.overflow = '';
  }

  function navigate(dir) {
    const items = visibleItems();
    currentIndex = (currentIndex + dir + items.length) % items.length;
    const item = items[currentIndex];
    const img = item.querySelector('img');
    lightboxImage.src = img.src;
    lightboxImage.alt = img.alt;
    lightboxCaption.textContent = item.dataset.caption || '';
  }

  galleryItems.forEach((item, i) => {
    item.addEventListener('click', () => {
      const items = visibleItems();
      const visibleIndex = items.indexOf(item);
      openLightbox(visibleIndex >= 0 ? visibleIndex : i);
    });
  });

  if (closeBtn) closeBtn.addEventListener('click', closeLightbox);
  if (prevBtn) prevBtn.addEventListener('click', () => navigate(-1));
  if (nextBtn) nextBtn.addEventListener('click', () => navigate(1));

  lightbox.addEventListener('click', (e) => {
    if (e.target === lightbox) closeLightbox();
  });

  document.addEventListener('keydown', (e) => {
    if (!lightbox.classList.contains('active')) return;
    if (e.key === 'Escape') closeLightbox();
    if (e.key === 'ArrowLeft') navigate(-1);
    if (e.key === 'ArrowRight') navigate(1);
  });

  // Gallery category filters
  const filterBtns = document.querySelectorAll('#gallery-filters .filter-pill, .gallery-filters .filter-pill');
  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => b.classList.remove('filter-pill--active'));
      btn.classList.add('filter-pill--active');
      const filter = btn.dataset.filter;
      galleryItems.forEach(item => {
        if (filter === 'all' || item.dataset.category === filter) {
          item.style.display = '';
        } else {
          item.style.display = 'none';
        }
      });
    });
  });
}


/* ---------- Blog Category Filters ---------- */
function initBlogFilters() {
  const filterBtns = document.querySelectorAll('#blog-filters .filter-pill');
  const blogCards = document.querySelectorAll('#blog-listing-grid .blog-card');

  if (!filterBtns.length || !blogCards.length) return;

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => b.classList.remove('filter-pill--active'));
      btn.classList.add('filter-pill--active');
      const filter = btn.dataset.filter;
      blogCards.forEach(card => {
        if (filter === 'all' || card.dataset.category === filter) {
          card.style.display = '';
          card.style.opacity = '0';
          requestAnimationFrame(() => { card.style.opacity = '1'; });
        } else {
          card.style.display = 'none';
        }
      });
    });
  });
}


/* ---------- Review Category Filters ---------- */
function initReviewFilters() {
  const filterBtns = document.querySelectorAll('#review-filters .filter-pill');
  const reviewCards = document.querySelectorAll('#reviews-grid .review-card');

  if (!filterBtns.length || !reviewCards.length) return;

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => b.classList.remove('filter-pill--active'));
      btn.classList.add('filter-pill--active');
      const filter = btn.dataset.filter;
      reviewCards.forEach(card => {
        if (filter === 'all' || card.dataset.category === filter) {
          card.style.display = '';
          card.style.opacity = '0';
          requestAnimationFrame(() => { card.style.opacity = '1'; });
        } else {
          card.style.display = 'none';
        }
      });
    });
  });
}

/* ---------- Hero Slider ---------- */
function initHeroSlider() {
  const slides = document.querySelectorAll('.hero-slide');
  if (slides.length === 0) return;

  const btnPrev = document.getElementById('slider-prev');
  const btnNext = document.getElementById('slider-next');
  let currentSlide = 0;
  let sliderInterval;

  function goToSlide(index) {
    slides[currentSlide].classList.remove('active');
    currentSlide = (index + slides.length) % slides.length;
    slides[currentSlide].classList.add('active');
    resetInterval();
  }

  function nextSlide() { goToSlide(currentSlide + 1); }
  function prevSlide() { goToSlide(currentSlide - 1); }

  function resetInterval() {
    clearInterval(sliderInterval);
    sliderInterval = setInterval(nextSlide, 6000);
  }

  if (btnNext) btnNext.addEventListener('click', nextSlide);
  if (btnPrev) btnPrev.addEventListener('click', prevSlide);

  // Touch Swipe Support
  const sliderSection = document.getElementById('hero-slider');
  let touchStartX = 0;
  let touchEndX = 0;

  if (sliderSection) {
    sliderSection.addEventListener('touchstart', e => {
      touchStartX = e.changedTouches[0].screenX;
      // Pause auto-play when user touches the slider
      clearInterval(sliderInterval);
    }, {passive: true});

    sliderSection.addEventListener('touchend', e => {
      touchEndX = e.changedTouches[0].screenX;
      handleSwipe();
      // Resume auto-play after interaction
      resetInterval();
    }, {passive: true});
  }

  function handleSwipe() {
    const swipeThreshold = 50; // Minimum pixels to qualify as a swipe
    if (touchEndX < touchStartX - swipeThreshold) {
      nextSlide(); // Swiped left
    }
    if (touchEndX > touchStartX + swipeThreshold) {
      prevSlide(); // Swiped right
    }
  }

  // Start auto play
  resetInterval();
}

