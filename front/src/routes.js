import Home from "./lib/Home.svelte";
import Article from "./lib/Article.svelte";
import NotFound from "./lib/NotFound.svelte";

export const routes = {
  "/": Home,
  "/article/:field1": Article,
  "*": NotFound
};