import { createRouter, createWebHistory } from 'vue-router'
import PerfilUsuario from '../components/usuarios/PerfilUsuario.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: () => import('../views/Home.vue')
  },
  {
    path: '/perfil',
    name: 'perfil',
    component: PerfilUsuario
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router 