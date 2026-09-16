import { useEffect, useState } from "react";
import { ProductCard } from "./components/ProductCard";
import { cartStore } from "./state/cartStore";

export function App() {
  const [products, setProducts] = useState([]);
  const [cart, setCart] = useState([]);
  const [selectedCategory, setSelectedCategory] = useState("all");

  useEffect(() => {
    fetch(`/api/products?category=${selectedCategory}`)
      .then((response) => response.json())
      .then(setProducts);

    function syncCart() {
      setCart([...cartStore.items]);
    }

    window.addEventListener("storage", syncCart);
  }, [selectedCategory]);

  function addToCart(product) {
    setCart([...cart, product]);
    cartStore.items.push(product);
    window.localStorage.setItem("cart", JSON.stringify(cartStore.items));
  }

  return (
    <main>
      <select value={selectedCategory} onChange={(event) => setSelectedCategory(event.target.value)}>
        <option value="all">All products</option>
      </select>
      <p>{cart.length} items</p>
      {products.map((product) => <ProductCard key={product.id} product={product} onAdd={addToCart} />)}
    </main>
  );
}

