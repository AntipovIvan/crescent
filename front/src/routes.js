import Home from "./pages/Home.svelte";
import NotFound from "./pages/NotFound.svelte";
import Products from "./pages/Products.svelte";
import News from "./pages/News.svelte";
import Fourdviews from "./pages/products/4dviews.svelte";
import Vicon from "./pages/products/Vicon.svelte";
import Standard from "./pages/products/Standard.svelte";
import Services from "./pages/Services.svelte";
import Service from "./pages/services/Service.svelte";
import Fourdstudio from "./pages/services/4dstudio.svelte";

export const routes = {
  "/": Home,
  "/products": Products,
  "/services": Services,
  "/services/4dstudio": Fourdstudio,
  "/services/:title": Service,
  "/product/vicon": Vicon,
  "/product/4dviews": Fourdviews,
  "/products/:title": Standard,
  "/news/:id": News,
  "*": NotFound
};