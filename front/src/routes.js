import Home from "./pages/Home.svelte";
import Article from "./pages/Article.svelte";
import NotFound from "./pages/NotFound.svelte";
import Products from "./pages/Products.svelte";
import News from "./pages/News.svelte";

export const routes = {
  "/": Home,
  "/products": Products,
  "/article/:field1": Article,
  "/news/:id": News,
  "*": NotFound
};