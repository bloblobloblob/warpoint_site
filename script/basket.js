document.addEventListener('DOMContentLoaded', () => {
    const addToCartButtons = document.querySelectorAll('.add-to-cart');
    const cartItemsContainer = document.getElementById('cart-items');
    const getCartItems = () => JSON.parse(localStorage.getItem('cartItems')) || [];
    const saveCartItems = (items) => localStorage.setItem('cartItems', JSON.stringify(items));
    const addItemToCart = (itemHtml) => {
        const cartItems = getCartItems();
        cartItems.push(itemHtml);
        saveCartItems(cartItems);
        renderCartItems();
    };

    const renderCartItems = () => {
        const cartItems = getCartItems();
        cartItemsContainer.innerHTML = '';
        cartItems.forEach(itemHtml => {
            const itemElement = document.createElement('li');
            itemElement.classList.add('items-element-card');
            itemElement.innerHTML = itemHtml;
            const addToCartButton = itemElement.querySelector('.add-to-cart');
            if (addToCartButton) {
                addToCartButton.remove();
            }
            cartItemsContainer.appendChild(itemElement);
        });
    };

    addToCartButtons.forEach(button => {
        button.addEventListener('click', (event) => {
            const itemId = event.currentTarget.dataset.itemId;
            const itemElement = document.getElementById(`item-${itemId}`).cloneNode(true);
            const addToCartButton = itemElement.querySelector('.add-to-cart');
            if (addToCartButton) {
                addToCartButton.remove();
            }
            addItemToCart(itemElement.innerHTML);
        });
    });

    renderCartItems();
});
