import React, { useState, useEffect } from 'react';
import axios from 'axios';
import LazyLoad from 'react-lazyload';

function App() {
  const [products, setProducts] = useState([]);
  const [filteredProducts, setFilteredProducts] = useState([]);
  const [category, setCategory] = useState('');
  const [priceRange, setPriceRange] = useState([0, 100]);
  const [cart, setCart] = useState([]);

  // Load cart from local storage when the app loads
  useEffect(() => {
    const storedCart = localStorage.getItem('cart');
    if (storedCart) {
      setCart(JSON.parse(storedCart));
    }
  }, []);

  // Fetch products from API when the component mounts
  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('Products.json');
        setProducts(response.data);
        setFilteredProducts(response.data);
      } catch (error) {
        console.error('Error fetching product data:', error);
      }
    };
    fetchData();
  }, []);

  // Filter products based on category and price range
  const handleFilter = () => {
    const filtered = products.filter((product) => {
      const inCategory = category === '' || product.category === category;
      const inPriceRange =
        product.price >= priceRange[0] && product.price <= priceRange[1];
      return inCategory && inPriceRange;
    });
    setFilteredProducts(filtered);
  };

  // Add item to cart and persist to local storage
  const addToCart = (product) => {
    const updatedCart = [...cart, product];
    setCart(updatedCart);
    localStorage.setItem('cart', JSON.stringify(updatedCart));
    alert(`${product.product_name} has been added to the cart.`);
  };

  return (
    <div className="p-6">
      <h1 className="text-4xl font-bold text-center mb-8">Product Listing</h1>

      {/* Filter Section */}
      <div className="mb-6 flex flex-col sm:flex-row justify-center gap-4">
        <select
          value={category}
          onChange={(e) => setCategory(e.target.value)}
          className="p-2 border rounded w-full sm:w-1/3"
        >
          <option value="">All Categories</option>
          <option value="Tops">Tops</option>
          <option value="Bottoms">Bottoms</option>
          <option value="Outerwear">Outerwear</option>
          <option value="Footwear">Footwear</option>
        </select>

        <div className="flex gap-2">
          <input
            type="number"
            value={priceRange[0]}
            onChange={(e) => setPriceRange([+e.target.value, priceRange[1]])}
            placeholder="Min Price"
            className="p-2 border rounded w-full"
          />
          <input
            type="number"
            value={priceRange[1]}
            onChange={(e) => setPriceRange([priceRange[0], +e.target.value])}
            placeholder="Max Price"
            className="p-2 border rounded w-full"
          />
        </div>

        <button
          onClick={handleFilter}
          className="bg-blue-500 text-white p-2 rounded w-full sm:w-auto"
        >
          Filter
        </button>
      </div>

      {/* Product Grid */}
      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
        {filteredProducts.map((product) => (
          <div
            key={product.id}
            className="border rounded-lg p-4 flex flex-col items-center shadow-lg"
          >
            <LazyLoad height={200} offset={100} once>
              <img
                src={product.image_url}
                alt={product.product_name}
                className="w-full h-48 object-cover mb-4"
              />
            </LazyLoad>
            <h2 className="text-xl font-semibold">{product.product_name}</h2>
            <p className="text-gray-600">{product.category}</p>
            <p className="text-green-500 font-bold">${product.price}</p>
            <button
              onClick={() => addToCart(product)}
              className="bg-green-500 text-white mt-4 px-4 py-2 rounded"
            >
              Add to Cart
            </button>
          </div>
        ))}
      </div>

      {/* Cart Section */}
      <div className="mt-8">
        <h2 className="text-2xl font-bold mb-4">Cart Items</h2>
        {cart.length === 0 ? (
          <p className="text-gray-600">Your cart is empty.</p>
        ) : (
          <ul className="list-disc list-inside">
            {cart.map((item, index) => (
              <li key={index} className="mb-2">
                {item.product_name} - ${item.price}
              </li>
            ))}
          </ul>
        )}
      </div>
    </div>
  );
}

export default App;