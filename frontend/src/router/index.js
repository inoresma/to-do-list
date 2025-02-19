import { createRouter, createWebHistory } from 'vue-router'
import PerfilUsuario from '../components/usuarios/PerfilUsuario.vue'
import Home from '@/views/Home.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/perfil',
    name: 'perfil',
    component: PerfilUsuario
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('../views/Login.vue')
  },
  {
    path: '/registro',
    name: 'registro',
    component: () => import('../views/Register.vue')
  },
  {
    path: '/tableros',
    name: 'tableros',
    component: () => import('../views/Tableros.vue')
  },
  {
    path: '/tableros/:id',
    name: 'tablero-detalle',
    component: () => import('../views/TableroDetalle.vue')
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router 