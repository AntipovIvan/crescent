import Home from "./pages/Home.svelte";
import Article from "./pages/Article.svelte";
import NotFound from "./pages/NotFound.svelte";
import Products from "./pages/Products.svelte";

export const routes = {
  "/": Home,
  "/products": Products,
  "/article/:field1": Article,
  "*": NotFound
};