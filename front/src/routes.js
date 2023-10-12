import Home from "./pages/Home.svelte";
import Article from "./pages/Article.svelte";
import NotFound from "./pages/NotFound.svelte";

export const routes = {
  "/": Home,
  "/article/:field1": Article,
  "*": NotFound
};