import { createRouter, createWebHistory } from 'vue-router';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('../views/HomeView.vue')
    }, {
      path: '/about',
      name: 'about',
      component: () => import('../views/AboutView.vue')
    }, {
      path: '/trucks',
      name: 'trucks',
      component: () => import('../views/TrucksView.vue')
    }, {
      path: '/foods',
      name: 'foods',
      component: () => import('../views/FoodsView.vue')
    }, {
      path: '/orders',
      name: 'orders',
      component: () => import('../views/OrdersView.vue')
    }, {
      path: '/screen',
      name: 'screen',
      component: () => import('../views/ScreenView.vue')
    }, {
      path: '/tablet',
      name: 'tablet',
      component: () => import('../views/TabletView.vue')
    }
  ]
});

export default router;
