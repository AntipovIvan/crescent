import Home from "./pages/Home.svelte";
import NotFound from "./pages/NotFound.svelte";
import Products from "./pages/Products.svelte";
import News from "./pages/News.svelte";
import Fourdviews from "./pages/products/4dviews.svelte";
import Vicon from "./pages/products/Vicon.svelte";
import ProductTemplate from "./pages/products/ProductTemplate.svelte";
import Services from "./pages/Services.svelte";
import ServiceTemplate from "./pages/services/ServiceTemplate.svelte";
import Fourdstudio from "./pages/services/4dstudio.svelte";
import NewsTemplate from "./pages/news/NewsTemplate.svelte";
import Contact from "./pages/Contact.svelte";
import Aboutus from "./pages/Aboutus.svelte";

export const routes = {
  "/": Home,
  "/products": Products,
  "/services": Services,
  "/contact": Contact,
  "/aboutus": Aboutus,
  "/services/4dstudio": Fourdstudio,
  "/services/:title": ServiceTemplate,
  "/product/vicon": Vicon,
  "/product/4dviews": Fourdviews,
  "/products/:title": ProductTemplate,
  "/news": News,
  "/news/:id": NewsTemplate,
  "*": NotFound
};