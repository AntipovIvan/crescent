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
import Development from "./pages/Development.svelte";
import AppDev from "./pages/development/AppDev.svelte";
import PluginDev from "./pages/development/PluginDev.svelte";
import Support from "./pages/development/Support.svelte";
import BodyLightcage from "./pages/services/BodyLightcage.svelte";
import FaceLightcage from "./pages/services/FaceLightcage.svelte";

export const routes = {
  "/": Home,
  "/products": Products,
  "/services": Services,
  "/development": Development,
  "/development/appdev": AppDev,
  "/development/plugindev": PluginDev,
  "/development/support": Support,
  "/contact": Contact,
  "/aboutus": Aboutus,
  "/services/4dstudio": Fourdstudio,
  "/services/bodylightcage": BodyLightcage,
  "/services/facelightcage": FaceLightcage,
  "/services/:title": ServiceTemplate,
  "/product/vicon": Vicon,
  "/product/4dviews": Fourdviews,
  "/products/:title": ProductTemplate,
  "/news": News,
  "/news/:id": NewsTemplate,
  "*": NotFound
};