import { useEffect, useState } from "react";
import { cartStore } from "../state/cartStore";

export function ProductCard({ product, onAdd }) {
  const [price, setPrice] = useState(product.price);

  useEffect(() => {
    fetch(`/api/products/${product.id}/price`)
      .then((response) => response.json())
      .then((data) => setPrice(data.price));
  }, [product.id]);

  function addProduct() {
    cartStore.items.push(product);
    onAdd(product);
  }

  return <button onClick={addProduct}>{product.name}: {price}</button>;
}

