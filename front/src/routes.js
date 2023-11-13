import Home from "./pages/Home.svelte";
import NotFound from "./pages/NotFound.svelte";
import Products from "./pages/Products.svelte";
import News from "./pages/News.svelte";
import Product from "./pages/Product.svelte";
import Vicon from "./pages/products/vicon/Vicon.svelte";
import Standard from "./pages/products/Standard.svelte";
import Services from "./pages/Services.svelte";
import Service from "./pages/services/Service.svelte";

export const routes = {
  "/": Home,
  "/products": Products,
  "/services": Services,
  "/services/:title": Service,
  "/product/vicon": Vicon,
  "/products/:title": Standard,
  "/news/:id": News,
  "*": NotFound
};