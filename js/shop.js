/**
 * GeneticHomeopathy — Legacy Shop Helpers
 *
 * NOTE: The main storefront UI is now handled by Shopify Storefront Web
 * Components in products.html (shopify-store, shopify-cart, etc.).
 * This file retains the cart drawer helpers used by older pages.
 *
 * Credentials are managed in products.html via the public Storefront token.
 */

const SHOPIFY_DOMAIN = 'genetic-homeopathy.myshopify.com';
// Public Storefront token is embedded directly in products.html <shopify-store> element.

// MOCK DATA (Fallback if API fails or token is missing)
const MOCK_PRODUCTS = [
  {
    id: 'gid://shopify/Product/7622378618955',
    title: 'R 25',
    handle: 'r-25',
    price: '0.00',
    currency: 'CAD',
    image: 'assets/images/product-placeholder.png',
    category: 'Respiratory',
    description: 'Homeopathic remedy for respiratory support.'
  },
  {
    id: 'gid://shopify/Product/7622612090955',
    title: 'Example Product 1',
    handle: 'healthcare-example-product-1',
    price: '100.00',
    currency: 'CAD',
    image: 'https://cdn.shopify.com/s/files/1/0661/1324/1163/files/healthcare-product-1.jpg?v=1773692606',
    category: 'Skin',
    description: 'Natural skincare solution.'
  },
  {
    id: 'gid://shopify/Product/7622612156491',
    title: 'Example Product 2',
    handle: 'healthcare-example-product-2',
    price: '100.00',
    currency: 'CAD',
    image: 'https://cdn.shopify.com/s/files/1/0661/1324/1163/files/healthcare-product-2.jpg?v=1773692608',
    category: 'Kids',
    description: 'Gentle care for your little ones.'
  }
];

let cart = JSON.parse(localStorage.getItem('gh_cart')) || [];

document.addEventListener('DOMContentLoaded', () => {
  initShop();
  initCartUI();
  renderProducts(MOCK_PRODUCTS); // Start with mock/cached data
});

function initShop() {
  const filterPills = document.querySelectorAll('.filter-pill');
  filterPills.forEach(pill => {
    pill.addEventListener('click', () => {
      filterPills.forEach(p => p.classList.remove('filter-pill--active'));
      pill.classList.add('filter-pill--active');
      const filter = pill.dataset.filter;
      
      const filtered = filter === 'all' 
        ? MOCK_PRODUCTS 
        : MOCK_PRODUCTS.filter(p => p.category === filter);
      
      renderProducts(filtered);
    });
  });
}

function renderProducts(products) {
  const container = document.getElementById('product-list');
  if (!container) return;

  container.innerHTML = products.map(product => `
    <div class="product-card fade-in visible" data-category="${product.category}">
      <div class="product-card__image">
        <img src="${product.image}" alt="${product.title}" loading="lazy">
      </div>
      <div class="product-card__body">
        <span class="product-card__category">${product.category}</span>
        <h3 class="product-card__title">${product.title}</h3>
        <p class="product-card__description">${product.description}</p>
        <div class="product-card__price">${product.currency} $${product.price}</div>
        <button class="btn btn--primary btn-add-cart" onclick="addToCart('${product.id}')">Add to Cart</button>
      </div>
    </div>
  `).join('');
}

// CART LOGIC
function addToCart(productId) {
  const product = MOCK_PRODUCTS.find(p => p.id === productId);
  if (!product) return;

  const existing = cart.find(item => item.id === productId);
  if (existing) {
    existing.quantity += 1;
  } else {
    cart.push({ ...product, quantity: 1 });
  }

  saveCart();
  updateCartUI();
  toggleCart(true);
}

function removeFromCart(index) {
  cart.splice(index, 1);
  saveCart();
  updateCartUI();
}

function saveCart() {
  localStorage.setItem('gh_cart', JSON.stringify(cart));
}

function initCartUI() {
  const trigger = document.getElementById('cart-trigger');
  const close = document.getElementById('cart-close');
  const drawer = document.getElementById('cart-drawer');
  const overlay = document.getElementById('nav-overlay');

  if (trigger) trigger.addEventListener('click', (e) => { e.preventDefault(); toggleCart(true); });
  if (close) close.addEventListener('click', () => toggleCart(false));
  if (overlay) overlay.addEventListener('click', () => toggleCart(false));

  updateCartUI();
}

function toggleCart(open) {
  const drawer = document.getElementById('cart-drawer');
  const overlay = document.getElementById('nav-overlay');
  if (!drawer) return;

  if (open) {
    drawer.classList.add('open');
    if (overlay) overlay.classList.add('active');
  } else {
    drawer.classList.remove('open');
    if (overlay) overlay.classList.remove('active');
  }
}

function updateCartUI() {
  const countEl = document.getElementById('cart-count');
  const itemsEl = document.getElementById('cart-items');
  const totalEl = document.getElementById('cart-total-amount');

  const totalCount = cart.reduce((sum, item) => sum + item.quantity, 0);
  if (countEl) countEl.textContent = totalCount;

  if (!itemsEl) return;

  if (cart.length === 0) {
    itemsEl.innerHTML = '<p style="text-align: center; color: var(--text-light); margin-top: 40px;">Your cart is empty</p>';
    if (totalEl) totalEl.textContent = 'CAD $0.00';
    return;
  }

  itemsEl.innerHTML = cart.map((item, index) => `
    <div class="cart-item">
      <img src="${item.image}" class="cart-item__img" alt="${item.title}">
      <div class="cart-item__info">
        <div class="cart-item__title">${item.title} x ${item.quantity}</div>
        <div class="cart-item__price">CAD $${(parseFloat(item.price) * item.quantity).toFixed(2)}</div>
        <div class="cart-remove" onclick="removeFromCart(${index})">Remove</div>
      </div>
    </div>
  `).join('');

  const totalPrice = cart.reduce((sum, item) => sum + (parseFloat(item.price) * item.quantity), 0);
  if (totalEl) totalEl.textContent = `CAD $${totalPrice.toFixed(2)}`;
  
  // Checkout Button logic
  const checkoutBtn = document.getElementById('checkout-btn');
  if (checkoutBtn) {
    checkoutBtn.onclick = () => {
      alert('Redirecting to Shopify Checkout...\nIn a production app, we would use the Storefront API to create a Checkout URL here.');
      // Example checkout URL construction:
      // window.location.href = `https://${SHOPIFY_DOMAIN}/cart/${cart.map(i => i.id.split('/').pop() + ':' + i.quantity).join(',')}`;
    };
  }
}
