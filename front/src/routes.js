import Home from "./pages/Home.svelte";
import NotFound from "./pages/NotFound.svelte";
import Products from "./pages/Products.svelte";
import News from "./pages/News.svelte";

export const routes = {
  "/": Home,
  "/products": Products,
  "/news/:id": News,
  "*": NotFound
};