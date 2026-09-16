export async function getProducts(category) {
  const response = await fetch(`/api/products?category=${category}`);
  return response.json();
}

