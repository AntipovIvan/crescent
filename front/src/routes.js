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
import Holosuite from "./pages/products/Holosuite.svelte";
import Usercase from "./pages/Usercase.svelte";
import UsercaseTemplate from "./pages/usercase/UsercaseTemplate.svelte";
import SpecialTemplate from "./pages/special/SpecialTemplate.svelte";
import Blog from "./pages/Blog.svelte";
import BlogTemplate from "./pages/blog/BlogTemplate.svelte";
import Vero from "./pages/products/vicon/camera/Vero.svelte";
import Valkyrie from "./pages/products/vicon/camera/Valkyrie.svelte";
import Shogun from "./pages/products/vicon/software/Shogun.svelte";
import Holosys from "./pages/products/4dviews/Holosys.svelte";
import Fourdfx from "./pages/products/4dviews/4dfx.svelte";
import Nexus from "./pages/products/vicon/software/Nexus.svelte";
import Tracker from "./pages/products/vicon/software/Tracker.svelte";
import Polygon from "./pages/products/vicon/software/Polygon.svelte";
import Vue from "./pages/products/vicon/hardware/Vue.svelte";
import Lockstudio from "./pages/products/vicon/hardware/Lockstudio.svelte";
import Bicam from "./pages/products/vicon/hardware/Bicam.svelte";
import AppDevSub from "./pages/development/AppDevSub.svelte";
import Recruit from "./pages/Recruit.svelte";

export const routes = {
  "/": Home,
  "/products": Products,
  "/services": Services,
  "/development": Development,
  "/development/appdev": AppDev,
  "/development/appdev/appdevsub": AppDevSub,
  "/development/plugindev": PluginDev,
  "/development/support": Support,
  "/contact": Contact,
  "/aboutus": Aboutus,
  "/services/4dstudio": Fourdstudio,
  "/services/bodylightcage": BodyLightcage,
  "/services/facelightcage": FaceLightcage,
  "/services/:title": ServiceTemplate,
  "/product/vicon": Vicon,
  "/product/vicon/camera/valkyrie": Valkyrie,
  "/product/vicon/camera/vero": Vero,
  "/product/vicon/software/shogun": Shogun,
  "/product/vicon/software/nexus": Nexus,
  "/product/vicon/software/tracker": Tracker,
  "/product/vicon/software/polygon": Polygon,
  "/product/vicon/hardware/vue": Vue,
  "/product/vicon/hardware/lockstudio": Lockstudio,
  "/product/vicon/hardware/bicam": Bicam,
  "/product/4dviews": Fourdviews,
  "/product/4dviews/capture/holosys": Holosys,
  "/product/4dviews/software/4dfx": Fourdfx,
  "/product/holosuite": Holosuite,
  "/products/:title": ProductTemplate,
  "/news": News,
  "/news/:id": NewsTemplate,
  "/usercase": Usercase,
  "/usercase/:id": UsercaseTemplate,
  "/special/:id":SpecialTemplate,
  "/blog": Blog,
  "/blog/:id": BlogTemplate,
  "/recruit":Recruit,
  "*": NotFound
};