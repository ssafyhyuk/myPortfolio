import { createRouter, createWebHistory } from 'vue-router'
import SignUpView from '../views/SignUpView.vue'
import LoginView from '../views/LoginView.vue'
import ArticleView from '../views/ArticleView.vue'
import ArticleDetailView from '@/views/ArticleDetailView.vue'
import CreateArticleView from '@/views/CreateArticleView.vue'
import HomeView from '@/views/HomeView.vue'
import ExchangeView from '@/views/ExchangeView.vue'
import MapView from '@/views/MapView.vue'
import ProductView from '@/views/ProductView.vue'
import ProductDetailView from '@/views/ProductDetailView.vue'
import UpdateArticle from '@/views/UpdateArticle.vue'
import SavingProductView from '@/views/SavingProductView.vue'
import SavingProductDetailView from '@/views/SavingProductDetailView.vue'
import ProfileView from '@/views/ProfileView.vue'
import UpdateProfileView from '@/views/UpdateProfileView.vue'
import { useCounterStore } from '@/stores/counter'



const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignUpView
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    {
      path: '/article',
      name: 'article',
      component: ArticleView
    },
    {
      path: '/articles/:id',
      name: 'articledetail',
      component: ArticleDetailView
    },
    {
      path: '/exchange',
      name: 'exchange',
      component: ExchangeView
    },
    {
      path: '/createarticle',
      name: 'createarticle',
      component: CreateArticleView
    },
    {
      path: '/map',
      name: 'map',
      component: MapView
    },
    {
      path: '/product',
      name: 'product',
      component: ProductView
    },
    {
      path: '/products/:str',
      name: 'productdetail',
      component: ProductDetailView
    },
    {
      path: '/updatearticle/:id',
      name: 'updatearticle',
      component: UpdateArticle
    },
    {
      path: '/saving-product',
      name: 'savingproduct',
      component: SavingProductView
    },
    {
      path: '/saving-product/:str',
      name: 'savingproductdetail',
      component: SavingProductDetailView
    },
    {
      path: '/profile',
      name: 'profile',
      component: ProfileView
    },
    {
      path: '/updateprofile',
      name: 'updateprofile',
      component : UpdateProfileView
    },
  ]
})

router.beforeEach((to, from, next) => {
  const store = useCounterStore();

  const protectedRoutes = ['createarticle', 'profile', 'articledetail', 'product', 'productdetail','savingproduct', 'savingproductdetail']
  if (protectedRoutes.includes(to.name) && !store.isLogin) {
    window.alert('로그인이 필요합니다.');
    next({ name: 'login' });
  } else {
    next();
  }
});
export default router
